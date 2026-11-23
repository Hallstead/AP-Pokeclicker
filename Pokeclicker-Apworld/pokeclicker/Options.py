from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, StartInventoryPool, Range, Toggle, TextChoice

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.
class Goal(Choice):
    """
    What is the goal of the game?
    """
    display_name = "Goal"

    option_travel_to_johto = 0
    option_travel_to_hoenn = 1

    default = option_travel_to_hoenn


class Dexsanity(Choice):
    """
    Pokemon join the pool of locations and items.
    With this enabled, capturing all Pokemon before traveling to the next region is logically required.
    
    None: Pokemon are not locations, and catching a Pokemon gives that Pokemon.
    Shuffled per Region: Pokemon locations are shuffled within each region. This is the region required to capture the Pokemon.
        For example Kanto Pokemon that cannot normally be caught until reaching Hoenn will be shuffled with Hoenn Pokemon.
    Shuffled: Pokemon locations contain Pokemon from any region.
    Full: All Pokemon are randomized into the item pool.
    """
    display_name = "Dexsanity"
    
    option_none = 0
    # option_locations_only = 1
    option_shuffled_per_region = 2
    option_shuffled = 3
    option_full = 4

    default = option_none

class IncludeAltPokemon(Toggle):
    """
    With this enabled, alternate forms of Pokemon will be included in the randomization pool.
    This does nothing if dexsanity is set to none.
    """
    display_name = "Include Alt Pokemon Forms"
    default = True

class BadgeRandomization(Choice):
    """
    This option sets how badges are randomized.
    None: Badges are placed in their vanilla locations. This option leads to more vanilla progression.
    Full: Badges are put into the item pool with everything else.
    """
    display_name = "Badge Randomization"

    option_none = 0
    option_full = 2

    default = option_none

class UseScripts(Toggle):
    """
    Should QoL scripts be enabled?
    """
    display_name = "Enable QoL Scripts"
    default = False

class IncludeScriptsAsItems(Toggle):
    """
    Are the scripts included as items in the randomization pool?
    Setting this option requires you to find the scripts as items before they can be used.
    This does nothing if use_scripts is false.
    """
    display_name = "Include QoL Scripts in the Itempool"
    default = False

class ProgressiveAutoClicker(Toggle):
    """
    Should the Auto Clicker speed be progressive?
    With this enabled, The first Enhanced Auto Clicker unlocks the Auto Clicker script,
    and each Enhanced Auto Clicker you find after will increase your clicks/second
    by 20 to a maximum of 100.
    This does nothing if use_scripts is false.
    """
    display_name = "Progressive Auto Clicker"
    default = False

class ProgressiveAutoSafariZone(Toggle):
    """
    Should the Auto Safari Zone speed be progressive?
    With this enabled, The first Enhanced Auto Safari Zone unlocks the Auto Safari Zone,
    and each Enhanced Auto Safari Zone you find after will increase your Animation speed a bit.
    This does nothing if use_scripts is false.
    """
    display_name = "Progressive Auto Safari Zone"
    default = False

class IncludeSeasonalEvents(Toggle):
    """
    Are Seasonal Event locations and Pokemon included in the pool?
    This option overrides the use_scripts option.
    """
    display_name = "Include Seasonal Event Pokemon"
    default = True

class IncludeCodesAsItems(Toggle):
    """
    Should the codes be included as items in the item pool?
    With this enabled, the input to enter codes manually will be disabled.
    """
    display_name = "Include Redeemable and Discord Codes as Items"
    default = False

class IncludePalaeontologistToken(Toggle):
    """
    Should a Palaeontologist Token be included in the item pool?
    With this enabled, a Palaeontologist Token will be available and logically required to trade for Pikachu (Palaeontologist) on Cinnabar Island.
    """
    display_name = "Include a Palaeontologist Token in the Pool"
    default = False

class IncludeBlackGlasses(Toggle):
    """
    Should a pair of Black Glasses be included as an item in the item pool?
    With this enabled, the Black Glasses will be available and logically required, so you will not need to grind for the rare loot.
    """
    display_name = "Include a Black Glasses in the Pool"
    default = False

