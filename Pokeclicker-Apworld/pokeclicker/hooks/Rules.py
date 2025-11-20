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
    has_town_map = state.count("Town Map", player) > 0
    return kanto_route_1(world, state, player) and has_town_map

def kanto_route_22(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 22."""
    return kanto_route_1(world, state, player)

def kanto_route_2(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 2."""
    return kanto_route_1(world, state, player)

def viridian_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Viridian City."""
    return kanto_route_1(world, state, player)

def viridian_forest(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Viridian Forest."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 102
    return kanto_route_2(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def pewter_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Pewter City."""
    return viridian_forest(world, state, player)

def kanto_route_3(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 3."""
    has_boulder_badge = state.count("Boulder Badge", player) > 0
    return has_boulder_badge

def mt_moon(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mt. Moon."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 834
    return kanto_route_3(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_4_pokecenter(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 4 Pokecenter."""
    return kanto_route_3(world, state, player)

def kanto_route_4(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 4."""
    return mt_moon(world, state, player)

def cerulean_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Cerulean City."""
    return kanto_route_4(world, state, player)

def kanto_route_24(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 24."""
    return kanto_route_4(world, state, player)

def kanto_route_25(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 25."""
    return kanto_route_24(world, state, player)

def bills_house(world: World, state: CollectionState, player: int):
    """Checks if the player can access Bill's House."""
    return kanto_route_24(world, state, player)

def kanto_route_5(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 5."""
    return kanto_route_25(world, state, player)

def kanto_route_6(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 6."""
    return kanto_route_5(world, state, player)

def vermilion_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Vermilion City."""
    return kanto_route_6(world, state, player)

def kanto_route_11(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 11."""
    return kanto_route_6(world, state, player)

def digletts_cave(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Diglett's Cave."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 2962
    return kanto_route_6(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_9(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 9."""
    has_cascade_badge = state.count("Cascade Badge", player) > 0
    return vermilion_city(world, state, player) and has_cascade_badge

def power_plant(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Power Plant."""
    has_soul_badge = state.count("Soul Badge", player) > 0
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 13507
    return kanto_route_9(world, state, player) and has_soul_badge and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_10(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 10."""
    return kanto_route_9(world, state, player)

def rock_tunnel(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Rock Tunnel."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 2048
    return kanto_route_10(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def lavender_town(world: World, state: CollectionState, player: int):
    """Checks if the player can access Lavender Town."""
    return rock_tunnel(world, state, player)

def pokemon_tower(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Pokemon Tower."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 7523
    return lavender_town(world, state, player) and rocket_game_corner(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_12(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 12."""
    return rock_tunnel(world, state, player)

def kanto_route_8(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 8."""
    return rock_tunnel(world, state, player)

def saffron_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Saffron City."""
    has_rainbow_badge = state.count("Rainbow Badge", player) > 0
    return celadon_city(world, state, player) or has_rainbow_badge

def silph_co(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Sylph Co. building."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 10515
    return saffron_city(world, state, player) and pokemon_tower(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_7(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 7."""
    return kanto_route_8(world, state, player)

def celadon_city(world: World, state: CollectionState, player: int):
    """Checks if the player can access Celadon City."""
    return kanto_route_7(world, state, player)

def rocket_game_corner(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Rocket Game Corner."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 5820
    return celadon_city(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_13(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 13."""
    return pokemon_tower(world, state, player)

def kanto_route_14(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 14."""
    return kanto_route_13(world, state, player)

def kanto_route_15(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 15."""
    return kanto_route_14(world, state, player)

def kanto_route_16(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 16."""
    return pokemon_tower(world, state, player)

def kanto_route_17(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 17."""
    return kanto_route_16(world, state, player)

def kanto_route_18(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 18."""
    return kanto_route_17(world, state, player)

def fuchsia_city(world: World, state: CollectionState, player: int):   
    """Checks if the player can access Fuchsia City."""
    return kanto_route_15(world, state, player) or kanto_route_18(world, state, player)

def safari_zone(world: World, state: CollectionState, player: int):
    """Checks if the player can access the Safari Zone."""
    has_safari_ticket = state.count("Safari Ticket", player) > 0
    return has_safari_ticket

def kanto_route_19(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 19."""
    has_soul_badge = state.count("Soul Badge", player) > 0
    return has_soul_badge

def seafoam_islands(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Seafoam Islands."""
    has_rainbow_badge = state.count("Rainbow Badge", player) > 0
    had_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 17226
    return kanto_route_19(world, state, player) and has_rainbow_badge and had_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_20(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 20."""
    return kanto_route_21(world, state, player) or seafoam_islands(world, state, player)

def kanto_route_21(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 21."""
    has_soul_badge = state.count("Soul Badge", player) > 0
    return has_soul_badge

def cinnabar_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Cinnabar Island."""
    return kanto_route_21(world, state, player)

def pokemon_mansion(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Pokemon Mansion."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 17760
    return cinnabar_island(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def kanto_route_23(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kanto Route 23."""
    has_earth_badge = state.count("Earth Badge", player) > 0
    return kanto_route_22(world, state, player) and has_earth_badge

def victory_road(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Victory Road."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    mimion_attack = 24595
    return kanto_route_23(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, mimion_attack, special_boss_attack, complete_dungeon)

def indigo_plateau(world: World, state: CollectionState, player: int):
    """Checks if the player can access Indigo Plateau."""
    return victory_road(world, state, player)

def cerulean_cave(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Cerulean Cave."""
    has_elite_badge_5 = state.count("Progressive Elite Badge", player) >= 5
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 28735
    return has_elite_badge_5 and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)


# Kanto - Sevii Islands 123
def one_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Sevii One Island."""
    has_volcano_badge = state.count("Volcano Badge", player) > 0
    return has_volcano_badge

def treasure_beach(world: World, state: CollectionState, player: int):
    """Checks if the player can access Treasure Beach on Sevii One Island."""
    has_volcano_badge = state.count("Volcano Badge", player) > 0
    return has_volcano_badge

def kindle_road(world: World, state: CollectionState, player: int):
    """Checks if the player can access Kindle Road on Sevii One Island."""
    has_volcano_badge = state.count("Volcano Badge", player) > 0
    return has_volcano_badge

def mount_ember(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mount Ember on Sevii One Island."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 18120
    return kindle_road(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)

def two_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Sevii Two Island."""
    return cinnabar_island(world, state, player) and one_island(world, state, player)

def cape_brink(world: World, state: CollectionState, player: int):
    """Checks if the player can access Cape Brink on Sevii Two Island."""
    has_volcano_badge = state.count("Volcano Badge", player) > 0
    return cinnabar_island(world, state, player) and has_volcano_badge

def three_island(world: World, state: CollectionState, player: int):
    """Checks if the player can access Sevii Three Island."""
    return two_island(world, state, player)

def bond_bridge(world: World, state: CollectionState, player: int):
    """Checks if the player can access Bond Bridge on Sevii Three Island."""
    return three_island(world, state, player)

def berry_forest(world: World, state: CollectionState, player: int, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Berry Forest on Sevii Three Island."""
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    minion_attack = 18120
    return bond_bridge(world, state, player) and has_dungeon_ticket and dungeon_attack_needed(world, state, player, minion_attack, special_boss_attack, complete_dungeon)


# Eggs and Stones
def can_get_grass_egg(world: World, state: CollectionState, player: int):
    """Checks if the player can obtain a Grass Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return lavender_town(world, state, player) and tutorial_complete

def can_get_fire_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Fire Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return cinnabar_island(world, state, player) and tutorial_complete

def can_get_water_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Water Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return cerulean_city(world, state, player) and tutorial_complete

def can_get_electric_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain an Electric Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return vermilion_city(world, state, player) and tutorial_complete

def can_get_fighting_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Fighting Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return saffron_city(world, state, player) and tutorial_complete

def can_get_dragon_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Dragon Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    return fuchsia_city(world, state, player) and tutorial_complete

def can_get_mystery_egg(world: World, state: CollectionState, player: int) -> bool:
    """Checks if the player can obtain a Mystery Egg."""
    tutorial_complete = state.count("Tutorial Complete", player) > 0
    enabled = world.options.mystery_egg.value
    return enabled and pewter_city(world, state, player) and tutorial_complete

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
def completed_bills_errand(world: World, state: CollectionState, player: int):
    """Checks if the player has completed Bill's Errand questline."""
    return cinnabar_island(world, state, player) and pokemon_mansion(world, state, player) and one_island(world, state, player) and two_island(world, state, player) and three_island(world, state, player)

def completed_bills_grandpas_treasure_hunt(world: World, state: CollectionState, player: int):
    """Checks if the player has completed Bill's Grandpa's Treasure Hunt questline."""
    # Must catch Jigglypuff, Oddish, Staryu, Growlithe, and Pikachu. Hatching egg does not count.
    has_dungeon_ticket = state.count("Dungeon Ticket", player) > 0
    return ((pallet_town(world, state, player)) and
        (kanto_route_3(world, state, player)) and # Jigglypuff 
        (kanto_route_24(world, state, player) or kanto_route_25(world, state, player) or kanto_route_5(world, state, player) or kanto_route_6(world, state, player) or kanto_route_8(world, state, player) or kanto_route_7(world, state, player) or kanto_route_12(world, state, player) or kanto_route_13(world, state, player) or kanto_route_14(world, state, player) or kanto_route_15(world, state, player) or cape_brink(world, state, player) or bond_bridge(world, state, player) or (berry_forest(world, state, player) and has_dungeon_ticket)) and # Oddish
        (kanto_route_20(world, state, player) or kanto_route_21(world, state, player)) and # Staryu
        (kanto_route_8(world, state, player) or kanto_route_7(world, state, player) or pokemon_mansion(world, state, player, False)) and #Growlithe
        (viridian_forest(world, state, player, True) or power_plant(world, state, player, False))) # Pikachu


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

# def get_catchable_pokemon(world: World, state: CollectionState, player: int) -> int:
#     """Returns the number of different Pokemon the player can catch in Kanto routes."""
#     catch_set = set()
#     has_super_rod = state.count("Super Rod", player) > 0
#     if kanto_route_1(world, state, player):
#         catch_set.union(set(['Pidgey', 'Rattata']))
#     if kanto_route_22(world, state, player):
#         catch_set.union(set(['Rattata', 'Spearow', 'Mankey']))
#         if has_super_rod:
#             catch_set.union(set(['Psyduck', 'Poliwag', 'Slowpoke', 'Goldeen', 'Magikarp']))
#     if kanto_route_2(world, state, player):
#         catch_set.union(set(['Caterpie', 'Weedle', 'Pidgey', 'Rattata']))
#     if kanto_route_3(world, state, player):
#         catch_set.union(set(['Pidgey', 'Spearow', 'Nidoran(F)', 'Nidoran(M)', 'Jigglypuff', 'Mankey']))
#     if kanto_route_4(world, state, player):
#         catch_set.union(set(['Rattata', 'Spearow', 'Ekans', 'Sandshrew', 'Mankey']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Magikarp']))
#     if kanto_route_24(world, state, player):
#         catch_set.union(set(['Caterpie', 'Metapod', 'Weedle', 'Kakuna', 'Pidgey', 'Oddish', 'Abra', 'Bellsprout']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Magikarp']))
#     if kanto_route_25(world, state, player):
#         catch_set.union(set(['Pidgey', 'Rattata', 'Spearow', 'Ekans', 'Sandshrew', 'Oddish', 'Abra', 'Bellsprout']))
#         if has_super_rod:
#             catch_set.union(set(['Psyduck', 'Poliwag', 'Tentacool', 'Slowpoke', 'Goldeen', 'Magikarp']))
#     if kanto_route_5(world, state, player):
#         catch_set.union(set(['Pidgey', 'Meowth', 'Oddish', 'Bellsprout']))
#     if kanto_route_6(world, state, player):
#         catch_set.union(set(['Pidgey', 'Meowth', 'Oddish', 'Bellsprout']))
#         if has_super_rod:
#             catch_set.union(set(['Psyduck', 'Poliwag', 'Slowpoke', 'Goldeen', 'Magikarp']))
#     if kanto_route_11(world, state, player):
#         catch_set.union(set(['Spearow', 'Ekans', 'Sandshrew', 'Drowzee']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Magikarp']))
#     if kanto_route_9(world, state, player):
#         catch_set.union(set(['Rattata', 'Spearow', 'Ekans', 'Sandshrew']))
#     if kanto_route_10(world, state, player):
#         catch_set.union(set(['Spearow', 'Ekans', 'Sandshrew', 'Voltorb']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Magikarp']))
#     if kanto_route_8(world, state, player):
#         catch_set.union(set(['Pidgey', 'Ekans', 'Sandshrew', 'Vulpix', 'Meowth', 'Growlithe']))
#     if kanto_route_7(world, state, player):
#         catch_set.union(set(['Pidgey', 'Vulpix', 'Oddish', 'Meowth', 'Growlithe', 'Bellsprout']))
#     if kanto_route_12(world, state, player):
#         catch_set.union(set(['Pidgey', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell', 'Farfetch\'d']))
#         if has_super_rod:
#             catch_set.union(set(['Poliwag', 'Slowpoke', 'Slowbro', 'Goldeen', 'Magikarp']))
#     if kanto_route_13(world, state, player):
#         catch_set.union(set(['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell', 'Farfetch\'d', 'Ditto']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Magikarp']))
#     if kanto_route_14(world, state, player):
#         catch_set.union(set(['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell', 'Ditto']))
#     if kanto_route_15(world, state, player):
#         catch_set.union(set(['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell', 'Ditto']))
#     if kanto_route_16(world, state, player):
#         catch_set.union(set(['Rattata', 'Raticate', 'Spearow', 'Doduo']))
#     if kanto_route_17(world, state, player):
#         catch_set.union(set(['Rattata', 'Raticate', 'Spearow', 'Fearow', 'Doduo']))
#     if kanto_route_18(world, state, player):
#         catch_set.union(set(['Rattata', 'Raticate', 'Spearow', 'Fearow', 'Doduo']))
#     if kanto_route_19(world, state, player):
#         catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Magikarp']))
#     if kanto_route_20(world, state, player):
#         catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Shellder', 'Staryu', 'Magikarp']))
#     if kanto_route_21(world, state, player):
#         catch_set.union(set(['Tangela']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Krabby', 'Horsea', 'Shellder', 'Staryu', 'Magikarp']))
    
#     if len(catch_set) > 0:
#         catch_set.union(set(['Mew'])) # Mew is available at any Kanto Route
    
#     if kanto_route_23(world, state, player):
#         catch_set.union(set(['Spearow', 'Fearow', 'Ekans', 'Arbok', 'Sandshrew', 'Sandslash', 'Mankey', 'Primeape']))
#         if has_super_rod:
#             catch_set.union(set(['Psyduck', 'Poliwag', 'Slowpoke', 'Goldeen', 'Magikarp']))
#     if treasure_beach(world, state, player):
#         catch_set.union(set(['Spearow', 'Fearow', 'Meowth', 'Persian', 'Psyduck', 'Slowpoke', 'Tangela']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Tentacruel', 'Krabby', 'Horsea', 'Magikarp']))
#     if kindle_road(world, state, player):
#         catch_set.union(set(['Spearow', 'Fearow', 'Meowth', 'Persian', 'Psyduck', 'Geodude', 'Ponyta', 'Rapidash', 'Slowpoke']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Tentacruel', 'Krabby', 'Horsea', 'Magikarp']))
#     if cape_brink(world, state, player):
#         catch_set.union(set(['Spearow', 'Fearow', 'Oddish', 'Gloom', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Bellsprout', 'Weepinbell', 'Slowpoke', 'Slowbro']))
#         if has_super_rod:
#             catch_set.union(set(['Poliwag', 'Goldeen', 'Magikarp']))
#     if bond_bridge(world, state, player):
#         catch_set.union(set(['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Meowth', 'Persian', 'Psyduck', 'Bellsprout', 'Weepinbell', 'Slowpoke']))
#         if has_super_rod:
#             catch_set.union(set(['Tentacool', 'Tentacruel', 'Krabby', 'Horsea', 'Magikarp'])) 

#     if viridian_forest(world, state, player):
#         catch_set.union(set(['Pikachu', 'Caterpie', 'Metapod', 'Weedle', 'Kakuna']))
#     if mt_moon(world, state, player):
#         catch_set.union(set(['Clefairy', 'Zubat', 'Paras', 'Geodude']))
#     if digletts_cave(world, state, player):
#         catch_set.union(set(['Diglett', 'Dugtrio']))
#     if rock_tunnel(world, state, player):
#         catch_set.union(set(['Zubat', 'Mankey', 'Geodude', 'Machop', 'Onix']))
#     if pokemon_tower(world, state, player):
#         catch_set.union(set(['Gastly', 'Haunter', 'Cubone', 'Marowak']))
#     if power_plant(world, state, player):
#         catch_set.union(set(['Pikachu', 'Magnemite', 'Magneton', 'Voltorb', 'Electrode', 'Electabuzz', 'Zapdos']))
#     if seafoam_islands(world, state, player):
#         catch_set.union(set(['Zubat', 'Golbat', 'Psyduck', 'Golduck', 'Slowpoke', 'Slowbro', 'Krabby', 'Horsea', 'Magikarp', 'Seel', 'Articuno']))
#     if pokemon_mansion(world, state, player):
#         catch_set.union(set(['Rattata', 'Raticate', 'Vulpix', 'Growlithe', 'Grimer', 'Muk', 'Koffing', 'Weezing', 'Ditto', 'Magmar']))
#     if mount_ember(world, state, player):
#         catch_set.union(set(['Spearow', 'Fearow', 'Machop', 'Machoke', 'Geodude', 'Graveler', 'Ponyta', 'Rapidash', 'Magmar', 'Moltres']))
#     if berry_forest(world, state, player):
#         catch_set.union(set(['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Psyduck', 'Golduck', 'Poliwag', 'Bellsprout', 'Weepinbell', 'Slowpoke', 'Slowbro', 'Drowzee', 'Exeggcute', 'Goldeen', 'Magikarp']))
#     if victory_road(world, state, player):
#         catch_set.union(set(['Arbok', 'Sandslash', 'Zubat', 'Golbat', 'Primeape', 'Machop', 'Geodude', 'Onix', 'Marowak', 'Machoke']))
#     if cerulean_cave(world, state, player):
#         catch_set.union(set(['Golbat', 'Parasect', 'Psyduck', 'Golduck', 'Primeape', 'Poliwag', 'Machoke', 'Slowpoke', 'Slowbro', 'Magneton', 'Electrode', 'Goldeen', 'Magikarp', 'Ditto', 'Kadabra', 'MewTwo']))
    
#     if safari_zone(world, state, player):
#         catch_set.union(set(['Nidoran(F)', 'Nidorina', 'Nidoran(M)', 'Nidorino', 'Exeggcute', 'Paras', 'Parasect', 'Rhyhorn', 'Chansey', 'Scyther', 'Pinsir', 'Kangaskhan', 'Tauros', 'Cubone', 'Marowak', 'Tangela',
#                              'Magikarp', 'Psyduck', 'Slowpoke', 'Poliwag', 'Goldeen', 'Seaking']))
    
#     mystery = can_get_mystery_egg(world, state, player)
#     if can_get_fire_egg(world, state, player) or mystery:
#         catch_set.union(set(['Charmander', 'Vulpix', 'Growlithe', 'Magmar']))
#     if can_get_water_egg(world, state, player) or mystery:
#         catch_set.union(set(['Squirtle', 'Lapras', 'Staryu', 'Slowpoke']))
#     if can_get_grass_egg(world, state, player) or mystery:
#         catch_set.union(set(['Bulbasaur', 'Oddish', 'Tangela', 'Paras']))
#     if can_get_electric_egg(world, state, player) or mystery:
#         catch_set.union(set(['Magnemite', 'Pikachu', 'Voltorb', 'Electabuzz']))
#     if can_get_fighting_egg(world, state, player) or mystery:
#         catch_set.union(set(['Hitmonlee', 'Hitmonchan', 'Machop', 'Mankey']))
#     if can_get_dragon_egg(world, state, player) or mystery:
#         catch_set.union(set(['Dratini', 'Dragonair', 'Dragonite']))
#     if mystery:
#         catch_set.union(set(['Gastly', 'Jigglypuff', 'Geodude', 'Doduo']))

#     num_badges = 0
#     badge_list = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge", "Volcano Badge", "Earth Badge", "Progressive Elite Badge"]
#     for badge in badge_list:
#         num_badges += state.count(badge, player)
#     if num_badges >= 0:
#         if "Bulbasaur" in catch_set:
#             catch_set.add('Ivysaur')
#         if "Charmander" in catch_set:
#             catch_set.add('Charmeleon')
#         if "Squirtle" in catch_set:
#             catch_set.add('Wartortle')
#         if "Caterpie" in catch_set:
#             catch_set.union(set(['Metapod', 'Butterfree']))
#         if "Weedle" in catch_set:
#             catch_set.union(set(['Kakuna', 'Beedrill']))
#         if "Pidgey" in catch_set:
#             catch_set.add('Pidgeotto')
#         if "Rattata" in catch_set:
#             catch_set.add('Raticate')
#         if "Spearow" in catch_set:
#             catch_set.add('Fearow')
#         if "Nidoran(F)" in catch_set:
#             catch_set.add('Nidorina')
#         if "Nidoran(M)" in catch_set:
#             catch_set.add('Nidorino')
#         if "Abra" in catch_set:
#             catch_set.add('Kadabra')
#         if "Magikarp" in catch_set:
#             catch_set.add('Gyarados')
#     if num_badges >= 1:
#         if "Ekans" in catch_set:
#             catch_set.add('Arbok')
#         if "Sandshrew" in catch_set:
#             catch_set.add('Sandslash')
#         if "Zubat" in catch_set:
#             catch_set.add('Golbat')
#         if "Oddish" in catch_set:
#             catch_set.add('Gloom')
#         if "Paras" in catch_set:
#             catch_set.add('Parasect')
#         if "Diglett" in catch_set:
#             catch_set.add('Dugtrio')
#         if "Meowth" in catch_set:
#             catch_set.add('Persian')
#         if "Mankey" in catch_set:
#             catch_set.add('Primeape')
#         if "Poliwag" in catch_set:
#             catch_set.add('Poliwhirl')
#         if "Machop" in catch_set:
#             catch_set.add('Machoke')
#         if "Bellsprout" in catch_set:
#             catch_set.add('Weepinbell')
#         if "Tentacool" in catch_set:
#             catch_set.add('Tentacruel')
#         if "Geodude" in catch_set:
#             catch_set.add('Graveler')
#         if "Magnemite" in catch_set:
#             catch_set.add('Magneton')
#         if "Gastly" in catch_set:
#             catch_set.add('Haunter')
#         if "Drowzee" in catch_set:
#             catch_set.add('Hypno')
#         if "Krabby" in catch_set:
#             catch_set.add('Kingler')
#         if "Voltorb" in catch_set:
#             catch_set.add('Electrode')
#         if "Cubone" in catch_set:
#             catch_set.add('Marowak')
#         if "Dratini" in catch_set:
#             catch_set.add('Dragonair')
#     if num_badges >= 2:
#         if "Ivysaur" in catch_set:
#             catch_set.add('Venusaur')
#         if "Charmeleon" in catch_set:
#             catch_set.add('Charizard')
#         if "Wartortle" in catch_set:
#             catch_set.add('Blastoise')
#         if "Pidgeotto" in catch_set:
#             catch_set.add('Pidgeot')
#         if "Venonat" in catch_set:
#             catch_set.add('Venomoth')
#         if "Psyduck" in catch_set:
#             catch_set.add('Golduck')
#         if "Ponyta" in catch_set:
#             catch_set.add('Rapidash')
#         if "Slowpoke" in catch_set:
#             catch_set.add('Slowbro')
#         if "Doduo" in catch_set:
#             catch_set.add('Dodrio')
#         if "Seel" in catch_set:
#             catch_set.add('Dewgong')
#         if "Grimer" in catch_set:
#             catch_set.add('Muk')
#         if "Koffing" in catch_set:
#             catch_set.add('Weezing')
#         if "Horsea" in catch_set:
#             catch_set.add('Seadra')
#         if "Goldeen" in catch_set:
#             catch_set.add('Seaking')
#         if "Omanyte" in catch_set:
#             catch_set.add('Omastar')
#         if "Kabuto" in catch_set:
#             catch_set.add('Kabutops')
#     if num_badges >= 3:
#         if "Rhyhorn" in catch_set:
#             catch_set.add('Rhydon')
#     if num_badges >= 4:
#         if "Dragonair" in catch_set:
#             catch_set.add('Dragonite')
    
#     if can_get_leaf_stone(world, state, player):
#         if "Gloom" in catch_set:
#             catch_set.add('Vileplume')
#         if "Weepinbell" in catch_set:
#             catch_set.add('Victreebel')
#         if "Exeggcute" in catch_set:
#             catch_set.add('Exeggutor')
#     if can_get_fire_stone(world, state, player):
#         if "Vulpix" in catch_set:
#             catch_set.add('Ninetales')
#         if "Growlithe" in catch_set:
#             catch_set.add('Arcanine')
#         if "Eevee" in catch_set:
#             catch_set.add('Flareon')
#     if can_get_water_stone(world, state, player):
#         if "Poliwhirl" in catch_set:
#             catch_set.add('Poliwrath')
#         if "Shellder" in catch_set:
#             catch_set.add('Cloyster')
#         if "Staryu" in catch_set:
#             catch_set.add('Starmie')
#         if "Eevee" in catch_set:
#             catch_set.add('Vaporeon')
#     if can_get_thunder_stone(world, state, player):
#         if "Pikachu" in catch_set:
#             catch_set.add('Raichu')
#         if "Eevee" in catch_set:
#             catch_set.add('Jolteon')
#     if can_get_moon_stone(world, state, player):
#         if "Nidorina" in catch_set:
#             catch_set.add('Nidoqueen')
#         if "Nidorino" in catch_set:
#             catch_set.add('Nidoking')
#         if "Clefairy" in catch_set:
#             catch_set.add('Clefable')
#         if "Jigglypuff" in catch_set:
#             catch_set.add('Wigglytuff')
#     if can_get_linking_cord(world, state, player):
#         if "Kadabra" in catch_set:
#             catch_set.add('Alakazam') 
#         if "Machoke" in catch_set:
#             catch_set.add('Machamp')
#         if "Graveler" in catch_set:
#             catch_set.add('Golem')
#         if "Haunter" in catch_set:
#             catch_set.add('Gengar')

#     return catch_set

def can_catch_x_pokemon(world: World, state: CollectionState, player: int, x: int):
    """Checks if the player can obtain at least X pokemon."""
    return state.count_group("Pokemon", player) >= int(x)
    return len(get_catchable_pokemon(world, state, player)) >= int(x)

def get_party_attack(world: World, state: CollectionState, player: int, num_pokemon: int) -> set:
    """Returns the attack value of the player's expected current party."""
    num_badges = 0
    badge_list = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge", "Volcano Badge", "Earth Badge", "Progressive Elite Badge"]
    for badge in badge_list:
        num_badges += state.count(badge, player)
    # total_attack = 0
    # for p in ["Bulbasaur", "Ivysaur", "Venusaur"]:
    #     total_attack += pokemon[p]["base"]["attack"]

    avgBaseAttack = 70 + 4.2 * num_badges
    avgLevel = min(100, 20 + 10 * num_badges)
    return num_pokemon * avgBaseAttack * (avgLevel / 100)

def get_click_attack(world: World, state: CollectionState, player: int, num_pokemon: int) -> set:
    """Returns the attack value of the player's expected clicker attack."""
    return (1 + num_pokemon) ** 1.4
    
def attack_needed(world: World, state: CollectionState, player: int, attack: int):
    """Checks if the player's expected current party attack is at least X."""
    num_pokemon = state.count_group("Pokemon", player) #len(get_catchable_pokemon(world, state, player))
    auto_clicker_count = state.count("Enhanced Auto Clicker", player)
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
    return world.options.dexsanity.value

def dexsanity_disabled(world: World, state: CollectionState, player: int):
    """Checks if Dexsanity is disabled."""
    return not world.options.dexsanity.value