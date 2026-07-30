
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from worlds.generic.Rules import forbid_items_for_player

from . import Helpers, items

if TYPE_CHECKING:
    from .world import PokeclickerWorld


def before_generate_basic(world: PokeclickerWorld):
    world.multiworld.early_items[world.player]["Town Map"] = world.options.early_town_map


    if world.options.dexsanity.value == 2: # Shuffled
        for location in world.location_data.values():
            if "Pokemon Locations" in location.groups:
                location.place_item_category = ["Pokemon"]
                
    # if world.options.mapsanity.value == 1: # Shuffled
    #     for location in location_name_to_location.keys():
    #         if "Mapsanity" in location_name_to_location[location]["category"]:
    #             world.location_name_to_location[location]["place_item_category"] = ["Mapsanity"]
    
    if world.options.badge_randomization.value == 0:
        for location_name in world.location_name_groups["Gyms"]:
            world.location_data[location_name].place_item = world.location_data[location_name].original_item
    # elif world.options.badge_randomization.value == 1:
    #     world.location_name_to_location["Brock"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Misty"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Lt. Surge"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Erika"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Koga"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Sabrina"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Blaine"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Giovanni"]["place_item_category"] = ["Badges"]
    #     world.location_name_to_location["Lorelei"]["place_item"] = ["Kanto Elite Lorelei Badge"]
    #     world.location_name_to_location["Bruno"]["place_item"] = ["Kanto Elite Bruno Badge"]
    #     world.location_name_to_location["Agatha"]["place_item"] = ["Kanto Elite Agatha Badge"]
    #     world.location_name_to_location["Lance"]["place_item"] = ["Kanto Elite Lance Badge"]

    # world.location_name_to_location["Kanto Route 1 - 1"]["place_item"] = ["Kanto Route 22"]
    # world.location_name_to_location["Kanto Route 1 - 2"]["place_item"] = ["Kanto Route 2"]
    # world.location_name_to_location["Kanto Route 1 - 3"]["place_item"] = ["Pallet Town"]
    # world.location_name_to_location["Kanto Route 1 - 4"]["place_item"] = ["Viridian City"]
    # world.location_name_to_location["Kanto Route 2"]["place_item"] = ["Viridian Forest"]
    # world.location_name_to_location["Kanto Route 3 - 1"]["place_item"] = ["Mt. Moon"]
    # world.location_name_to_location["Kanto Route 3 - 2"]["place_item"] = ["Kanto Route 4 Pokemon Center"]
    # world.location_name_to_location["Kanto Route 4"]["place_item"] = ["Cerulean City"]
    # world.location_name_to_location["Kanto Route 24"]["place_item"] = ["Kanto Route 25"]
    # world.location_name_to_location["Kanto Route 25 - 1"]["place_item"] = ["Kanto Route 5"]
    # world.location_name_to_location["Kanto Route 25 - 2"]["place_item"] = ["Bill's House"]
    # world.location_name_to_location["Kanto Route 5"]["place_item"] = ["Kanto Route 6"]
    # world.location_name_to_location["Kanto Route 6 - 1"]["place_item"] = ["Kanto Route 11"]
    # world.location_name_to_location["Kanto Route 6 - 2"]["place_item"] = ["Diglett's Cave"]
    # world.location_name_to_location["Kanto Route 6 - 3"]["place_item"] = ["Vermilion City"]
    # world.location_name_to_location["Kanto Route 9"]["place_item"] = ["Kanto Route 10"]
    # world.location_name_to_location["Kanto Route 10"]["place_item"] = ["Rock Tunnel"]
    # world.location_name_to_location["Kanto Route 8"]["place_item"] = ["Kanto Route 7"]
    # world.location_name_to_location["Kanto Route 7 - 1"]["place_item"] = ["Celadon City"]
    # world.location_name_to_location["Kanto Route 7 - 2"]["place_item"] = ["Rocket Game Corner"]
    # world.location_name_to_location["Kanto Route 13 or 15"]["place_item"] = ["Kanto Route 14"]
    # world.location_name_to_location["Kanto Route 14 or 18"]["place_item"] = ["Kanto Route 15"]
    # world.location_name_to_location["Kanto Route 14 or Snorlax (Route 12)"]["place_item"] = ["Kanto Route 13"]
    # world.location_name_to_location["Kanto Route 15 or 17"]["place_item"] = ["Kanto Route 18"]
    # world.location_name_to_location["Kanto Route 15 or 18"]["place_item"] = ["Fuchsia City"]
    # world.location_name_to_location["Kanto Route 16 or 18"]["place_item"] = ["Kanto Route 17"]
    # world.location_name_to_location["Kanto Route 17 or Snorlax (Route 16)"]["place_item"] = ["Kanto Route 16"]
    # world.location_name_to_location["Kanto Route 19"]["place_item"] = ["Seafoam Islands"]
    # world.location_name_to_location["Kanto Route 20 or 21 - 1"]["place_item"] = ["Cinnabar Island"]
    # world.location_name_to_location["Kanto Route 20 or 21 - 2"]["place_item"] = ["Pokemon Mansion"]
    # world.location_name_to_location["Kanto Route 21 or Seafoam Islands"]["place_item"] = ["Kanto Route 20"]
    # world.location_name_to_location["Kanto Route 23"]["place_item"] = ["Victory Road"]
    # world.location_name_to_location["Kindle Road - 1"]["place_item"] = ["Mt. Ember"]
    # world.location_name_to_location["Kindle Road - 2"]["place_item"] = ["Mt. Ember Summit"]
    # world.location_name_to_location["Bond Bridge"]["place_item"] = ["Berry Forest"]
    # world.location_name_to_location["Brock - 2"]["place_item"] = ["Kanto Route 3"]
    # world.location_name_to_location["Erika or Rocket Game Corner"]["place_item"] = ["Saffron City"]
    # world.location_name_to_location["Koga - 2"]["place_item"] = ["Kanto Route 19"]
    # world.location_name_to_location["Koga - 3"]["place_item"] = ["Kanto Route 21"]
    # world.location_name_to_location["Koga - 4"]["place_item"] = ["Power Plant"]
    # world.location_name_to_location["Blaine - 2"]["place_item"] = ["One Island"]
    # world.location_name_to_location["Blaine - 3"]["place_item"] = ["Kindle Road"]
    # world.location_name_to_location["Blaine - 4"]["place_item"] = ["Treasure Beach"]
    # world.location_name_to_location["Blaine - 5"]["place_item"] = ["Client Island"]
    # world.location_name_to_location["Champion Blue - 2"]["place_item"] = ["Cerulean Cave"]
    # world.location_name_to_location["Viridian Forest - 2"]["place_item"] = ["Pewter City"]
    # world.location_name_to_location["Mt. Moon - 2"]["place_item"] = ["Kanto Route 4"]
    # world.location_name_to_location["Rock Tunnel - 2"]["place_item"] = ["Lavender Town"]
    # world.location_name_to_location["Rock Tunnel - 3"]["place_item"] = ["Kanto Route 12"]
    # world.location_name_to_location["Rock Tunnel - 4"]["place_item"] = ["Kanto Route 8"]
    # world.location_name_to_location["Rocket Game Corner - 2"]["place_item"] = ["Pokemon Tower"]
    # world.location_name_to_location["Victory Road - 2"]["place_item"] = ["Indigo Plateau Kanto"]
    # world.location_name_to_location["Blue 2 - 2"]["place_item"] = ["Kanto Route 24"]
    # world.location_name_to_location["Blue 3 - 2"]["place_item"] = ["Kanto Route 9"]
    # world.location_name_to_location["Blue 4 - 2"]["place_item"] = ["Silph Co."]
    # world.location_name_to_location["Blue 6 - 2"]["place_item"] = ["Kanto Route 23"]
    # world.location_name_to_location["Bill's Errand Questline; Speak with Celio on One Island - 1"]["place_item"] = ["Two Island"]
    # world.location_name_to_location["Bill's Errand Questline; Speak with Celio on One Island - 2"]["place_item"] = ["Cape Brink"]
    # world.location_name_to_location["Bill's Errand Questline; Ask the Game Corner owner on Two Island about the meteorite"]["place_item"] = ["Three Island"]
    # world.location_name_to_location["Bill's Errand Questline; Defeat the biker gang's leader"]["place_item"] = ["Bond Bridge"]
    # world.location_name_to_location["Unfinished Business; Talk to Professor Oak in Pallet Town."]["place_item"] = ["Professor Ivy's Lab"]