class Mapsanity(Choice):
    """
    This option adds all map locations to the item pool.
    Instead of unlocking their normal map locations, when you would unlock a route or town, it instead sends a check to the server.
    None: This option is disabled, and map location unlock as normal
    Shuffled: Map locations are shuffled amongst themselves.
    Full: Map locations are added to the item pool with everything else
    """
    display_name = "Mapsanity"
    option_none = 0
    option_shuffled = 1
    option_full = 2
    default = option_none

class StartingSafariLevel(Range):
    """
    Sets the starting level for the Safari Zone.
    """
    display_name = "Starting Safari Level"
    range_start = 1
    range_end = 40
    default = 1

class StartingUndergroundLevel(Range):
    """
    Sets the starting level for the Underground.
    """
    display_name = "Starting Underground Level"
    range_start = 0
    range_end = 60
    default = 0

class RoamingEncounterMultiplier(Range):
    """
    Sets the multiplier for roaming encounter rates on the boosted route.
    Higher values make roaming Pokemon appear more frequently on that route.
    If the multiplier is set to 137, roaming pokemon will appear roughly 5-10% of encounters,
        depending on where the boosted route is.
    To activate this multipier in a given region, talk to that region's Roamer NPC after defeating the champion.
    """
    display_name = "Roaming Encounter Chance Multiplier"
    range_start = 1
    range_end = 150
    default = 2

class RoamingEncounterMultiplierRoute(Toggle):
    """
    Should the roaming encounter rate multiplier apply to the boosted route only?
    With this enabled, only the boosted route will have increased roaming encounter rates.
    With this disabled, all routes will have increased roaming encounter rates,
       but the boosted route will still have the highest rate.
    """
    display_name = "Roaming Encounter Chance Multiplier Only For Boosted Route"
    default = True

class PokedollarMultiplier(Range):
    """
    A multiplier for the amount of Pokedollars earned from all sources.
    """
    display_name = "Pokedollar Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class DungeonTokenMultiplier(Range):
    """
    A multiplier for the amount of Dungeon Tokens earned from all sources.
    """
    display_name = "Dungeon Token Multiplier"
    range_start = 1
    range_end = 10
    default = 1
    
class QuestPointMultiplier(Range):
    """
    A multiplier for the amount of Quest Points earned from all sources.
    """
    display_name = "Quest Point Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class DiamondMultiplier(Range):
    """
    A multiplier for the amount of Diamonds earned from all sources.
    """
    display_name = "Diamond Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class FarmPointMultiplier(Range):
    """
    A multiplier for the amount of Farm Points earned from all sources.
    """
    display_name = "Farm Point Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class BattlePointMultiplier(Range):
    """
    A multiplier for the amount of Battle Points earned from all sources.
    """
    display_name = "Battle Point Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class ContestTokenMultiplier(Range):
    """
    A multiplier for the amount of Contest Tokens earned from all sources.
    """
    display_name = "Contest Token Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class ExpMultiplier(Range):
    """
    A multiplier for the amount of exp earned from battles.
    """
    display_name = "Exp Multiplier"
    range_start = 1
    range_end = 10
    default = 1
    
class WandererAppearanceMultiplier(Range):
    """
    A multiplier for the chance a Wanderer has to appear in the farm.
    """
    display_name = "Wanderer Appearance Multiplier"
    range_start = 1
    range_end = 10
    default = 1

class WandererBaseCatchRate(Range):
    """
    Sets the base chance to catch a Wanderer.
    100 would be a guaranteed catch. 0 uses the default catch rate from the game.
    """
    display_name = "Wanderer Base Catch Rate"
    range_start = 0
    range_end = 100
    default = 0

class StarterLogic(Toggle):
    """
    Are starter Pokemon considered in logic at the beginning of the region?
    With this enabled, you would be expected to reset the game to obtain all the starters.
    This does nothing if dexsanity is set to None.
    """
    display_name = "Include Starter Selection In Logic"
    default = False

