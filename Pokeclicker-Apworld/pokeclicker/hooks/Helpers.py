from typing import Optional, TYPE_CHECKING
from BaseClasses import MultiWorld, Item, Location

if TYPE_CHECKING:
    from ..Items import ManualItem
    from ..Locations import ManualLocation

from .. import Helpers

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "Scripts":
        return Helpers.is_option_enabled(multiworld, player, "use_scripts") and Helpers.is_option_enabled(multiworld, player, "include_scripts_as_items")
    
    if category_name == "Shop":
        return False
    
    if category_name == "Not Implemented":
        return False
    
    if category_name == "Alt Pokemon":
        return Helpers.is_option_enabled(multiworld, player, "include_alt_pokemon")
    
    if category_name == "Seasonal Events":
        return Helpers.is_option_enabled(multiworld, player, "use_scripts")
    
    if category_name == "Palaeontologist":
        return Helpers.is_option_enabled(multiworld, player, "include_palaeontologist_token")
    
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: "ManualItem") -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: "ManualLocation") -> Optional[bool]:
    return None
