import BadgeEnums from '../../enums/Badges';
import NotificationConstants from '../../notifications/NotificationConstants';
import Notifier from '../../notifications/Notifier';

import {
    // BouncedPacket, JSONRecord, itemsHandlingFlags,LocationInfoPacket, MessageNode,
    Client, Item as APItem, clientStatuses,
    NetworkSlot, Player as APPlayer,
    Item,
} from 'archipelago.js';
import KeyItemType from '../../enums/KeyItemType';
import OakItemType from '../../enums/OakItemType';
import Rand from '../../utilities/Rand';
import BuyKeyItem from '../../items/buyKeyItem';
import PokemonItem from '../../items/PokemonItem';
import { getPokemonByName } from '../../pokemons/PokemonHelper';

// Modules-side Archipelago integration. This file keeps all Archipelago client
// logic inside the modules build (webpack) and exposes a runtime global that
// legacy scripts can call without importing TS modules.

class ArchipelagoIntegrationModule {
    private client: any = null;
    private player: APPlayer = null;
    public connected = false;
    public lastError: any = null;
    // Queue outbound location checks until we're connected
    private pendingLocationChecks: number[] = [];
    // Queue inbound item packets until the game is ready
    private pendingItemPackets: { items: APItem[]; startingIndex: number }[] = [];
    // If set by the public login() wrapper, prefer calling the package's
    // login(host:port, player, game) with these arguments during init.
    private preferLoginCall: { server: string; player: string; game: string } | null = null;
    nowItems: {};

    // Wait until the legacy game is ready (App.game exists). Returns true if ready, false if timed out.
    private async waitForGameReady(timeoutMs = 10000, intervalMs = 100): Promise<boolean> {
        const start = Date.now();
        // Fast path: already ready via global flag or App.game present
        try {
            if (typeof window !== 'undefined') {
                const w: any = window as any;
                if ((w.__AP_GAME_READY__ === true) || (w.App && w.App.game)) return true;
            }
        } catch (_) { }

        // Prefer event-based detection if available
        const eventPromise = new Promise<boolean>((resolve) => {
            try {
                if (typeof window !== 'undefined' && typeof window.addEventListener === 'function') {
                    const handler = () => {
                        try { (window as any).removeEventListener?.('ap:game-ready', handler as any); } catch (_) { }
                        resolve(true);
                    };
                    window.addEventListener('ap:game-ready', handler, { once: true } as any);
                }
            } catch (_) { }
        });

        // Poll as a fallback while also racing with the event and timeout
        const pollPromise = (async () => {
            while (Date.now() - start < timeoutMs) {
                try {
                    const w: any = window as any;
                    if (w.__AP_GAME_READY__ === true || (w.App && w.App.game)) return true;
                } catch (_) { }
                await new Promise(r => setTimeout(r, intervalMs));
            }
            return false;
        })();

        const winner = await Promise.race([
            eventPromise,
            pollPromise,
            new Promise<boolean>(r => setTimeout(() => r(false), timeoutMs)),
        ]);
        if (!winner) { try { console.warn('[ArchipelagoModule] App.game not ready after wait; continuing to connect anyway'); } catch (_) { } }
        return winner;
    }

    public displayItemReceived(item: any, article: string) {
        const itemReceivedNotificationType = NotificationConstants.NotificationOption.success;

        if (article == 'a') {
            if (item.name.match(/^[aeiou]/i)) {
                article = 'an';
            } else {
                article = 'a';
            }
        }

        let space = ' ';
        if (article == '') {
            space = '';
        }

        if (item.sender.alias && item.sender.alias != item.receiver.alias) {
            Notifier.notify({
                message: `You received ${article}${space}${item.name} from ${item.sender}!`,
                type: itemReceivedNotificationType,
                timeout: 5000,
            });
        } else {
            Notifier.notify({
                message: `You found ${article}${space}${item.name}!`,
                type: itemReceivedNotificationType,
                timeout: 5000,
            });
        }
    }