class EarlyTownMap(Toggle):
    """
    Determines if the Town Map is forced early.
    """
    display_name = "Early Town Map"
    default = False

class MysteryEggInLogic(Toggle):
    """
    Are Mystery Eggs considered in logic for obtaining Pokemon?
    """
    display_name = "Mystery Egg Counts For Egg Logic"
    default = False

class ClicksPerSecond(Range):
    """
    Sets the assumed clicks per second for the player.
    This affects the logic for attack needed for the player to be expected to defeat dungeons and gym leaders.
    It is recommended to check your clicks per second rate with an online CPS tester to ensure you can click as fast as your setting.
    """
    display_name = "Your Average Clicks Per Second"
    range_start = 1
    range_end = 20
    default = 5

class DungeonLogic(Choice):
    """
    This option determines how much attack power is needed to reliably find and catch a dungeon Pokemon.
    Early: Dungeons and their Pokemon are brought into logic if you can clear only one or two dungeon spaces for the event that the Pokemon/boss is one of them. This option is much more RNG dependant.
    Half: Dungeons and their Pokemon are brought into logic if you can clear about half the dungeon spaces for the event that the Pokemon/boss is one of them.
    All: Dungeons and their Pokemon assume you must be able to fully clear the dungeon to be in logic.
    """
    display_name = "How Much of a Dungeon is Expected to be Clearable to find the Boss"
    option_none = 0
    option_half = 1
    option_full = 2
    default = 1

class SafariZoneLogic(Toggle):
    """
    Is the Auto Safari Zone script logically required to obtain Pokemon in the Safari Zone?
    This does nothing if use_scripts or include_scripts_as_items are false.
    """
    display_name = "Auto Safari Zone Script Required for Safari Pokemon Logic"
    default = False

class WanderersInLogic(Toggle):
    """
    Are Wanderers considered in logic for obtaining Pokemon?
    This will remove wandering in the farm from logic. It does not remove those Pokemon from the pool.
    **At this time wanderers are not implemented in logic and this option has no effect.**
    """
    display_name = "Include Farm Wandering Logic"
    default = False

class RegionalAttackDebuff(Toggle):
    """
    Lowers Pokemon attack based on native region and highest-reached region.
    """
    display_name = "Regional Attack Debuff"
    default = True

class RequireCompletePokedex(Toggle):
    """
    Requires a complete regional Pokedex before moving on to the next region.
    """
    display_name = "Require Complete Pokedex"
    default = True

class NoClickAttack(Toggle):
    """
    Disables the ability to use Click Attacks.
    """
    display_name = "No Click Attack"
    default = False

class NoBattleItems(Toggle):
    """
    Disables the usage of Battle Items.
    At this time, Battle Items are not factored into the apworld logic.
    """
    display_name = "No Battle Items"
    default = False

class NoMasterBalls(Toggle):
    """
    Disables the usage of Master Balls.
    """
    display_name = "No Master Balls"
    default = False

class NoOakItems(Toggle):
    """
    Disables the usage of all Oak Items.
    """
    display_name = "No Oak Items"
    default = False

class NoGemUpgrades(Toggle):
    """
    Disables the usage of Gems to increase type effectiveness.
    At this time, Gems are not factored into the apworld logic.
    """
    display_name = "No Gem Upgrades"
    default = False

class NoVitamins(Toggle):
    """
    Disables the usage of Vitamins.
    At this time, Vitamins are not factored into the apworld logic.
    """
    display_name = "No Vitamins"
    default = False

class SlowEVs(Toggle):
    """
    Gain EVs 10x slower.
    """
    display_name = "Slow EVs"
    default = False

