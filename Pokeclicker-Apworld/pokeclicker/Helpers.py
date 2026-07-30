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
        return world.options.use_scripts and world.options.include_scripts_as_items
    
    if category_name == "Shop":
        return False
    
    if category_name == "Not Implemented":
        return False
    
    if category_name == "Alt Pokemon":
        return False
    
    if category_name == "Johto Pokemon":
        return False
    
    if category_name == "Alt Pokemon":
        return world.options.include_alt_pokemon
    
    if category_name == "Seasonal Events":
        return world.options.include_seasonal_events
    
    if category_name == "Palaeontologist":
        return world.options.include_palaeontologist_token
    
    if category_name == "Codes":
        return world.options.include_codes_as_items
    
    if category_name == "Mapsanity":
        return False
        return world.options.mapsanity.value >= 1

    if category_name == "Not Progressive Auto Clicker":
        return not world.options.progressive_autoclicker
    
    if category_name == "Progressive Auto Clicker":
        return world.options.progressive_autoclicker

    if category_name == "Not Progressive Safari Zone":
        return not world.options.progressive_auto_safari_zone

    if category_name == "Progressive Safari Zone":
        return world.options.progressive_auto_safari_zone

# # Use this if you want to override the default behavior of is_option_enabled
# # Return True to enable the item, False to disable it, or None to use the default behavior
# def before_is_item_enabled(multiworld: MultiWorld, player: int, item: "PokeclickerItem") -> Optional[bool]:
#     return None

# # Use this if you want to override the default behavior of is_option_enabled
# # Return True to enable the location, False to disable it, or None to use the default behavior
# def before_is_location_enabled(multiworld: MultiWorld, player: int, location: "PokeclickerLocation") -> Optional[bool]:
#     return None