    // Initialize and optionally auto-connect. We dynamically import the runtime
    // package so the modules bundle doesn't crash at build time if unavailable.
    public async init(serverUrl = 'ws://localhost:38281', playerName = 'Player') {

        this.client = new Client();

        type Players = Record<number, {
            slot: number,
            name: string,
            game: string,
            alias: string
        }>;
        let players: Players = {};


        type GameOptions = {
            dexsanity: number,
            use_scripts: number,
            include_scripts_as_items: number,
            progressive_autoclicker: number,
            progressive_auto_safari_zone: number,
            roaming_encounter_multiplier: number,
            roaming_encounter_multiplier_route: boolean,
            pokedollar_multiplier: number,
            dungeon_token_multiplier: number,
            quest_point_multiplier: number,
            diamond_multiplier: number,
            farm_point_multiplier: number,
            battle_point_multiplier: number,
            conquest_token_multiplier: number,
            exp_multiplier: number
        };
        let options: GameOptions = {
            dexsanity: 0,
            use_scripts: 0,
            include_scripts_as_items: 0,
            progressive_autoclicker: 0,
            progressive_auto_safari_zone: 0,
            roaming_encounter_multiplier: 1,
            roaming_encounter_multiplier_route: true,
            pokedollar_multiplier: 1,
            dungeon_token_multiplier: 1,
            quest_point_multiplier: 1,
            diamond_multiplier: 1,
            farm_point_multiplier: 1,
            battle_point_multiplier: 1,
            conquest_token_multiplier: 1,
            exp_multiplier: 1,
        };

        // Ensure global runtime flag object exists and supports get/set with event dispatch
        const w: any = window as any;
        if (!w.APFlags) {
            w.APFlags = Object.assign(Object.create(null), {
                gameReady: false,
                autoBattleItems: false,
                catchFilterFantasia: false,
                enhancedAutoClicker: false,
                enhancedAutoClickerProgressive: 0,
                enhancedAutoHatchery: false,
                enhancedAutoMine: false,
                simpleAutoFarmer: false,
                autoQuestCompleter: false,
                autoSafariZone: false,
                autoSafariZoneProgressive: 0,
                catchSpeedAdjuster: false,
                infiniteSeasonalEvents: true,
                oakItemsUnlimited: false,
                omegaProteinGains: false,
                overnightBerryGrowth: false,
                simpleWeatherChanger: false,
                progressivePokeballs: 0,
                progressiveEliteBadges: 0,
                extraEggSlots: 0,
                starter1: 30,
                starter2: 60,
                starter3: 42,
            });
        }
        if (typeof w.APFlags.set !== 'function') {
            w.APFlags.set = (key: string, value: any) => {
                try { w.APFlags[key] = value; } catch (_) { /* ignore */ }
                try { window.dispatchEvent(new CustomEvent('ap:flag-changed', { detail: { key, value } })); } catch (_) { /* ignore */ }
            };
        }
        if (typeof w.APFlags.get !== 'function') {
            w.APFlags.get = (key: string) => {
                try { return w.APFlags[key]; } catch (_) { return undefined; }
            };
        }
        w.APFlags.set('recievedItems', {});

        w.sendLocationCheck = (locationNumber: number, isPokemon: boolean = false) => {
            try {
                if (typeof locationNumber !== 'number' || Number.isNaN(locationNumber)) {
                    console.warn('[ArchipelagoModule] Ignoring invalid LocationCheck id:', locationNumber);
                    return;
                }
                if (!this.client) {
                    console.warn('[ArchipelagoModule] Client not initialized yet; queuing LocationCheck', locationNumber);
                    this.pendingLocationChecks.push(locationNumber);
                    return;
                }
                if (!this.connected || !this.isGameReady()) {
                    // Wait for both connection and game init
                    console.warn('[ArchipelagoModule] Not ready (connection/game); queuing LocationCheck', locationNumber);
                    this.pendingLocationChecks.push(locationNumber);
                    return;
                }
                if (isPokemon) {
                    if (locationNumber % 1 !== 0) {
                        locationNumber = locationNumber * 100 + 3000;
                    }
                    locationNumber += 2000;
                }
                if (!this.client.room.checkedLocations.includes(locationNumber)) {
                    this.client.socket.send({ cmd: 'LocationChecks', locations: [locationNumber] });
                }
            } catch (e) {
                this.lastError = e;
                try { console.error('Unable to send packets to the server; not connected to a server.', e); } catch (_) { /* noop */ }
            }
        };

        w.sendVictory = () => {
            this.client.updateStatus(clientStatuses.goal);
        };

        w.setItem = (key: string, value: string) => {
            let dataKey = `pokeclicker:${this.player.team}:${this.player.slot}:${key}`;
            this.client.storage.prepare(dataKey, value).replace(value).commit();
        };

        w.getItem = async (key: string): Promise<string | null> => {
            let dataKey = `pokeclicker:${this.player.team}:${this.player.slot}:${key}`;
            const data = await this.client.storage.fetch(dataKey);
            //console.log(data);
            return data || null;
        };

        w.getItemOld = async (key: string): Promise<string | null> => {
            const data = await this.client.storage.fetch(key);
            //console.log(data);
            return data || null;
        };

        w.scout = (locationID: number) => {
            return this.client.scout([locationID], 0).then((data: any) => data[0]);
        };


        w.scoutShopItem = (item: Item): Promise<string | undefined> => {
            if (item instanceof BuyKeyItem && item.locationId !== null) {
                return w.scout(item.locationId).then(result => {
                    if (this.client.room.checkedLocations.includes(item.locationId)) {
                        item.isPurchased(true);
                    }
                    return Promise.resolve(`${result.receiver.alias}'s ${result.name}`);
                });
            }
            if (item instanceof PokemonItem) {
                let id = getPokemonByName(item.type).id;
                if (id % 1 != 0) {
                    id = id * 100 + 3000;
                }
                id += 2000;
                return w.scout(id).then(result => {
                    if (result) {
                        return Promise.resolve(`${result.receiver.alias}'s ${result.name}`);
                    }
                    return Promise.resolve(undefined);
                });
            }
            return Promise.resolve(undefined);
        };


        this.client.messages.on('connected', async (text: string, player: APPlayer) => {
            // console.log('Connected to server: ', player);
            this.connected = true;
            this.player = player;
            this.nowItems = {};


            // Start the game if not already started
            if (!App.game) {
                //set save key
                Save.key = (await w.getItem('saveKey', true)) || (await w.getItemOld(player.name + 'save key', true)) || Rand.string(6);
                await w.setItem('saveKey', Save.key);
                //console.log('Using save key: ', Save.key);
                document.querySelector('#saveSelector').remove();
                App.start();
            }

            const slots: Record<number, NetworkSlot> = this.client.players.slots;
            Object.entries(slots).forEach(([key, slot]: [string, NetworkSlot]) => {
                const slotNumber: number = parseInt(key);
                const slotPlayer: APPlayer = this.client.players.findPlayer(slotNumber);
                players[slotNumber] = {
                    slot: slotNumber,
                    name: slot.name,
                    game: slot.game,
                    alias: slotPlayer.alias,
                };
            });

            options = await player.fetchSlotData().then(res => res as GameOptions);
            if (options) {
                // console.log('Game options: ', options);
                w.APFlags.set('options', options);
                w.APFlags.set('name', player.name);
                // Mirror explicit boolean for easy access
                if (typeof options.dexsanity !== 'undefined') {
                    w.APFlags.set('dexsanity', !!options.dexsanity);
                    App.game.challenges.list.requireCompletePokedex.active(!!options.dexsanity);
                }
                if (typeof options.use_scripts !== 'undefined' && typeof options.include_scripts_as_items !== 'undefined') {
                    if (options.use_scripts && !options.include_scripts_as_items) {
                        w.APFlags.set('autoBattleItems', !!options.use_scripts);
                        w.APFlags.set('catchFilterFantasia', !!options.use_scripts);
                        w.APFlags.set('enhancedAutoClicker', !!options.use_scripts);
                        w.APFlags.set('enhancedAutoHatchery', !!options.use_scripts);
                        w.APFlags.set('enhancedAutoMine', !!options.use_scripts);
                        w.APFlags.set('simpleAutoFarmer', !!options.use_scripts);
                        w.APFlags.set('autoQuestCompleter', !!options.use_scripts);
                        w.APFlags.set('autoSafariZone', !!options.use_scripts);
                        w.APFlags.set('catchSpeedAdjuster', !!options.use_scripts);
                        w.APFlags.set('infiniteSeasonalEvents', !!options.use_scripts);
                        w.APFlags.set('oakItemsUnlimited', !!options.use_scripts);
                        w.APFlags.set('simpleWeatherChanger', !!options.use_scripts);
                    }
                }
                if (typeof options.roaming_encounter_multiplier !== 'undefined') {
                    w.APFlags.set('roaming_encounter_multiplier', options.roaming_encounter_multiplier);
                }
                if (typeof options.roaming_encounter_multiplier_route !== 'undefined') {
                    w.APFlags.set('roaming_encounter_multiplier_route', options.roaming_encounter_multiplier_route);
                }
                w.APFlags.set('kanto_roamer_rate', 1);
                //if (typeof options.)
            }

            // Only flush queued location checks if game is ready; otherwise they will be flushed later.
            if (this.isGameReady()) {
                try {
                    if (this.pendingLocationChecks.length) {
                        const batch = [...this.pendingLocationChecks];
                        this.pendingLocationChecks.length = 0;
                        this.client.socket.send({ cmd: 'LocationChecks', locations: batch });
                    }
                } catch (e) {
                    this.lastError = e;
                    console.error('Failed to flush queued LocationChecks:', e);
                }
            }
        });

        this.client.messages.on('disconnected', async () => {
            this.connected = false;
            Notifier.notify({
                message: 'Archipelago: disconnected from server.',
                type: NotificationConstants.NotificationOption.warning,
            });
            (window as any).apLoginFromSaveSelector();
        });

        // add item handler
        this.client.items.on('itemsReceived', async (items: APItem[], startingIndex: number) => {
            // Defer processing until game is ready
            if (!this.isGameReady()) {
                this.pendingItemPackets.push({ items, startingIndex });
                return;
            }
            this.processItemPacket(items, startingIndex);
        });

        // Connect immediately; we now gate item/check handling on game readiness.
        await this.client.login(
            serverUrl.startsWith('ws') ?
                `${serverUrl}` :
                `wss://${serverUrl}`,
            playerName,
            'Pokeclicker',
        ).then(() => {
            Notifier.notify({
                message: `Archipelago: connected to ${serverUrl} as '${playerName}'`,
                type: NotificationConstants.NotificationOption.success,
            });
            // console.log('Connected to the server');
            // login resolves once the socket is opened, but we mark connected in the event as well
        }).catch(error => {
            console.error('Failed to connect:', error);
            this.lastError = error;
            this.connected = false;
        });
        // Start async wait for App.game; when ready flush queued items & checks.
        this.ensureGameReady().catch(() => { /* ignore */ });
    }

