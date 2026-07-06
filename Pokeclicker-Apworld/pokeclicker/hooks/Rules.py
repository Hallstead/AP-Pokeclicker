from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"


# Kanto
def kanto_route_1(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 1."""
    return True

def pallet_town(world: World, state: CollectionState, player: int):
    """Checks if the player can access Pallet Town."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pallet Town", player) > 0
    #     return has_location
    has_town_map = state.count("Town Map", player) > 0
    return kanto_route_1(world, state, player) and has_town_map

def kanto_route_22(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 22."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 22", player) > 0
        return has_location
    return kanto_route_1(world, state, player)

def kanto_route_2(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 2."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 2", player) > 0
        return has_location
    return kanto_route_1(world, state, player)

def viridian_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Viridian City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Viridian City", player) > 0
    #     return has_location
    return kanto_route_1(world, state, player)

def viridian_forest(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Viridian Forest."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 102
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Viridian Forest", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_2(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def pewter_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Pewter City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pewter City", player) > 0
    #     return has_location
    return viridian_forest(world, state, player)

def kanto_route_3(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 3."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 3", player) > 0
        return has_location
    has_boulder_badge = state.count("Boulder Badge", player) > 0
    return has_boulder_badge

def mt_moon(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mt. Moon."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 834
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Mt. Moon", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_3(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_4_pokecenter(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 4 Pokecenter."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 4 Pokemon Center", player) > 0
    #     return has_location
    return kanto_route_3(world, state, player)

def kanto_route_4(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 4."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 4", player) > 0
        return has_location
    return mt_moon(world, state, player)

def cerulean_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Cerulean City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Cerulean City", player) > 0
    #     return has_location
    return kanto_route_4(world, state, player)

def kanto_route_24(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 24."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 24", player) > 0
        return has_location
    return kanto_route_4(world, state, player) and attack_needed(world, state, player, 14041)

def kanto_route_25(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 25."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 25", player) > 0
        return has_location
    return kanto_route_24(world, state, player)

def bills_house(world: World, state: CollectionState, player: int):
    """Checks if the player can access Bill's House."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Bill's House", player) > 0
    #     return has_location
    return kanto_route_25(world, state, player)

def kanto_route_5(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 5."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 5", player) > 0
        return has_location
    return kanto_route_25(world, state, player)

def kanto_route_6(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 6."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 6", player) > 0
        return has_location
    return kanto_route_5(world, state, player)

def vermilion_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Vermilion City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Vermilion City", player) > 0
    #     return has_location
    return kanto_route_6(world, state, player)

def kanto_route_11(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 11."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 11", player) > 0
        return has_location
    return kanto_route_6(world, state, player)

def digletts_cave(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Diglett's Cave."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 2962
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Diglett's Cave", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_6(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_9(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 9."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 9", player) > 0
        return has_location
    has_cascade_badge = state.count("Cascade Badge", player) > 0
    return vermilion_city(world, state, player) and attack_needed(world, state, player, 50431) and has_cascade_badge

def power_plant(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Power Plant."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 13507
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Power Plant", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    has_soul_badge = state.count("Soul Badge", player) > 0
    return kanto_route_9(world, state, player) and has_soul_badge and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_10(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 10."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 10", player) > 0
        return has_location
    return kanto_route_9(world, state, player)

def rock_tunnel(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Rock Tunnel."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 2048
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Rock Tunnel", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_10(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def lavender_town(world: World, state: CollectionState, player: int):
    """Checks if the player can access Lavender Town."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Lavender Town", player) > 0
    #     return has_location
    return rock_tunnel(world, state, player)

