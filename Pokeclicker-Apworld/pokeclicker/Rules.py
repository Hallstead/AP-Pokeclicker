from __future__ import annotations

import dataclasses
from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, ClassVar

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasGroup, HasGroupUnique, Rule, CanReachLocation, False_, True_

from worlds.AutoWorld import World
from BaseClasses import CollectionState

from .Helpers import is_category_enabled, is_option_enabled

if TYPE_CHECKING:
    from .world import PokeclickerWorld

@dataclasses.dataclass(init=False)
class WorldRule(Rule, game="Pokeclicker"):
    """Composable rule wrapper for functions that need (world, state)."""

    func: Callable[[World, CollectionState], bool]

    def __init__(self, func: Callable[[World, CollectionState], bool], options: Iterable[OptionFilter] = (), filtered_resolution: bool = False):
        super().__init__(options=options, filtered_resolution=filtered_resolution)
        self.func = func

    def _instantiate(self, world: World) -> Rule.Resolved:
        def evaluate(state: CollectionState, *, world=world, func=self.func) -> bool:
            result = func(world, state)
            if isinstance(result, Rule.Resolved):
                return result(state)
            if isinstance(result, Rule):
                return result.resolve(world)(state)
            return result

        return self.Resolved(evaluate, player=world.player, caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(Rule.Resolved):
        func: Callable[[CollectionState], bool]
        # force_recalculate: ClassVar[bool] = True

        def _evaluate(self, state: CollectionState) -> bool:
            return self.func(state)


def _evaluate_rule(rule, world: PokeclickerWorld, state: CollectionState) -> bool:
    if isinstance(rule, Rule.Resolved):
        return rule(state)

    if isinstance(rule, Rule):
        return rule.resolve(world)(state)

    if callable(rule):
        try:
            return rule(state)
        except TypeError:
            return rule(world, state)

    raise TypeError(f"Unsupported rule type: {type(rule)!r}")


def _resolve_rule(rule):
    if isinstance(rule, Rule):
        return rule
    if isinstance(rule, Rule.Resolved):
        return rule
    if callable(rule):
        return make_rule(rule)
    raise TypeError(f"Unsupported rule type: {type(rule)!r}")


def make_rule(rule_func, *args, **kwargs):
    """Create a composable rule from a function that expects (world, state)."""
    if isinstance(rule_func, Rule):
        return rule_func
    if isinstance(rule_func, Rule.Resolved):
        return rule_func
    if isinstance(rule_func, str):
        # Handle string function names - resolve at runtime
        func = globals().get(rule_func)
        if func is None:
            # Return a rule that always evaluates to False
            return False_()
        rule_func = func
    if callable(rule_func):
        return WorldRule(lambda world, state: rule_func(world, state, *args, **kwargs))
    raise TypeError(f"Unsupported rule type: {type(rule_func)!r}")


def make_state_rule(world: PokeclickerWorld, rule_func):
    """Wrap a rule function or a composable WorldRule into an AP rule callable."""
    resolved_rule = _resolve_rule(rule_func)

    if isinstance(resolved_rule, Rule):
        return resolved_rule.resolve(world)

    if isinstance(resolved_rule, Rule.Resolved):
        return resolved_rule

    def rule(state: CollectionState) -> bool:
        return _evaluate_rule(resolved_rule, world, state)

    return rule

def make_pokemon_rule(
    name,
    *,
    allow_breed=True,
):
    # Import here to avoid the rules <-> pokemon_data module import cycle.
    from .pokemon_data import POKEMON_RULES

    pokemon = POKEMON_RULES.get(name)
    if not pokemon:
        raise ValueError(f"No data exists for Pokémon: {name}")
    
    region = pokemon.get("native_region", None)
    
    access_rule = None

    def add_or(rule_part):
        nonlocal access_rule
        if rule_part is None:
            return
        access_rule = rule_part if access_rule is None else (access_rule | rule_part)

    # Routes
    routes = pokemon.get("routes", ())
    if routes:
        add_or(route_rules(routes))

    # Dungeons
    for dungeon in pokemon.get("dungeons", ()):
        add_or(make_rule(dungeon, False))
    for dungeon, attack in pokemon.get("dungeon boss", ()):
        add_or(make_rule(dungeon, True, attack))
    for dungeon in pokemon.get("dungeon chest", ()):
        add_or(make_rule(dungeon, False))

    # Egg and Breeding
    if pokemon.get("egg", None) is not None:
        egg = pokemon.get("egg")
        add_or((Has(region) if region is not None else True_()) & make_rule(can_get_egg, egg))
    for mon in pokemon.get("breeding", ()):
        add_or((Has(region) if region is not None else True_()) & make_rule(can_breed, mon))

    # Evolution
    for data_dict in pokemon.get("evolution", []):
        add_or((Has(region) if region is not None else True_()) & evolution_rule(data_dict))

    # Safari Zones
    for region in pokemon.get("safari zone", ()):
        if region not in SAFARI_REGIONS:
            continue
        add_or(make_rule(SAFARI_REGIONS[region]))

    # Farm Wandering
    # for berry in pokemon.get("farm wandering", ()):
    #     pass

    # Temporary Battles
    for battle in pokemon.get("temporary battle", ()):
        add_or(make_rule(battle))

    # Trades
    for location, item_list in pokemon.get("trades", ()):
        rule = make_rule(location)
        for item in item_list:
            rule = rule & make_rule(can_get_item, item)
        add_or(rule)

    # Shops
    for location, currency in pokemon.get("shops", ()):
        rule = make_rule(location) & make_rule(can_get_item, currency)
        add_or(rule)

    # Shadow Pokemon
    for location in pokemon.get("shadow pokemon", ()):
        add_or(make_rule(location))

    # Quest Rewards
    for quest in pokemon.get("quest rewards", ()):
        add_or(make_rule(quest))

    # Dream Orbs
    # for location in pokemon.get("dream orbs", ()):
    #     pass

    # Roamer
    for region in pokemon.get("roamer", ()):
        if region not in ROAMER_REGIONS:
            continue
        add_or(make_rule(ROAMER_REGIONS[region]))

    #Discord
    for region in pokemon.get("discord", ()):
        add_or(make_rule(discord_pokemon, name, region))

    # Special
    for s in pokemon.get("special", ()):
        add_or((s))

    # Self Breeding
    if allow_breed:
        add_or(make_rule(can_breed, name))

    return access_rule

def route_rules(routes: dict):
    if not routes:
        return None
    
    access_rule = None

    def add_or(rule_part):
        nonlocal access_rule
        if rule_part is None:
            return
        access_rule = rule_part if access_rule is None else (access_rule | rule_part)

    land = routes.get("land", ())
    if land:
        for location in land:
            add_or(make_rule(location))
    water = routes.get("water", ())
    if water:
        for location in water:
            add_or((Has("Super Rod") & make_rule(location)))
    headbutt = routes.get("headbutt", ())
    if headbutt:
        for location in headbutt:
            add_or(make_rule(location))

    return access_rule

def evolution_rule(evolution_data: dict):
    if not evolution_data:
        return False_()


    def add_and(rule_part):
        nonlocal evolution_rule
        if rule_part is None:
            return
        evolution_rule = rule_part if evolution_rule is None else (evolution_rule & rule_part)

    
    prev = evolution_data.get("prev", None)
    level = evolution_data.get("level", None)
    item = evolution_data.get("item", None)
    questline = evolution_data.get("questline", None)
    dungeon_evolution = evolution_data.get("dungeon_evolution", None)
    environment = evolution_data.get("environment", None)

    evolution_rule = None
            
    if prev is not None:
        add_and(Has(prev))
    if level is not None:
        if level <= 0:
            badge_count = 0
        else:
            badge_count = -(-(level - 20) // 10)
        add_and(HasGroup("Badges", badge_count))
    if item is not None:
        add_and(make_rule(can_get_item, item))
    if questline is not None:
        add_and(make_rule(questline))
    if dungeon_evolution is not None:
        add_and(make_rule(dungeon_evolution))
    # if environment is not None:
    #     add_and(make_rule(can_access_environment, environment))
    rule = evolution_rule if evolution_rule is not None else False_()

    return rule

def set_all_rules(world: PokeclickerWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)
    print(world.options)
            


def set_all_entrance_rules(world: PokeclickerWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    # overworld_to_bottom_right_room = world.get_entrance("Overworld to Bottom Right Room")

    # Now, let's make some rules!
    # First, let's handle the transition from the overworld to the bottom right room,
    # which requires slashing a bush with the Sword.
    # For this, we need a rule that says "player has a Sword".
    # We can use a "Has"-type rule from the rule_builder module for this.
    # can_destroy_bush = Has("Sword")

    # Now we can set our "can_destroy_bush" rule to the entrance which requires slashing a bush to clear the path.
    # The easiest way to do this is by calling world.set_rule, which works for both Locations and Entrances.
    
    # world.set_rule(route1_to_kanto, Has("Town Map"))
    # world.set_rule(kanto_to_sevii_islands_123, Has("Volcano Badge"))
    # world.set_rule(kanto_to_indigo_plateau, has_all_kanto_badges)

    # Conditions can also depend on event items.
    # button_pressed = Has("Top Left Room Button Pressed")
    # world.set_rule(right_room_to_final_boss_room, button_pressed)

    # Some entrance rules may only apply if the player enabled certain options.
    # In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
    # Overworld to the Top Middle Room.
    # if world.options.hammer:
    #     overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
    #     can_smash_brick = Has("Hammer")
    #     world.set_rule(overworld_to_top_middle_room, can_smash_brick)

    # So far, we've been using "Has" from the Rule Builder to make our rules.
    # There is another way to make rules that you will see in a lot of older worlds.
    # A rule can just be a function that takes a "state" argument and returns a bool.
    # As a demonstration of what that looks like, let's do it with our final Entrance rule:
    # world.set_rule(overworld_to_top_left_room, lambda state: state.has("Key", world.player))
    # This style is not really recommended anymore, though.
    # Notice how you have to explicitly capture world.player here so that the rule applies to the correct player?
    # Well, Rule Builder does this part for you, inside of world.set_rule.
    # This doesn't just result in shorter code, it also means you can define rules statically (at the module level).
    # APQuest opts to create its Rule objects locally, but just to show what this would look like,
    # we'll re-set the "Overworld to Top Left Room" rule to a constant defined at the top of this file:
    # world.set_rule(overworld_to_top_left_room, HAS_KEY)

    # Beyond these structural advantages,
    # Rule Builder also allows the core AP code to do a lot of under-the-hood optimizations.
    # Rule Builder is quite comprehensive, and even if you have really esoteric rules,
    # you can make custom rules by subclassing CustomRule.
    pass

def set_all_location_rules(world: PokeclickerWorld) -> None:
    # # Location rules work no differently from Entrance rules.
    # # Most of our locations are chests that can simply be opened by walking up to them.
    # # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    # # reach the region that the chest sits in.
    # # However, our two enemies work differently.
    # # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    # # So, we need to set requirements on the Locations themselves.
    # # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.

    # # In "set_all_entrance_rules", we had a rule for a location that doesn't always exist.
    # # In this case, we had to check for its existence (by checking the player's chosen options) before setting the rule.
    # # Other times, you may have a situation where a location can have two different rules depending on the options.
    # # In our case, the enemy in the right room has more health if hard mode is selected,
    # # so ontop of the Sword, the player will either need one more health or a Shield in hard mode.
    # # First, let's make our sword condition.
    # can_defeat_basic_enemy: Rule = Has("Sword")

    # # Next, we'll check whether hard mode has been chosen in the player options.
    # if world.options.hard_mode:
    #     # We'll make the condition for "Has a Shield or a Health Upgrade".
    #     # We can chain two "Has" conditions together with the | operator to make "Has Shield or has Health Upgrade".
    #     can_withstand_a_hit = Has("Shield") | Has("Health Upgrade")

    #     # Now, we chain this rule to our Sword rule.
    #     # Since we want both conditions to be true, in this case, we have to chain them in an "and" way.
    #     # For this, we can use the & operator.
    #     can_defeat_basic_enemy = can_defeat_basic_enemy & can_withstand_a_hit

    # # Finally, we set our rule onto the Right Room Enemy Drop location.
    # right_room_enemy = world.get_location("Right Room Enemy Drop")
    # world.set_rule(right_room_enemy, can_defeat_basic_enemy)

    # # For the final boss, we also need to chain multiple conditions.
    # # First of all, you always need a Sword and a Shield.
    # # So far, we used the | and & operators to chain "Has" rules.
    # # Instead, we can also use HasAny for an or-chain of items, or HasAll for an and-chain of items.
    # has_sword_and_shield: Rule = HasAll("Sword", "Shield")

    # # In hard mode, the player also needs both Health Upgrades to survive long enough to defeat the boss.
    # # For this, we can use the optional "count" parameter for "Has".
    # has_both_health_upgrades = Has("Health Upgrade", count=2)

    # # Previously, we used an "if world.options.hard_mode" condition to check if we should apply the extra requirement.
    # # However, if you're comfortable with boolean logic, there is another way.
    # # OptionFilter is a rule component which isn't a "Rule" on its own, but when used in a boolean expression with
    # # rules, it acts like True if the option has the specified value, and acts like False otherwise.
    # hard_mode_is_off = OptionFilter(HardMode, False)

    # # So with this option-checking rule component in hand, we can write our boss condition like this:
    # can_defeat_final_boss = has_sword_and_shield & (hard_mode_is_off | has_both_health_upgrades)
    # # If you're not as comfortable with boolean logic, it might be somewhat confusing why this is correct.
    # # There is nothing wrong with using "if" conditions to check for options, if you find that easier to understand.

    # # Finally, we apply the rule to our "Final Boss Defeated" event location.
    # final_boss = world.get_location("Final Boss Defeated")
    # world.set_rule(final_boss, can_defeat_final_boss)
   
    
    for location_data_entry in world.location_data.values():
        if location_data_entry.rule is None:
            continue
        if not location_data_entry.inclusion:
            continue

        location = world.get_location(location_data_entry.name)
        if location is None:
            continue

        world.set_rule(location, make_state_rule(world, location_data_entry.rule))


def set_completion_condition(world: PokeclickerWorld) -> None:
    # Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    # For this, we can use world.set_completion_rule.
    # You can just set a completion condition directly like any other condition, referencing items the player receives:
    # world.set_completion_rule(HasAll("Sword", "Shield"))

    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.set_completion_rule(Has("Victory!"))


# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".

# Kanto
def kanto_route_1(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 1."""
    return True

def pallet_town(world: World, state: CollectionState):
    """Checks if the player can access Pallet Town."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pallet Town", world.player) > 0
    #     return has_location
    has_town_map = state.count("Town Map", world.player) > 0
    return kanto_route_1(world, state) and has_town_map

def kanto_route_22(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 22."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 22", world.player) > 0
    #     return has_location
    return kanto_route_1(world, state)

def kanto_route_2(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 2."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 2", world.player) > 0
    #     return has_location
    return kanto_route_1(world, state)

def viridian_city(world: World, state: CollectionState):
    """Checks if the player can access Viridian City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Viridian City", world.player) > 0
    #     return has_location
    return kanto_route_1(world, state)

def viridian_forest(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Viridian Forest."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 102
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Viridian Forest", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_2(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def pewter_city(world: World, state: CollectionState):
    """Checks if the player can access Pewter City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pewter City", world.player) > 0
    #     return has_location
    return viridian_forest(world, state)

def kanto_route_3(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 3."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 3", world.player) > 0
    #     return has_location
    has_boulder_badge = state.count("Boulder Badge", world.player) > 0
    return has_boulder_badge

def mt_moon(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mt. Moon."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 834
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Mt. Moon", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_3(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def route_4_pokemon_center(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 4 Pokecenter."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 4 Pokemon Center", world.player) > 0
    #     return has_location
    return kanto_route_3(world, state)

def kanto_route_4(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 4."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 4", world.player) > 0
    #     return has_location
    return mt_moon(world, state)

def cerulean_city(world: World, state: CollectionState):
    """Checks if the player can access Cerulean City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Cerulean City", world.player) > 0
    #     return has_location
    return kanto_route_4(world, state)

def kanto_route_24(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 24."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 24", world.player) > 0
    #     return has_location
    return kanto_route_4(world, state) and attack_needed(world, state, 14041, "Kanto")

def kanto_route_25(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 25."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 25", world.player) > 0
    #     return has_location
    return kanto_route_24(world, state)

def bills_house(world: World, state: CollectionState):
    """Checks if the player can access Bill's House."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Bill's House", world.player) > 0
    #     return has_location
    return kanto_route_25(world, state)

def kanto_route_5(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 5."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 5", world.player) > 0
    #     return has_location
    return kanto_route_25(world, state)

def kanto_route_6(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 6."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 6", world.player) > 0
    #     return has_location
    return kanto_route_5(world, state)

def vermilion_city(world: World, state: CollectionState):
    """Checks if the player can access Vermilion City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Vermilion City", world.player) > 0
    #     return has_location
    return kanto_route_6(world, state)

def kanto_route_11(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 11."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 11", world.player) > 0
    #     return has_location
    return kanto_route_6(world, state)

def digletts_cave(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Diglett's Cave."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 2962
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Diglett's Cave", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_6(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def kanto_route_9(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 9."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 9", world.player) > 0
    #     return has_location
    has_cascade_badge = state.count("Cascade Badge", world.player) > 0
    return vermilion_city(world, state) and attack_needed(world, state, 50431, "Kanto") and has_cascade_badge

def power_plant(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Power Plant."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Power Plant", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 13507
    has_soul_badge = state.count("Soul Badge", world.player) > 0
    return kanto_route_9(world, state) and has_soul_badge and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def kanto_route_10(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 10."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 10", world.player) > 0
    #     return has_location
    return kanto_route_9(world, state)

def rock_tunnel(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Rock Tunnel."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 2048
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Rock Tunnel", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return kanto_route_10(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def lavender_town(world: World, state: CollectionState):
    """Checks if the player can access Lavender Town."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Lavender Town", world.player) > 0
    #     return has_location
    return rock_tunnel(world, state)

def pokemon_tower(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Pokemon Tower."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 7523
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pokemon Tower", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return lavender_town(world, state) and rocket_game_corner(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def kanto_route_12(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 12."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 12", world.player) > 0
    #     return has_location
    return rock_tunnel(world, state)

def kanto_route_8(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 8."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 8", world.player) > 0
    #     return has_location
    return rock_tunnel(world, state)

def saffron_city(world: World, state: CollectionState):
    """Checks if the player can access Saffron City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Saffron City", world.player) > 0
    #     return has_location
    has_rainbow_badge = state.count("Rainbow Badge", world.player) > 0
    return celadon_city(world, state) or has_rainbow_badge

def silph_co(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Sylph Co. building."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 10515
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Silph Co.", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return saffron_city(world, state) and pokemon_tower(world, state) and attack_needed(world, state, 151990, "Kanto") and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def kanto_route_7(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 7."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 7", world.player) > 0
    #     return has_location
    return kanto_route_8(world, state)

def celadon_city(world: World, state: CollectionState):
    """Checks if the player can access Celadon City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Celadon City", world.player) > 0
    #     return has_location
    return kanto_route_7(world, state)

def rocket_game_corner(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Rocket Game Corner."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 5820
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Rocket Game Corner", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return celadon_city(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def kanto_route_13(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 13."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 13", world.player) > 0
    #     return has_location
    return pokemon_tower(world, state)

def kanto_route_14(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 14."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 14", world.player) > 0
    #     return has_location
    return kanto_route_13(world, state)

def kanto_route_15(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 15."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 15", world.player) > 0
    #     return has_location
    return kanto_route_14(world, state)

def kanto_route_16(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 16."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 16", world.player) > 0
    #     return has_location
    return pokemon_tower(world, state)

def kanto_route_17(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 17."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 17", world.player) > 0
    #     return has_location
    return kanto_route_16(world, state)

def kanto_route_18(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 18."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 18", world.player) > 0
    #     return has_location
    return kanto_route_17(world, state)

def fuchsia_city(world: World, state: CollectionState):   
    """Checks if the player can access Fuchsia City."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Fuchsia City", world.player) > 0
    #     return has_location
    return kanto_route_15(world, state) or kanto_route_18(world, state)

def safari_zone(world: World, state: CollectionState):
    """Checks if the player can access the Safari Zone."""
    has_safari_ticket = state.has("Safari Ticket", world.player)
    quest_points = can_get_quest_point(world, state)
    
    if world.options.safari_zone_logic.value and world.options.use_scripts.value:
        return has_safari_ticket and quest_points and (state.count("Auto Safari Zone", world.player) > 0 or state.count("Auto Safari Zone (Progressive Fast Animations)", world.player) > 0)
    else:
        return has_safari_ticket and quest_points

def kanto_route_19(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 19."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 19", world.player) > 0
    #     return has_location
    has_soul_badge = state.count("Soul Badge", world.player) > 0
    return has_soul_badge

def seafoam_islands(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Seafoam Islands."""
    had_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 17226
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Seafoam Islands", world.player) > 0
    #     return has_location and had_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    has_rainbow_badge = state.count("Rainbow Badge", world.player) > 0
    return kanto_route_19(world, state) and has_rainbow_badge and had_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def kanto_route_20(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 20."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 20", world.player) > 0
    #     return has_location
    return kanto_route_21(world, state) or seafoam_islands(world, state)

def kanto_route_21(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 21."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 21", world.player) > 0
    #     return has_location
    has_soul_badge = state.count("Soul Badge", world.player) > 0
    return has_soul_badge

def cinnabar_island(world: World, state: CollectionState):
    """Checks if the player can access Cinnabar Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Cinnabar Island", world.player) > 0
    #     return has_location
    return kanto_route_21(world, state)

def pokemon_mansion(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access the Pokemon Mansion."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 17760
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Pokemon Mansion", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return cinnabar_island(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def kanto_route_23(world: World, state: CollectionState):
    """Checks if the player can access Kanto Route 23."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kanto Route 23", world.player) > 0
    #     return has_location
    has_earth_badge = state.count("Earth Badge", world.player) > 0
    return kanto_route_22(world, state) and has_earth_badge and attack_needed(world, state, 426771, "Kanto")

def victory_road(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Victory Road."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 24595
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Victory Road", world.player) > 0
    #     return has_location
    has_badges = state.count("Boulder Badge", world.player) + state.count("Cascade Badge", world.player) + state.count("Thunder Badge", world.player) + state.count("Rainbow Badge", world.player) + state.count("Soul Badge", world.player) + state.count("Marsh Badge", world.player) + state.count("Volcano Badge", world.player) + state.count("Earth Badge", world.player) == 8
    return kanto_route_23(world, state) and has_badges and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def indigo_plateau(world: World, state: CollectionState):
    """Checks if the player can access Indigo Plateau."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Indigo Plateau Kanto", world.player) > 0
    #     return has_location
    return victory_road(world, state)

def cerulean_cave(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Cerulean Cave."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 28735
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Cerulean Cave", world.player) > 0
    #     return has_location and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    has_elite_champion_badge = state.count("Kanto Elite Champion Badge", world.player) > 0
    return has_elite_champion_badge and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def new_island(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access New Island dungeon in Kanto."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    has_infinite_seasonal_events = has_script(world, state, "Infinite Seasonal Events")
    minion_attack = 18500
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("New Island", world.player) > 0
    #     return has_location and has_dungeon_ticket and has_infinite_seasonal_events and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon)
    return has_dungeon_ticket and has_infinite_seasonal_events and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

# Kanto - Sevii Islands 123
def client_island(world: World, state: CollectionState):
    """Checks if the player can access Client Island on Sevii Islands."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Client Island", world.player) > 0
    #     return has_location
    has_volcano_badge = state.count("Volcano Badge", world.player) > 0
    return has_volcano_badge

def one_island(world: World, state: CollectionState):
    """Checks if the player can access Sevii One Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("One Island", world.player) > 0
    #     return has_location
    has_volcano_badge = state.count("Volcano Badge", world.player) > 0
    return has_volcano_badge

def treasure_beach(world: World, state: CollectionState):
    """Checks if the player can access Treasure Beach on Sevii One Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Treasure Beach", world.player) > 0
    #     return has_location
    has_volcano_badge = state.count("Volcano Badge", world.player) > 0
    return has_volcano_badge

def kindle_road(world: World, state: CollectionState):
    """Checks if the player can access Kindle Road on Sevii One Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Kindle Road", world.player) > 0
    #     return has_location
    has_volcano_badge = state.count("Volcano Badge", world.player) > 0
    return has_volcano_badge

def mt_ember_summit(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mount Ember on Sevii One Island."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 18120
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Mt. Ember Summit", world.player) > 0
    #     return has_location
    return kindle_road(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def two_island(world: World, state: CollectionState):
    """Checks if the player can access Sevii Two Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Two Island", world.player) > 0
    #     return has_location
    return bills_errand0(world, state)

def cape_brink(world: World, state: CollectionState):
    """Checks if the player can access Sevii Cape Brink."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Cape Brink", world.player) > 0
    #     return has_location
    return two_island(world, state)

def three_island(world: World, state: CollectionState):
    """Checks if the player can access Sevii Three Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Three Island", world.player) > 0
    #     return has_location
    return bills_errand1(world, state)

def bond_bridge(world: World, state: CollectionState):
    """Checks if the player can access Bond Bridge on Sevii Three Island."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Bond Bridge", world.player) > 0
    #     return has_location
    return three_island(world, state) and attack_needed(world, state, 443328, "Kanto")

def berry_forest(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Berry Forest on Sevii Three Island."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 18120
    return bond_bridge(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Kanto")

def professor_ivys_lab(world: World, state: CollectionState):
    """Checks if the player can access Professor Ivy's Lab."""
    # if world.options.mapsanity.value > 0:
    #     has_location = state.count("Professor Ivy's Lab", world.player) > 0
    #     return has_location
    return started_unfinished_business(world, state)

def blue1(world: World, state: CollectionState):
    """Checks if the player can beat Blue 1."""
    return kanto_route_22(world, state) and attack_needed(world, state, 2718, "Kanto")

def blue2(world: World, state: CollectionState):
    """Checks if the player can beat Blue 2."""
    return kanto_route_4(world, state) and attack_needed(world, state, 14041, "Kanto")

def blue3(world: World, state: CollectionState):
    """Checks if the player can beat Blue 3."""
    return kanto_route_6(world, state) and attack_needed(world, state, 50431, "Kanto")

def blue4(world: World, state: CollectionState):
    """Checks if the player can beat Blue 4."""
    return pokemon_tower(world, state) and attack_needed(world, state, 151990, "Kanto")

def blue5(world: World, state: CollectionState):
    """Checks if the player can beat Blue 5."""
    return team_rocket1(world, state) and attack_needed(world, state, 203971, "Kanto")

def blue6(world: World, state: CollectionState):
    """Checks if the player can beat Blue 6."""
    return kanto_route_22(world, state) and state.has("Earth Badge", world.player) and attack_needed(world, state, 426771, "Kanto")

def fighting_dojo(world: World, state: CollectionState):
    """Checks if the player can access the Fighting Dojo."""
    return (state.has("Rainbow Badge", world.player) or rocket_game_corner(world, state)) and attack_needed(world, state, 217970, "Kanto")

def snorlax_route12(world: World, state: CollectionState):
    """Checks if the player can access Snorlax on Route 12."""
    return kanto_route_12(world, state) and blue4(world, state)

def snorlax_route16(world: World, state: CollectionState):
    """Checks if the player can access Snorlax on Route 16."""
    return kanto_route_7(world, state) and blue4(world, state)

def biker_goon(world: World, state: CollectionState):
    """Checks if the player can beat a Biker Goon."""
    return bills_errand1(world, state) and attack_needed(world, state, 396954, "Kanto") and three_island(world, state)

def cueball_paxton(world: World, state: CollectionState):
    """Checks if the player can beat Cueball Paxton."""
    return bills_errand1(world, state) and attack_needed(world, state, 443328, "Kanto") and three_island(world, state)

def ash_ketchum_new_island(world: World, state: CollectionState):
    """Checks if the player can beat Ash Ketchum on New Island."""
    return new_island(world, state, True, 131500) and attack_needed(world, state, 454992, "Kanto")

def bills_grandpa(world: World, state: CollectionState):
    """Checks if the player can beat Bill's Grandpa."""
    return completed_bills_grandpa_treasure_hunt(world, state)

def santa_jynx1(world: World, state: CollectionState):
    """Checks if the player can beat Santa Jynx Band 1."""
    return has_script(world, state, "Infinite Seasonal Events") and bills_house(world, state) and attack_needed(world, state, 10048, "Kanto")

def ash_ketchum_kanto(world: World, state: CollectionState):
    """Checks if the player can beat Ash Ketchum in Kanto."""
    return state.has("Kanto Elite Champion Badge", world.player) and attack_needed(world, state, 737710, "Kanto")

# Johto
def johto_route_29(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 29"""
    johto = state.has("Johto", world.player)
    return johto and state.has("Kanto Elite Champion Badge", world.player)

def johto_route_30(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 30"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_29(world, state)

def johto_route_31(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 31"""
    johto = state.has("Johto", world.player)
    return johto and silver1(world, state)

def johto_route_32(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 32"""
    johto = state.has("Johto", world.player)
    return johto and state.has("Zephyr Badge", world.player)

def johto_route_33(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 33"""
    johto = state.has("Johto", world.player)
    return johto and union_cave(world, state)

def johto_route_34(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 34"""
    johto = state.has("Johto", world.player)
    return johto and ilex_forest(world, state)

def johto_route_35(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 35"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_34(world, state)

def johto_route_36(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 36"""
    johto = state.has("Johto", world.player)
    return johto and (johto_route_35(world, state) or sudowoodo(world, state))

def johto_route_37(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 37"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_36(world, state) & sudowoodo(world, state)

def johto_route_38(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 38"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_37(world, state)

def johto_route_39(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 39"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_38(world, state)

def johto_route_40(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 40"""
    johto = state.has("Johto", world.player)
    return johto and state.has("Fog Badge", world.player) and johto_route_39(world, state)

def johto_route_41(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 41"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_40(world, state)

def johto_route_42(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 42"""
    johto = state.has("Johto", world.player)
    has_fog_badge = state.count("Fog Badge", world.player) > 0
    return johto and (has_fog_badge or mt_mortar(world, state))

def johto_route_43(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 43"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_42(world, state)

def johto_route_44(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 44"""
    johto = state.has("Johto", world.player)
    return johto and radio_tower(world, state)

def johto_route_45(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 45"""
    johto = state.has("Johto", world.player)
    return johto and ice_path(world, state)

def johto_route_46(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 46"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_29(world, state)

def johto_route_47(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 47"""
    has_mineral_badge = state.has("Mineral Badge", world.player)
    johto = state.has("Johto", world.player)
    return johto and has_mineral_badge

def johto_route_48(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 48"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_47(world, state)

def johto_route_26(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 26"""
    johto = state.has("Johto", world.player)
    return johto and johto_route_27(world, state)

def johto_route_27(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 27"""
    johto = state.has("Johto", world.player)
    return johto and tohjo_falls(world, state)

def johto_route_28(world: World, state: CollectionState):
    """Checks if the player can access Johto Route 28"""
    has_johto_champion_badge = state.has("Johto Elite Champion Badge", world.player)
    johto = state.has("Johto", world.player)
    return johto and has_johto_champion_badge

def new_bark_town(world: World, state: CollectionState):
    """Checks if the player can access New Bark Town"""
    johto = state.has("Johto", world.player)
    has_kanto_champion_badge = state.count("Kanto Elite Champion Badge", world.player) > 0
    return johto and has_kanto_champion_badge

def cherrygrove_city(world: World, state: CollectionState):
    """Checks if the player can access Cherrygrove City."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_29(world, state)

def violet_city(world: World, state: CollectionState):
    """Checks if the player can access Violet City."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_31(world, state)

def azalea_town(world: World, state: CollectionState):
    """Checks if the player can access Azalea Town."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_33(world, state)

def goldenrod_city(world: World, state: CollectionState):
    """Checks if the player can access Goldenrod City."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_34(world, state)

def ecruteak_city(world: World, state: CollectionState):
    """Checks if the player can access Ecruteak City."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_37(world, state)

def olivine_city(world: World, state: CollectionState):
    """Checks if the player can access Olivine City."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_39(world, state)

def cianwood_city(world: World, state: CollectionState):
    """Checks if the player can access Cianwood City."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_41(world, state)

def mahogany_town(world: World, state: CollectionState):
    """Checks if the player can access Mahogany Town."""
    johto = state.has("Johto", world.player)
    return johto and (johto_route_42(world, state) or mt_mortar(world, state))

def blackthorn_city(world: World, state: CollectionState):
    """Checks if the player can access Blackthorn City."""
    johto = state.has("Johto", world.player)
    return johto and ice_path(world, state)

def indigo_plateau_johto(world: World, state: CollectionState):
    """Checks if the player can access Indigo Plateau (Johto)."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_26(world, state) and silver5(world, state)

def national_park(world: World, state: CollectionState):
    """Checks if the player can access National Park."""
    johto = state.has("Johto", world.player)
    return johto and johto_route_35(world, state)

def sprout_tower(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Sprout Tower."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 56735
    johto = state.has("Johto", world.player)
    return johto and johto_route_31(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def ruins_of_alph(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Ruins of Alph."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 60600
    johto = state.has("Johto", world.player)
    return johto and johto_route_32(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")
    
def union_cave(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Union Cave."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 63600
    johto = state.has("Johto", world.player)
    return johto and johto_route_32(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def slowpoke_well(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Slowpoke Well."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 67900
    johto = state.has("Johto", world.player)
    return johto and johto_route_33(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def ilex_forest(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Ilex Forest."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 82200
    has_hive_badge = state.count("Hive Badge", world.player) > 0
    johto = state.has("Johto", world.player)
    return has_hive_badge and johto and silver2(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def burned_tower(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Burned Tower."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 88500
    johto = state.has("Johto", world.player)
    return johto and legendary_beasts0(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")
    
def olivine_lighthouse(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Olivine Lighthouse."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 88500
    johto = state.has("Johto", world.player)
    return johto and johto_route_39(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def tin_tower(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Tin Tower."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 88500
    johto = state.has("Johto", world.player)
    return johto and radio_tower(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def whirl_islands(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Whirl Islands."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 92800
    johto = state.has("Johto", world.player)
    return johto and radio_tower(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def mt_mortar(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mt. Mortar."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 104100
    johto = state.has("Johto", world.player)
    return johto and johto_route_37(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def team_rockets_hideout(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Team Rocket's Hideout."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 104100
    johto = state.has("Johto", world.player)
    return johto and red_gyarados(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")
    
def radio_tower(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Radio Tower."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 112000
    johto = state.has("Johto", world.player)
    return johto and silver4(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def ice_path(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Ice Path."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 120400
    johto = state.has("Johto", world.player)
    return johto and johto_route_44(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def dark_cave(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Dark Cave."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 127000
    johto = state.has("Johto", world.player)
    return johto and johto_route_45(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def tohjo_falls(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Tohjo Falls."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 127750
    johto = state.has("Johto", world.player)
    return johto and state.has("Rising Badge", world.player) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def victory_road_johto(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Victory Road Johto."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 128500
    johto = state.has("Johto", world.player)
    return johto and johto_route_26(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")

def mt_silver(world: World, state: CollectionState, complete_dungeon: bool = True, special_boss_attack: int = 0):
    """Checks if the player can access Mt. Silver."""
    has_dungeon_ticket = state.count("Dungeon Ticket", world.player) > 0
    minion_attack = 130500
    johto = state.has("Johto", world.player)
    return johto and johto_route_28(world, state) and has_dungeon_ticket and dungeon_attack_needed(world, state, minion_attack, special_boss_attack, complete_dungeon, "Johto")


def silver1(world: World, state: CollectionState):
    """Checks if the player can beat Silver 1."""
    return johto_route_30(world, state) and attack_needed(world, state, 176000, "Johto")

def silver2(world: World, state: CollectionState):
    """Checks if the player can beat Silver 2."""
    return johto_route_33(world, state) and attack_needed(world, state, 679348, "Johto")

def sudowoodo(world: World, state: CollectionState):
    """Checks if the player can beat Sudowoodo."""
    return johto_route_31(world, state) and state.has("Plain Badge", world.player) and attack_needed(world, state, 540000, "Johto")

def silver3(world: World, state: CollectionState):
    """Checks if the player can beat Silver 3."""
    return legendary_beasts1(world, state) and burned_tower(world, state, False) and attack_needed(world, state, 930600, "Johto")

def silver4(world: World, state: CollectionState):
    """Checks if the player can beat Silver 4."""
    return state.has("Mineral Badge", world.player) and state.has("Glacier Badge", world.player) and goldenrod_city(world, state) and team_rocket_again1(world, state) and attack_needed(world, state, 1372600, "Johto")

def silver5(world: World, state: CollectionState):
    """Checks if the player can beat Silver 5."""
    return victory_road_johto(world, state) and attack_needed(world, state, 2239084, "Johto")

def suicune1(world: World, state: CollectionState):
    """Checks if the player can beat Suicune 1."""
    return started_eusines_chase(world, state) and johto_route_41(world, state) and attack_needed(world, state, 1044000, "Johto")

def eusine(world: World, state: CollectionState):
    """Checks if the player can beat Eusine."""
    return eusines_chase1(world, state) and attack_needed(world, state, 1055000, "Johto")

def suicune2(world: World, state: CollectionState):
    """Checks if the player can beat Suicune 2."""
    return eusines_chase2(world, state) and johto_route_42(world, state) and attack_needed(world, state, 1115500, "Johto")

def red_gyarados(world: World, state: CollectionState):
    """Checks if the player can beat Red Gyarados."""
    return started_team_rocket_again(world, state) and johto_route_43(world, state) and attack_needed(world, state, 1100000, "Johto")

def suicune3(world: World, state: CollectionState):
    """Checks if the player can beat Suicune 3."""
    return state.has("Johto Elite Champion Badge", world.player) and eusines_chase4(world, state) and attack_needed(world, state, 3269100, "Kanto")

def suicune4(world: World, state: CollectionState):
    """Checks if the player can beat Suicune 4."""
    return eusines_chase6(world, state) and kanto_route_14(world, state) and attack_needed(world, state, 3359100, "Kanto")

def suicune5(world: World, state: CollectionState):
    """Checks if the player can beat Suicune 5."""
    return eusines_chase8(world, state) and attack_needed(world, state, 3449100, "Kanto")

def suicune6(world: World, state: CollectionState):
    """Checks if the player can beat Suicune 6."""
    return eusines_chase10(world, state) and attack_needed(world, state, 3539100, "Kanto")

def kimono_girls(world: World, state: CollectionState):
    """Checks if the player can beat the Kimono Girls."""
    return rainbow_guardian0(world, state) and ecruteak_city(world, state) and attack_needed(world, state, 3300000, "Johto")

def spiky_eared_pichu(world: World, state: CollectionState):
    """Checks if the player can beat Spiky-eared Pichu."""
    return unfinished_business6(world, state) and ilex_forest(world, state, False) and attack_needed(world, state, 3178500, "Johto")

def rocket_boss_giovanni(world: World, state: CollectionState):
    """Checks if the player can beat Rocket Boss Giovanni."""
    return unfinished_business9(world, state) and tohjo_falls(world, state, False) and attack_needed(world, state, 3459100, "Johto")

def silver6(world: World, state: CollectionState):
    """Checks if the player can beat Silver 6."""
    return state.has("Johto Elite Champion Badge", world.player) and mt_moon(world, state, False) and attack_needed(world, state, 3326791, "Kanto")

def silver7(world: World, state: CollectionState):
    """Checks if the player can beat Silver 7."""
    return silver6(world, state) and indigo_plateau_johto(world, state) and attack_needed(world, state, 4024754, "Johto")

def red(world: World, state: CollectionState):
    """Checks if the player can beat Red."""
    return state.has("Johto Elite Champion Badge", world.player) and mt_silver(world, state) and attack_needed(world, state, 4149102, "Johto")

def youngster_joey(world: World, state: CollectionState):
    """Checks if the player can beat Youngster Joey."""
    return state.has("Kanto Elite Champion Badge", world.player) and cherrygrove_city(world, state) and has_script(world, state, "Infinite Seasonal Events") and cherrygrove_city(world, state) and attack_needed(world, state, 548919101828, "Johto")

def ash_ketchum_johto(world: World, state: CollectionState):
    """Checks if the player can beat Ash Ketchum (Johto)."""
    return ash_ketchum_kanto(world, state) and state.has("Johto Elite Champion Badge", world.player) and johto_route_48(world, state) and attack_needed(world, state, 5423120, "Johto") 

# Eggs and Stones
def can_get_egg(world: World, state: CollectionState, egg_type: str) -> bool:
    """Checks if the player can obtain a specific type of egg."""
    if egg_type not in EGG_TYPES:
        raise ValueError(f"Invalid egg type: {egg_type}")
    return EGG_TYPES[egg_type](world, state)

def can_get_grass_egg(world: World, state: CollectionState):
    """Checks if the player can obtain a Grass Egg."""
    quest_points = can_get_quest_point(world, state)
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    return (lavender_town(world, state) or azalea_town(world, state) or can_get_mystery_egg(world, state)) and quest_points and has_hatchery

def can_get_fire_egg(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Fire Egg."""
    quest_points = can_get_quest_point(world, state)
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    return (cinnabar_island(world, state) or ecruteak_city(world, state) or can_get_mystery_egg(world, state)) and quest_points and has_hatchery

def can_get_water_egg(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Water Egg."""
    quest_points = can_get_quest_point(world, state)
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    return (cerulean_city(world, state) or olivine_city(world, state) or can_get_mystery_egg(world, state)) and quest_points and has_hatchery

def can_get_electric_egg(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain an Electric Egg."""
    quest_points = can_get_quest_point(world, state)
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    return (vermilion_city(world, state) or olivine_city(world, state) or can_get_mystery_egg(world, state)) and quest_points and has_hatchery

def can_get_fighting_egg(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Fighting Egg."""
    quest_points = can_get_quest_point(world, state)
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    return (saffron_city(world, state) or cianwood_city(world, state) or can_get_mystery_egg(world, state)) and quest_points and has_hatchery

def can_get_dragon_egg(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Dragon Egg."""
    quest_points = can_get_quest_point(world, state)
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    return (fuchsia_city(world, state) or blackthorn_city(world, state) or can_get_mystery_egg(world, state)) and quest_points and has_hatchery

def can_get_mystery_egg(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Mystery Egg."""
    quest_points = can_get_quest_point(world, state)
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    enabled = world.options.mystery_egg_in_logic.value
    return enabled and (pewter_city(world, state) or violet_city(world, state)) and quest_points and has_hatchery

EGG_TYPES = {
    "Grass Egg": can_get_grass_egg,
    "Fire Egg": can_get_fire_egg,
    "Water Egg": can_get_water_egg,
    "Electric Egg": can_get_electric_egg,
    "Fighting Egg": can_get_fighting_egg,
    "Dragon Egg": can_get_dragon_egg,
    "Mystery Egg": can_get_mystery_egg,
}

def can_get_item(world: World, state: CollectionState, item_type: str) -> bool:
    """Checks if the player can obtain a specific item."""
    if item_type not in ITEM_TYPES:
        raise ValueError(f"Invalid item type: {item_type}")
    return ITEM_TYPES[item_type](world, state)

def can_get_moon_stone(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Moon Stone."""
    quest_points = can_get_quest_point(world, state)
    return (saffron_city(world, state) or cianwood_city(world, state)) and quest_points

def can_get_leaf_stone(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Leaf Stone."""
    quest_points = can_get_quest_point(world, state)
    return (saffron_city(world, state) or azalea_town(world, state)) and quest_points

def can_get_fire_stone(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Fire Stone."""
    quest_points = can_get_quest_point(world, state)
    return (cinnabar_island(world, state) or ecruteak_city(world, state)) and quest_points

def can_get_water_stone(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Water Stone."""
    quest_points = can_get_quest_point(world, state)
    return (cerulean_city(world, state) or olivine_city(world, state)) and quest_points

def can_get_thunder_stone(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Thunder Stone."""
    quest_points = can_get_quest_point(world, state)
    return (vermilion_city(world, state) or olivine_city(world, state)) and quest_points

def can_get_linking_cord(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Linking Cord."""
    quest_points = can_get_quest_point(world, state)
    return (fuchsia_city(world, state) or mahogany_town(world, state)) and quest_points

def can_get_sun_stone(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Sun Stone."""
    quest_points = can_get_quest_point(world, state)
    return (cianwood_city(world, state)) and quest_points

def can_get_soothe_bell(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Soothe Bell."""
    quest_points = can_get_quest_point(world, state)
    return (ecruteak_city(world, state)) and quest_points

def can_get_metal_coat(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Metal Coat."""
    quest_points = can_get_quest_point(world, state)
    return (olivine_city(world, state)) and quest_points

def can_get_kings_rock(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a King's Rock."""
    quest_points = can_get_quest_point(world, state)
    return (azalea_town(world, state)) and quest_points

def can_get_upgrade(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain an Upgrade."""
    quest_points = can_get_quest_point(world, state)
    return (mahogany_town(world, state)) and quest_points

def can_get_dragon_scale(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Dragon Scale."""
    quest_points = can_get_quest_point(world, state)
    return (blackthorn_city(world, state)) and quest_points

def can_get_ice_stone(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain an Ice Stone."""
    quest_points = can_get_quest_point(world, state)
    return False
    # return (can_get_ice_stone(world, state)) and quest_points

def can_get_black_glasses(world: World, state: CollectionState):
    """Checks if the player can get the Black Glasses item.""" #next Hoenn
    if world.options.include_black_glasses.value:
        return state.has("Black Glasses", world.player)
    return team_rockets_hideout(world, state) # or the_under(world, state) or newmoon_island(world, state) or team_flare_secret_hq(world, state) or tower_of_darkness(world, state)

def can_get_palaeontologist_token(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Palaeontologist Token."""
    if world.options.include_palaeontologist_token.value:
        return state.has("Palaeontologist Token", world.player)
    return state.has("Explorer Kit", world.player) and has_script(world, state, "Enhanced Auto Mine")

def can_get_fossil(world: World, state: CollectionState, region: str) -> bool:
    """Checks if the player can obtain a Fossil in the specified region."""
    return state.has("Explorer Kit", world.player) and has_script(world, state, "Enhanced Auto Mine") #and state.has(region, world.player)

def can_get_quest_point(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Quest Point."""
    tutorial_complete = state.has("Tutorial Complete", world.player)
    return tutorial_complete

def can_get_farm_point(world: World, state: CollectionState) -> bool:
    """Checks if the player can obtain a Farm Point."""
    return state.has("Wailmer Pail", world.player)

ITEM_TYPES = {
    "Moon Stone": can_get_moon_stone,
    "Leaf Stone": can_get_leaf_stone,
    "Fire Stone": can_get_fire_stone,
    "Water Stone": can_get_water_stone,
    "Thunder Stone": can_get_thunder_stone,
    "Linking Cord": can_get_linking_cord,
    "Sun Stone": can_get_sun_stone,
    "Soothe Bell": can_get_soothe_bell,
    "Metal Coat": can_get_metal_coat,
    "Kings Rock": can_get_kings_rock,
    "Upgrade": can_get_upgrade,
    "Dragon Scale": can_get_dragon_scale,
    "Ice Stone": can_get_ice_stone,
    "Black Glasses": can_get_black_glasses,
    "Pinkan Berry": lambda world, state: False,
    "Palaeontologist Token": can_get_palaeontologist_token,
    "Helix Fossil": lambda world, state: can_get_fossil(world, state, "Kanto"),
    "Dome Fossil": lambda world, state: can_get_fossil(world, state, "Kanto"),
    "Old Amber": lambda world, state: can_get_fossil(world, state, "Kanto"),
    "Root Fossil": lambda world, state: can_get_fossil(world, state, "Hoenn"),
    "Claw Fossil": lambda world, state: can_get_fossil(world, state, "Hoenn"),
    "Snover Berry": lambda world, state: False,
    "Skull Fossil": lambda world, state: can_get_fossil(world, state, "Sinnoh"),
    "Armor Fossil": lambda world, state: can_get_fossil(world, state, "Sinnoh"),
    "Odd Keystone": lambda world, state: False,
    "Meadow Plate": lambda world, state: False,
    "Pixie Plate": lambda world, state: False,
    "Cover Fossil": lambda world, state: can_get_fossil(world, state, "Unova"),
    "Plume Fossil": lambda world, state: can_get_fossil(world, state, "Unova"),
    "Red Shard": lambda world, state: False,
    "Yellow Shard": lambda world, state: False,
    "Green Shard": lambda world, state: False,
    "Blue Shard": lambda world, state: False,
    "Grey Shard": lambda world, state: False,
    "Purple Shard": lambda world, state: False,
    "Ochre Shard": lambda world, state: False,
    "Black Shard": lambda world, state: False,
    "Crimson Shard": lambda world, state: False,
    "Lime Shard": lambda world, state: False,
    "White Shard": lambda world, state: False,
    "Pink Shard": lambda world, state: False,
    'Jaw Fossil': lambda world, state: can_get_fossil(world, state, "Kalos"),
    'Sail Fossil': lambda world, state: can_get_fossil(world, state, "Kalos"),
    'Fossilized Bird': lambda world, state: can_get_fossil(world, state, "Galar"),
    'Fossilized Drake': lambda world, state: can_get_fossil(world, state, "Galar"),
    'Fossilized Fish': lambda world, state: can_get_fossil(world, state, "Galar"),
    'Fossilized Dino': lambda world, state: can_get_fossil(world, state, "Galar"),
    "money": lambda world, state: True,
    "dungeonToken": lambda world, state: False,
    "questPoint": can_get_quest_point,
    'farmPoint': can_get_farm_point,
    'diamond': lambda world, state: False,
    'contestToken': lambda world, state: False,
    'battlePoint': lambda world, state: False,
    'Normal Gems': lambda world, state: False,
    'Water Gems': lambda world, state: False,
    'Fire Gems': lambda world, state: False,
    'Grass Gems': lambda world, state: False,
    'Electric Gems': lambda world, state: False,
    'Fighting Gems': lambda world, state: False,
    'Psychic Gems': lambda world, state: False,
    'Poison Gems': lambda world, state: False,
    'Ground Gems': lambda world, state: False,
    'Flying Gems': lambda world, state: False,
    'Rock Gems': lambda world, state: False,
    'Bug Gems': lambda world, state: False,
    'Ice Gems': lambda world, state: False,
    'Ghost Gems': lambda world, state: False,
    'Dragon Gems': lambda world, state: False,
    'Dark Gems': lambda world, state: False,
    'Steel Gems': lambda world, state: False,
    'Fairy Gems': lambda world, state: False,

}


# Questlines
def tutorial_quests0(world: World, state: CollectionState): # defeat starter
    """Checks if the first step of the tutorial questline can be completed."""
    return True

def tutorial_quests1(world: World, state: CollectionState): #capture a pokemon
    """Checks if the second step of the tutorial questline can be completed."""
    return True

def tutorial_quests2(world: World, state: CollectionState): # Kill 10 on Route 2
    """Checks if the third step of the tutorial questline can be completed."""
    return kanto_route_2(world, state)

def tutorial_quests3(world: World, state: CollectionState): # Say bye to mom
    """Checks if the fourth step of the tutorial questline can be completed."""
    return tutorial_quests2(world, state) and pallet_town(world, state)

def tutorial_quests4(world: World, state: CollectionState): # Buy 10 pokeballs
    """Checks if the fifth step of the tutorial questline can be completed."""
    return tutorial_quests3(world, state) and can_buy_pokeballs(world, state)

def tutorial_quests5(world: World, state: CollectionState): # talk to old man in viridian city
    """Checks if the sixth step of the tutorial questline can be completed."""
    return tutorial_quests4(world, state) and viridian_city(world, state)

def tutorial_quests6(world: World, state: CollectionState): # catch 5 pidgeys
    """Checks if the seventh step of the tutorial questline can be completed."""
    return tutorial_quests5(world, state) and _evaluate_rule(make_pokemon_rule("Pidgey", allow_breed=False), world, state)

def tutorial_quests7(world: World, state: CollectionState): # buy dungeon ticket
    """Checks if the eighth step of the tutorial questline can be completed."""
    return tutorial_quests6(world, state) and state.has("Dungeon Ticket", world.player)

def tutorial_quests8(world: World, state: CollectionState): # Clear Viridian Forest
    """Checks if the ninth step of the tutorial questline can be completed."""
    return tutorial_quests7(world, state) and viridian_forest(world, state, True)

def completed_tutorial_quests(world: World, state: CollectionState): # Defeat Pewter City Gym
    """Checks if the player has completed the tutorial questline."""
    return tutorial_quests8(world, state) and pewter_city(world, state) and attack_needed(world, state, 2092)  # Beat Brock

def started_bills_grandpa_treasure_hunt(world: World, state: CollectionState):
    """Checks if the player has started Bill's Grandpa's Treasure Hunt questline."""
    return pallet_town(world, state) and kanto_route_25(world, state)

def bills_grandpa_treasure_hunt0(world: World, state: CollectionState):
    """Checks if the first step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return started_bills_grandpa_treasure_hunt(world, state) and bills_house(world, state)

def can_catch_jigglypuff(world: World, state: CollectionState):
    """Checks if the player can catch Jigglypuff."""
    return _evaluate_rule(make_pokemon_rule("Jigglypuff", allow_breed=False), world, state)

def bills_grandpa_treasure_hunt1(world: World, state: CollectionState):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpa_treasure_hunt0(world, state) and can_catch_jigglypuff(world, state)

def can_catch_oddish(world: World, state: CollectionState):
    """Checks if the player can catch Oddish."""
    return _evaluate_rule(make_pokemon_rule("Oddish", allow_breed=False), world, state)

def bills_grandpa_treasure_hunt2(world: World, state: CollectionState):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpa_treasure_hunt1(world, state) and can_catch_oddish(world, state)

def can_catch_staryu(world: World, state: CollectionState):
    """Checks if the player can catch Staryu."""
    return _evaluate_rule(make_pokemon_rule("Staryu", allow_breed=False), world, state)

def bills_grandpa_treasure_hunt3(world: World, state: CollectionState):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpa_treasure_hunt2(world, state) and can_catch_staryu(world, state)

def can_catch_growlithe(world: World, state: CollectionState):
    """Checks if the player can catch Growlithe."""
    return _evaluate_rule(make_pokemon_rule("Growlithe", allow_breed=False), world, state)

def bills_grandpa_treasure_hunt4(world: World, state: CollectionState):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpa_treasure_hunt3(world, state) and can_catch_growlithe(world, state)

def can_catch_pikachu(world: World, state: CollectionState):
    """Checks if the player can catch Pikachu."""
    return _evaluate_rule(make_pokemon_rule("Pikachu", allow_breed=False), world, state)

def bills_grandpa_treasure_hunt5(world: World, state: CollectionState):
    """Checks if the second step of Bill's Grandpa's Treasure Hunt questline can be completed."""
    return bills_grandpa_treasure_hunt4(world, state) and can_catch_pikachu(world, state)

def completed_bills_grandpa_treasure_hunt(world: World, state: CollectionState):
    """Checks if the player has completed Bill's Grandpa's Treasure Hunt questline."""
    return bills_grandpa_treasure_hunt5(world, state) and attack_needed(world, state, 525000)

def started_team_rocket(world: World, state: CollectionState):
    """Checks if the player has started the Team Rocket questline."""
    return cerulean_city(world, state) and attack_needed(world, state, 10800)

def team_rocket0(world: World, state: CollectionState): # Rocket Game Corner
    """Checks if the first step of the Team Rocket questline can be completed."""
    return started_team_rocket(world, state) and rocket_game_corner(world, state)

def team_rocket1(world: World, state: CollectionState): # Silph Co
    """Checks if the second step of the Team Rocket questline can be completed."""
    return team_rocket0(world, state) and silph_co(world, state)

def team_rocket2(world: World, state: CollectionState): # blue 5
    """Checks if the third step of the Team Rocket questline can be completed."""
    return team_rocket1(world, state) and blue5(world, state)

def team_rocket3(world: World, state: CollectionState): # Silph Co
    """Checks if the fourth step of the Team Rocket questline can be completed."""
    return team_rocket2(world, state) and silph_co(world, state, True, 52576) # Beat Giovanni

def completed_team_rocket(world: World, state: CollectionState):
    """Checks if the player has completed the Team Rocket questline."""
    return team_rocket3(world, state) and viridian_city(world, state) and state.has_all(("Thunder Badge", "Rainbow Badge", "Marsh Badge"), world.player) and completed_bills_errand(world, state) and attack_needed(world, state, 244850)

def started_mining_expedition(world: World, state: CollectionState): # beat Fuchsia City Gym
    """Checks if the player has started the Mining Expedition questline."""
    return fuchsia_city(world, state) and attack_needed(world, state, 137100)

def mining_expedition(world: World, state: CollectionState): # Receive the Explorer's Kit
    """Checks if the first step of the Mining Expedition questline can be completed."""
    return started_mining_expedition(world, state) and state.has("Explorers Kit", world.player)

def started_bills_errand(world: World, state: CollectionState):
    """Checks if the player has started Bill's Errand questline."""
    return cinnabar_island(world, state) and pokemon_mansion(world, state) and attack_needed(world, state, 175290) # Beat Blaine

def bills_errand0(world: World, state: CollectionState):
    """Checks if the first step of Bill's Errand questline can be completed."""
    return started_bills_errand(world, state) and one_island(world, state)

def bills_errand1(world: World, state: CollectionState):
    """Checks if the second step of Bill's Errand questline can be completed."""
    return bills_errand0(world, state) and two_island(world, state)

def bills_errand2(world: World, state: CollectionState):
    """Checks if the third step of Bill's Errand questline can be completed."""
    return bills_errand1(world, state) and three_island(world, state) and attack_needed(world, state, 396954)

def bills_errand3(world: World, state: CollectionState):
    """Checks if the fourth step of Bill's Errand questline can be completed."""
    return bills_errand2(world, state) and three_island(world, state) and attack_needed(world, state, 443328)

def completed_bills_errand(world: World, state: CollectionState):
    """Checks if the fifth step of Bill's Errand questline can be completed."""
    return bills_errand3(world, state) and berry_forest(world, state)

def started_persons_of_interest(world: World, state: CollectionState):
    """Checks if the player has started the Persons of Interest questline."""
    return completed_team_rocket(world, state)

def persons_of_interest0(world: World, state: CollectionState): # Talk to the Breeder in Saffron City
    """Checks if the first step of the Persons of Interest questline can be completed."""
    return started_persons_of_interest(world, state) and saffron_city(world, state)

def persons_of_interest1(world: World, state: CollectionState): # Talk to the Gem Scientist in Pewter City
    """Checks if the second step of the Persons of Interest questline can be completed."""
    return started_persons_of_interest(world, state) and pewter_city(world, state)

def started_unfinished_business(world: World, state: CollectionState):
    """Checks if the player has started the Unfinished Business questline."""
    return pallet_town(world, state) and completed_bills_errand(world, state)

def unfinished_business0(world: World, state: CollectionState):
    """Checks if the player has started the Unfinished Business questline."""
    return started_unfinished_business(world, state)

def unfinished_business1(world: World, state: CollectionState):
    """Checks if the second step of the Unfinished Business questline can be completed."""
    return unfinished_business0(world, state) and professor_ivys_lab(world, state)

def unfinished_business2(world: World, state: CollectionState):
    """Checks if the third step of the Unfinished Business questline can be completed."""
    return unfinished_business1(world, state)

def unfinished_business3(world: World, state: CollectionState):
    """Checks if the fourth step of the Unfinished Business questline can be completed."""
    return unfinished_business2(world, state) and azalea_town(world, state)

def unfinished_business4(world: World, state: CollectionState):
    """Checks if the fifth step of the Unfinished Business questline can be completed."""
    return unfinished_business3(world, state) and state.has("Johto Elite Champion Badge", world.player)

def unfinished_business5(world: World, state: CollectionState):
    """Checks if the fifth step of the Unfinished Business questline can be completed."""
    return unfinished_business4(world, state)

def unfinished_business6(world: World, state: CollectionState):
    """Checks if the fifth step of the Unfinished Business questline can be completed."""
    return unfinished_business5(world, state) and ilex_forest(world, state, False)

def unfinished_business7(world: World, state: CollectionState):
    """Checks if the seventh step of the Unfinished Business questline can be completed."""
    return unfinished_business6(world, state)
    
def unfinished_business8(world: World, state: CollectionState):
    """Checks if the eighth step of the Unfinished Business questline can be completed."""
    return unfinished_business7(world, state)
    
def unfinished_business9(world: World, state: CollectionState):
    """Checks if the ninth step of the Unfinished Business questline can be completed."""
    return unfinished_business8(world, state) and tohjo_falls(world, state)

def completed_unfinished_business(world: World, state: CollectionState):
    """Checks if the Unfinished Business questline has been completed."""
    return unfinished_business9(world, state)

def started_sick_ampharos(world: World, state: CollectionState):
    """Checks if the player has started the Sick Ampharos questline."""
    return ecruteak_city(world, state) and state.has("Plain Badge", world.player)

def sick_ampharos1(world: World, state: CollectionState):
    """Checks if the first step of the Sick Ampharos questline can be completed."""
    return started_sick_ampharos(world, state) and olivine_lighthouse(world, state)

def sick_ampharos2(world: World, state: CollectionState):
    """Checks if the second step of the Sick Ampharos questline can be completed."""
    return sick_ampharos1(world, state) and cianwood_city(world, state)

def completed_sick_ampharos(world: World, state: CollectionState):
    """Checks if the Sick Ampharos questline has been completed."""
    return sick_ampharos2(world, state)

def started_team_rocket_again(world: World, state: CollectionState):
    """Checks if the player has started the Team Rocket Again questline."""
    return ecruteak_city(world, state) and state.has("Plain Badge", world.player)

def team_rocket_again0(world: World, state: CollectionState):
    """Checks if the first step of the Team Rocket Again questline can be completed."""
    return started_team_rocket_again(world, state) and johto_route_43(world, state)

def team_rocket_again1(world: World, state: CollectionState):
    """Checks if the second step of the Team Rocket Again questline can be completed."""
    return team_rocket_again0(world, state) and team_rockets_hideout(world, state)

def team_rocket_again2(world: World, state: CollectionState):
    """Checks if the third step of the Team Rocket Again questline can be completed."""
    return team_rocket_again1(world, state) and radio_tower(world, state)

def completed_team_rocket_again(world: World, state: CollectionState):
    """Checks if the Team Rocket Again questline has been completed."""
    return team_rocket_again2(world, state)

def started_legendary_beasts(world: World, state: CollectionState):
    """Checks if the player has started the Legendary Beasts questline."""
    return new_bark_town(world, state) and johto_route_37(world, state)

def legendary_beasts0(world: World, state: CollectionState): # Talk to Eusine in Ecruteak City
    """Checks if the first step of the Legendary Beasts questline can be completed."""
    return started_legendary_beasts(world, state) and ecruteak_city(world, state)

def legendary_beasts1(world: World, state: CollectionState): # Clear the Burned Tower
    """Checks if the second step of the Legendary Beasts questline can be completed."""
    return legendary_beasts0(world, state) and burned_tower(world, state)

def legendary_beasts2(world: World, state: CollectionState): # Silver 3
    """Checks if the third step of the Legendary Beasts questline can be completed."""
    return legendary_beasts1(world, state)

def legendary_beasts3(world: World, state: CollectionState): # Talk to Pokéfan Derek in Ecruteak City
    """Checks if the fourth step of the Legendary Beasts questline can be completed."""
    return legendary_beasts2(world, state)

def legendary_beasts4(world: World, state: CollectionState): # Catch the Legendary Beasts
    """Checks if the fifth step of the Legendary Beasts questline can be completed."""
    return legendary_beasts3(world, state) and johto_roamer(world, state) and eusines_chase11(world, state)

def completed_legendary_beasts(world: World, state: CollectionState):
    """Checks if the Legendary Beasts questline has been completed."""
    return legendary_beasts4(world, state)

def started_eusines_chase(world: World, state: CollectionState):
    """Checks if the player has started the Eusine's Chase questline."""
    return legendary_beasts3(world, state)

def eusines_chase0(world: World, state: CollectionState): # Suicune 1
    """Checks if the first step of the Eusine's Chase questline can be completed."""
    return started_eusines_chase(world, state) and johto_route_41(world, state)

def eusines_chase1(world: World, state: CollectionState): # Talk to Eusine in Cianwood City
    """Checks if the second step of the Eusine's Chase questline can be completed."""
    return eusines_chase0(world, state) and cianwood_city(world, state)

def eusines_chase2(world: World, state: CollectionState): # Defeat Eusine
    """Checks if the third step of the Eusine's Chase questline can be completed."""
    return eusines_chase1(world, state)

def eusines_chase3(world: World, state: CollectionState): # Suicune 2
    """Checks if the fourth step of the Eusine's Chase questline can be completed."""
    return eusines_chase2(world, state) and johto_route_42(world, state)

def eusines_chase4(world: World, state: CollectionState): # Talk to Eusine in Mahogany Town
    """Checks if the fifth step of the Eusine's Chase questline can be completed."""
    return eusines_chase3(world, state) and mahogany_town(world, state)

def eusines_chase5(world: World, state: CollectionState): # Suicune 3
    """Checks if the sixth step of the Eusine's Chase questline can be completed."""
    return eusines_chase4(world, state) and state.has("Johto Elite Champion Badge", world.player)

def eusines_chase6(world: World, state: CollectionState): # Talk to Eusine in Vermilion City
    """Checks if the seventh step of the Eusine's Chase questline can be completed."""
    return eusines_chase5(world, state) and vermilion_city(world, state)

def eusines_chase7(world: World, state: CollectionState): # Suicune 4
    """Checks if the eighth step of the Eusine's Chase questline can be completed."""
    return eusines_chase6(world, state) and kanto_route_14(world, state)

def eusines_chase8(world: World, state: CollectionState): # Talk to Eusine in Fuchsia City
    """Checks if the ninth step of the Eusine's Chase questline can be completed."""
    return eusines_chase7(world, state) and fuchsia_city(world, state)

def eusines_chase9(world: World, state: CollectionState): # Suicune 5
    """Checks if the tenth step of the Eusine's Chase questline can be completed."""
    return eusines_chase8(world, state)

def eusines_chase10(world: World, state: CollectionState): # Talk to Eusine in Bill's House
    """Checks if the eleventh step of the Eusine's Chase questline can be completed."""
    return eusines_chase9(world, state) and bills_house(world, state)

def eusines_chase11(world: World, state: CollectionState): # Suicune 6
    """Checks if the twelfth step of the Eusine's Chase questline can be completed."""
    return eusines_chase10(world, state)

def completed_eusines_chase(world: World, state: CollectionState):
    """Checks if the Eusine's Chase questline has been completed."""
    return eusines_chase11(world, state)

def started_whirl_guardian(world: World, state: CollectionState):
    """Checks if the player has started the Whirl Guardian questline."""
    return completed_team_rocket_again(world, state) and new_bark_town(world, state)

def whirl_guardian0(world: World, state: CollectionState): # Talk to Kimono Girl Zuki in Violet City
    """Checks if the first step of the Whirl Guardian questline can be completed."""
    return started_whirl_guardian(world, state) and violet_city(world, state)

def whirl_guardian1(world: World, state: CollectionState): # Hatch eggs
    """Checks if the second step of the Whirl Guardian questline can be completed."""
    return whirl_guardian0(world, state) and state.has("Mystery Egg", world.player)

def whirl_guardian2(world: World, state: CollectionState): # Talk to Kimono Girl Naoko in the Ilex Forest
    """Checks if the third step of the Whirl Guardian questline can be completed."""
    return whirl_guardian1(world, state) and ilex_forest(world, state, False)

def whirl_guardian3(world: World, state: CollectionState): # Clear Ilex Forest to lead Naoko to safety
    """Checks if the fourth step of the Whirl Guardian questline can be completed."""
    return whirl_guardian2(world, state) and ilex_forest(world, state)

def whirl_guardian4(world: World, state: CollectionState): # Talk to Kimono Girl Miki at the Ecruteak City Dance Theatre
    """Checks if the fifth step of the Whirl Guardian questline can be completed."""
    return whirl_guardian3(world, state) and ecruteak_city(world, state)

def whirl_guardian5(world: World, state: CollectionState): # Talk to Kimono Girl Sayo in the Ice Path
    """Checks if the sixth step of the Whirl Guardian questline can be completed."""
    return whirl_guardian4(world, state) and ice_path(world, state, False)

def whirl_guardian6(world: World, state: CollectionState): # Clear the Ice Path to give Sayo a push
    """Checks if the seventh step of the Whirl Guardian questline can be completed."""
    return whirl_guardian5(world, state) and ice_path(world, state, True)

def whirl_guardian7(world: World, state: CollectionState): # Talk to Kimono Girl Kuni in Goldenrod City
    """Checks if the eighth step of the Whirl Guardian questline can be completed."""
    return whirl_guardian6(world, state) and goldenrod_city(world, state)

def whirl_guardian8(world: World, state: CollectionState): # Clear the Radio Tower to get rid of any lingering Team Rocket activity
    """Checks if the ninth step of the Whirl Guardian questline can be completed."""
    return whirl_guardian7(world, state) and radio_tower(world, state)

def whirl_guardian9(world: World, state: CollectionState): # Meet the Kimono Girls at the Whirl Islands
    """Checks if the tenth step of the Whirl Guardian questline can be completed."""
    return whirl_guardian8(world, state) and whirl_islands(world, state, False)

def whirl_guardian10(world: World, state: CollectionState): # Catch Lugia in the Whirl Islands
    """Checks if the eleventh step of the Whirl Guardian questline can be completed."""
    return whirl_guardian9(world, state) and whirl_islands(world, state, True, 1410000)

def completed_whirl_guardian(world: World, state: CollectionState):
    """Checks if the Whirl Guardian questline has been completed."""
    return whirl_guardian10(world, state)

def started_rainbow_guardian(world: World, state: CollectionState):
    """Checks if the player has started the Rainbow Guardian questline."""
    return completed_whirl_guardian(world, state) and completed_legendary_beasts(world, state) and new_bark_town(world, state)

def rainbow_guardian0(world: World, state: CollectionState): # Meet the Kimono Girls at the Ecruteak Dance Theatre
    """Checks if the first step of the Rainbow Guardian questline can be completed."""
    return started_rainbow_guardian(world, state) and ecruteak_city(world, state)

def rainbow_guardian1(world: World, state: CollectionState): # Prove your abilities as a trainer to the Kimono Girls of Ecruteak City
    """Checks if the second step of the Rainbow Guardian questline can be completed."""
    return rainbow_guardian0(world, state) and ecruteak_city(world, state)

def rainbow_guardian2(world: World, state: CollectionState): # Catch Ho-Oh in the Tin Tower
    """Checks if the third step of the Rainbow Guardian questline can be completed."""
    return rainbow_guardian1(world, state) and tin_tower(world, state, True, 1410000)

def completed_rainbow_guardian(world: World, state: CollectionState):
    """Checks if the Rainbow Guardian questline has been completed."""
    return rainbow_guardian2(world, state)

def started_how_blue_mouse(world: World, state: CollectionState):
    """Checks if the player has started the How Blue Mouse questline."""
    return has_script(world, state, "Infinite Seasonal Events") and any_bulletin_board(world, state)

def how_blue_mouse(world: World, state: CollectionState): # Talk to the Blue Mouse in New Bark Town
    """Checks if the How Blue Mouse questline can be completed."""
    return started_how_blue_mouse(world, state) and _evaluate_rule(make_pokemon_rule("Marill", allow_breed=False), world, state)

def started_egg_hunt(world: World, state: CollectionState):
    """Checks if the player has started the Easter Egg Hunt questline."""
    return has_script(world, state, "Infinite Seasonal Events") and any_bulletin_board(world, state)

def egg_hunt0(world: World, state: CollectionState): 
    """Checks if the first step of the Easter Egg Hunt questline can be completed."""
    return started_egg_hunt(world, state) and viridian_forest(world, state)

def egg_hunt1(world: World, state: CollectionState): 
    """Checks if the second step of the Easter Egg Hunt questline can be completed."""
    return egg_hunt0(world, state) and ilex_forest(world, state)

def egg_hunt23(world: World, state: CollectionState): 
    """Checks if the third step of the Easter Egg Hunt questline can be completed."""
    return egg_hunt1(world, state) # and petalburg_woods(world, state)

def completed_egg_hunt(world: World, state: CollectionState):
    """Checks if the Easter Egg Hunt questline has been completed."""
    return egg_hunt23(world, state)

# def started_detective_pikachu(world: World, state: CollectionState):
#     """Checks if the player has started the Detective Pikachu questline."""
#     return has_script(world, state, "Detective Pikachu") and vaniville_town(world, state)

def completed_detective_pikachu(world: World, state: CollectionState):
    """Checks if the Detective Pikachu questline has been completed."""
    return False

# Special Conditions
def any_bulletin_board(world: World, state: CollectionState):
    """Checks if the player can access any bulletin board."""
    return (
        pallet_town(world, state)
         or new_bark_town(world, state)
    )

def any_kanto_route(world: World, state: CollectionState):
    """Checks if the player can access any Kanto route."""
    return (
        kanto_route_1(world, state) or kanto_route_2(world, state) or kanto_route_3(world, state) or
        kanto_route_4(world, state) or kanto_route_5(world, state) or kanto_route_6(world, state) or
        kanto_route_7(world, state) or kanto_route_8(world, state) or kanto_route_9(world, state) or
        kanto_route_10(world, state) or kanto_route_11(world, state) or kanto_route_12(world, state) or
        kanto_route_13(world, state) or kanto_route_14(world, state) or kanto_route_15(world, state) or
        kanto_route_16(world, state) or kanto_route_17(world, state) or kanto_route_18(world, state) or
        kanto_route_19(world, state) or kanto_route_20(world, state) or kanto_route_21(world, state) or
        kanto_route_22(world, state) or kanto_route_23(world, state) or kanto_route_24(world, state) or
        kanto_route_25(world, state)
    )

def any_sevii123_route(world: World, state: CollectionState):
    """Checks if the player can access any Sevii 123 route."""
    return (
        treasure_beach(world, state) or kindle_road(world, state) or
        cape_brink(world, state) or bond_bridge(world, state)
    )

# def any_sevii4567_route(world: World, state: CollectionState):
#     """Checks if the player can access any Sevii 4567 route."""
#     return (
#         five_isle_meadow(world, state) or memorial_pillar(world, state) or
#         water_labyrinth(world, state) or resort_gorgeous(world, state) or
#         water_path(world, state) or green_path(world, state) or
#         outcast_island(world, state) or ruin_valley(world, state) or
#         canyon_entrance(world, state) or sevault_canyon(world, state) or
#         valencia_island(world, state) or pinkan_forest(world, state) or
#         pinkan_plains(world, state)
#     )

def any_johto_route(world: World, state: CollectionState):
    """Checks if the player can access any Johto route."""
    return (
        johto_route_29(world, state) or johto_route_30(world, state) or johto_route_31(world, state) or
        johto_route_32(world, state) or johto_route_33(world, state) or johto_route_34(world, state) or
        johto_route_35(world, state) or johto_route_36(world, state) or johto_route_37(world, state) or
        johto_route_38(world, state) or johto_route_39(world, state) or johto_route_40(world, state) or
        johto_route_41(world, state) or johto_route_42(world, state) or johto_route_43(world, state) or
        johto_route_44(world, state) or johto_route_45(world, state) or johto_route_46(world, state) or
        johto_route_47(world, state) or johto_route_48(world, state) or johto_route_26(world, state) or
        johto_route_27(world, state) or johto_route_28(world, state)
    )

# def any_hoenn_route(world: World, state: CollectionState):
#     """Checks if the player can access any Hoenn route."""
#     return (
#         hoenn_route_101(world, state) or hoenn_route_102(world, state) or hoenn_route_103(world, state) or
#         hoenn_route_104(world, state) or hoenn_route_105(world, state) or hoenn_route_106(world, state) or
#         hoenn_route_107(world, state) or hoenn_route_108(world, state) or hoenn_route_109(world, state) or
#         hoenn_route_110(world, state) or hoenn_route_111(world, state) or hoenn_route_112(world, state) or
#         hoenn_route_113(world, state) or hoenn_route_114(world, state) or hoenn_route_115(world, state) or
#         hoenn_route_116(world, state) or hoenn_route_117(world, state) or hoenn_route_118(world, state) or
#         hoenn_route_119(world, state) or hoenn_route_120(world, state) or hoenn_route_121(world, state) or
#         hoenn_route_122(world, state) or hoenn_route_123(world, state) or hoenn_route_124(world, state) or
#         hoenn_route_125(world, state) or hoenn_route_126(world, state) or hoenn_route_127(world, state) or
#         hoenn_route_128(world, state) or hoenn_route_129(world, state) or hoenn_route_130(world, state) or
#         hoenn_route_131(world, state) or hoenn_route_132(world, state) or hoenn_route_133(world, state) or
#         hoenn_route_134(world, state) or rock_poke_spot(world, state) or oasis_poke_spot(world, state) or cave_poke_spot(world, state)
#     )

def can_buy_pokeballs(world: World, state: CollectionState):
    """Checks if the player can buy Pokéballs.""" # kanto, sevii123, and johto cities
    return viridian_city(world, state) or pewter_city(world, state) or cerulean_city(world, state) or vermilion_city(world, state) or lavender_town(world, state) or celadon_city(world, state) or saffron_city(world, state) or fuchsia_city(world, state) or cinnabar_island(world, state) or one_island(world, state) or two_island(world, state) or three_island(world, state) or cherrygrove_city(world, state) or violet_city(world, state) or azalea_town(world, state) or goldenrod_city(world, state) or ecruteak_city(world, state) or olivine_city(world, state) or cianwood_city(world, state) or mahogany_town(world, state) or blackthorn_city(world, state)

def can_catch_x_pokemon(world: World, state: CollectionState, x: int):
    """Checks if the player can obtain at least X pokemon."""
    return state.count_group("Pokemon", world.player) >= int(x)

def get_party_attack(world: World, state: CollectionState, num_pokemon: int, region: str = "Kanto") -> set:
    """Returns the attack value of the player's expected current party."""
    count_pokemon = state.count_group("Pokemon", world.player)
    count_region = state.count_group(f"{region} Pokemon", world.player)
    num_badges = state.count_group("Badges", world.player)
    avgBaseAttack = 70 + 4.2 * num_badges
    avgLevel = min(100, 20 + 10 * num_badges)
    return num_pokemon * avgBaseAttack * (avgLevel / 100)

def get_click_attack(world: World, state: CollectionState, num_pokemon: int) -> set:
    """Returns the attack value of the player's expected clicker attack."""
    achievement_bonus = 1
    num_caught = num_pokemon
    num_shiny = 0
    num_resistant = 0
    num_purified = 0
    has_shiny_code = state.has("Shiny-Charmer Code", world.player)
    has_rocky_helmet = state.has("Rocky Helmet", world.player)
    has_black_flute = state.has("Black Flute", world.player)
    has_x_click = state.has("X Click", world.player)
    if has_shiny_code:
        num_shiny += 1
    
    attack = ((1 + achievement_bonus) * ((num_caught + num_shiny + num_resistant + num_purified + 1) ** 1.4))

    if has_rocky_helmet:
        attack *= 1.5
    if has_black_flute:
        attack *= float(round(.02 * (achievement_bonus + 1) + 1, 4))
    if has_x_click:
        attack *= 1.5
    return attack
    
def attack_needed(world: World, state: CollectionState, attack: int, region: str = "Kanto"):
    """Checks if the player's expected current party attack is at least X."""
    num_pokemon = state.count_group("Pokemon", world.player) #len(get_catchable_pokemon(world, state))
    auto_clicker_count = state.count("Enhanced Auto Clicker", world.player)
    if world.options.use_scripts.value and not world.options.include_scripts_as_items.value:
        auto_clicker_count = 1
    progressive_auto_clicker_count = state.count("Enhanced Auto Clicker (Progressive Clicks/Second)", world.player)
    if progressive_auto_clicker_count > 0:
        auto_clicker_count = 0
    clicks_per_second = max(world.options.clicks_per_second.value, auto_clicker_count * 100, progressive_auto_clicker_count * 20)
    attack_from_clicks = get_click_attack(world, state, num_pokemon) * clicks_per_second
    can_breed = (state.count_group("Badges", world.player) >= 8 and state.has("Mystery Egg", world.player))
    return (can_breed or (get_party_attack(world, state, num_pokemon, region) + attack_from_clicks) * 25 >= int(attack))

def dungeon_attack_needed(world: World, state: CollectionState, minion_attack: int, special_boss_attack: int, complete_dungeon: bool, region: str = "Kanto"):
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
    return attack_needed(world, state, attack, region)

def dexsanity_enabled(world: World, state: CollectionState):
    """Checks if Dexsanity is enabled."""
    return world.options.dexsanity.value > 0

def dexsanity_disabled(world: World, state: CollectionState):
    """Checks if Dexsanity is disabled."""
    return world.options.dexsanity.value == 0

def can_breed(world: World, state: CollectionState, pokemon: str):
    """Checks if the pokemon has been received and can be hatched."""
    has_pokemon = state.count(pokemon, world.player) > 0
    has_8_badges = state.count_group("Badges", world.player) >= 8
    has_hatchery = state.count("Mystery Egg", world.player) > 0
    return has_pokemon and has_8_badges and has_hatchery

def starter_pokemon(world: World, state: CollectionState):
    """Checks if the starters are in logic."""
    return world.options.starter_logic.value

def kanto_starter(world: World, state: CollectionState):
    """Checks if the Kanto starters are in logic."""
    # To be implemented later
    return starter_pokemon(world, state)

def kanto_roamer(world: World, state: CollectionState):
    """Checks if the Kanto roamers are in logic."""
    has_champion_badge = state.has("Kanto Elite Champion Badge", world.player)
    return has_champion_badge and fuchsia_city(world, state)

# def sevii_roamer(world: World, state: CollectionState):
#     """Checks if the Sevii roamers are in logic."""
#     has_champion_badge = state.has("Elite Orange Champion Badge", world.player)
#     return has_champion_badge and six_island(world, state)

def johto_roamer(world: World, state: CollectionState):
    """Checks if the Johto roamers are in logic."""
    has_champion_badge = state.has("Johto Elite Champion Badge", world.player)
    return has_champion_badge and blackthorn_city(world, state)

ROAMER_REGIONS = {
    "Kanto": kanto_roamer,
    "Johto": johto_roamer,
}

def roamer(world: World, state: CollectionState, region: str):
    """Checks if the roamer in the specified region is in logic."""
    if region not in ROAMER_REGIONS:
        return False
    return ROAMER_REGIONS[region](world, state)

def has_script(world: World, state: CollectionState, script_name: str):
    """Checks if the player needs a specific script."""
    if not world.options.use_scripts.value:
        return True
    # script_item = get_items_with_value(world, f"Script: {script_name}")
    return state.has(script_name, world.player)

def can_wander(world: World, state: CollectionState):
    """Checks if wanderer pokemon are in logic."""
    if not world.options.wanderers_in_logic.value:
        return False
    return state.has("Wailmer Pail", world.player)

def has_all_in_group(world: World, state: CollectionState, group_name: str):
    """Return a rule that checks whether the player has every item in the given group."""
    group_items = world.item_name_groups.get(group_name, ())
    return state.has_group(group_name, world.player, len(group_items))


SAFARI_REGIONS = {
    "Kanto": safari_zone,
    "Johto": national_park,
}

def region_safari(world: World, state: CollectionState, region: str):
    """Checks if the region safari zone is in logic."""
    if region not in SAFARI_REGIONS:
        return False
    return SAFARI_REGIONS[region](world, state)

def discord_pokemon(world: World, state: CollectionState, name: str, region: str):
    """Checks if the discord pokemon are in logic."""
    reached_region = state.has(region, world.player)
    code_items = bool(world.options.include_codes_as_items.value)
    code_needed = state.has(f"{name} Code", world.player) if code_items else True
    return reached_region and code_needed