    // Public wrapper that prefers the archipelago.js login(host:port, player, game)
    // signature. This will import/initialize the client and then use login.
    public async login(serverOrHostPort: string, playerName: string, gameName = 'Pokeclicker') {
        this.preferLoginCall = { server: serverOrHostPort, player: playerName, game: gameName };
        try {
            await this.init(serverOrHostPort, playerName);
        } finally {
            // clear preference regardless of success so future init() calls behave normally
            this.preferLoginCall = null;
        }
        return this.connected;
    }

    public connect() {
        if (this.client && typeof this.client.connect === 'function') {
            this.client.connect();
        }
    }

    public disconnect() {
        if (this.client && typeof this.client.disconnect === 'function') {
            this.client.disconnect();
            this.connected = false;
        }
    }

    public async processItemPacket(items: APItem[], startingIndex: number) {
        const w: any = window as any;
        // Set APFlags for each script item
        const setFlag = (key: string, value: any) => {
            if (w.APFlags?.set) {
                w.APFlags.set(key, value);
            } else {
                w.APFlags = w.APFlags || Object.create(null);
                w.APFlags[key] = value;
                try { window.dispatchEvent(new CustomEvent('ap:flag-changed', { detail: { key, value } })); } catch (_) { /* ignore */ }
            }
        };

        // console.log('Received items: ', items);
        // if this is a sync packet reset all our item addresses without changing anything else
        if (startingIndex === 0) {
            setFlag('progressivePokeballs', 0);
            setFlag('progressiveEliteBadges', 0);
            setFlag('extraEggSlots', 0);

            w.APFlags.receivedItems = await w.getItem('receivedItems') || {};
        }

        // Item Categories:
        const keyItemsOffset = 1;
        const oakItemsOffset = 101;
        const scriptsOffset = 201;
        const badgesOffset = 301;
        const otherItemsOffset = 501;
        const eventItemsOffset = 1001;
        const pokemonOffset = 2001; // 2001 - 3025
        const altPokemonOffset = 5001; // 5101 - 107500
        const mapsanityOffset = 110001; // 110001 - 110578
        const splitDungeonTicketsOffset = 111001; // 111001 - 111222
        const fillerOffset = 1000001;

        for (let i: number = 0; i < items.length; i++) {
            let item: APItem = items[i];

            // console.log('Processing item: ', item);
            // console.log(item.id);

            if (item.id >= keyItemsOffset && item.id < oakItemsOffset) {
                // Key items
                let index = item.id - 1;
                const keyItems = [
                    KeyItemType.Town_map,
                    KeyItemType.Dungeon_ticket,
                    KeyItemType.Mystery_egg,
                    KeyItemType.Wailmer_pail,
                    KeyItemType.Super_rod,
                    KeyItemType.Safari_ticket,
                    KeyItemType.Explorer_kit,
                    KeyItemType.Gem_case,
                    KeyItemType.Holo_caster,
                ];
                if (!App.game.keyItems.hasKeyItem(keyItems[index])) {
                    App.game.keyItems.gainKeyItem(keyItems[index], false);
                    this.displayItemReceived(item, 'the');
                }
            } else if (item.id >= oakItemsOffset && item.id < scriptsOffset) {
                // Oak items
                let index = item.id - oakItemsOffset;
                const oakItems = [
                    OakItemType.Magic_Ball,
                    OakItemType.Amulet_Coin,
                    OakItemType.Rocky_Helmet,
                    OakItemType.Exp_Share,
                    OakItemType.Sprayduck,
                    OakItemType.Shiny_Charm,
                    OakItemType.Magma_Stone,
                    OakItemType.Cell_Battery,
                    OakItemType.Explosive_Charge,
                    OakItemType.Treasure_Scanner,
                ];
                if (!App.game.oakItems.isUnlocked(oakItems[index])) {
                    App.game.oakItems.itemList[oakItems[index]].received = true;
                    this.displayItemReceived(item, 'the');
                }
            } else if (item.id >= scriptsOffset && item.id < badgesOffset) {
                // scripts
                let index = item.id - scriptsOffset;
                switch (index) {
                    case 0: setFlag('autoBattleItems', true); break;
                    case 1: setFlag('catchFilterFantasia', true); break;
                    case 2:
                        // Enhanced Auto Clicker (base)
                        setFlag('enhancedAutoClicker', true);
                        // Back-compat with older consumers
                        setFlag('autoclicker', true);
                        break;
                    case 3:
                        // Progressive clicks/second
                        setFlag('enhancedAutoClicker', true);
                        setFlag('autoclicker', true);
                        {
                            const cur = (w.APFlags?.get ? w.APFlags.get('enhancedAutoClickerProgressive') : w.APFlags?.enhancedAutoClickerProgressive) || 0;
                            setFlag('enhancedAutoClickerProgressive', Number(cur) + 1);
                        }
                        break;
                    case 4: setFlag('enhancedAutoHatchery', true); break;
                    case 5: setFlag('enhancedAutoMine', true); break;
                    case 6: setFlag('simpleAutoFarmer', true); break;
                    case 7: setFlag('autoQuestCompleter', true); break;
                    case 8: setFlag('autoSafariZone', true); break;
                    case 9:
                        setFlag('autoSafariZone', true);
                        {
                            const cur = (w.APFlags?.get ? w.APFlags.get('autoSafariZoneProgressive') : w.APFlags?.autoSafariZoneProgressive) || 0;
                            setFlag('autoSafariZoneProgressive', Number(cur) + 1);
                        }
                        break;
                    case 10: setFlag('catchSpeedAdjuster', true); break;
                    case 11: setFlag('infiniteSeasonalEvents', true); break;
                    case 12: setFlag('oakItemsUnlimited', true); break;
                    case 13: setFlag('simpleWeatherChanger', true); break;
                    default:
                        break;
                }

                this.displayItemReceived(item, 'the');
            } else if (item.id >= badgesOffset && item.id < otherItemsOffset) {
                // Badges
                let index = item.id - badgesOffset;
                const badges = [
                    BadgeEnums.Boulder,
                    BadgeEnums.Cascade,
                    BadgeEnums.Thunder,
                    BadgeEnums.Rainbow,
                    BadgeEnums.Marsh,
                    BadgeEnums.Soul,
                    BadgeEnums.Volcano,
                    BadgeEnums.Earth,
                    BadgeEnums.Elite_Lorelei,
                    BadgeEnums.Elite_Bruno,
                    BadgeEnums.Elite_Agatha,
                    BadgeEnums.Elite_Lance,
                    BadgeEnums.Elite_KantoChampion,
                ];
                const eliteBadges = [
                    BadgeEnums.Elite_Lorelei,
                    BadgeEnums.Elite_Bruno,
                    BadgeEnums.Elite_Agatha,
                    BadgeEnums.Elite_Lance,
                    BadgeEnums.Elite_KantoChampion,
                ];

                if (index == 8) {
                    const currentEliteBadges = w.APFlags.get('progressiveEliteBadges') || 0;
                    if (currentEliteBadges < 5 && !App.game.badgeCase.hasBadge(eliteBadges[currentEliteBadges])) {
                        App.game.badgeCase.gainBadge(eliteBadges[currentEliteBadges]);
                        if (item.name.includes('Progressive')) {
                            this.displayItemReceived(item, 'a');
                        } else {
                            this.displayItemReceived(item, 'the');
                        }

                    }
                    w.APFlags.set('progressiveEliteBadges', currentEliteBadges + 1);
                } else {
                    if (!App.game.badgeCase.hasBadge(badges[index])) {
                        this.displayItemReceived(item, 'the');
                        App.game.badgeCase.gainBadge(badges[index]);
                    }
                }

            } else if (item.id >= otherItemsOffset && item.id < eventItemsOffset) {
                // Other items
                let index = item.id - otherItemsOffset;
                if (index == 0) {
                    // Progressive Pokeballs
                    // TODO: Establish global variable for progressive pokeball state
                    this.displayItemReceived(item, 'a');
                } else if (index == 1) {
                    // Extra Egg Slot
                    const currentExtraEggSlots = w.APFlags.get('extraEggSlots') + 1 || 1;
                    w.APFlags.set('extraEggSlots', currentExtraEggSlots);
                    if (currentExtraEggSlots > App.game.breeding._eggList().length - 4) {
                        App.game.breeding.gainAdditionalEggSlot();
                        App.game.breeding.gainEggSlot();
                        this.displayItemReceived(item, 'a');
                    }
                }
            } else if (item.id >= eventItemsOffset && item.id < pokemonOffset) {
                // Event items
                Notifier.notify({
                    message: 'You received an AP event item. This should not happen. Please report the issue on the AP Pokeclicker Github repo.',
                    type: NotificationConstants.NotificationOption.danger,
                });
            } else if (item.id >= pokemonOffset && item.id < 2152) {
                // Pokemon
                let id = item.id - pokemonOffset + 1;
                if (!App.game.party.alreadyReceived(id)) {
                    App.game.party.receivePokemonById(id, false, false);
                    this.displayItemReceived(item, '');
                }
            } else if (item.id > altPokemonOffset && item.id < mapsanityOffset) {
                // Alternate Form Pokemon
                let id = (item.id - altPokemonOffset + 1) / 100;
                if (!App.game.party.alreadyReceived(id)) {
                    App.game.party.receivePokemonById(id, false, false);
                    this.displayItemReceived(item, '');
                }
            } else if (item.id >= mapsanityOffset && item.id < splitDungeonTicketsOffset) {
            } else if (item.id >= splitDungeonTicketsOffset && item.id < fillerOffset - 1) {
            } else {
                // Filler
                if (!this.nowItems[item.id]) {
                    this.nowItems[item.id] = 0;
                }
                this.nowItems[item.id] += 1;

                if (w.APFlags.receivedItems[item.id] && w.APFlags.receivedItems[item.id] >= this.nowItems[item.id]) {
                    // Already received this item in a previous sync packet
                    continue;
                }
                let id = item.id - fillerOffset;
                if (id == -1) {
                    this.client.updateStatus(clientStatuses.goal);
                }
                if (id == 0) {
                    App.game.wallet.gainMoney(100000 / ((window as any).APFlags.options.pokedollar_multiplier || 1), true);
                    this.displayItemReceived(item, '');
                } else if (id == 1) {
                    App.game.wallet.gainDungeonTokens(10000 / ((window as any).APFlags.options.dungeon_token_multiplier || 1), true);
                    this.displayItemReceived(item, '');
                } else if (id == 2) {
                    App.game.wallet.gainQuestPoints(1000 / ((window as any).APFlags.options.quest_point_multiplier || 1), true);
                    this.displayItemReceived(item, '');
                } else if (id == 3) {
                    App.game.wallet.gainDiamonds(100 / ((window as any).APFlags.options.diamond_multiplier || 1), true);
                    this.displayItemReceived(item, '');
                } else if (id == 4) {
                    App.game.wallet.gainFarmPoints(1000 / ((window as any).APFlags.options.farm_point_multiplier || 1), true);
                    this.displayItemReceived(item, '');
                } else {
                    player.gainItem('Protein', 1);
                    this.displayItemReceived(item, 'a');
                }
            }
        }
        // Save received items state
        await w.setItem('receivedItems', this.nowItems);
    }

