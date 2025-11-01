import OakItemType from '../enums/OakItemType';
import { Currency } from '../GameConstants';
import BoughtOakItem from '../oakItems/BoughtOakItem';
import Item from './Item';

export default class BuyOakItem extends Item {
    item: OakItemType;
    locationId: number | null = null;

    constructor(item: OakItemType, basePrice: number, currency: Currency = Currency.questPoint, locationId = null) {
        super(OakItemType[item], basePrice, currency, { maxAmount: 1 }, undefined, 'Purchase to unlock this Oak Item');
        this.item = item;
        this.locationId = locationId;
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
        const oakItem = App.game.oakItems.itemList[this.item];
        if (oakItem instanceof BoughtOakItem) {
            (window as any).sendLocationCheck(this.locationId);
            oakItem.purchased = true;
        }
    }

    isAvailable(): boolean {
        const oakItem = App.game.oakItems.itemList[this.item];
        const purchased = (oakItem instanceof BoughtOakItem) ? oakItem.purchased : true;
        return super.isAvailable() && !purchased;
    }

    get image(): string {
        return `assets/images/oakitems/${this.name}.png`;
    }
}
