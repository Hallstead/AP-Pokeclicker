// ==UserScript==
// @name          [Pokeclicker] Redeemable Code Generator
// @namespace     Pokeclicker Scripts
// @author        Ephenia (Original/Credit: G1)
// @description   Lets you generate infinite amounts of Discord codes for Pokémon that are exclusive and locked behind Pokeclicker's Discord bot & activities. No linking of a Discord account required + fully works offline.
// @copyright     https://github.com/Ephenia
// @license       GPL-3.0 License
// @version       1.3.3

// @homepageURL   https://github.com/Ephenia/Pokeclicker-Scripts/
// @supportURL    https://github.com/Ephenia/Pokeclicker-Scripts/issues

// @match         https://www.pokeclicker.com/
// @icon          https://www.google.com/s2/favicons?domain=pokeclicker.com
// @grant         unsafeWindow
// @run-at        document-idle
// ==/UserScript==

var resCodes;
var validCode = [];

function initCodeGen() {
    App.game.redeemableCodes.codeList.forEach(code => validCode.push(code));
    genCodes();
    const saveTab = document.getElementById('codeEntry');
    var fragment = new DocumentFragment();
    for (let i = 0; i < validCode.length; i++) {
        var codeHTML = document.createElement("div");
        codeHTML.id = `red-wrap-${i}`;
        codeHTML.innerHTML = `<button id="red-${i}" class="btn btn-primary btn-block" value="${validCode[i].hash}">${validCode[i].name}</button>`
        console.log(validCode[i].hash);
        fragment.appendChild(codeHTML)
    }
    saveTab.prepend(fragment)
    for (let ii = 0; ii < validCode.length; ii++) {
       document.getElementById('red-'+ii).addEventListener('click', submitRedeemableCode, false);
    }
    updateRedeemableVisibility();
    window.addEventListener('ap:flag-changed', updateRedeemableVisibility);
    if (window.APFlags.options.include_codes_as_items == true) {
        document.getElementById('redeemable-code-form').style.display = "none";
    }
}

function updateRedeemableVisibility() {
    let anyVisible = false;
    for (let i = 0; i < validCode.length; i++) {
        const unlocked = window.APFlags?.[`redeemableCode${i}`] === true;
        const redeemed = App.game.redeemableCodes.codeList[i].isRedeemed;
        document.getElementById(`red-wrap-${i}`).style.display = (unlocked && !redeemed) ? '' : 'none';
        anyVisible = anyVisible || (unlocked && !redeemed);
    }
}

function submitRedeemableCode() {
    const id = event.target.id.split('-')[1];
    code = validCode[id];
    code.redeem();
    updateRedeemableVisibility()
    return;
}

function resetHTML() {
    for (let i = 0; i < validCode.length; i++) {
        document.getElementById(`red-` + i).innerHTML = validCode[i].name;
    }
}

// function genCodes() {
//     resCodes = [];
//     App.game.discord.codes.forEach(e => e.claimed = false);
//     var discordID = Math.floor((Math.random() * 65536) + 1);
//     App.game.discord.ID(discordID);
//     for (const codeString of validCode.map(c => c.name)) {
//         let codeSeed = codeString.split('').reverse().map(l => l.charCodeAt(0)).reduce((s, b) => s * (b / 10), 1);
//         SeededRand.seed(discordID + codeSeed);
//         const arr = [];
//         for (let i = 0; i < 14; i++) {
//             let int;
//             while (int == undefined || int.length != 1) {
//                 int = SeededRand.intBetween(0, 35).toString(36);
//             }
//             arr.push(int);
//         }

//         arr[4] = '-';
//         arr[9] = '-';
//         resCodes.push(arr.join('').toUpperCase());
//     }
// }

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

loadEpheniaScript('redeemablecodegenerator', initCodeGen);
