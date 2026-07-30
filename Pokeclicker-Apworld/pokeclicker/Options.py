from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, TextChoice

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

class Dexsanity(Choice):
    """
    Pokemon join the pool of locations and items.
    With this enabled, capturing all pokemon before traveling to the next region is logically required.
    
    None: Pokemon are not locations, and catching a pokemon gives that pokemon.
    Shuffled: Pokemon locations only contain Pokemon
    Full: All Pokemon are randomized into the item pool.
    
    Note: Enabling Dexsanity turns on the challenge that you must capture all Pokemon before progressing to the next region.
    This can be disabled in Start Menu > Challenge Modes.
    """
    display_name = "Dexsanity"
    
    option_none = 0
    option_shuffled = 2
    option_full = 3

    default = option_none

class IncludeAltPokemon(Toggle):
    """
    With this enabled, alternate forms of Pokemon will be included in the randomization pool.
    This does nothing if dexsanity is set to none.
    """
    display_name = "Include Alternate Pokemon"
    default = False

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
    display_name = "Use Scripts"
    default = False

class IncludeScriptsAsItems(Toggle):
    """
    Are the scripts included as items in the randomization pool?
    Setting this option requires you to find the scripts as items before they can be used.
    This does nothing if use_scripts is false.
    """
    display_name = "Include Scripts as Items"
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
    Are Seasonal Event locations and pokemon included in the pool?
    This option overrides the use_scripts option.
    """
    display_name = "Include Seasonal Events"
    default = False

class IncludeCodesAsItems(Toggle):
    """
    Should the codes be included as items in the item pool?
    With this enabled, the input to enter codes manually will be disabled.
    """
    display_name = "Include Codes as Items"
    default = False

class IncludePalaeontologistToken(Toggle):
    """
    Should a Palaeontologist Token be included in the item pool?
    With this enabled, a Palaeontologist Token will be available to trade for Pikachu (Palaeontologist) on Cinnabar Island.
    """
    display_name = "Include Palaeontologist Token"
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
    """
    display_name = "Roaming Encounter Multiplier"
    range_start = 1
    range_end = 100
    default = 2

class RoamingEncounterMultiplierRoute(Toggle):
    """
    Should the roaming encounter rate multiplier apply to the boosted route only?
    With this enabled, only the boosted route will have increased roaming encounter rates.
    With this disabled, all routes will have increased roaming encounter rates.
    """
    display_name = "Roaming Encounter Multiplier Route"
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

class ConquestTokenMultiplier(Range):
    """
    A multiplier for the amount of Conquest Tokens earned from all sources.
    """
    display_name = "Conquest Token Multiplier"
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
    """
    display_name = "Starter Logic"
    default = False

class EarlyTownMap(Toggle):
    """
    Determines if the Town Map is forced early.
    """
    display_name = "Early Town Map"
    default = False

class MysteryEggInLogic(Toggle):
    """
    Are Mystery Eggs considered in logic for obtaining pokemon?
    """
    display_name = "Mystery Egg In Logic"
    default = False

class ClicksPerSecond(Range):
    """
    Sets the assumed clicks per second for the player.
    This affects the logic for attack needed for the player to be expected to defeat dungeons and gym leaders.
    It is recommended to check your clicks per second rate with an online CPS tester to ensure you can click as fast as your setting.
    """
    display_name = "Clicks Per Second"
    range_start = 1
    range_end = 20
    default = 5

class DungeonLogic(Choice):
    """
    This option determines how much attack power is needed to reliably find and catch a dungeon pokemon.
    Early: Dungeons and their pokemon are brought into logic if you can clear only one or two dungeon spaces for the event that the pokemon/boss is one of them. This option is much more RNG dependant.
    Half: Dungeons and their pokemon are brought into logic if you can clear about half the dungeon spaces for the event that the pokemon/boss is one of them.
    All: Dungeons and their pokemon assume you must be able to fully clear the dungeon to be in logic.
    """
    display_name = "Dungeon Logic"
    option_none = 0
    option_half = 1
    option_full = 2
    default = 1

class SafariZoneLogic(Toggle):
    """
    Is the Auto Safari Zone script logically required to obtain pokemon in the Safari Zone?
    This does nothing if use_scripts or include_scripts_as_items are false.
    """
    display_name = "Safari Zone Logic"
    default = False

class WanderersInLogic(Toggle):
    """
    Are Wanderers considered in logic for obtaining pokemon?
    This will remove wandering in the farm from logic. It does not remove those pokemon from the pool.
    """
    display_name = "Wanderers In Logic"
    default = False


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class PokeclickerOptions(PerGameCommonOptions):
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
    starting_safari_level: StartingSafariLevel
    starting_underground_level: StartingUndergroundLevel
    roaming_encounter_multiplier: RoamingEncounterMultiplier
    roaming_encounter_multiplier_route: RoamingEncounterMultiplierRoute
    pokedollar_multiplier: PokedollarMultiplier
    dungeon_token_multiplier: DungeonTokenMultiplier
    quest_point_multiplier: QuestPointMultiplier
    diamond_multiplier: DiamondMultiplier
    farm_point_multiplier: FarmPointMultiplier
    exp_multiplier: ExpMultiplier
    wanderer_appearance_multiplier: WandererAppearanceMultiplier
    wanderer_base_catch_rate: WandererBaseCatchRate
    starter_logic: StarterLogic
    early_town_map: EarlyTownMap
    mystery_egg_in_logic: MysteryEggInLogic
    clicks_per_second: ClicksPerSecond
    dungeon_logic: DungeonLogic
    safari_zone_logic: SafariZoneLogic
    wanderers_in_logic: WanderersInLogic


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Game Options",
        [Dexsanity, IncludeAltPokemon, BadgeRandomization, UseScripts, IncludeScriptsAsItems, ProgressiveAutoClicker, ProgressiveAutoSafariZone, IncludeSeasonalEvents, IncludeCodesAsItems, IncludePalaeontologistToken, StartingSafariLevel, StartingUndergroundLevel],
    ),
    OptionGroup(
        "Multiplier Options",
        [PokedollarMultiplier, DungeonTokenMultiplier, QuestPointMultiplier, DiamondMultiplier, FarmPointMultiplier, ExpMultiplier, WandererAppearanceMultiplier, WandererBaseCatchRate],
    ),
    OptionGroup(
        "Logic Options",
        [StarterLogic, EarlyTownMap, MysteryEggInLogic, ClicksPerSecond, DungeonLogic, SafariZoneLogic, WanderersInLogic],
    ),
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
