import {
    BouncedPacket, Client, Item, itemsHandlingFlags,
    JSONRecord, LocationInfoPacket,
    MessageNode, NetworkSlot, Player,
} from "archipelago.js";

// Modules-side Archipelago integration. This file keeps all Archipelago client
// logic inside the modules build (webpack) and exposes a runtime global that
// legacy scripts can call without importing TS modules.

type AnyFn = (...args: any[]) => any;

class ArchipelagoIntegrationModule {
    private client: any = null;
    public connected = false;
    public lastError: any = null;
    // If set by the public login() wrapper, prefer calling the package's
    // login(host:port, player, game) with these arguments during init.
    private preferLoginCall: { server: string; player: string; game: string } | null = null;

    // Callbacks set by consumer (script bootstrap)
    public onConnected: AnyFn | null = null;
    public onPrint: ((msg: string) => void) | null = null;
    public onItemReceived: ((item: any) => void) | null = null;

    // Emit a single item to the script-side callback, guard against exceptions
    private emitItem = (item: any) => {
        try { this.onItemReceived?.(item); } catch (e) { try { console.warn('[ArchipelagoModule] onItemReceived handler error', e); } catch (_) {} }
    };

    // Debug control: enable/disable verbose packet logging at runtime via window.__AP_DEBUG_PACKETS__
    private debugPacketsEnabled(): boolean {
        try {
            if (typeof window !== 'undefined') {
                const w = window as any;
                if (typeof w.__AP_DEBUG_PACKETS__ === 'boolean') return w.__AP_DEBUG_PACKETS__;
            }
        } catch (_) {}
        // default: enabled to satisfy current request
        return true;
    }
    private debugPacket(payload: any, source: string, eventName: string) {
        try {
            if (!this.debugPacketsEnabled()) return;
            // Avoid throwing on circular structures
            let printable: any = payload;
            if (typeof payload === 'string') {
                printable = payload;
            } else {
                try { printable = JSON.parse(JSON.stringify(payload)); } catch (_) { /* leave as-is */ }
            }
            // eslint-disable-next-line no-console
            console.log('[Archipelago][pkt]', { source, event: eventName, payload: printable });
        } catch (_) { /* ignore logging errors */ }
    }

    // Normalize various payload shapes to individual item emissions
    private handleAnyItemPayload = (payload: any) => {
        try {
            if (!payload) return;
            // Direct single item shape
            if (payload.item != null || payload.location != null || payload.player != null) {
                this.emitItem(payload);
                return;
            }
            // Packet with cmd and items
            if (payload.cmd === 'ReceivedItems' && Array.isArray(payload.items)) {
                payload.items.forEach((it: any) => this.emitItem(it));
                return;
            }
            // Generic { items: [...] }
            if (Array.isArray(payload.items)) {
                (payload.items as any[]).forEach((it) => this.emitItem(it));
                return;
            }
            // Array of items
            if (Array.isArray(payload)) {
                (payload as any[]).forEach((it) => this.emitItem(it));
                return;
            }
            // Some clients wrap differently
            if (payload.data && (payload.data.cmd === 'ReceivedItems' || Array.isArray(payload.data?.items))) {
                this.handleAnyItemPayload(payload.data);
                return;
            }
        } catch (e) {
            try { console.warn('[ArchipelagoModule] error normalizing item payload', e, payload); } catch (_) {}
        }
    };

