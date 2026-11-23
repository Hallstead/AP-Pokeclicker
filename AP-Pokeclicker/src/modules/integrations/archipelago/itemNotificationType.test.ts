import { itemClassifications } from 'archipelago.js';
import { describe, expect, it } from 'vitest';
import NotificationOption from '../../notifications/NotificationOption';
import itemNotificationType from './itemNotificationType';

describe('Archipelago item notification type', () => {
    it('maps each item classification to its notification type', () => {
        expect(itemNotificationType(itemClassifications.progression)).toBe(NotificationOption.progression);
        expect(itemNotificationType(itemClassifications.useful)).toBe(NotificationOption.useful);
        expect(itemNotificationType(itemClassifications.none)).toBe(NotificationOption.filler);
        expect(itemNotificationType(itemClassifications.trap)).toBe(NotificationOption.trap);
    });

    it('prioritizes traps, then progression, for combined flags', () => {
        expect(itemNotificationType(itemClassifications.progression | itemClassifications.useful)).toBe(NotificationOption.progression);
        expect(itemNotificationType(itemClassifications.trap | itemClassifications.progression)).toBe(NotificationOption.trap);
    });

    it('keeps the previous notification type when classification is unavailable', () => {
        expect(itemNotificationType(undefined)).toBe(NotificationOption.success);
    });
});