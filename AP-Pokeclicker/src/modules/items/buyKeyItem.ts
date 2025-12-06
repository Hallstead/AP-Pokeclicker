import KeyItemType from '../enums/KeyItemType';
import { Currency } from '../GameConstants';
import Item from './Item';
import { ShopOptions } from './types';

export default class BuyKeyItem extends Item {
    item: KeyItemType;
    locationId: number | null = null;
    isPurchased: KnockoutObservable<boolean>;

    constructor(item: KeyItemType, basePrice: number, currency: Currency = Currency.questPoint, options?: ShopOptions, displayName?: string, locationId: number | null = null) {
        super(KeyItemType[item], basePrice, currency, { maxAmount: 1, ...options }, displayName);
        this.item = item;
        this.locationId = locationId;
        this.isPurchased =  ko.observable(false);
    }

    totalPrice(amount: number) {
        let amt = amount;
        if (amt > this.maxAmount) {
            amt = this.maxAmount;
        }
        return this.basePrice * amt;
    }

    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    gain(amt: number) {
        if (this.locationId !== null) {
            (window as any).sendLocationCheck(this.locationId);
            this.isPurchased(true);
        } else {
            App.game.keyItems.gainKeyItem(this.item);
        }
        // App.game.keyItems.gainKeyItem(this.item);
    }

    isSoldOut(): boolean {
        return this.isPurchased();
    }

    get image(): string {
        return `assets/images/keyitems/${this.name}.png`;
    }

    get description() {
        return App.game.keyItems.itemList[this.item].description;
    }
}
