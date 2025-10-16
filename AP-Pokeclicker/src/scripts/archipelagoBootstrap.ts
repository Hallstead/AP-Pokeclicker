// Script-side bootstrap for Archipelago integration (legacy scripts flow).
// This file does not import modules; it expects the modules build to expose
// `window.ArchipelagoIntegrationModule` (see src/modules/integrations/archipelago/ArchipelagoIntegration.ts).

(function() {
    // Guard: require App and window module to exist
    function tryInit() {
        const mod = (window as any).ArchipelagoIntegrationModule;
        if (!mod || !window['App'] || !window['App'].game) return;

        try {
            // Wire handlers: delegate items received to App.game via a small adapter.
            mod.onConnected = () => { console.info('[ArchipelagoBootstrap] Module connected'); Notifier.notify({ message: 'Archipelago: Connected', type: NotificationConstants.NotificationOption.success }); };
            mod.onPrint = (m: string) => { console.info('[ArchipelagoBootstrap]', m); Notifier.notify({ message: `Archipelago: ${m}`, type: NotificationConstants.NotificationOption.info }); };
            mod.onItemReceived = (item) => {
                // Keep this adapter minimal: emit a game-level notification and attempt
                // to map a few simple items. Do not import modules here.
                try {
                    const mapped = mapReceivedItem(item?.item ?? item);
                    if (mapped?.type === 'badge') {
                        try { App.game.badgeCase.gainBadge(mapped.value); } catch (e) { console.warn('Failed to grant badge', e); }
                    } else if (mapped?.type === 'flag') {
                        // example: grant bike
                        player.hasBike = true;
                    }
                    Notifier.notify({ message: `Received ${mapped?.name ?? 'an item'} via Archipelago`, type: NotificationConstants.NotificationOption.info });
                } catch (e) {
                    console.warn('[ArchipelagoBootstrap] Error handling item', e);
                }
            };

            // Init the module (server/player can be customized later via UI)
            try {
                // Prefer an in-game player name if available
                let playerName = 'Player';
                try {
                    if (window['App'] && (App as any).game && (App as any).game.player && (App as any).game.player.name) playerName = (App as any).game.player.name;
                } catch (e) {
                    // fallback to env/default
                }
                // fallback to JH if still default
                if (!playerName || playerName === 'Player') playerName = 'JH';
                mod.init('ws://localhost:38281', playerName, true);
                // If the module reports a lastError after a short delay, surface it
                setTimeout(() => {
                    try {
                        const last = (mod as any).lastError || (window as any).__AP_INTEGRATION_DEBUG?.getLastError?.();
                        if (last) {
                            Notifier.notify({ message: `Archipelago error: ${last.message || last}`, type: NotificationConstants.NotificationOption.danger });
                        }
                    } catch (ignore) {}
                }, 500);
            } catch (e) {
                console.warn('[ArchipelagoBootstrap] init failed', e);
                Notifier.notify({ message: `Archipelago init failed: ${e?.message ?? e}`, type: NotificationConstants.NotificationOption.danger });
            }
        } catch (e) {
            console.warn('[ArchipelagoBootstrap] wiring failed', e);
        }
    }

    // Very small mapping example. Extend as needed.
    function mapReceivedItem(idOrName) {
        const map = {
            1: { type: 'badge', name: 'Boulder Badge', value: BadgeEnums?.Boulder },
            2: { type: 'badge', name: 'Cascade Badge', value: BadgeEnums?.Cascade },
            3: { type: 'flag', name: 'Bike', value: null },
        };
        if (typeof idOrName === 'number') return map[idOrName] || { type: 'unknown', name: `Item #${idOrName}` };
        return { type: 'unknown', name: idOrName };
    }

    // Attempt init periodically until module and App are available
    let attempts = 0;
    const interval = setInterval(() => {
        attempts++;
        tryInit();
        if ((window as any).ArchipelagoIntegrationModule && window['App'] && window['App'].game) {
            clearInterval(interval);
        }
        if (attempts > 60) clearInterval(interval);
    }, 500);

    // Detect when the save selector is removed (user selected/created a save) and
    // connect Archipelago automatically. This avoids modifying App.start directly.
    try {
        const target = document.getElementById('saveSelector');
        if (target) {
            const observer = new MutationObserver((mutations) => {
                for (const m of mutations) {
                    for (const removed of Array.from(m.removedNodes || [])) {
                        if ((removed as Element).id === 'saveSelector' || !(document.getElementById('saveSelector'))) {
                            // trigger init (safe no-op if module not present)
                            try {
                                const mod = (window as any).ArchipelagoIntegrationModule;
                                if (mod) {
                                    let playerName = 'JH';
                                    try { if ((App as any).game?.player?.name) playerName = (App as any).game.player.name; } catch (e) {}
                                    mod.init('ws://localhost:38281', playerName, true);
                                }
                            } catch (e) {}
                            observer.disconnect();
                            return;
                        }
                    }
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        }
    } catch (e) {
        // ignore observer failures
    }
    // Expose a global connect helper for UI buttons to call.
    try {
        (window as any).archipelagoConnect = function(serverUrl?: string, playerName?: string) {
            try {
                var mod = (window as any).ArchipelagoIntegrationModule;
                var player = playerName || 'JH';
                // try { if (window['App'] && (App as any).game && (App as any).game.player && (App as any).game.player.name) player = (App as any).game.player.name; } catch (e) {}
                var url = serverUrl || 'ws://localhost:38281';
                if (mod && typeof mod.init === 'function') {
                    Notifier.notify({ message: 'Archipelago: attempting to connect...', type: NotificationConstants.NotificationOption.info });
                    mod.init(url, player, true);
                    return true;
                }
                try { Notifier.notify({ message: 'Archipelago module not available', type: NotificationConstants.NotificationOption.warning }); } catch (_) {}
            } catch (e) {
                try { Notifier.notify({ message: 'Archipelago connect failed: ' + (e && e.message ? e.message : e), type: NotificationConstants.NotificationOption.danger }); } catch (_) {}
            }
            return false;
        };
    } catch (e) {
        // ignore
    }
})();