def generate_basic(world):
    def _as_list(value):
        if value is None:
            return []
        if isinstance(value, list):
            return value
        return [value]

    # Handle item forbidding
    manual_locations_with_forbid = {location.name: location for location in world.location_data.values() if location.dont_place_item or location.dont_place_item_category}
    locations_with_forbid = [l for l in world.multiworld.get_unfilled_locations(player=world.player) if l.name in manual_locations_with_forbid.keys()]
    for location in locations_with_forbid:
        manual_location = manual_locations_with_forbid[location.name]
        forbidden_item_names = []

        if manual_location.dont_place_item:
            forbidden_item_names.extend([i for i in items.item_table.keys() if i in manual_location.dont_place_item])

        if manual_location.dont_place_item_category:
            forbidden_item_names.extend([
                item_name
                for item_name, item_data in items.item_table.items()
                if set(item_data.groups).intersection(manual_location.dont_place_item_category)
            ])

        if forbidden_item_names:
            forbid_items_for_player(location, set(forbidden_item_names), world.player)

    # Handle specific item placements using fill_restrictive
    manual_locations_with_placements = {location.name: location for location in world.location_data.values() if location.place_item or location.place_item_category}
    locations_with_placements = [l for l in world.multiworld.get_unfilled_locations(player=world.player) if l.name in manual_locations_with_placements.keys()]
    for location in locations_with_placements:
        location_data = manual_locations_with_placements[location.name]
        eligible_items = []
        eligible_item_names = []
        forbidden_item_names = []
        place_messages = []
        forbid_messages = []

        #First we get possible items names
        if location_data.place_item:
            place_item_names = _as_list(location_data.place_item)
            eligible_item_names += place_item_names
            place_messages.append('", "'.join(place_item_names))

        if location_data.place_item_category:
            eligible_item_names += [
                item_name
                for item_name, item_data in items.item_table.items()
                if set(item_data.groups).intersection(location_data.place_item_category)
            ]
            place_messages.append('", "'.join(location_data.place_item_category) + " category(ies)")

        # Second we check for forbidden items names
        if location_data.dont_place_item:
            dont_place_item_names = _as_list(location_data.dont_place_item)
            forbidden_item_names += dont_place_item_names
            forbid_messages.append('", "'.join(dont_place_item_names) + ' items')

        if location_data.dont_place_item_category:
            forbidden_item_names += [
                item_name
                for item_name, item_data in items.item_table.items()
                if set(item_data.groups).intersection(location_data.dont_place_item_category)
            ]
            forbid_messages.append('", "'.join(location_data.dont_place_item_category) + ' category(ies)')

        # If we forbid some names, check for those in the possible names and remove them
        if forbidden_item_names:
            eligible_item_names = [name for name in eligible_item_names if name not in forbidden_item_names]

        if eligible_item_names:
            eligible_items = [item for item in world.multiworld.itempool if item.player == world.player and item.name in eligible_item_names]

        if len(eligible_items) == 0:
            nl = "\n"
            if forbidden_item_names:
                raise Exception(f'Could not find a suitable item to place at "{location_data.name}".\n    No items that match "{f"{nl}     or ".join(place_messages)}"\n    Maybe because of forbidden "{f"{nl}     or ".join(forbid_messages)}"')
            raise Exception(f'Could not find a suitable item to place at "{location_data.name}". \n    No items that match "{f"{nl}     or ".join(place_messages)}"')

        print(f'Placing item at location "{location_data.name}"')
        item_to_place = world.random.choice(eligible_items)
        location.place_locked_item(item_to_place)

        # remove the item we're about to place from the pool so it isn't placed twice
        world.multiworld.itempool.remove(item_to_place)