    // Attempt to listen to as many likely item events as possible on client and socket
    private wireItemListeners(c: any) {
        try {
            const tryOn = (obj: any, ev: string, fn: AnyFn) => {
                try { if (obj && typeof obj.on === 'function') obj.on(ev, fn); } catch (_) {}
            };
            const tryAddEvent = (obj: any, ev: string, fn: AnyFn) => {
                try { if (obj && typeof obj.addEventListener === 'function') obj.addEventListener(ev, fn); } catch (_) {}
            };

            // Client-level event names seen across variants
            ['ItemReceived', 'ItemsReceived', 'item', 'items', 'receivedItems', 'itemsReceived', 'packet', 'message']
                .forEach((ev) => tryOn(c, ev, (p: any) => { this.debugPacket(p, 'client', ev); this.handleAnyItemPayload(p); }));

            // Socket-level generic message events
            const s = c?.socket;
            ['message', 'data', 'packet', 'json']
                .forEach((ev) => tryOn(s, ev, (p: any) => {
                    try {
                        this.debugPacket(p, 'socket', ev);
                        let parsed = p;
                        if (p && typeof p === 'string') { try { parsed = JSON.parse(p); } catch (_) {} }
                        else if (p && p.data && typeof p.data === 'string') { try { parsed = JSON.parse(p.data); } catch (_) { parsed = p.data; } }
                        else if (p && p.data) { parsed = p.data; }
                        this.handleAnyItemPayload(parsed);
                    } catch (e) { /* ignore */ }
                }));
            // Browser WebSocket path
            tryAddEvent(s, 'message', (ev: any) => {
                try {
                    const data = ev?.data;
                    this.debugPacket(data, 'WebSocket', 'message');
                    let parsed = data;
                    if (typeof data === 'string') { try { parsed = JSON.parse(data); } catch (_) {} }
                    this.handleAnyItemPayload(parsed);
                } catch (e) { /* ignore */ }
            });
        } catch (e) { /* ignore wiring errors */ }
    }

    private sendSyncRequest() {
        try {
            const c: any = this.client;
            const msg = { cmd: 'Sync' };
            if (c?.socket && typeof c.socket.send === 'function') return c.socket.send(msg);
            if (typeof c?.send === 'function') return c.send(msg);
            if (c?.socket && typeof c.socket.emit === 'function') return c.socket.emit('Sync', msg);
        } catch (_) {}
    }

