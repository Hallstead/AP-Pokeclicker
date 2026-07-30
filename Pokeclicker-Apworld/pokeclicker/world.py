from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import generate_basic, items, locations, regions, rules, web_world
from . import options as pokeclicker_options  # rename due to a name conflict with World.options

# APQuest will go through all the parts of the world api one step at a time,
# with many examples and comments across multiple files.
# If you'd rather read one continuous document, or just like reading multiple sources,
# we also have this document specifying the entire world api:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md


# The world class is the heart and soul of an apworld implementation.
# It holds all the data and functions required to build the world and submit it to the multiworld generator.
# You could have all your world code in just this one class, but for readability and better structure,
# it is common to split up world functionality into multiple files.
# This implementation in particular has the following additional files, each covering one topic:
# regions.py, locations.py, rules.py, items.py, options.py and web_world.py.
# It is recommended that you read these in that specific order, then come back to the world class.
class PokeclickerWorld(World):
    """
    APQuest is a minimal 8bit-era inspired adventure game with grid-like movement.
    Good games don't need more than six checks.
    """

    # The docstring should contain a description of the game, to be displayed on the WebHost.

    # You must override the "game" field to say the name of the game.
    game = "Pokeclicker"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.PokeclickerWebWorld()

    # This is how we associate the options defined in our options.py with our world.
    # (Note: options.py has been imported as "pokeclicker_options" at the top of this file to avoid a name conflict)
    options_dataclass = pokeclicker_options.PokeclickerOptions
    options: pokeclicker_options.PokeclickerOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = {location.name: location.id for location in locations.location_data.values()}
    item_name_to_id = items.item_name_to_id
    item_name_groups = items.item_groups
    location_name_groups = locations.location_name_groups
    location_data = locations.location_data

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Route 1"

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def generate_basic(self):
        generate_basic.before_generate_basic(self)
        generate_basic.generate_basic(self)

        

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.
    def create_item(self, name: str) -> items.PokeclickerItem:
        return items.create_item_with_correct_classification(self, name)

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "dexsanity",
            "include_alt_pokemon",
            "badge_randomization",
            "use_scripts",
            "include_scripts_as_items",
            "progressive_autoclicker",
            "progressive_auto_safari_zone",
            "include_seasonal_events",
            "include_codes_as_items",
            "include_palaeontologist_token",
            "starting_safari_level",
            "starting_underground_level",
            "roaming_encounter_multiplier",
            "roaming_encounter_multiplier_route",
            "pokedollar_multiplier",
            "dungeon_token_multiplier",
            "quest_point_multiplier",
            "diamond_multiplier",
            "farm_point_multiplier",
            "exp_multiplier",
            "wanderer_appearance_multiplier",
            "wanderer_base_catch_rate",
            "starter_logic",
            "early_town_map",
            "mystery_egg_in_logic",
            "clicks_per_second",
            "dungeon_logic",
            "safari_zone_logic",
            "wanderers_in_logic"
        )

    def interpret_slot_data(self, slot_data: dict[str, any]):
        #this is called by tools like UT
        if not slot_data:
            return False

        regen = False
        for key, value in slot_data.items():
            if key in self.options_dataclass.type_hints:
                getattr(self.options, key).value = value
                regen = True

        return regen
