// Note: avoid importing Knockout types here to prevent TS resolution issues; use `any` for internal observables
import { Currency } from '../GameConstants';
import GameHelper from '../GameHelper';
import ExpUpgrade from '../upgrades/ExpUpgrade';
import Amount from '../wallet/Amount';
import AmountFactory from '../wallet/AmountFactory';

export default class OakItem extends ExpUpgrade {
    defaults = {
        level: 0,
        exp: 0,
        isActive: false,
    };

    private isActiveKO: any;
    private receivedKO: any;
    private locationID: number | null;
    private locationSent: boolean;
    private levelLocationIds: number[];

    constructor(
        name: any,
        displayName: string,
        public description: string,
        increasing: boolean,
        bonusList: number[],
        public inactiveBonus: number,
        public unlockReq: number,
        public expGain: number,
        expList: number[] = [500, 1000, 2500, 5000, 10000],
        maxLevel = 5,
        costList: Amount[] = AmountFactory.createArray([50000, 100000, 250000, 500000, 1000000], Currency.money),
        public bonusSymbol: string = '×',
        locationID: number | null = null,
        locationSent: boolean = false,
        levelLocationIds: number[] = [],
    ) {
        super(name, displayName, maxLevel, expList, costList, bonusList, increasing);
        this.isActiveKO = ko.observable(false);
        this.receivedKO = ko.observable(false);
        this.locationID = locationID;
        this.locationSent = locationSent;
        this.levelLocationIds = levelLocationIds;
    }

    use(exp: number = this.expGain, scale = 1) {
        if (!this.isActive) {
            return;
        }
        if (!this.isMaxLevel()) {
            this.gainExp(exp * scale);
        }
        GameHelper.incrementObservable(App.game.statistics.oakItemUses[this.name]);
    }

    isUnlocked(): boolean {
        try {
            // Only attempt to send once, and only if we have a valid location id
            if (!this.locationSent && this.locationID != null && App.game.party.caughtPokemon.length >= this.unlockReq) {
                (window as any).sendLocationCheck?.(this.locationID);
                this.locationSent = true;
            }
        } catch (e) {
            // Don't let network issues break KO bindings; log and continue
            try { console.warn('[OakItem] Failed to send LocationCheck for', this.name, e); } catch (_) { /* noop */ }
        }
        return this.received;
    }

    isChecked(): boolean {
        return App.game.party.caughtPokemon.length >= this.unlockReq;
    }

    // TODO: do we need both of these hint methods?
    getHint(): string {
        return `Capture ${this.unlockReq - App.game.party.caughtPokemon.length} more unique Pokémon`;
    }

    get hint() {
        return ko.pureComputed(() => `Capture ${this.unlockReq - App.game.party.caughtPokemon.length} more unique Pokémon`);
    }

    calculateBonus(level: number = this.level): number {
        if (!this.isActive) {
            return this.inactiveBonus;
        }
        return super.calculateBonus(level);
    }

    calculateBonusIfActive(level: number = this.level) {
        return super.calculateBonus(level);
    }

    toJSON(): Record<string, any> {
        const json = super.toJSON();
        json.isActive = this.isActive;
        return json;
    }

    fromJSON(json: Record<string, any>): void {
        super.fromJSON(json);
        this.isActive = json.isActive ?? this.defaults.isActive;
    }

    // Knockout getters/setters
    get expPercentage() {
        const nextLevelExp = this.level === 0 ? this.expList[this.level] : this.expList[this.level] - this.expList[this.level - 1];
        return (Math.ceil(this.normalizedExp / this.expGain) / Math.ceil(nextLevelExp / this.expGain)) * 100;
    }

    get progressString(): string {
        const nextLevelExp = this.level === 0 ? this.expList[this.level] : this.expList[this.level] - this.expList[this.level - 1];
        return `${Math.ceil(this.normalizedExp / this.expGain).toLocaleString('en-US')} / ${Math.ceil(nextLevelExp / this.expGain).toLocaleString('en-US')}`;
    }

    get isActive() {
        return this.isActiveKO();
    }

    set isActive(bool: boolean) {
        this.isActiveKO(bool);
    }

    get bonusText(): string {
        return `${this.calculateBonusIfActive()}${this.bonusSymbol}`;
    }

    get tooltip() {
        return ko.pureComputed(() => `<u>${this.displayName}</u><br/><p>${this.description}</p>Level: <strong>${this.level}/${this.maxLevel}</strong><br/>Bonus: <strong>${this.bonusText}</strong>`);
    }

    get received(): boolean {
        return this.receivedKO();
    }

    set received(bool: boolean) {
        this.receivedKO(bool);
    }

    buy(): void {
        let level = this.level;
        super.buy();
        if (this.level > level) {
            (window as any).sendLocationCheck?.(this.levelLocationIds[this.level - 1]);
        }
    }
}
