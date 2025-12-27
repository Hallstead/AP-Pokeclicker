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
        
        // --- APFlags gate: start hidden and OFF; show when APFlags.enhancedAutoMine is true ---
        function getAPEnhancedAutoMineFlag() {
            try {
                const flags = (window.APFlags ?? {});
                if (typeof flags.get === 'function') {
                    const v = flags.get('enhancedAutoMine');
                    if (typeof v !== 'undefined') return !!v;
                }
                if (Object.prototype.hasOwnProperty.call(flags, 'enhancedAutoMine')) {
                    return !!flags.enhancedAutoMine;
                }
            } catch (_) { /* ignore */ }
            return false;
        }
        function applyAutoMineAccessFromFlag(force) {
            const enabled = !!getAPEnhancedAutoMineFlag();
            const btn = document.getElementById('auto-mine-start');
            if (btn && !enabled) {
                btn.style.display = enabled ? '' : 'none';
            }
            if (!enabled || !App.game.underground.canAccess()) {
                // Ensure the feature is OFF when disabled
                mineState = false;
                try { clearInterval(autoMineTimer); } catch (_) { }
                if (btn) {
                    btn.classList.remove('btn-success');
                    if (!btn.classList.contains('btn-danger')) btn.classList.add('btn-danger');
                    btn.textContent = 'Auto Mine [OFF]';
                }
            } else {
                // When enabled, reflect persisted preference and start if ON
                if (btn) {
                    btn.classList.toggle('btn-success', !!mineState);
                    btn.classList.toggle('btn-danger', !mineState);
                    btn.textContent = `Auto Mine [${mineState ? 'ON' : 'OFF'}]`;
                }
                if (mineState) {
                    setTimeout(setAutoMineInterval, 100);
                }
            }
        }

        // Apply current APFlags state and subscribe for changes
        try { applyAutoMineAccessFromFlag(true); } catch (_) { }
        window.addEventListener('ap:flag-changed', (ev) => {
            try {
                const detail = ev && ev.detail;
                if (detail && detail.key === 'enhancedAutoMine') {
                    applyAutoMineAccessFromFlag(true);
                }
            } catch (_) { /* ignore */ }
        });

        if (mineState && getAPEnhancedAutoMineFlag()) {
            setTimeout(setAutoMineInterval, 1000);
        }
    }

    function toggleAutoMine(event) {
        // Guard: don't allow enabling if AP flag is false
        const flags = (window.APFlags ?? {});
        const enabled = !!flags.get('enhancedAutoMine');
        const el = event.target;
        if (!enabled) {
            // Force OFF state and UI (do not change persisted preference)
            mineState = false;
            try { clearInterval(autoMineTimer); } catch (_) { }
            el.classList.toggle('btn-success', false);
            el.classList.toggle('btn-danger', true);
            el.textContent = 'Auto Mine [OFF]';
            return;
        }
        mineState = !mineState;
        localStorage.setItem('autoMineState', mineState);
        el.classList.toggle('btn-success', mineState);
        el.classList.toggle('btn-danger', !mineState);
        el.textContent = `Auto Mine [${mineState ? 'ON' : 'OFF'}]`;
        mineState ? setAutoMineInterval() : clearInterval(autoMineTimer);
    }


    function setAutoMineInterval() {
        clearInterval(autoMineTimer);
        let interval = (20 - App.game.underground.undergroundLevel) * 50;
        if (interval < 100) {
            interval = 100;
        }
        autoMineTimer = setInterval(doAutoMine, interval);
    }

    function doAutoMine() {
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