import { itemClassifications } from 'archipelago.js';
import NotificationOption from '../../notifications/NotificationOption';

export default function itemNotificationType(flags: number | undefined): NotificationOption {
    if (typeof flags !== 'number') {
        return NotificationOption.success;
    }
    // Classification flags may be combined; prioritize traps, then progression.
    if (flags & itemClassifications.trap) return NotificationOption.trap;
    if (flags & itemClassifications.progression) return NotificationOption.progression;
    if (flags & itemClassifications.useful) return NotificationOption.useful;
    return NotificationOption.filler;
}