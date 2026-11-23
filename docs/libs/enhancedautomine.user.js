// ==UserScript==
// @name          [Pokeclicker] Enhanced Auto Mine (v0.10.23 compatible)
// @namespace     Pokeclicker Scripts
// @version       3.1.1
// @description   Automatically mines the Underground using bombs, hammer and chisels intelligently.
// @match         https://www.pokeclicker.com/
// @grant         unsafeWindow
// @run-at        document-idle
// ==/UserScript==

(function () {
    'use strict';

    let mineLevel = 0;
    let mineState = JSON.parse(localStorage.getItem('autoMineState') || 'false');
    let autoMineTimer;

    function getAPEnhancedAutoMineFlag() {
        try {
            const flags = (window.APFlags ?? {});
            if (typeof flags.get === 'function') {
                const value = flags.get('enhancedAutoMine');
                if (typeof value !== 'undefined') return !!value;
            }
            if (Object.prototype.hasOwnProperty.call(flags, 'enhancedAutoMine')) {
                return !!flags.enhancedAutoMine;
            }
        } catch (_) { /* ignore */ }
        return false;
    }

    function hasAutoMineAccess() {
        return getAPEnhancedAutoMineFlag() && App.game.underground.canAccess();
    }

    function addGlobalStyle(css) {
        const head = document.head || document.getElementsByTagName('head')[0];
        if (!head) return;
        const style = document.createElement('style');
        style.innerHTML = css;
        head.appendChild(style);
    }

    function initAutoMine() {
        if (!document.getElementById('auto-mine-start')) {
            const minerHTML = document.createElement("div");
            minerHTML.innerHTML = `
            <div id="auto-miner">
                <button id="auto-mine-start" class="col-12 col-md-4 btn btn-${mineState ? 'success' : 'danger'}">
                    Auto Mine [${mineState ? 'ON' : 'OFF'}]
                </button>
            </div>`;
            document.querySelector('#mineModal .modal-body').prepend(minerHTML);
            addGlobalStyle('#auto-miner { display:flex; flex-wrap:wrap; justify-content:center; align-items:center; margin-bottom:10px }');
        }

        document.getElementById('auto-mine-start').addEventListener('click', toggleAutoMine);
        
        function applyAutoMineAccess() {
            const enabled = hasAutoMineAccess();
            const btn = document.getElementById('auto-mine-start');
            if (btn) {
                btn.style.display = enabled ? '' : 'none';
                btn.disabled = !enabled;
                btn.classList.toggle('btn-success', enabled && !!mineState);
                btn.classList.toggle('btn-danger', !enabled || !mineState);
                btn.textContent = `Auto Mine [${enabled && mineState ? 'ON' : 'OFF'}]`;
            }
            if (enabled && mineState) {
                setAutoMineInterval();
            } else {
                clearInterval(autoMineTimer);
                autoMineTimer = undefined;
            }
        }

        // canAccess() tracks the Explorer Kit's observable unlock state.
        const mineAccess = ko.pureComputed(() => App.game.underground.canAccess());
        mineAccess.subscribe(applyAutoMineAccess);
        applyAutoMineAccess();
        window.addEventListener('ap:flag-changed', (ev) => {
            try {
                const detail = ev && ev.detail;
                if (detail && detail.key === 'enhancedAutoMine') {
                    applyAutoMineAccess();
                }
            } catch (_) { /* ignore */ }
        });
    }

    function toggleAutoMine(event) {
        if (!hasAutoMineAccess()) {
            return;
        }
        const el = event.currentTarget;
        mineState = !mineState;
        localStorage.setItem('autoMineState', mineState);
        el.classList.toggle('btn-success', mineState);
        el.classList.toggle('btn-danger', !mineState);
        el.textContent = `Auto Mine [${mineState ? 'ON' : 'OFF'}]`;
        mineState ? setAutoMineInterval() : clearInterval(autoMineTimer);
    }


    function setAutoMineInterval() {
        clearInterval(autoMineTimer);
        autoMineTimer = undefined;
        if (!mineState || !hasAutoMineAccess()) return;
        let interval = (20 - App.game.underground.undergroundLevel) * 50;
        if (interval < 100) {
            interval = 100;
        }
        autoMineTimer = setInterval(doAutoMine, interval);
    }

    function doAutoMine() {
        if (!mineState || !hasAutoMineAccess()) return;
        if (App.game.underground.undergroundLevel > mineLevel) {
            mineLevel = App.game.underground.undergroundLevel;
            setAutoMineInterval()
        }
        const mine = App.game.underground.mine;
        const tools = App.game.underground.tools;

        if (App.game.underground.loadingNewLayer) return;

        const battery = App.game.underground.battery;
        if (battery.charges === battery.maxCharges) battery.discharge();

        const bomb = tools.getTool(UndergroundToolType.Bomb);
        const hammer = tools.getTool(UndergroundToolType.Hammer);
        const chisel = tools.getTool(UndergroundToolType.Chisel);
        const grid = mine.grid;

        // if (bomb.durability >= bomb.durabilityPerUse) {
        //     const targetIndex = grid.findIndex(tile => tile && tile.layerDepth > 0);
        //     if (targetIndex !== -1) {
        //         tools.selectedToolType = UndergroundToolType.Bomb;
        //         UndergroundController.clickModalMineSquare(targetIndex);
        //         return;
        //     }
        // }

        const rewardTiles = grid
            .map((tile, index) => ({ tile, index }))
            .filter(({ tile }) => tile && tile.reward && tile.layerDepth > 0);

        if (rewardTiles.length > 0) {
            const target = rewardTiles[Math.floor(Math.random() * rewardTiles.length)];

            let toolToUse = null;
            if (hammer.durability >= hammer.durabilityPerUse) {
                toolToUse = UndergroundToolType.Hammer;
            } else if (chisel.durability >= chisel.durabilityPerUse) {
                toolToUse = UndergroundToolType.Chisel;
            }

            if (toolToUse !== null) {
                tools.selectedToolType = toolToUse;
                UndergroundController.clickModalMineSquare(target.index);
            }
        }
    }

    function waitForMineModal() {
        const modalCheck = setInterval(() => {
            const modal = document.querySelector('#mineModal .modal-body');
            if (modal && modal.children.length > 0) {
                clearInterval(modalCheck);
                initAutoMine();
            }
        }, 500);
    }

    function waitForGameLoad() {
        const interval = setInterval(() => {
            if (typeof App !== 'undefined' && App.game?.underground?.mine) {
                clearInterval(interval);
                waitForMineModal();
            }
        }, 100);
    }

    waitForGameLoad();
})();