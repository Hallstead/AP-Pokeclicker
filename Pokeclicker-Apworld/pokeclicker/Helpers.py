from typing import Optional, TYPE_CHECKING
from BaseClasses import MultiWorld, Item, Location
from worlds.AutoWorld import World

if TYPE_CHECKING:
    from .items import PokeclickerItem
    from .locations import PokeclickerLocation

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def is_category_enabled(world: World, category_name: str) -> Optional[bool]:
    if category_name == "Scripts":
        return bool(world.options.use_scripts) and bool(world.options.include_scripts_as_items)
    
    if category_name == "Shop":
        return False
    
    if category_name == "Not Implemented":
        return False

    if category_name in ["Johto", "Johto Pokemon", "Johto Badges"]:
        return bool(world.options.goal.value > 0)
    
    if category_name == "Hoenn":
        return bool(world.options.goal.value >= 1)

    if category_name == "Pokemon":
        return world.options.dexsanity.value >= 2
    
    if category_name == "Alt Pokemon":
        return bool(world.options.include_alt_pokemon)
    
    if category_name == "Seasonal Events":
        return bool(world.options.include_seasonal_events)

    if category_name == "Golden Week" or category_name == "Easter":
        return False
    
    if category_name == "Palaeontologist":
        return bool(world.options.include_palaeontologist_token)

    if category_name == "Squirtle Squad":
        return bool(world.options.include_black_glasses)
    
    if category_name == "Codes":
        return bool(world.options.include_codes_as_items)
    
    if category_name == "Mapsanity":
        return False
        return world.options.mapsanity.value >= 1

    if category_name == "Not Progressive Auto Clicker":
        return not bool(world.options.progressive_autoclicker)
    
    if category_name == "Progressive Auto Clicker":
        return bool(world.options.progressive_autoclicker)

    if category_name == "Not Progressive Safari Zone":
        return not bool(world.options.progressive_auto_safari_zone)

    if category_name == "Progressive Safari Zone":
        return bool(world.options.progressive_auto_safari_zone)

    if category_name == "Wanderers":
        return False

    return True

# # Use this if you want to override the default behavior of is_option_enabled
# # Return True to enable the item, False to disable it, or None to use the default behavior
# def before_is_item_enabled(multiworld: MultiWorld, player: int, item: "PokeclickerItem") -> Optional[bool]:
#     return None

# # Use this if you want to override the default behavior of is_option_enabled
# # Return True to enable the location, False to disable it, or None to use the default behavior
# def before_is_location_enabled(multiworld: MultiWorld, player: int, location: "PokeclickerLocation") -> Optional[bool]:
#     return None

def is_option_enabled(world: World, option_name: str) -> Optional[bool]:
    option = getattr(world.options, option_name, None)
    if option is None:
        return None
    return option.value > 0