def pokemon_tower(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Pokemon Tower."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 7523
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pokemon Tower", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return lavender_town(world, state, player) and rocket_game_corner(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_12(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 12."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 12", player) > 0
        return has_location
    return rock_tunnel(world, state, player)

def kanto_route_8(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 8."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 8", player) > 0
        return has_location
    return rock_tunnel(world, state, player)

def saffron_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Saffron City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Saffron City", player) > 0
    #     return has_location
    has_rainbow_badge = state.count("Rainbow Badge", player) > 0
    return celadon_city(world, state, player) or has_rainbow_badge

def silph_co(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Sylph Co. building."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 10515
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Silph Co.", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return saffron_city(world, state, player) and pokemon_tower(world, state, player) and attack_needed(world, state, player, 151990) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_7(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 7."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 7", player) > 0
        return has_location
    return kanto_route_8(world, state, player)

def celadon_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Celadon City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Celadon City", player) > 0
    #     return has_location
    return kanto_route_7(world, state, player)

def rocket_game_corner(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Rocket Game Corner."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 5820
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Rocket Game Corner", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return celadon_city(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_13(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 13."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 13", player) > 0
        return has_location
    return pokemon_tower(world, state, player)

def kanto_route_14(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 14."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 14", player) > 0
        return has_location
    return kanto_route_13(world, state, player)

def kanto_route_15(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 15."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 15", player) > 0
        return has_location
    return kanto_route_14(world, state, player)

def kanto_route_16(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 16."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 16", player) > 0
        return has_location
    return pokemon_tower(world, state, player)

def kanto_route_17(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 17."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 17", player) > 0
        return has_location
    return kanto_route_16(world, state, player)

def kanto_route_18(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 18."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 18", player) > 0
        return has_location
    return kanto_route_17(world, state, player)

def fuchsia_city(world: World, state: CollectionState, player: int):   
    """Checks if the player can access Fuchsia City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Fuchsia City", player) > 0
    #     return has_location
    return kanto_route_15(world, state, player) or kanto_route_18(world, state, player)

def safari_zone(world: World, state: CollectionState, player: int):
    """Checks if the player can access the Safari Zone."""
    has_safari_ticket = state.count("Safari Ticket", player) > 0
    completed_tutorial = state.count("Tutorial Complete", player) > 0
    
    if world.options.safari_zone_logic.value and world.options.use_scripts.value and world.options.include_scripts_as_items.value:
        return has_safari_ticket and completed_tutorial and (state.count("Auto Safari Zone", player) > 0 or state.count("Auto Safari Zone (Progressive Fast Animations)", player) > 0)
    else:
        return has_safari_ticket and completed_tutorial

def kanto_route_19(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 19."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 19", player) > 0
        return has_location
    has_soul_badge = state.count("Soul Badge", player) > 0
    return has_soul_badge

def seafoam_islands(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Seafoam Islands."""
    had_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 17226
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Seafoam Islands", player) > 0
    #     return has_location and had_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    has_rainbow_badge = state.count("Rainbow Badge", player) > 0
    return kanto_route_19(world, state, player) and has_rainbow_badge and had_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_20(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 20."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 20", player) > 0
        return has_location
    return kanto_route_21(world, state, player) or seafoam_islands(world, state, player)

def kanto_route_21(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 21."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 21", player) > 0
        return has_location
    has_soul_badge = state.count("Soul Badge", player) > 0
    return has_soul_badge

def cinnabar_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Cinnabar Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Cinnabar Island", player) > 0
    #     return has_location
    return kanto_route_21(world, state, player)

def pokemon_mansion(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Pokemon Mansion."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 17760
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pokemon Mansion", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return cinnabar_island(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_23(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 23."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kanto Route 23", player) > 0
        return has_location
    has_earth_badge = state.count("Earth Badge", player) > 0
    return kanto_route_22(world, state, player) and has_earth_badge and attack_needed(world, state, player, 426771)

def victory_road(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Victory Road."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 24595
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Victory Road", player) > 0
    #     return has_location
    return kanto_route_23(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def indigo_plateau(world: World, state: CollectionState, player: int):
    """Checks if the player can access Indigo Plateau."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Indigo Plateau Kanto", player) > 0
    #     return has_location
    return victory_road(world, state, player)

def cerulean_cave(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Cerulean Cave."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 28735
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Cerulean Cave", player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    has_elite_champion_badge = state.count("Kanto Elite Champion Badge", player) > 0
    return has_elite_champion_badge and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def new_island(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access New Island dungeon in Kanto."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    has_infinite_seasonal_events = has_script(world, state, player, "Infinite Seasonal Events")
    minion_attack = 18500
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("New Island", player) > 0
    #     return has_location and has_dungeon_ticket and has_infinite_seasonal_events and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)
    return has_dungeon_ticket and has_infinite_seasonal_events and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

# Kanto - Sevii Islands 123
def one_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Sevii One Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("One Island", player) > 0
    #     return has_location
    has_volcano_badge = state.count("Volcano Badge", player) > 0
    return has_volcano_badge

def treasure_beach(world: World, state: CollectionState, player: int):
    """Checks if the player can access Treasure Beach on Sevii One Island."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Treasure Beach", player) > 0
        return has_location
    has_volcano_badge = state.count("Volcano Badge", player) > 0
    return has_volcano_badge

def kindle_road(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kindle Road on Sevii One Island."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Kindle Road", player) > 0
        return has_location
    has_volcano_badge = state.count("Volcano Badge", player) > 0
    return has_volcano_badge

def mount_ember(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mount Ember on Sevii One Island."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 18120
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Mt. Ember Summit", player) > 0
    #     return has_location
    return kindle_road(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def two_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Sevii Two Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Two Island", player) > 0
    #     return has_location
    return bills_errand1(world, state, player)

def cape_brink(world: World, state: CollectionState, player: int):
    """Checks if the player can access Sevii Cape Brink."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Cape Brink", player) > 0
        return has_location
    return two_island(world, state, player)

def three_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Sevii Three Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Three Island", player) > 0
    #     return has_location
    return bills_errand2(world, state, player)

def bond_bridge(world: World, state: CollectionState, player: int):
    """Checks if the player can access Bond Bridge on Sevii Three Island."""
    if world.options.mapsanity.value > 0:
        has_location = state.count("Bond Bridge", player) > 0
        return has_location
    return three_island(world, state, player) and attack_needed(world, state, player, 443328)

def berry_forest(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Berry Forest on Sevii Three Island."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 18120
    return bond_bridge(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def professor_ivys_lab(world: World, state: CollectionState, player: int):
    """Checks if the player can access Professor Ivy's Lab."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Professor Ivy's Lab", player) > 0
    #     return has_location
    return True
    

# Eggs and Stones
def can_get_grass_egg(world: World, state: CollectionState, player: int):
    """Checks if the player can obtain a Grass Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    has_hatchery = state.count("Mystery Egg", player) > 0
    return (lavender_town(world, state, player) or can_get_mystery_egg(world, state, player)) and tutorial_complete and has_hatchery

def can_get_fire_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Fire Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    has_hatchery = state.count("Mystery Egg", player) > 0
    return (cinnabar_island(world, state, player) or can_get_mystery_egg(world, state, player)) and tutorial_complete and has_hatchery

def can_get_water_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Water Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    has_hatchery = state.count("Mystery Egg", player) > 0
    return (cerulean_city(world, state, player) or can_get_mystery_egg(world, state, player)) and tutorial_complete and has_hatchery

def can_get_electric_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain an Electric Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    has_hatchery = state.count("Mystery Egg", player) > 0
    return (vermilion_city(world, state, player) or can_get_mystery_egg(world, state, player)) and tutorial_complete and has_hatchery

def can_get_fighting_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Fighting Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    has_hatchery = state.count("Mystery Egg", player) > 0
    return (saffron_city(world, state, player) or can_get_mystery_egg(world, state, player)) and tutorial_complete and has_hatchery

def can_get_dragon_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Dragon Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    has_hatchery = state.count("Mystery Egg", player) > 0
    return (fuchsia_city(world, state, player) or can_get_mystery_egg(world, state, player)) and tutorial_complete and has_hatchery

def can_get_mystery_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Mystery Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    has_hatchery = state.count("Mystery Egg", player) > 0
    enabled = world.options.mystery_egg_in_logic.value
    return enabled and pewter_city(world, state, player) and tutorial_complete and has_hatchery

def can_get_moon_stone(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Moon Stone."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return saffron_city(world, state, player) and tutorial_complete

def can_get_leaf_stone(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Leaf Stone."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return saffron_city(world, state, player) and tutorial_complete

def can_get_fire_stone(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Fire Stone."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return cinnabar_island(world, state, player) and tutorial_complete

def can_get_water_stone(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Water Stone."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return cerulean_city(world, state, player) and tutorial_complete

def can_get_thunder_stone(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Thunder Stone."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return vermilion_city(world, state, player) and tutorial_complete

def can_get_linking_cord(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Linking Cord."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return fuchsia_city(world, state, player) and tutorial_complete


# Questlines
def bills_grandpas_treasure_hunt1(world: World, state: CollectionState, player: int):
    """Checks if the first step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return pallet_town(world, state, player) and bills_house(world, state, player)

def can_catch_jigglypuff(world: World, state: CollectionState, player: int):
    """Checks if the player can catch Jigglypuff."""
    return kanto_route_3(world, state, player)

def bills_grandpas_treasure_hunt2(world: World, state: CollectionState, player: int):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpas_treasure_hunt1(world, state, player) and can_catch_jigglypuff(world, state, player)

def can_catch_oddish(world: World, state: CollectionState, player: int):
    """Checks if the player can catch Oddish."""
    return kanto_route_24(world, state, player) or kanto_route_25(world, state, player) or kanto_route_5(world, state, player) or kanto_route_6(world, state, player) or kanto_route_8(world, state, player) or kanto_route_7(world, state, player) or kanto_route_12(world, state, player) or kanto_route_13(world, state, player) or kanto_route_14(world, state, player) or kanto_route_15(world, state, player) or cape_brink(world, state, player) or bond_bridge(world, state, player) or berry_forest(world, state, player, False) # Oddish

def bills_grandpas_treasure_hunt3(world: World, state: CollectionState, player: int):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpas_treasure_hunt2(world, state, player) and can_catch_oddish(world, state, player)

def can_catch_staryu(world: World, state: CollectionState, player: int):
    """Checks if the player can catch Staryu."""
    return kanto_route_20(world, state, player) or kanto_route_21(world, state, player)

def bills_grandpas_treasure_hunt4(world: World, state: CollectionState, player: int):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpas_treasure_hunt3(world, state, player) and can_catch_staryu(world, state, player)

def can_catch_growlithe(world: World, state: CollectionState, player: int):
    """Checks if the player can catch Growlithe."""
    return kanto_route_8(world, state, player) or kanto_route_7(world, state, player) or pokemon_mansion(world, state, player, False)

def bills_grandpas_treasure_hunt5(world: World, state: CollectionState, player: int):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpas_treasure_hunt4(world, state, player) and can_catch_growlithe(world, state, player)

def can_catch_pikachu(world: World, state: CollectionState, player: int):
    """Checks if the player can catch Pikachu."""
    return viridian_forest(world, state, player, True) or power_plant(world, state, player, False)

def bills_grandpas_treasure_hunt6(world: World, state: CollectionState, player: int):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpas_treasure_hunt5(world, state, player) and can_catch_pikachu(world, state, player)

def completed_bills_grandpas_treasure_hunt(world: World, state: CollectionState, player: int):
    """Checks if the player has completed Bill's Grandpa's Treasure Hunt questline."""
    return bills_grandpas_treasure_hunt6(world, state, player) and attack_needed(world, state, player, 525000)

def started_bills_errand(world: World, state: CollectionState, player: int):
    """Checks if the player has started Bill's Errand questline."""
    return cinnabar_island(world, state, player) and pokemon_mansion(world, state, player) and attack_needed(world, state, player, 175290) # Beat Blaine

def bills_errand1(world: World, state: CollectionState, player: int):
    """Checks if the first step of Bill's Errand questline can be completed."""
    return started_bills_errand(world, state, player) and one_island(world, state, player)

def bills_errand2(world: World, state: CollectionState, player: int):
    """Checks if the second step of Bill's Errand questline can be completed."""
    return bills_errand1(world, state, player) and two_island(world, state, player)

def bills_errand3(world: World, state: CollectionState, player: int):
    """Checks if the third step of Bill's Errand questline can be completed."""
    return bills_errand2(world, state, player) and three_island(world, state, player) and attack_needed(world, state, player, 396954)

def bills_errand4(world: World, state: CollectionState, player: int):
    """Checks if the fourth step of Bill's Errand questline can be completed."""
    return bills_errand3(world, state, player) and three_island(world, state, player) and attack_needed(world, state, player, 443328)

def completed_bills_errand(world: World, state: CollectionState, player: int):
    """Checks if the fifth step of Bill's Errand questline can be completed."""
    return bills_errand4(world, state, player) and berry_forest(world, state, player)

def unfinished_business1(world: World, state: CollectionState, player: int):
    """Checks if the player has started the Unfinished Business questline."""
    return pallet_town(world, state, player) and completed_bills_errand(world, state, player)


# Special Conditions
def any_kanto_route(world: World, state: CollectionState, player: int):
    """Checks if the player can access any Kanto route."""
    return (kanto_route_1(world, state, player) or kanto_route_2(world, state, player) or kanto_route_3(world, state, player) or
            kanto_route_4(world, state, player) or kanto_route_5(world, state, player) or kanto_route_6(world, state, player) or
            kanto_route_7(world, state, player) or kanto_route_8(world, state, player) or kanto_route_9(world, state, player) or
            kanto_route_10(world, state, player) or kanto_route_11(world, state, player) or kanto_route_12(world, state, player) or
            kanto_route_13(world, state, player) or kanto_route_14(world, state, player) or kanto_route_15(world, state, player) or
            kanto_route_16(world, state, player) or kanto_route_17(world, state, player) or kanto_route_18(world, state, player) or
            kanto_route_19(world, state, player) or kanto_route_20(world, state, player) or kanto_route_21(world, state, player) or
            kanto_route_22(world, state, player) or kanto_route_23(world, state, player) or kanto_route_24(world, state, player) or
            kanto_route_25(world, state, player))

def can_catch_x_pokemon(world: World, state: CollectionState, player: int, x: int):
    """Checks if the player can obtain at least X pokemon."""
    return state.count_group("Pokemon", player) >= int(x)

def get_party_attack(world: World, state: CollectionState, player: int, num_pokemon: int) -> set:
    """Returns the attack value of the player's expected current party."""
    num_badges = 0
    badge_list = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge", "Volcano Badge", "Earth Badge", "Kanto Elite Lorelei Badge", "Kanto Elite Bruno Badge", "Kanto Elite Agatha Badge", "Kanto Elite Lance Badge", "Kanto Elite Champion Badge"]
    for badge in badge_list:
        num_badges += state.count(badge, player)

    avgBaseAttack = 70 + 4.2 * num_badges
    avgLevel = min(100, 20 + 10 * num_badges)
    return num_pokemon * avgBaseAttack * (avgLevel / 100)

def get_click_attack(world: World, state: CollectionState, player: int, num_pokemon: int) -> set:
    """Returns the attack value of the player's expected clicker attack."""
    has_shiny_code = state.count("Shiny-Charmer Code", player) > 0
    has_rocky_helmet = state.count("Rocky Helmet", player) > 0
    if has_shiny_code:
        num_pokemon += 1
    attack = (1 + num_pokemon) ** 1.4
    if has_rocky_helmet:
        attack *= 1.4
    return attack
    
def attack_needed(world: World, state: CollectionState, player: int, attack: int):
    """Checks if the player's expected current party attack is at least X."""
    num_pokemon = state.count_group("Pokemon", player) #len(get_catchable_pokemon(world, state, player))
    auto_clicker_count = state.count("Enhanced Auto Clicker", player)
    if world.options.use_scripts.value and not world.options.include_scripts_as_items.value:
        auto_clicker_count = 1
    progressive_auto_clicker_count = state.count("Enhanced Auto Clicker (Progressive Clicks/Second)", player)
    if progressive_auto_clicker_count > 0:
        auto_clicker_count = 0
    clicks_per_second = max(world.options.clicks_per_second.value, auto_clicker_count * 100, progressive_auto_clicker_count * 20)
    attack_from_clicks = get_click_attack(world, state, player, num_pokemon) * clicks_per_second
    return (get_party_attack(world, state, player, num_pokemon) + attack_from_clicks) * 25 >= int(attack)

def dungeon_attack_needed(world: World, state: CollectionState, player: int, minion_attack: int, special_boss_attack: int, complete_dungeon: bool):
    """Checks if the player's expected current party attack is at least X for dungeons."""
    dungeon_logic = world.options.dungeon_logic.value
    boss_attack = 0
    if complete_dungeon:
        boss_attack = special_boss_attack or minion_attack * 5
    final_pokemon_attack = boss_attack or minion_attack

    early_attack = final_pokemon_attack
    half_attack = minion_attack * 6 + final_pokemon_attack
    full_attack = minion_attack * 13 + boss_attack

    attack = [early_attack, half_attack, full_attack][dungeon_logic]
    return attack_needed(world, state, player, attack)

def dexsanity_enabled(world: World, state: CollectionState, player: int):
    """Checks if Dexsanity is enabled."""
    return world.options.dexsanity.value > 0

def dexsanity_disabled(world: World, state: CollectionState, player: int):
    """Checks if Dexsanity is disabled."""
    return world.options.dexsanity.value == 0

def can_breed(world: World, state: CollectionState, player: int, pokemon: str):
    """Checks if the pokemon has been received and can be hatched."""
    has_pokemon = state.count(pokemon, player) > 0
    has_8_badges = state.count_group("Badges", player) >= 8
    has_hatchery = state.count("Mystery Egg", player) > 0
    return has_pokemon and has_8_badges and has_hatchery

def starter(world: World, state: CollectionState, player: int):
    """Checks if the starters are in logic."""
    return world.options.starter_logic.value

def kanto_starter(world: World, state: CollectionState, player: int):
    """Checks if the Kanto starters are in logic."""
    # To be implemented later
    return starter(world, state, player)

def kanto_roamer(world: World, state: CollectionState, player: int):
    """Checks if the Kanto roamers are in logic."""
    has_champion_badge = state.count("Kanto Elite Champion Badge", player) > 0
    return has_champion_badge and fuchsia_city(world, state, player)

def has_script(world: World, state: CollectionState, player: int, script_name: str):
    """Checks if the player needs a specific script."""
    if not world.options.use_scripts.value or not world.options.include_scripts_as_items.value:
        return True
    # script_item = get_items_with_value(world, f"Script: {script_name}")
    return state.count(script_name, player) > 0