class RealEvolution(Toggle):
    """
    Your Pokémon go away when they evolve.
    At this time, Real Evolution is not factored into the apworld logic.
    It is recommended to disable the Require Complete Pokedex option when using Real Evolution.
    -Enable at your own risk-

    """
    display_name = "Real Evolution"
    default = False


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class PokeclickerOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    dexsanity: Dexsanity
    include_alt_pokemon: IncludeAltPokemon
    badge_randomization: BadgeRandomization
    use_scripts: UseScripts
    include_scripts_as_items: IncludeScriptsAsItems
    progressive_autoclicker: ProgressiveAutoClicker
    progressive_auto_safari_zone: ProgressiveAutoSafariZone
    include_seasonal_events: IncludeSeasonalEvents
    include_codes_as_items: IncludeCodesAsItems
    include_palaeontologist_token: IncludePalaeontologistToken
    include_black_glasses: IncludeBlackGlasses
    starting_safari_level: StartingSafariLevel
    starting_underground_level: StartingUndergroundLevel
    roaming_encounter_multiplier: RoamingEncounterMultiplier
    roaming_encounter_multiplier_route: RoamingEncounterMultiplierRoute
    pokedollar_multiplier: PokedollarMultiplier
    dungeon_token_multiplier: DungeonTokenMultiplier
    quest_point_multiplier: QuestPointMultiplier
    diamond_multiplier: DiamondMultiplier
    farm_point_multiplier: FarmPointMultiplier
    contest_token_multiplier: ContestTokenMultiplier
    # battle_point_multiplier: BattlePointMultiplier
    exp_multiplier: ExpMultiplier
    # wanderer_appearance_multiplier: WandererAppearanceMultiplier
    # wanderer_base_catch_rate: WandererBaseCatchRate
    starter_logic: StarterLogic
    early_town_map: EarlyTownMap
    mystery_egg_in_logic: MysteryEggInLogic
    clicks_per_second: ClicksPerSecond
    dungeon_logic: DungeonLogic
    safari_zone_logic: SafariZoneLogic
    # wanderers_in_logic: WanderersInLogic
    regional_attack_debuff: RegionalAttackDebuff
    require_complete_pokedex: RequireCompletePokedex
    no_click_attack: NoClickAttack
    no_battle_items: NoBattleItems
    no_master_balls: NoMasterBalls
    no_oak_items: NoOakItems
    no_gem_upgrades: NoGemUpgrades
    no_vitamins: NoVitamins
    # slow_evs: SlowEVs
    real_evolution: RealEvolution


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Game Options",
        [Goal, Dexsanity, IncludeAltPokemon, BadgeRandomization, UseScripts, IncludeScriptsAsItems, ProgressiveAutoClicker, ProgressiveAutoSafariZone, IncludeSeasonalEvents, IncludeCodesAsItems, IncludePalaeontologistToken, IncludeBlackGlasses, StartingSafariLevel, StartingUndergroundLevel],
    ),
    OptionGroup(
        "Multiplier Options",
        [PokedollarMultiplier, DungeonTokenMultiplier, QuestPointMultiplier, DiamondMultiplier, FarmPointMultiplier, ContestTokenMultiplier, ExpMultiplier, RoamingEncounterMultiplier, RoamingEncounterMultiplierRoute],
        # [WandererAppearanceMultiplier, WandererBaseCatchRate],
    ),
    OptionGroup(
        "Logic Options",
        [StarterLogic, EarlyTownMap, MysteryEggInLogic, ClicksPerSecond, DungeonLogic, SafariZoneLogic],
    ),
    OptionGroup(
        "Challenges",
        [RegionalAttackDebuff, RequireCompletePokedex, NoClickAttack, NoBattleItems, NoMasterBalls, NoOakItems, NoGemUpgrades, NoVitamins, # SlowEVs,
        RealEvolution],
    )
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    # "boring": {
    #     "hard_mode": False,
    #     "hammer": False,
    #     "extra_starting_chest": False,
    #     "start_with_one_confetti_cannon": False,
    #     "trap_chance": 0,
    #     "confetti_explosiveness": ConfettiExplosiveness.range_start,
    #     "player_sprite": PlayerSprite.option_human,
    # },
    # "the true way to play": {
    #     "hard_mode": True,
    #     "hammer": True,
    #     "extra_starting_chest": True,
    #     "start_with_one_confetti_cannon": True,
    #     "trap_chance": 50,
    #     "confetti_explosiveness": ConfettiExplosiveness.range_end,
    #     "player_sprite": PlayerSprite.option_duck,
    # },
}
