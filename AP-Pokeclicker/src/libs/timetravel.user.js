// ==UserScript==
// @name          [Pokeclicker] Time Travel
// @namespace     Pokeclicker Scripts
// @author        Hallstead
// @description   Enables time travel functionality in the game.
// @copyright     https://github.com/Ephenia
// @license       GPL-3.0 License
// @version       1.0.0

// @match         https://www.pokeclicker.com/
// @icon          https://www.google.com/s2/favicons?domain=pokeclicker.com
// @grant         unsafeWindow
// @run-at        document-idle
// ==/UserScript==

function initTimeTravel() {
    const timeOfDayStorageKey = 'timeTravelDayCycle';
    const timeOfDayOptions = ['Dawn', 'Day', 'Dusk', 'Night'];
    const storedTimeOfDay = localStorage.getItem(timeOfDayStorageKey);
    const selectedTimeOfDay = ko.observable(timeOfDayOptions.includes(storedTimeOfDay) ? storedTimeOfDay : '');
    let dayOffset = 0;

    // Override only the day-cycle part used by time-of-day requirements.
    // The real clock remains untouched, so elapsed-time systems (such as berry growth) are unaffected.
    const getCurrentDayCyclePart = DayCycle.currentDayCyclePart;
    const timeTravelEnabled = ko.observable(false);
    DayCycle.currentDayCyclePart = ko.pureComputed(() => {
        const selected = selectedTimeOfDay();
        if (!timeTravelEnabled() || !timeOfDayOptions.includes(selected)) {
            return getCurrentDayCyclePart();
        }
        const part = Object.keys(DayCycle.dayCycleMoments).find(key => DayCycle.dayCycleMoments[key].description === selected);
        return part === undefined ? getCurrentDayCyclePart() : Number(part);
    });

    const townMapHeader = document.getElementById('townMap-body');
    const timeOfDayControl = document.createElement('div');
    timeOfDayControl.className = 'd-flex align-items-center ml-auto';
    timeOfDayControl.innerHTML = //`<label class="small mb-0 mr-2" for="time-travel-day-cycle">Time of day</label>
        `<select id="time-travel-day-cycle" class="custom-select custom-select-sm" title="Time of Day" aria-label="Override time of day" style="width: 130px;">
            <option value="">Use local time</option>
            <option value="Dawn">Dawn</option>
            <option value="Day">Day</option>
            <option value="Dusk">Dusk</option>
            <option value="Night">Night</option>
        </select>
        <button id="time-travel-next-day" type="button" class="btn btn-sm btn-secondary ml-2" title="Advance date-seeded Pokémon rotations for this session">+1 Day</button>
        <button id="time-travel-reset" type="button" class="btn btn-sm btn-secondary ml-1" title="Reset date and time of day">Reset</button>`;
    townMapHeader.style.display = 'flex';
    townMapHeader.style.alignItems = 'center';
    townMapHeader.style.marginLeft = '1rem';
    townMapHeader.appendChild(timeOfDayControl);
    timeOfDayControl.addEventListener('click', event => event.stopPropagation());
    const timeOfDaySelect = timeOfDayControl.querySelector('select');
    timeOfDaySelect.value = selectedTimeOfDay();
    timeOfDaySelect.addEventListener('change', () => {
        selectedTimeOfDay(timeOfDaySelect.value);
        localStorage.setItem(timeOfDayStorageKey, timeOfDaySelect.value);
    });

    function getVirtualDate(atMidnight = false) {
        const date = new Date();
        date.setDate(date.getDate() + dayOffset);
        if (atMidnight) {
            date.setHours(0, 0, 0, 0);
        }
        return date;
    }

    // Date-seeded dungeon requirements read GameHelper.today. Keep the offset in
    // memory only, so a reload always starts on the real current day.
    const originalUpdateDay = GameHelper.updateDay;
    GameHelper.updateDay = function (...args) {
        const result = originalUpdateDay.apply(this, args);
        GameHelper.today(getVirtualDate(true));
        return result;
    };

    // Friend Safari reads `new Date()` directly. Temporarily supply the virtual
    // date only while its daily list is generated; other systems keep real time.
    const pageWindow = typeof unsafeWindow !== 'undefined' ? unsafeWindow : window;
    const originalGenerateKalosSafariList = SafariPokemonList.generateKalosSafariList;
    SafariPokemonList.generateKalosSafariList = function (...args) {
        const RealDate = pageWindow.Date;
        const virtualNow = getVirtualDate();
        pageWindow.Date = class extends RealDate {
            constructor(...dateArgs) {
                super(...(dateArgs.length ? dateArgs : [virtualNow]));
            }
            static now() {
                return RealDate.now();
            }
        };
        try {
            return originalGenerateKalosSafariList.apply(this, args);
        } finally {
            pageWindow.Date = RealDate;
        }
    };

    const nextDayButton = timeOfDayControl.querySelector('#time-travel-next-day');
    nextDayButton.addEventListener('click', () => {
        dayOffset += 1;
        GameHelper.today(getVirtualDate(true));
        SafariPokemonList.generateKalosSafariList();
        if ((new DreamOrbTownContent()).isUnlocked()) {
            const unlockedOrbs = App.game.dreamOrbController.orbs.filter(orb => !orb.requirement || orb.requirement.isCompleted());
            for (let i = 0; i < 24 && unlockedOrbs.length; i++) {
                GameHelper.incrementObservable(Rand.fromArray(unlockedOrbs).amount);
            }
        }
        nextDayButton.textContent = `+1 Day (${dayOffset})`;
    });

    const resetButton = timeOfDayControl.querySelector('#time-travel-reset');
    resetButton.addEventListener('click', () => {
        dayOffset = 0;
        GameHelper.today(getVirtualDate(true));
        SafariPokemonList.generateKalosSafariList();
        selectedTimeOfDay('');
        timeOfDaySelect.value = '';
        localStorage.removeItem(timeOfDayStorageKey);
        nextDayButton.textContent = '+1 Day';
    });

    // --- APFlags helpers ---
    function getAPTimeTravelFlag() {
        try {
            return true;
            const w = window;
            if (w.APFlags?.get) return !!w.APFlags.get('timeTravel');
            return !!w.APFlags?.timeTravel;
        } catch (_) { return false; }
    }

    function onAPFlagChanged(ev) {
        try {
            const detail = ev?.detail || {};
            if (!detail || detail.key === 'timeTravel') {
                applyTimeTravelAccessFromFlag();
            }
        } catch (_) { /* ignore */ }
    }

    function applyTimeTravelAccessFromFlag() {
        const enabled = getAPTimeTravelFlag();
        timeTravelEnabled(enabled);
        timeOfDayControl.style.display = enabled ? 'flex' : 'none';
    }

    // Apply gating now and listen for future changes
    applyTimeTravelAccessFromFlag();
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

loadEpheniaScript('timetravel', initTimeTravel);
