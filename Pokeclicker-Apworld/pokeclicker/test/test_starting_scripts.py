import unittest
from argparse import Namespace
from collections import Counter
from types import SimpleNamespace
from unittest.mock import patch

from BaseClasses import CollectionState, MultiWorld
from worlds.AutoWorld import call_all

from .. import items, rules
from ..world import PokeclickerWorld


class Option:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)


class StartingScriptsTest(unittest.TestCase):
    def make_world(self, *, scripts=True, pooled=False, seasonal=True, progressive=False):
        options = SimpleNamespace(**{
            name: Option(value) for name, value in {
                "use_scripts": scripts,
                "include_scripts_as_items": pooled,
                "include_seasonal_events": seasonal,
                "progressive_autoclicker": progressive,
                "progressive_auto_safari_zone": progressive,
                "goal": 0,
                "dexsanity": 3,
                "include_alt_pokemon": True,
                "include_palaeontologist_token": False,
                "include_black_glasses": False,
                "include_codes_as_items": False,
            }.items()
        })
        world = SimpleNamespace(
            options=options,
            player=1,
            multiworld=SimpleNamespace(itempool=[], get_unfilled_locations=lambda player: []),
            precollected=[],
        )
        world.create_item = lambda name: items.create_item_with_correct_classification(world, name)
        world.push_precollected = world.precollected.append
        return world

    def test_scripts_start_enabled_without_entering_pool(self):
        for progressive in (False, True):
            with self.subTest(progressive=progressive):
                world = self.make_world(progressive=progressive)
                items.create_all_items(world)
                starting_names = {item.name for item in world.precollected}
                pool_names = {item.name for item in world.multiworld.itempool}
                self.assertIn("Infinite Seasonal Events Script", starting_names)
                self.assertIn("Enhanced Auto Mine Script", starting_names)
                self.assertNotIn("Infinite Seasonal Events Script", pool_names)
                self.assertIn(
                    "Auto Safari Zone Script (Progressive Fast Animations)" if progressive else "Auto Safari Zone Script",
                    starting_names,
                )
                self.assertNotIn(
                    "Auto Safari Zone Script" if progressive else "Auto Safari Zone Script (Progressive Fast Animations)",
                    starting_names,
                )

    def test_disabled_seasonal_script_is_not_precollected(self):
        world = self.make_world(seasonal=False)
        items.create_all_items(world)
        self.assertNotIn("Infinite Seasonal Events Script", {item.name for item in world.precollected})
        self.assertIn("Enhanced Auto Mine Script", {item.name for item in world.precollected})

    def test_pooled_scripts_are_not_precollected(self):
        world = self.make_world(pooled=True)
        items.create_all_items(world)
        self.assertFalse(world.precollected)
        self.assertIn("Infinite Seasonal Events Script", {item.name for item in world.multiworld.itempool})

    def test_scripts_disabled_do_not_start_as_items(self):
        world = self.make_world(scripts=False)
        items.create_all_items(world)
        self.assertFalse(world.precollected)
        self.assertNotIn("Infinite Seasonal Events Script", {item.name for item in world.multiworld.itempool})

    def test_seasonal_location_rules_use_starting_script(self):
        world = self.make_world()
        items.create_all_items(world)
        inventory = Counter(item.name for item in world.precollected)
        inventory["Dungeon Ticket"] = 1
        state = SimpleNamespace(
            has=lambda name, player: inventory[name] > 0,
            count=lambda name, player: inventory[name],
        )
        with patch.object(rules, "dungeon_attack_needed", return_value=True), \
             patch.object(rules, "attack_needed", return_value=True), \
             patch.object(rules, "bills_house", return_value=True):
            for rule in (rules.new_island, rules.ash_ketchum_new_island, rules.santa_jynx1):
                with self.subTest(rule=rule.__name__):
                    self.assertTrue(rule(world, state))
                    inventory["Infinite Seasonal Events Script"] = 0
                    self.assertFalse(rule(world, state))
                    inventory["Infinite Seasonal Events Script"] = 1

    def test_all_six_locations_reachable_in_real_multiworld(self):
        overrides = {
            "dexsanity": 3,
            "include_alt_pokemon": True,
            "use_scripts": True,
            "include_scripts_as_items": False,
            "include_seasonal_events": True,
        }
        multiworld = MultiWorld(1)
        multiworld.game[1] = "Pokeclicker"
        multiworld.player_name = {1: "Tester"}
        multiworld.set_seed(19341395265576256878)
        args = Namespace()
        for name, option in PokeclickerWorld.options_dataclass.type_hints.items():
            setattr(args, name, {1: option.from_any(overrides.get(name, option.default))})
        multiworld.set_options(args)
        multiworld.state = CollectionState(multiworld)
        for step in ("generate_early", "create_regions", "create_items", "set_rules",
                     "connect_entrances", "generate_basic", "pre_fill"):
            call_all(multiworld, step)
        state = multiworld.get_all_state()
        self.assertTrue(state.has("Infinite Seasonal Events Script", 1))
        for name in (
            "New Island",
            "Ash Ketchum New Island",
            "Santa Jynx Band 1",
            "Santa Jynx Band 2",
            "Santa Jynx Band 3",
            "Santa Jynx Band 4",
        ):
            with self.subTest(location=name):
                self.assertTrue(multiworld.get_location(name, 1).can_reach(state))