import BadgeEnums from '../../enums/Badges';
import NotificationConstants from '../../notifications/NotificationConstants';
import Notifier from '../../notifications/Notifier';

import {
    // BouncedPacket, JSONRecord, itemsHandlingFlags,LocationInfoPacket, MessageNode,
    Client, Item as APItem, clientStatuses,
    NetworkSlot, Player as APPlayer,
} from 'archipelago.js';
import KeyItemType from '../../enums/KeyItemType';
import OakItemType from '../../enums/OakItemType';

// Modules-side Archipelago integration. This file keeps all Archipelago client
// logic inside the modules build (webpack) and exposes a runtime global that
// legacy scripts can call without importing TS modules.

class ArchipelagoIntegrationModule {
    private client: any = null;
    public connected = false;
    public lastError: any = null;
    // Queue outbound location checks until we're connected
    private pendingLocationChecks: number[] = [];
    // If set by the public login() wrapper, prefer calling the package's
    // login(host:port, player, game) with these arguments during init.
    private preferLoginCall: { server: string; player: string; game: string } | null = null;

    
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

        if (item.sender && item.sender != item.receiver) {
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
            DeathLink?: number,
            DeathLink_Amnesty?: number,
            MedalHunt?: number,
            ExtraCheckpoint?: number,
            ExtraChecks?: number
        };
        let options: GameOptions = {};
        
        // Ensure global runtime flag object exists and supports get/set with event dispatch
        const w: any = window as any;
        if (!w.APFlags) {
            w.APFlags = Object.assign(Object.create(null), {
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
                infiniteSeasonalEvents: false,
                oakItemsUnlimited: false,
                omegaProteinGains: false,
                overnightBerryGrowth: false,
                simpleWeatherChanger: false,
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
        
        w.sendLocationCheck = (locationNumber: number) => {
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
                if (!this.connected) {
                    // Don't throw during UI computations; queue to send after connection
                    console.warn('[ArchipelagoModule] Not connected; queuing LocationCheck', locationNumber);
                    this.pendingLocationChecks.push(locationNumber);
                    return;
                }
                this.client.socket.send({ cmd: 'LocationChecks', locations: [locationNumber] });
            } catch (e) {
                this.lastError = e;
                try { console.error('Unable to send packets to the server; not connected to a server.', e); } catch (_) { /* noop */ }
            }
        };

        w.sendVictory = () => {
            this.client.updateStatus(clientStatuses.goal);
        };

        // Expose constructor and instance on window for legacy bootstrap/legacy scripts.  
        this.client.messages.on('connected', async (text: string, player: APPlayer) => { //, tags: string[], nodes: MessageNode[]) => {
            // console.log('Connected to server: ', player);
            this.connected = true;
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
                w.APFlags.set('options', options);
            }

            // this.client.socket.send({ cmd: 'Sync' });
            // Flush any queued location checks now that we're connected
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
        });

        // add item handler
        this.client.items.on('itemsReceived', async (items: APItem[], startingIndex: number) => {
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
                setFlag('autoBattleItems', false);
                setFlag('catchFilterFantasia', false);
                setFlag('enhancedAutoClicker', false);
                setFlag('enhancedAutoClickerProgressive', 0);
                setFlag('enhancedAutoHatchery', false);
                setFlag('enhancedAutoMine', false);
                setFlag('simpleAutoFarmer', false);
                setFlag('autoQuestCompleter', false);
                setFlag('autoSafariZone', false);
                setFlag('autoSafariZoneProgressive', 0);
                setFlag('catchSpeedAdjuster', false);
                setFlag('infiniteSeasonalEvents', false);
                setFlag('oakItemsUnlimited', false);
                setFlag('simpleWeatherChanger', false);
            }

            for (let i: number = 0; i < items.length; i++) {
                let item: APItem = items[i];
                // console.log('Processing item: ', item);
                // console.log(item.id);

                // Item Categories:
                const keyItemsLastIndex = 9;
                const oakItemsLastIndex = keyItemsLastIndex + 10;
                const scriptsLastIndex = oakItemsLastIndex + 14;
                const progressivePokeballsIndex = scriptsLastIndex + 1;
                const badgesLastIndex = progressivePokeballsIndex + 9;
                const breedingIndex = badgesLastIndex + 1;
                const pokemonLastIndex = breedingIndex + 151;

                if (item.id >= 1 && item.id <= keyItemsLastIndex) {
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
                } else if (item.id <= oakItemsLastIndex) {
                    // Oak items
                    let index = item.id - keyItemsLastIndex - 1;
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
                    // TODO: Establish global variables for oak items active state
                    if (!App.game.oakItems.isUnlocked(oakItems[index])) {
                        App.game.oakItems.itemList[oakItems[index]].received = true;
                        this.displayItemReceived(item, 'the');
                    }
                } else if (item.id <= scriptsLastIndex) {
                    // scripts
                    let index = item.id - oakItemsLastIndex - 1;
                    // const scripts = [
                    //     'Auto Battle Items',
                    //     'Catch Filter Fantasia',
                    //     'Enhanced Auto Clicker',
                    //     'Enhanced Auto Clicker (Progressive Clicks/Second)',
                    //     'Enhanced Auto Hatchery',
                    //     'Enhanced Auto Mine',
                    //     'Simple Auto Farmer',
                    //     'Auto Quest Completer',
                    //     'Auto Safari Zone',
                    //     'Auto Safari Zone (Progressive Fast Animations)',
                    //     'Catch Speed Adjuster',
                    //     'Infinite Seasonal Events',
                    //     'Oak Items Unlimited',
                    //     'Simple Weather Changer',
                    // ];

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
                } else if (item.id == progressivePokeballsIndex) {
                    // progressive pokeballs
                    // TODO: Establish global variable for progressive pokeball state
                } else if (item.id <= badgesLastIndex) {
                    // Badges
                    let index = item.id - progressivePokeballsIndex - 1;
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
                    
                    if (index < 8) {
                        if (!App.game.badgeCase.hasBadge(badges[index])) {
                            this.displayItemReceived(item, 'the');
                            App.game.badgeCase.gainBadge(badges[index]);
                        }
                    } else {
                        for (let j = index; j < badges.length; j++) {
                            if (!App.game.badgeCase.hasBadge(badges[j])) {
                                App.game.badgeCase.gainBadge(badges[j]);
                                this.displayItemReceived(item, 'a');
                                break;
                            }
                        }
                    }

                } else if (item.id == breedingIndex) {
                    App.game.breeding.gainAdditionalEggSlot();
                    App.game.breeding.gainEggSlot();
                    this.displayItemReceived(item, 'a');
                } else if (item.id <= pokemonLastIndex) {
                    // Pokemon
                    let id = item.id - breedingIndex;
                    if (!App.game.party.alreadyCaughtPokemon(id)) {
                        App.game.party.gainPokemonById(id, false, false);
                        this.displayItemReceived(item, '');
                    }
                } else {
                    // Filler
                    player.gainItem('Protein', 1);
                    this.displayItemReceived(item, 'a');
                }

            }
        });

        // Ensure the game is initialized before logging in so that early item events
        // don't try to access App.game while undefined.
        await this.waitForGameReady(15000, 100);
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
                if (!name || name === 'Player') name = 'JH';
            }
        } catch (_) { name = name || 'JH'; }

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
            const h = hostEl?.value || 'localhost';
            const p = portEl?.value || '38281';
            const s = slotEl?.value || 'JH';
            const url = `ws://${h}:${p}`;
            if ((window as any).archipelagoConnect) {
                (window as any).archipelagoConnect(url, s, 'Pokeclicker');
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