    // Wait for App.game, mark ready, then flush queued packets.
    private async ensureGameReady(timeoutMs = 15000) {
        if (this.isGameReady()) return;
        const ready = await this.waitForGameReady(timeoutMs, 100);
        if (!ready) {
            try { console.warn('[ArchipelagoModule] Proceeding without confirmed App.game readiness after timeout'); } catch (_) { }
        }
        (window as any).APFlags.set('gameReady', true); // Treat timeout as ready to avoid indefinite queue
        this.flushQueuedItems();
        this.flushQueuedLocationChecks();
    }

    private flushQueuedItems() {
        if (!this.isGameReady() || !this.pendingItemPackets.length) return;
        for (const packet of this.pendingItemPackets) {
            this.processItemPacket(packet.items, packet.startingIndex);
        }
        this.pendingItemPackets.length = 0;
    }

    private flushQueuedLocationChecks() {
        if (!this.isGameReady() || !this.connected || !this.pendingLocationChecks.length) return;
        try {
            const batch = [...this.pendingLocationChecks];
            this.pendingLocationChecks.length = 0;
            this.client.socket.send({ cmd: 'LocationChecks', locations: batch });
        } catch (e) {
            this.lastError = e;
            try { console.error('Failed to flush queued LocationChecks after game ready:', e); } catch (_) { }
        }
    }

