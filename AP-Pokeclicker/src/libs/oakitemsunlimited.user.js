// ==UserScript==
// @name          [Pokeclicker] Oak Items Unlimited
// @namespace     Pokeclicker Scripts
// @author        Ephenia
// @description   Removes the limit for the amount of Oak Items that you're able to equip so that you're able to equip all of them.
// @copyright     https://github.com/Ephenia
// @license       GPL-3.0 License
// @version       1.0.3

// @homepageURL   https://github.com/Ephenia/Pokeclicker-Scripts/
// @supportURL    https://github.com/Ephenia/Pokeclicker-Scripts/issues
// @downloadURL   https://raw.githubusercontent.com/Ephenia/Pokeclicker-Scripts/master/custom/oakitemsunlimited.user.js
// @updateURL     https://raw.githubusercontent.com/Ephenia/Pokeclicker-Scripts/master/custom/oakitemsunlimited.user.js

// @match         https://www.pokeclicker.com/
// @icon          https://www.google.com/s2/favicons?domain=pokeclicker.com
// @grant         unsafeWindow
// @run-at        document-idle
// ==/UserScript==

function initOakItems() {
    const oakItems = App.game.oakItems;

    function updateHeader(currentMax) {
        try {
            const header = document.getElementById('oakItemsModal')?.querySelector('h5');
            if (header) {
                header.innerHTML = "Oak Items Equipped: " + oakItems.activeCount() + '/' + currentMax;
            }
        } catch (_) { /* ignore */ }
    }

    function applyFromFlag() {
        // Core game now controls the max via AP flag; just update the header to reflect it
        const currentMax = (typeof oakItems.maxActiveCount === 'function')
            ? oakItems.maxActiveCount()
            : oakItems.maxActiveCount;
        updateHeader(currentMax);
    }

    function onAPFlagChanged(ev) {
        try {
            const detail = ev?.detail || {};
            if (!detail || detail.key === 'oakItemsUnlimited') {
                applyFromFlag();
            }
        } catch (_) { /* ignore */ }
    }

    // Initial apply and listen for runtime changes
    applyFromFlag();
    window.addEventListener('ap:flag-changed', onAPFlagChanged);
}

function loadEpheniaScript(scriptName, initFunction, priorityFunction) {
    function reportScriptError(scriptName, error) {
        console.error(`Error while initializing '${scriptName}' userscript:\n${error}`);
        Notifier.notify({
            type: NotificationConstants.NotificationOption.warning,
            title: scriptName,
            message: `The '${scriptName}' userscript crashed while loading. Check for updates or disable the script, then restart the game.\n\nReport script issues to the script developer, not to the Pokéclicker team.`,
            timeout: GameConstants.DAY,
        });
    }
    const windowObject = (!App.isUsingClient && typeof unsafeWindow !== 'undefined') ? unsafeWindow : window;
    // Inject handlers if they don't exist yet
    if (windowObject.epheniaScriptInitializers === undefined) {
        windowObject.epheniaScriptInitializers = {};
        const oldInit = Preload.hideSplashScreen;
        var hasInitialized = false;

        // Initializes scripts once enough of the game has loaded
        Preload.hideSplashScreen = function (...args) {
            var result = oldInit.apply(this, args);
            if (App.game && !hasInitialized) {
                // Initialize all attached userscripts
                Object.entries(windowObject.epheniaScriptInitializers).forEach(([scriptName, initFunction]) => {
                    try {
                        initFunction();
                    } catch (e) {
                        reportScriptError(scriptName, e);
                    }
                });
                hasInitialized = true;
            }
            return result;
        }
    }

    // Prevent issues with duplicate script names
    if (windowObject.epheniaScriptInitializers[scriptName] !== undefined) {
        console.warn(`Duplicate '${scriptName}' userscripts found!`);
        Notifier.notify({
            type: NotificationConstants.NotificationOption.warning,
            title: scriptName,
            message: `Duplicate '${scriptName}' userscripts detected. This could cause unpredictable behavior and is not recommended.`,
            timeout: GameConstants.DAY,
        });
        let number = 2;
        while (windowObject.epheniaScriptInitializers[`${scriptName} ${number}`] !== undefined) {
            number++;
        }
        scriptName = `${scriptName} ${number}`;
    }
    // Add initializer for this particular script
    windowObject.epheniaScriptInitializers[scriptName] = initFunction;
    // Run any functions that need to execute before the game starts
    if (priorityFunction) {
        $(document).ready(() => {
            try {
                priorityFunction();
            } catch (e) {
                reportScriptError(scriptName, e);
                // Remove main initialization function  
                windowObject.epheniaScriptInitializers[scriptName] = () => null;
            }
        });
    }
}

if (!App.isUsingClient || localStorage.getItem('oakitemsunlimited') === 'true') {
    loadEpheniaScript('oakitemsunlimited', initOakItems);
}