    // Initialize and optionally auto-connect. We dynamically import the runtime
    // package so the modules bundle doesn't crash at build time if unavailable.
    public async init(serverUrl = 'ws://localhost:38281', playerName = 'Player', autoConnect = true) {
    //     try {
        this.client = new Client();

        let thisPlayer: number = 0;
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
        let options: GameOptions = {}

        // Expose constructor and instance on window for legacy bootstrap/legacy scripts.  
        this.client.messages.on("connected", async (text: string, player: Player, tags: string[], nodes: MessageNode[]) => {
            console.log("Connected to server: ", player);
            thisPlayer = player.slot;
            const slots: Record<number, NetworkSlot> = this.client.players.slots;
            Object.entries(slots).forEach(([key, slot]: [string, NetworkSlot]) => {
                const slotNumber: number = parseInt(key)
                const slotPlayer: Player = this.client.players.findPlayer(slotNumber);
                players[slotNumber] = {
                    slot: slotNumber,
                    name: slot.name,
                    game: slot.game,
                    alias: slotPlayer.alias,
                }
            });

            options = await player.fetchSlotData().then(res => res as GameOptions);

            this.client.socket.send({ cmd: "Sync" });
        });

        // add item handler for gpio layer
        this.client.items.on("itemsReceived", async(items: Item[], startingIndex: number) => {
            console.log("Received items: ", items);
            // if this is a sync packet reset all our item addresses without changing anything else
            if (startingIndex === 0) {
                for (let i: number = 10; i < 20; i++) {
                    // gpio[i] = 0;
                }
            }

            // go through all our item addresses and if they are not set, check the received items for their ap id,
            // and set the gpio flag if we received it
            // on the scale I expect pico-8 games to be, this will be good enough
            // console.log(`gpio: ${gpio}`)
            for (let i: number = 0; i < items.length; i++) {
                console.log("Processing item: ", items[i]);
                // let item: Item = items[i];
                // if (item.id == base_id + 9) {
                //     if (item.sender.slot === thisPlayer) {
                //         message_pico8("found counterfeit medal :(");
                //     } else {
                //         message_pico8(`got counterfeit medal from ${item.sender.alias} :(`.toLowerCase())
                //     }
                // }

                // for (const flag in item_flags) {
                //     if (base_id + item_flags[flag][1] === item.id) {
                //         const byte = Math.floor(item_flags[flag][0] / 8) + 10;
                //         const item_bit = 2 ** (item_flags[flag][0] % 8);
                //         if (gpio[byte] & item_bit) {  // yes this is supposed to be bitwise and
                //             console.log(`${flag} has already been received`);
                //         } else {
                //             gpio[byte] |= item_bit;
                //             if (item.sender.slot === thisPlayer) {
                //                 message_pico8(`found ${flag}`.toLowerCase())
                //             } else {
                //                 message_pico8(`got ${flag} from ${item.sender.alias}`.toLowerCase())
                //             }
                //         }
                //     }
                // }
            }
        });

        //add location info listener to give game sent item text
        this.client.socket.on("locationInfo", (packet: LocationInfoPacket) => {
            console.log("Location Info: ", packet);
            packet.locations.forEach(location => {
                if (location.player !== thisPlayer) {
                    const itemName = new Item(
                        this.client, location, this.client.players.self, this.client.players.findPlayer(location.player)
                    ).name;
                    console.log(`sent ${itemName} to ${players[location.player].alias}`.toLowerCase());
                }
            });
        });

        await this.client.login(
            serverUrl.startsWith("ws") ?
                `${serverUrl}` :
                `wss://${serverUrl}`,
            playerName,
            'Pokeclicker'
        ).then(() => {
            console.log("Connected to the server");
        }).catch(error => {
            console.error("Failed to connect:", error);
        });

    //         // Try dynamic import (preferred) but fall back to require for environments
    //         // where TypeScript/webpack resolve types differently.
    //         // let pkg: any;
    //         // try {
    //         //     // @ts-ignore - dynamic import and missing types for archipelago.js; handled at runtime/bundle
    //         //     pkg = await import('archipelago.js');
    //         // } catch (e) {
    //         //     try {
    //         //         // eslint-disable-next-line @typescript-eslint/no-var-requires, global-require
    //         //         // @ts-ignore
    //         //         pkg = require('archipelago.js');
    //         //     } catch (err) {
    //         //         // preserve original import error
    //         //         this.lastError = e;
    //         //         throw e;
    //         //     }
    //         // }

    //         // The package may export the client under different shapes; try common ones
    //         console.log('[ArchipelagoModule] imported package shape:', pkg);
    //         let ArchipelagoClient: any = null;
    //         const tryCandidates = [
    //             pkg?.ArchipelagoClient,
    //             pkg?.default?.ArchipelagoClient,
    //             pkg?.default,
    //             pkg,
    //             pkg?.ArchipelagoWebsocketClient,
    //             pkg?.ArchipelagoWebSocketClient,
    //             pkg?.Client,
    //             pkg?.default?.Client,
    //         ];
    //         for (const c of tryCandidates) {
    //             if (typeof c === 'function') {
    //                 ArchipelagoClient = c;
    //                 break;
    //             }
    //         }
    //         // If still not found, scan the exported values for a callable
    //         if (!ArchipelagoClient) {
    //             try {
    //                 for (const v of Object.values(pkg || {})) {
    //                     if (typeof v === 'function') { ArchipelagoClient = v; break; }
    //                 }
    //             } catch (e) {
    //                 // ignore
    //             }
    //         }

    //         if (!ArchipelagoClient) {
    //             this.lastError = new Error('Archipelago client constructor not found in package exports');
    //             console.warn('[ArchipelagoModule] Unable to find a callable Archipelago client in package exports', pkg);
    //             return;
    //         }

    //         // Construct client instance (try new, then factory)
    //         try {
    //             this.client = new ArchipelagoClient({ serverUrl, game: 'Pokeclicker', playerName });
    //         } catch (e) {
    //             // Some shims expose a factory; try calling as function
    //             try {
    //                 this.client = ArchipelagoClient({ serverUrl, game: 'Pokeclicker', playerName });
    //             } catch (err) {
    //                 this.lastError = err;
    //                 console.error('[ArchipelagoModule] Failed to construct client', err);
    //                 return;
    //             }
    //         }

    //         // Expose constructor and instance on window for legacy bootstrap/legacy scripts.
    //         try {
    //             if (typeof window !== 'undefined') {
    //                 const w = window as any;
    //                 // expose constructor under several common names
    //                 w.Archipelago = w.Archipelago || {};
    //                 w.Archipelago.Client = w.Archipelago.Client || ArchipelagoClient;
    //                 w.ArchipelagoClient = w.ArchipelagoClient || ArchipelagoClient;
    //                 w.ArchipelagoClientConstructor = w.ArchipelagoClientConstructor || ArchipelagoClient;
    //                 // expose the created instance
    //                 w.archipelagoClientInstance = this.client;
    //                 // also set a generic client global for debugging/legacy code
    //                 w.client = w.client || this.client;
    //                 console.log('[ArchipelagoModule] exposed Archipelago constructor and instance on window');
    //             }
    //         } catch (e) {
    //             // ignore exposure failures
    //         }

    //         // Expose additional runtime exports (if present) to window for legacy scripts
    //         try {
    //             const wanted = [
    //                 'BouncedPacket', 'Client', 'Item', 'itemsHandlingFlags',
    //                 'JSONRecord', 'LocationInfoPacket', 'MessageNode', 'NetworkSlot', 'Player'
    //             ];
    //             const w = (window as any);
    //             w.Archipelago = w.Archipelago || {};
    //             const debugExportsEnabled = (() => {
    //                 try { return !!(typeof window !== 'undefined' && (window as any).__AP_DEBUG_EXPORTS__); } catch (_) { return false; }
    //             })();
    //             for (const name of wanted) {
    //                 let val: any = undefined;
    //                 try {
    //                     if (pkg && Object.prototype.hasOwnProperty.call(pkg, name)) val = (pkg as any)[name];
    //                     if (val === undefined && pkg && pkg.default && Object.prototype.hasOwnProperty.call(pkg.default, name)) val = (pkg as any).default[name];
    //                     // try lowercase-first alternative (some libs export lowercased keys)
    //                     if (val === undefined) {
    //                         const alt = name.charAt(0).toLowerCase() + name.slice(1);
    //                         if (pkg && Object.prototype.hasOwnProperty.call(pkg, alt)) val = (pkg as any)[alt];
    //                         if (val === undefined && pkg && pkg.default && Object.prototype.hasOwnProperty.call(pkg.default, alt)) val = (pkg as any).default[alt];
    //                     }
    //                 } catch (e) { /* ignore lookup errors */ }

    //                 if (val !== undefined) {
    //                     try { if (!w.Archipelago[name]) w.Archipelago[name] = val; } catch (e) {}
    //                     try { if (!w[name]) w[name] = val; } catch (e) {}
    //                 } else {
    //                     // not fatal; only log when export debugging explicitly enabled
    //                     if (debugExportsEnabled) {
    //                         try { console.warn(`[ArchipelagoModule] export '${name}' not found on package; skipping`); } catch (e) {}
    //                     }
    //                 }
    //             }
    //             if (debugExportsEnabled) { try { console.log('[ArchipelagoModule] exposed additional archipelago exports to window.Archipelago'); } catch (e) {} }
    //         } catch (e) {
    //             // ignore exposure errors
    //         }

    //         // Compatibility shims for legacy bootstrap expectations.
    //         try {
    //             const c = this.client as any;
    //             // Ensure a messages.on API that proxies to client.on or socket events
    //             if (!c.messages || typeof c.messages.on !== 'function') {
    //                 c.messages = c.messages || {};
    //                 c.messages.on = c.messages.on || function (ev: string, cb: any) {
    //                     if (typeof c.on === 'function') {
    //                         try { c.on(ev, (...args: any[]) => cb(...args)); return; } catch (e) { /* continue */ }
    //                     }
    //                     if (c.socket && typeof c.socket.on === 'function') {
    //                         try { c.socket.on(ev, cb); return; } catch (e) { /* continue */ }
    //                     }
    //                     // fallback no-op
    //                     // store subscribers optionally (not necessary for now)
    //                 };
    //             }

    //             // Ensure players.findPlayer exists and slots shape is present
    //             c.players = c.players || { slots: {} };
    //             if (typeof c.players.findPlayer !== 'function') {
    //                 c.players.findPlayer = function (slotNumber: number) {
    //                     try {
    //                         const s = c.players.slots && c.players.slots[slotNumber];
    //                         if (s) return s;
    //                     } catch (e) { }
    //                     return { alias: '' };
    //                 };
    //             }

    //             // Ensure socket.send exists and proxies to common send/connect variants
    //             c.socket = c.socket || {};
    //             if (typeof c.socket.send !== 'function') {
    //                 if (typeof c.send === 'function') {
    //                     c.socket.send = (...args: any[]) => c.send(...args);
    //                 } else if (c.socket && typeof c.socket.emit === 'function') {
    //                     c.socket.send = (...args: any[]) => c.socket.emit(...args);
    //                 } else {
    //                     c.socket.send = (_: any) => { /* noop */ };
    //                 }
    //             }
    //         } catch (e) {
    //             // ignore shim failures
    //         }

    //         // Wire known hooks if present (client implementations differ slightly)
    //         try {
    //             if ('onConnected' in this.client) {
    //                 this.client.onConnected = () => { this.connected = true; this.onConnected?.(); this.sendSyncRequest(); };
    //             } else if (this.client.on) {
    //                 this.client.on('connected', () => { this.connected = true; this.onConnected?.(); this.sendSyncRequest(); });
    //             }
    //             if ('onPrint' in this.client) {
    //                 this.client.onPrint = (m: string) => this.onPrint?.(m);
    //             } else if (this.client.on) {
    //                 this.client.on('print', (m: string) => this.onPrint?.(m));
    //             }
    //             // items: wire a broad net of listeners
    //             if ('onItemReceived' in this.client) {
    //                 this.client.onItemReceived = (it: any) => this.handleAnyItemPayload(it);
    //             }
    //             if (this.client.on) {
    //                 ['ItemReceived', 'ItemsReceived', 'item', 'items', 'receivedItems', 'itemsReceived']
    //                     .forEach((ev) => { try { console.log("Item received"); this.client.on(ev, (p: any) => this.handleAnyItemPayload(p)); } catch (_) {} });
    //             }
    //             // Also wire lower-level listeners on client/socket
    //             this.wireItemListeners(this.client);
    //             // Also attach to socket-level events if available
    //             try {
    //                 const sock = this.client?.socket;
    //                 if (sock && typeof sock.on === 'function') {
    //                     const markConnected = () => { this.connected = true; this.onConnected?.(); this.sendSyncRequest(); };
    //                     // listen for common socket events
    //                     ['connected', 'connect', 'open', 'ready'].forEach((ev) => {
    //                         try { sock.on(ev, markConnected); } catch (e) { /* ignore */ }
    //                     });
    //                     // some socket implementations expose an 'onConnected' property
    //                     try { if ('onConnected' in sock) { (sock as any).onConnected = markConnected; } } catch (e) {}
    //                 }
    //             } catch (e) {
    //                 // ignore socket hook failures
    //             }
    //         } catch (e) {
    //             this.lastError = e;
    //             console.warn('[ArchipelagoModule] Warning wiring client hooks', e);
    //         }

    //         if (autoConnect) {
    //             // Ensure common option shapes include the requested server URL so
    //             // different client implementations can find it.
    //             try {
    //                 // common: client.options.connectionOptions.url
    //                 if (!this.client.options) { this.client.options = {}; }
    //                 if (!this.client.options.connectionOptions) { this.client.options.connectionOptions = {}; }
    //                 this.client.options.connectionOptions.url = serverUrl;
    //             } catch (e) {
    //                 // ignore
    //             }
    //                 try {
    //                     // also set playerName in common locations
    //                     if (!this.client.options) this.client.options = {};
    //                     this.client.options.playerName = this.client.options.playerName || playerName;
    //                     this.client.options.connectionOptions = this.client.options.connectionOptions || {};
    //                     this.client.options.connectionOptions.playerName = this.client.options.connectionOptions.playerName || playerName;
    //                     // set direct fields if present
    //                     try { if (!this.client.playerName) (this.client as any).playerName = playerName; } catch (e) {}
    //                     try { if (!this.client.name) (this.client as any).name = playerName; } catch (e) {}
    //                     try { if (!this.client.username) (this.client as any).username = playerName; } catch (e) {}
    //                     // also set serverUrl in other common shapes
    //                     try { (this.client as any).serverUrl = (this.client as any).serverUrl || serverUrl; } catch (e) {}
    //                     try { this.client.options.url = this.client.options.url || serverUrl; } catch (e) {}
    //                 } catch (e) {}
    //                 try {
    //                     // also propagate into nested connection/socket objects some libs store configuration there
    //                     try { this.client.connectionOptions = this.client.connectionOptions || {}; this.client.connectionOptions.url = this.client.connectionOptions.url || serverUrl; } catch (e) {}
    //                     const s = (this.client as any).socket;
    //                     if (s) {
    //                         try { s.connectionOptions = s.connectionOptions || {}; s.connectionOptions.url = s.connectionOptions.url || serverUrl; } catch (e) {}
    //                         try { s.options = s.options || {}; s.options.url = s.options.url || serverUrl; } catch (e) {}
    //                         try { s.serverUrl = s.serverUrl || serverUrl; } catch (e) {}
    //                         try { s.playerName = s.playerName || playerName; } catch (e) {}
    //                     }
    //                 } catch (e) {}
    //             try {
    //                 // some implementations use defaultConnectionOptions on instance
    //                 if (typeof (this.client as any).defaultConnectionOptions === 'object') {
    //                     (this.client as any).defaultConnectionOptions.url = serverUrl;
    //                 }
    //             } catch (e) {}
    //             // Try the official login(host:port, player, game) first when available.
    //             let connectedViaLogin = false;
    //             try {
    //                 const c: any = this.client;
    //                 const loginFn = c && typeof c.login === 'function' ? c.login.bind(c) : null;
    //                 if (loginFn) {
    //                     const gameName = this.preferLoginCall?.game || 'Pokeclicker';
    //                     const hostPort = String(serverUrl).replace(/^wss?:\/\//i, '');
    //                     const serverVariants = [hostPort, serverUrl, `ws://${hostPort}`].filter((v, i, a) => !!v && a.indexOf(v) === i);
    //                     for (const sv of serverVariants) {
    //                         try {
    //                             console.log('[ArchipelagoModule] attempting login(server, player, game) with', { server: sv, playerName, gameName });
    //                             const r = loginFn(sv, playerName, gameName);
    //                             if (r && typeof r.then === 'function') {
    //                                 await r;
    //                             }
    //                             connectedViaLogin = true;
    //                             console.log('[ArchipelagoModule] login() call succeeded');
    //                             break;
    //                         } catch (e) {
    //                             this.lastError = e;
    //                             console.warn('[ArchipelagoModule] login() attempt failed for server variant', sv, e);
    //                         }
    //                     }
    //                 }
    //             } catch (e) {
    //                 this.lastError = e;
    //                 console.warn('[ArchipelagoModule] error during login() attempts', e);
    //             }

    //             // Try several possible connect entry points. Different package versions
    //             // expose connect on different objects (client.connect, client.socket.connect, etc.).
    //             const connectCandidates: Array<{ obj: any; fn: string }> = [
    //                 // prefer socket-level connect with explicit URL
    //                 { obj: this.client?.socket, fn: 'connect' },
    //                 // keep login here as a fallback in case the above explicit login block didn't run
    //                 { obj: this.client, fn: 'login' },
    //                 { obj: this.client, fn: 'connect' },
    //                 { obj: this.client, fn: 'start' },
    //                 { obj: this.client, fn: 'open' },
    //                 { obj: this.client?.socket, fn: 'open' },
    //                 { obj: this.client?.socket, fn: 'connectTo' },
    //                 { obj: this.client?.socket, fn: 'connectWS' },
    //                 { obj: this.client?.socket, fn: 'create' },
    //             ];

    //             let connected = connectedViaLogin;
    //             for (const cand of connectCandidates) {
    //                 try {
    //                     if (cand.obj && typeof cand.obj[cand.fn] === 'function') {
    //                         if (connected) break;
    //                         console.log(`[ArchipelagoModule] attempting connect via ${cand.fn} on`, cand.obj);
    //                         // Try multiple common argument shapes
    //                         let res: any;
    //                         // Log connection-related values for debugging
    //                         try {
    //                             console.log('[ArchipelagoModule] pre-connect options', {
    //                                 clientOptions: (this.client && this.client.options) || null,
    //                                 clientConnectionOptions: (this.client && this.client.connectionOptions) || null,
    //                                 socketOptions: (this.client && (this.client as any).socket && (this.client as any).socket.options) || null,
    //                                 socketConnectionOptions: (this.client && (this.client as any).socket && (this.client as any).socket.connectionOptions) || null,
    //                                 serverUrl,
    //                                 playerName,
    //                             });
    //                         } catch (e) {}

    //                         // Prefer socket.connect(serverUrl) where available (explicit URL avoids mis-parsing)
    //                         try {
    //                             if (cand.obj === this.client?.socket && typeof cand.obj[cand.fn] === 'function') {
    //                                 res = cand.obj[cand.fn](serverUrl);
    //                             } else {
    //                                 // Prefer calling with no args for methods like 'login' that use configured options
    //                                 try { res = cand.obj[cand.fn](); } catch (e) {
    //                                     // If the method is login, try the 3-argument form explicitly
    //                                     if (cand.fn === 'login') {
    //                                         const gameName = this.preferLoginCall?.game || 'Pokeclicker';
    //                                         const hostPort = String(serverUrl).replace(/^wss?:\/\//i, '');
    //                                         try { res = cand.obj[cand.fn](hostPort, playerName, gameName); } catch (eL1) {
    //                                             try { res = cand.obj[cand.fn](serverUrl, playerName, gameName); } catch (eL2) {
    //                                                 try { res = cand.obj[cand.fn](`ws://${hostPort}`, playerName, gameName); } catch (eL3) { res = null; }
    //                                             }
    //                                         }
    //                                     }
    //                                     if (res == null) {
    //                                         try { res = cand.obj[cand.fn]({ url: serverUrl }); } catch (e2) {
    //                                             try { res = cand.obj[cand.fn]({ connectionOptions: { url: serverUrl } }); } catch (e3) {
    //                                                 try { res = cand.obj[cand.fn](serverUrl); } catch (e4) {
    //                                                     try { res = cand.obj[cand.fn](playerName); } catch (e5) { res = null; }
    //                                                 }
    //                                             }
    //                                         }
    //                                     }
    //                                 }
    //                             }
    //                         } catch (e) {
    //                             res = null;
    //                         }
    //                         if (res && typeof res.then === 'function') {
    //                             // await promise-like results
    //                             try {
    //                                 await res;
    //                             } catch (e) {
    //                                 this.lastError = e;
    //                                 console.warn(`[ArchipelagoModule] ${cand.fn} promise rejected`, e);
    //                                 continue;
    //                             }
    //                         }
    //                         connected = true;
    //                         console.log(`[ArchipelagoModule] connect succeeded via ${cand.fn}`);
    //                         break;
    //                     }
    //                 } catch (e) {
    //                     this.lastError = e;
    //                     console.warn(`[ArchipelagoModule] ${cand.fn} threw`, e);
    //                 }
    //             }
    //             if (!connected) {
    //                 console.warn('[ArchipelagoModule] No connect method succeeded; socket may be managed separately.');
    //             }
    //             // If none of the connect calls immediately signalled connected, poll the socket
    //             // for a short period to detect when it becomes connected and fire onConnected.
    //             (async () => {
    //                 try {
    //                     const maxChecks = 25; // ~5 seconds at 200ms
    //                     for (let i = 0; i < maxChecks; i++) {
    //                         const s = this.client?.socket as any;
    //                         // check common public indicators
    //                         if (!s) { /* wait */ }
    //                         else if (s.connected === true || s.isConnected === true || s._connected === true) {
    //                             this.connected = true; this.onConnected?.(); console.log('[ArchipelagoModule] marked connected via public flag'); break;
    //                         }
    //                         // try underscored/private fields
    //                         try {
    //                             if (s['#connected'] === true) { this.connected = true; this.onConnected?.(); console.log('[ArchipelagoModule] marked connected via #connected'); break; }
    //                         } catch (e) {}
    //                         try {
    //                             if (s._isConnected === true) { this.connected = true; this.onConnected?.(); console.log('[ArchipelagoModule] marked connected via _isConnected'); break; }
    //                         } catch (e) {}
    //                         try {
    //                             // reflect private field symbols
    //                             const symNames = Object.getOwnPropertySymbols(s || {}).map(String);
    //                             if (symNames.some(n => /connected/i.test(n))) { this.connected = true; this.onConnected?.(); console.log('[ArchipelagoModule] marked connected via symbol'); break; }
    //                         } catch (e) {}
    //                         await new Promise(r => setTimeout(r, 200));
    //                     }
    //                 } catch (e) {
    //                     // ignore polling errors
    //                 }
    //             })();
    //         }
    //     } catch (e) {
    //         this.lastError = e;
    //         console.warn('[ArchipelagoModule] dynamic import failed', e);
    //     }
    }

    // Public wrapper that prefers the archipelago.js login(host:port, player, game)
    // signature. This will import/initialize the client and then use login.
    public async login(serverOrHostPort: string, playerName: string, gameName = 'Pokeclicker') {
        this.preferLoginCall = { server: serverOrHostPort, player: playerName, game: gameName };
        try {
            await this.init(serverOrHostPort, playerName, true);
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
}

export default instance;