    private isGameReady(): boolean {
        try {
            const w: any = window as any;
            if (w?.APFlags) {
                return !!w.APFlags.get('gameReady');
            }
        } catch (_) { }
        return false;
    }
}

const instance = new ArchipelagoIntegrationModule();
// Expose to window for legacy script consumers and add a tiny debug helper
if (typeof window !== 'undefined') {
    (window as any).ArchipelagoIntegrationModule = instance;
    // debug helper to inspect last error quickly
    (window as any).__AP_INTEGRATION_DEBUG = {
        getLastError: () => (instance as any).lastError,
        isConnected: () => (instance as any).connected,
        forceConnect: () => instance.connect(),
    };

    // Minimal UI helpers (moved from bootstrap) so the Save Selector button can connect without a separate script.
    (window as any).archipelagoConnect = async function (
        serverUrl?: string,
        playerName?: string,
        gameName?: string,
    ): Promise<boolean> {
        const url = serverUrl || 'ws://localhost:38281';
        let name = playerName;
        try {
            if (!name) {
                name = (window as any).App?.game?.player?.name || 'Player';
                if (!name) name = 'Player';
            }
        } catch (_) { name = name || 'Player'; }

        try {
            Notifier.notify({
                message: `Archipelago: connecting to ${url} as '${name}'...`,
                type: NotificationConstants.NotificationOption.info,
            });

            if (typeof instance.login === 'function') {
                await (instance as any).login(url, name, gameName || 'Pokeclicker');
            } else {
                await instance.init(url, name);
            }

            // Delay-check error state
            setTimeout(() => {
                if (!instance.connected && instance.lastError) {
                    const errMsg = instance.lastError?.message || String(instance.lastError);
                    Notifier.notify({
                        message: `Archipelago connection failed: ${errMsg}`,
                        type: NotificationConstants.NotificationOption.danger,
                    });
                }
            }, 500);
            return true;
        } catch (e: any) {
            Notifier.notify({
                message: `Archipelago connect failed: ${e?.message ?? e}`,
                type: NotificationConstants.NotificationOption.danger,
            });
            return false;
        }
    };

    (window as any).apLoginFromSaveSelector = function (): boolean {
        try {
            const hostEl = document.getElementById('ap-host') as HTMLInputElement | null;
            const portEl = document.getElementById('ap-port') as HTMLInputElement | null;
            const slotEl = document.getElementById('ap-slot') as HTMLInputElement | null;
            const h = hostEl?.value;
            const p = portEl?.value;
            const s = slotEl?.value;
            let url = '';
            if (h.includes('localhost')) {
                if (p == null || p.trim() === '') {
                    url = `ws://${h}`;
                } else {
                    url = `ws://${h}:${p}`;
                }
            } else {
                if (p == null || p.trim() === '') {
                    url = `wss://${h}`;
                } else {
                    url = `wss://${h}:${p}`;
                }
            }
            if ((window as any).archipelagoConnect) {
                (window as any).archipelagoConnect(url, s, 'Pokeclicker');
                localStorage.setItem('ap-last-host', h);
                localStorage.setItem('ap-last-port', p);
                localStorage.setItem('ap-last-slot', s);
                return true;
            }
            Notifier.notify({ message: 'Archipelago module not available yet', type: NotificationConstants.NotificationOption.warning });
        } catch (e: any) {
            Notifier.notify({ message: `Archipelago connect failed: ${e?.message ?? e}`, type: NotificationConstants.NotificationOption.danger });
        }
        return false;
    };
}

export default instance;
