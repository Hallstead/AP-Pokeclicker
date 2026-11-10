from .rules import *
from rule_builder.rules import Has, HasGroupUnique

# Pokemon-specific rules
routes = "routes"
land = "land"
water = "water"
headbutt = "headbutt"
dungeons = "dungeons"
dungeon_boss = "dungeon boss"
dungeon_chest = "dungeon chest"
prev = "prev"
egg = "egg"
breeding = "breeding"
evolution = "evolution"
level = "level"
item = "item"
questline = "questline"
dungeon_evolution = "dungeon evolution"
environment = "environment"
weather = "weather"
dayCyclePart = "dayCyclePart"
safari = "safari zone"
farm_wandering = "farm wandering"
trades = "trades"
shops = "shops"
shadow_pokemon = "shadow pokemon"
quest_rewards = "quest rewards"
dream_orbs = "dream orbs"
special = "special"
starter = "starter"
time = "time"
discord = "discord"
temporary_battle = "temporary battle"
region = "region"
battle_cafe = "battle cafe"
roamer = "roamer"
native_region = "native_region"

dungeon = "dungeon"
rule = "rule"
requirements = "requirements"
args = "args"
attack = "attack"
attackIsPercent = "attackIsPercent"
route = "route"

POKEMON_RULES = {
    'Bulbasaur': {
        native_region: 'Kanto',
        routes: {
            land: [
                'alola_route_2',
            ],
        },
        egg: 'Grass Egg',
        starter: ['Kanto'],
        farm_wandering: ['Rindo Berry'],
    },
    'Bulbasaur (Clone)': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto') & make_rule('new_island', True),
        ],
    },
    'Spooky Bulbasaur': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_1'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_22'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_2'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_3'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_4'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_24'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_25'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_5'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_6'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_11'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_9'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_10'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_8'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_7'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_12'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_13'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_14'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_15'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_16'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_17'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_18'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_19'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_20'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_21'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_23'),
        ],
    },
    'Bulbasaur (Rose)': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('flower_paradise', True, 16000000),
        ],
    },
    'Ivysaur': {
        native_region: 'Kanto',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Bulbasaur',
                level: 16,
            },
        ],
    },
    'Ivysaur (Clone)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Bulbasaur (Clone)',
                level: 16,
            },
        ],
        special: [
            Has('Ivysaur (Clone)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Spooky Ivysaur': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Spooky Bulbasaur',
                level: 16,
            },
        ],
        special: [
            Has('Spooky Ivysaur') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Ivysaur (Rose)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Bulbasaur (Rose)',
                level: 16,
            },
        ],
        special: [
            Has('Ivysaur (Rose)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Venusaur': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Ivysaur',
                level: 32,
            },
        ],
        special: [
            Has('Venusaur') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Mega Venusaur': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Venusaur',
                item: 'Venusaurite',
            },
        ],
    },
    'Gigantamax Venusaur': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Venusaur') | make_rule('lair_of_giants3')) & make_rule('max_lair'),
        ],
    },
    'Venusaur (Clone)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Ivysaur (Clone)',
                level: 32,
            },
        ],
        special: [
            Has('Venusaur (Clone)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Spooky Venusaur': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Spooky Ivysaur',
                level: 32,
            },
        ],
        special: [
            Has('Spooky Venusaur') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Venusaur (Rose)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Ivysaur (Rose)',
                level: 32,
            },
        ],
        special: [
            Has('Venusaur (Rose)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Charmander': {
        native_region: 'Kanto',
        routes: {
            land: [
                'alola_route_3',
            ],
        },
        egg: 'Fire Egg',
        starter: ['Kanto'],
        farm_wandering: ['Occa Berry'],
    },
    'Charmander (Clone)': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto') & make_rule('new_island', True),
        ],
    },
    'Charmeleon': {
        native_region: 'Kanto',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Charmander',
                level: 16,
            },
        ],
    },
    'Charmeleon (Clone)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Charmander (Clone)',
                level: 16,
            },
        ],
        special: [
            Has('Charmeleon (Clone)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Charizard': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Charmeleon',
                level: 36,
            },
        ],
        special: [
            Has('Charizard') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Mega Charizard X': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Charizard',
                item: 'Charizardite X',
                time: 'day',
            },
        ],
    },
    'Mega Charizard Y': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Charizard',
                item: 'Charizardite Y',
                time: 'night',
            },
        ],
    },
    'Gigantamax Charizard': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Charizard') | make_rule('lair_of_giants4')) & make_rule('max_lair'),
        ],
    },
    'Charizard (Clone)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Charmeleon (Clone)',
                level: 36,
            },
        ],
        special: [
            Has('Charizard (Clone)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Squirtle': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('seaward_cave', 59226690),
        ],
        egg: 'Water Egg',
        starter: ['Kanto'],
        farm_wandering: ['Passho Berry'],
    },
    'Squirtle (Clone)': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto') & make_rule('new_island', True),
        ],
    },
    'Squad Leader Squirtle': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Squirtle',
                level: 10,
                item: 'Black Glasses',
            },
        ],
        special: [
            Has('Squad Leader Squirtle') & make_rule('kanto_route_11'),
        ],
    },
    'Wartortle': {
        native_region: 'Kanto',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Squirtle',
                level: 16,
            },
        ],
    },
    'Wartortle (Clone)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Squirtle (Clone)',
                level: 16,
            },
        ],
        special: [
            Has('Wartortle (Clone)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Blastoise': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Wartortle',
                level: 36,
            },
        ],
        special: [
            Has('Blastoise') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Mega Blastoise': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Blastoise',
                item: 'Blastoisinite',
            },
        ],
    },
    'Gigantamax Blastoise': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Blastoise') | make_rule('lair_of_giants5')) & make_rule('max_lair'),
        ],
    },
    'Blastoise (Clone)': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Wartortle (Clone)',
                level: 36,
            },
        ],
        special: [
            Has('Blastoise (Clone)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Caterpie': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_2',
                'kanto_route_24',
                'kanto_route_25',
                'johto_route_30',
                'johto_route_31',
                'kalos_route_2',
                'alola_route_1',
                'alola_route_5',
                'galar_route_1',
            ],
        },
        dungeons: [
            'viridian_forest',
            'pattern_bush',
            'ilex_forest',
            'santalune_forest',
            'melemele_meadow',
        ],
        safari: ['Johto'],
    },
    'Pinkan Caterpie': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
            ],
        },
    },
    'Metapod': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_24',
                'kanto_route_25',
                'johto_route_30',
                'johto_route_31',
                'alola_route_5',
                'rolling_fields',
            ],
            headbutt: [
                'johto_route_47',
            ],
        },
        dungeons: [
            'viridian_forest',
            'pattern_bush',
            'ilex_forest',
            'santalune_forest',
            'melemele_meadow',
            'lush_jungle',
        ],
        evolution: [
            {
                prev: 'Caterpie',
                level: 7,
            },
        ],
        safari: ['Johto'],
    },
    'Butterfree': {
        native_region: 'Kanto',
        routes: {
            land: [
                'alola_route_5',
                'rolling_fields',
                'east_lake_axewell',
                'giants_mirror',
            ],
            headbutt: [
                'johto_route_47',
            ],
        },
        dungeons: [
            'melemele_meadow',
            'slumbering_weald_shrine',
        ],
        dungeon_boss: [
            ('ilex_forest', 340000),
        ],
        evolution: [
            {
                prev: 'Metapod',
                level: 10,
            },
        ],
        safari: ['Johto'],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Gigantamax Butterfree': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Butterfree') | make_rule('lair_of_giants6')) & make_rule('max_lair'),
        ],
    },
    'Valencian Butterfree': {
        native_region: 'Kanto',
        routes: {
            land: [
                'valencia_island',
            ],
        },
    },
    'Pink Butterfree': {
        native_region: 'Kanto',
        special: [
            Has('Elite Orange Champion Badge') & make_rule('roamer', 'Kanto - Sevii Islands'),
        ],
    },
    'Ash\'s Butterfree': {
        native_region: 'Kanto',
        special: [
            Has('Elite Orange Champion Badge') & make_rule('roamer', 'Kanto - Sevii Islands'),
        ],
    },
    'Weedle': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_2',
                'kanto_route_24',
                'kanto_route_25',
                'johto_route_30',
                'johto_route_31',
                'kalos_route_2',
            ],
        },
        dungeons: [
            'viridian_forest',
            'pattern_bush',
            'ilex_forest',
            'santalune_forest',
        ],
        safari: ['Johto'],
    },
    'Pinkan Weedle': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
            ],
        },
    },
    'Kakuna': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_24',
                'kanto_route_25',
                'johto_route_30',
                'johto_route_31',
            ],
            headbutt: [
                'johto_route_47',
            ],
        },
        dungeons: [
            'viridian_forest',
            'pattern_bush',
            'ilex_forest',
            'santalune_forest',
        ],
        evolution: [
            {
                prev: 'Weedle',
                level: 7,
            },
        ],
        safari: ['Johto'],
    },
    'Beedrill': {
        native_region: 'Kanto',
        routes: {
            land: [
                'alola_route_4',
            ],
            headbutt: [
                'johto_route_47',
            ],
        },
        dungeon_boss: [
            ('ilex_forest', 340000),
        ],
        evolution: [
            {
                prev: 'Kakuna',
                level: 10,
            },
        ],
        safari: ['Johto'],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Mega Beedrill': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Beedrill',
                item: 'Beedrillite',
            },
        ],
    },
    'Pidgey': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_1',
                'kanto_route_2',
                'kanto_route_3',
                'kanto_route_24',
                'kanto_route_25',
                'kanto_route_5',
                'kanto_route_6',
                'kanto_route_8',
                'kanto_route_7',
                'kanto_route_12',
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'bond_bridge',
                'five_isle_meadow',
                'johto_route_29',
                'johto_route_30',
                'johto_route_31',
                'johto_route_35',
                'johto_route_36',
                'johto_route_37',
                'sinnoh_route_229',
                'kalos_route_2',
                'kalos_route_3',
            ],
        },
        dungeons: [
            'berry_forest',
        ],
    },
    'Pinkan Pidgey': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
                'pinkan_plains',
            ],
        },
    },
    'Pidgeotto': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'bond_bridge',
                'five_isle_meadow',
                'johto_route_37',
                'johto_route_43',
            ],
        },
        dungeons: [
            'berry_forest',
        ],
        evolution: [
            {
                prev: 'Pidgey',
                level: 18,
            },
        ],
        safari: ['Alola'],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Pinkan Pidgeotto': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Pinkan Pidgey',
                level: 18,
                questline: 'Team Rocket\'s Pinkan Theme Park',
            },
        ],
        special: [
            Has('Pinkan Pidgeotto') & make_rule('pinkan_plains'),
        ],
    },
    'Pidgeot': {
        native_region: 'Kanto',
        routes: {
            land: [
                'alola_route_10',
            ],
        },
        evolution: [
            {
                prev: 'Pidgeotto',
                level: 36,
            },
        ],
    },
    'Mega Pidgeot': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Pidgeot',
                item: 'Pidgeotite',
            },
        ],
    },
    'Rattata': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_1',
                'kanto_route_22',
                'kanto_route_2',
                'kanto_route_4',
                'kanto_route_9',
                'kanto_route_16',
                'kanto_route_17',
                'kanto_route_18',
                'johto_route_29',
                'johto_route_30',
                'johto_route_31',
                'johto_route_32',
                'johto_route_33',
                'johto_route_34',
                'johto_route_38',
                'johto_route_39',
                'johto_route_46',
                'sinnoh_route_225',
                'sinnoh_route_226',
            ],
        },
        dungeons: [
            'pokemon_mansion',
            'sprout_tower',
            'union_cave',
            'burned_tower',
            'tin_tower',
            'mt_mortar',
            'tohjo_falls',
            'castelia_sewers',
            'relic_passage',
        ],
    },
    'Alolan Rattata': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_1',
                'alola_route_2',
                'kalae_bay',
                'alola_route_4',
                'alola_route_6',
                'alola_route_8',
            ],
        },
        dungeons: [
            'verdant_cavern',
        ],
    },
    'Pinkan Rattata': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_plains',
            ],
        },
        dungeons: [
            'pinkan_mountain',
        ],
    },
    'Raticate': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_16',
                'kanto_route_17',
                'kanto_route_18',
                'johto_route_38',
                'johto_route_39',
                'johto_route_47',
                'johto_route_26',
                'johto_route_27',
                'sinnoh_route_225',
                'sinnoh_route_226',
            ],
        },
        dungeons: [
            'pokemon_mansion',
            'burned_tower',
            'mt_mortar',
            'tohjo_falls',
            'relic_passage',
            'dreamyard',
        ],
        dungeon_boss: [
            ('tin_tower', 380000),
        ],
        evolution: [
            {
                prev: 'Rattata',
                level: 20,
            },
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Alolan Raticate': {
        native_region: 'Alola',
        routes: {
            land: [
                'akala_outskirts',
                'alola_route_10',
                'alola_route_15',
                'alola_route_16',
                'alola_route_17',
                'poni_plains',
            ],
        },
        dungeons: [
            'mount_lanakila',
        ],
        dungeon_boss: [
            ('verdant_cavern', 57978365),
        ],
        evolution: [
            {
                prev: 'Alolan Rattata',
                level: 20,
                time: 'night',
            },
        ],
    },
    'Totem Raticate': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_welcome_to_paradise_cousin') & make_rule('verdant_cavern', True, 82543791),
        ],
    },
    'Valencian Raticate': {
        native_region: 'Kanto',
        routes: {
            land: [
                'valencia_island',
            ],
        },
    },
    'Spearow': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_22',
                'kanto_route_3',
                'kanto_route_4',
                'kanto_route_11',
                'kanto_route_9',
                'kanto_route_10',
                'kanto_route_16',
                'kanto_route_17',
                'kanto_route_18',
                'kanto_route_23',
                'treasure_beach',
                'kindle_road',
                'cape_brink',
                'water_path',
                'ruin_valley',
                'canyon_entrance',
                'johto_route_33',
                'johto_route_42',
                'johto_route_46',
                'johto_route_47',
                'sinnoh_route_225',
                'alola_route_2',
                'alola_route_3',
            ],
            headbutt: [
                'johto_route_31',
                'johto_route_44',
                'johto_route_45',
            ],
        },
        dungeons: [
            'mt_ember_summit',
            'hall_of_origin',
        ],
        shadow_pokemon: [
            'phenac_stadium',
        ],
    },
    'Red Spearow': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto'),
        ],
    },
    'Fearow': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_17',
                'kanto_route_18',
                'kanto_route_23',
                'treasure_beach',
                'kindle_road',
                'cape_brink',
                'water_path',
                'ruin_valley',
                'canyon_entrance',
                'sevault_canyon',
                'johto_route_47',
                'johto_route_48',
                'sinnoh_route_225',
                'sinnoh_route_226',
                'sinnoh_route_227',
                'alola_route_10',
                'mount_hokulani',
                'alola_route_17',
                'poni_plains',
            ],
        },
        dungeons: [
            'mt_ember_summit',
            'stark_mountain',
            'pledge_grove',
        ],
        evolution: [
            {
                prev: 'Spearow',
                level: 20,
            },
        ],
    },
    'Ekans': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_4',
                'kanto_route_11',
                'kanto_route_9',
                'kanto_route_10',
                'kanto_route_8',
                'kanto_route_23',
                'johto_route_32',
                'johto_route_33',
                'alola_route_2',
            ],
        },
    },
    'Arbok': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_23',
                'johto_route_26',
                'johto_route_27',
            ],
        },
        dungeons: [
            'victory_road',
        ],
        evolution: [
            {
                prev: 'Ekans',
                level: 22,
            },
        ],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Pinkan Arbok': {
        native_region: 'Kanto',
        trades: [
            ('pinkan_pokemon_reserve', ['Pinkan Berry']),
        ],
    },
    'Pikachu': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kalos_route_3',
                'rolling_fields',
                'galar_route_4',
                'stony_wilderness',
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'natures_pantry',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'power_plant',
            'pikachu_valley',
        ],
        dungeon_boss: [
            ('viridian_forest', 510),
            ('santalune_forest', 51738600),
        ],
        evolution: [
            {
                prev: 'Pichu',
                item: 'Soothe Bell',
            },
        ],
        egg: 'Electric Egg',
        starter: ['Kanto'],
        farm_wandering: ['Wacan Berry'],
    },
    'Pikachu (Original Cap)': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pikachu_valley', 59764020),
        ],
    },
    'Pikachu (Hoenn Cap)': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pikachu_valley', 59764020),
        ],
    },
    'Pikachu (Sinnoh Cap)': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pikachu_valley', 59764020),
        ],
    },
    'Pikachu (Unova Cap)': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pikachu_valley', 59764020),
        ],
    },
    'Pikachu (Kalos Cap)': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pikachu_valley', 59764020),
        ],
    },
    'Pikachu (Alola Cap)': {
        native_region: 'Kanto',
        special: [
            Has('Champion Stamp Badge') & make_rule('pikachu_valley', True, 59764020),
        ],
    },
    'Pikachu (World Cap)': {
        native_region: 'Kanto',
        special: [
            Has('Elite Galar Champion Badge') & make_rule('pikachu_valley', True, 59764020),
        ],
    },
    'Pikachu (Partner Cap)': {
        native_region: 'Kanto',
        special: [
            make_rule('pikachu_valley', False) & make_rule('ash_ketchum_alola'),
        ],
    },
    'Gigantamax Pikachu': {
        native_region: 'Kanto',
        special: [
            make_rule('max_lair'),
        ],
    },
    'Flying Pikachu': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto'),
        ],
    },
    'Surfing Pikachu': {
        native_region: 'Kanto',
        discord: ['Kanto'],
        special: [
            Has('Surfing Pikachu') & make_rule('kanto_route_19'),
        ],
    },
    'Pikachu (Gengar)': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_101'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_102'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_103'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_104'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_105'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_106'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_107'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_108'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_109'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_110'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_111'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_112'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_113'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_114'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_115'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_116'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_117'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_118'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_119'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_120'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_121'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_122'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_123'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_124'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_125'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_126'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_127'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_128'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_129'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_130'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_131'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_132'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_133'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_134'),
        ],
    },
    'Let\'s Go Pikachu': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto'),
        ],
    },
    'Pinkan Pikachu': {
        native_region: 'Kanto',
        special: [
            make_rule('pinkan_mountain', False) & make_rule('ash_ketchum_pinkan'),
        ],
    },
    'Detective Pikachu': {
        native_region: 'Kanto',
        farm_wandering: ['Enigma Berry'],
    },
    'Pikachu (Clone)': {
        native_region: 'Kanto',
        temporary_battle: [
            'ash_ketchum_new_island',
        ],
        special: [
            Has('Pikachu (Clone)') & make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto'),
        ],
    },
    'Pikachu (Easter)': {
        native_region: 'Kanto',
        special: [
            {
                dungeon: 'viridian_forest',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('viridian_forest', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Pikachu (Easter)',
                            '0',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'digletts_cave',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('digletts_cave', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Pikachu (Easter)',
                            '1',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'pokemon_tower',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('pokemon_tower', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Pikachu (Easter)',
                            '2',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'power_plant',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('power_plant', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Pikachu (Easter)',
                            '3',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'seafoam_islands',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('seafoam_islands', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Pikachu (Easter)',
                            '4',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'victory_road',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('victory_road', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Pikachu (Easter)',
                            '5',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
        ],
    },
    'Pikachu (Palaeontologist)': {
        native_region: 'Kanto',
        trades: [
            ('cinnabar_island', ['Palaeontologist Token']),
        ],
    },
    'Raichu': {
        native_region: 'Kanto',
        routes: {
            land: [
                'soothing_wetlands',
                'forest_of_focus',
            ],
        },
        dungeons: [
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Pikachu',
                item: 'Thunder Stone',
                region: 'allButAlola',
            },
        ],
    },
    'Alolan Raichu': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Pikachu',
                item: 'Thunder Stone',
                region: 'alolaOnly',
            },
        ],
    },
    'Detective Raichu': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Detective Pikachu',
                item: 'Thunder Stone',
                questline: 'Detective Pikachu',
            },
        ],
        quest_rewards: [
            'completed_detective_pikachu',
        ],
    },
    'Sandshrew': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_4',
                'kanto_route_11',
                'kanto_route_9',
                'kanto_route_10',
                'kanto_route_8',
                'kanto_route_23',
                'hoenn_route_111',
                'rock_poke_spot',
                'desert_resort',
            ],
        },
        dungeons: [
            'union_cave',
            'relic_castle',
            'warm_up_tunnel',
        ],
        farm_wandering: ['Shuca Berry'],
    },
    'Alolan Sandshrew': {
        native_region: 'Alola',
        dungeons: [
            'mount_lanakila',
        ],
    },
    'Sandslash': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_23',
                'johto_route_26',
                'johto_route_27',
                'unova_route_15',
                'kalos_route_18',
                'forest_of_focus',
                'potbottom_desert',
            ],
        },
        dungeons: [
            'victory_road',
            'relic_castle',
            'terminus_cave',
        ],
        dungeon_boss: [
            ('victory_road_johto', 500000),
        ],
        evolution: [
            {
                prev: 'Sandshrew',
                level: 22,
            },
        ],
    },
    'Alolan Sandslash': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Alolan Sandshrew',
                item: 'Ice Stone',
            },
        ],
    },
    'Nidoran(F)': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_3',
                'valencia_island',
                'johto_route_35',
                'johto_route_36',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
            ],
        },
        safari: ['Kanto'],
    },
    'Pinkan Nidoran(F)': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_plains',
            ],
        },
        dungeons: [
            'pinkan_mountain',
        ],
    },
    'Nidorina': {
        native_region: 'Kanto',
        routes: {
            land: [
                'valencia_island',
                'kalos_route_11',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Nidoran(F)',
                level: 16,
            },
        ],
        safari: ['Kanto'],
    },
    'Nidoqueen': {
        native_region: 'Kanto',
        routes: {
            land: [
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Nidorina',
                item: 'Moon Stone',
            },
        ],
    },
    'Nidoran(M)': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_3',
                'valencia_island',
                'johto_route_35',
                'johto_route_36',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
            ],
        },
        safari: ['Kanto'],
    },
    'Pinkan Nidoran(M)': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_plains',
            ],
        },
        dungeons: [
            'pinkan_mountain',
        ],
    },
    'Nidorino': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kalos_route_11',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Nidoran(M)',
                level: 16,
            },
        ],
        safari: ['Kanto'],
    },
    'Nidoking': {
        native_region: 'Kanto',
        routes: {
            land: [
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Nidorino',
                item: 'Moon Stone',
            },
        ],
    },
    'Pinkan Nidoking': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pinkan_mountain', 7000000),
        ],
    },
    'Clefairy': {
        native_region: 'Kanto',
        routes: {
            land: [
                'motostoke_riverbank',
                'giants_cap',
                'giants_bed',
                'snowslide_slope',
                'fabled_spring',
            ],
        },
        dungeons: [
            'mt_moon',
            'mt_coronet_south',
            'mt_coronet_north',
            'spear_pillar',
            'giant_chasm',
            'lake_of_the_sunne_and_moone',
            'tunnel_to_the_top',
        ],
        evolution: [
            {
                prev: 'Cleffa',
                item: 'Soothe Bell',
            },
        ],
        farm_wandering: ['Roseli Berry'],
    },
    'Clefable': {
        native_region: 'Kanto',
        routes: {
            land: [
                'motostoke_riverbank',
                'giants_bed',
                'snowslide_slope',
                'fabled_spring',
            ],
        },
        dungeons: [
            'dyna_tree_hill',
            'tunnel_to_the_top',
        ],
        dungeon_boss: [
            ('fullmoon_island', 11000000),
        ],
        evolution: [
            {
                prev: 'Clefairy',
                item: 'Moon Stone',
            },
        ],
    },
    'Vulpix': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_8',
                'kanto_route_7',
                'johto_route_36',
                'johto_route_37',
                'johto_route_48',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'axews_eye',
                'watchtower_ruins',
                'galar_route_3',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'pokemon_mansion',
            'mt_pyre',
            'liberty_garden',
            'abundant_shrine',
            'veilstone_cape',
        ],
        egg: 'Fire Egg',
        shadow_pokemon: [
            'pyrite_building',
        ],
    },
    'Alolan Vulpix': {
        native_region: 'Alola',
        dungeons: [
            'mount_lanakila',
        ],
    },
    'Ninetales': {
        native_region: 'Kanto',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        dungeon_boss: [
            ('firespit_island', 10000000),
        ],
        evolution: [
            {
                prev: 'Vulpix',
                item: 'Fire Stone',
            },
        ],
    },
    'Alolan Ninetales': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Alolan Vulpix',
                item: 'Ice Stone',
            },
        ],
    },
    'Jigglypuff': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_3',
                'hoenn_route_115',
                'unova_route_2',
                'unova_route_1',
                'kalos_route_20',
                'fields_of_honor',
                'challenge_beach',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'dreamyard',
            'pokemon_village',
        ],
        evolution: [
            {
                prev: 'Igglybuff',
                item: 'Soothe Bell',
            },
        ],
        egg: 'Mystery Egg',
    },
    'Wigglytuff': {
        native_region: 'Kanto',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
            ],
        },
        evolution: [
            {
                prev: 'Jigglypuff',
                item: 'Moon Stone',
            },
        ],
    },
    'Zubat': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_30',
                'johto_route_31',
                'johto_route_32',
                'johto_route_33',
                'johto_route_42',
                'cave_poke_spot',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_206',
                'sinnoh_route_207',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_214',
                'sinnoh_route_211',
                'sinnoh_route_216',
                'deertrack_path',
                'deertrack_heights',
                'windswept_run',
                'natures_pantry',
                'worn_bridge',
                'tidewater_dam',
                'cloudpool_ridge',
                'diamond_heath',
                'bolderoll_slope',
                'heavenward_lookout',
                'wayward_wood',
            ],
        },
        dungeons: [
            'mt_moon',
            'rock_tunnel',
            'seafoam_islands',
            'victory_road',
            'icefall_cave',
            'lost_cave',
            'altering_cave',
            'union_cave',
            'slowpoke_well',
            'ilex_forest',
            'burned_tower',
            'whirl_islands',
            'mt_mortar',
            'ice_path',
            'dark_cave',
            'tohjo_falls',
            'granite_cave',
            'meteor_falls',
            'shoal_cave',
            'cave_of_origin',
            'seafloor_cavern',
            'sealed_chamber',
            'victory_road_hoenn',
            'oreburgh_gate',
            'wayward_cave',
            'mt_coronet_south',
            'solaceon_ruins',
            'iron_island',
            'mt_coronet_north',
            'castelia_sewers',
            'connecting_cave',
            'hauoli_cemetery',
            'verdant_cavern',
            'seaward_cave',
            'ten_carat_hill',
            'digletts_tunnel',
            'memorial_hill',
            'resolution_cave',
            'roaring_sea_caves',
            'lakeside_cave',
            'tunnel_to_the_top',
            'oreburrow_tunnel',
            'heartwood',
            'ancient_wayward_cave',
            'ancient_snowpoint_temple',
        ],
    },
    'Golbat': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_227',
                'deertrack_heights',
                'tidewater_dam',
                'cloudpool_ridge',
                'diamond_heath',
                'bolderoll_slope',
                'heavenward_lookout',
                'wayward_wood',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'victory_road',
            'cerulean_cave',
            'icefall_cave',
            'lost_cave',
            'whirl_islands',
            'mt_mortar',
            'dark_cave',
            'victory_road_johto',
            'meteor_falls',
            'shoal_cave',
            'cave_of_origin',
            'seafloor_cavern',
            'sky_pillar',
            'victory_road_hoenn',
            'oreburgh_gate',
            'iron_island',
            'spear_pillar',
            'distortion_world',
            'victory_road_sinnoh',
            'sendoff_spring',
            'snowpoint_temple',
            'stark_mountain',
            'celestial_tower',
            'cave_of_being',
            'dreamyard',
            'thrifty_megamart',
            'vast_poni_canyon',
            'roaring_sea_caves',
            'tunnel_to_the_top',
            'heartwood',
            'ancient_wayward_cave',
            'ancient_snowpoint_temple',
        ],
        dungeon_boss: [
            ('burned_tower', 360000),
            ('tohjo_falls', 480000),
            ('sealed_chamber', 4500000),
            ('mount_lanakila', 81064250),
            ('resolution_cave', 85572310),
        ],
        evolution: [
            {
                prev: 'Zubat',
                level: 22,
            },
        ],
    },
    'Oddish': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_24',
                'kanto_route_25',
                'kanto_route_5',
                'kanto_route_6',
                'kanto_route_7',
                'kanto_route_12',
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'cape_brink',
                'bond_bridge',
                'water_path',
                'hoenn_route_110',
                'hoenn_route_117',
                'hoenn_route_119',
                'hoenn_route_120',
                'hoenn_route_121',
                'hoenn_route_123',
                'sinnoh_route_224',
                'sinnoh_route_230',
                'kalos_route_6',
                'rolling_fields',
                'dappled_grove',
                'east_lake_axewell',
                'watchtower_ruins',
            ],
        },
        dungeons: [
            'berry_forest',
            'ilex_forest',
        ],
        egg: 'Grass Egg',
    },
    'Pinkan Oddish': {
        native_region: 'Kanto',
        trades: [
            ('pinkan_pokemon_reserve', ['Pinkan Berry']),
        ],
    },
    'Gloom': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_12',
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'cape_brink',
                'bond_bridge',
                'water_path',
                'johto_route_47',
                'johto_route_48',
                'hoenn_route_121',
                'hoenn_route_123',
                'sinnoh_route_224',
                'sinnoh_route_230',
                'axews_eye',
                'giants_mirror',
                'giants_cap',
            ],
        },
        dungeons: [
            'berry_forest',
            'flower_paradise',
        ],
        evolution: [
            {
                prev: 'Oddish',
                level: 21,
            },
        ],
    },
    'Vileplume': {
        native_region: 'Kanto',
        routes: {
            land: [
                'dappled_grove',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
        evolution: [
            {
                prev: 'Gloom',
                item: 'Leaf Stone',
            },
        ],
    },
    'Valencian Vileplume': {
        native_region: 'Kanto',
        routes: {
            land: [
                'valencia_island',
            ],
        },
    },
    'Pinkan Vileplume': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
            ],
        },
    },
    'Paras': {
        native_region: 'Kanto',
        routes: {
            land: [
                'natures_pantry',
                'golden_lowlands',
                'cloudpool_ridge',
                'diamond_heath',
                'droning_meadow',
                'heavenward_lookout',
                'wayward_wood',
            ],
        },
        dungeons: [
            'mt_moon',
            'ilex_forest',
            'brooklet_hill',
            'lush_jungle',
            'ancient_solaceon_ruins',
        ],
        egg: 'Grass Egg',
        safari: ['Kanto', 'Johto', 'Sinnoh'],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Valencian Paras': {
        native_region: 'Kanto',
        routes: {
            land: [
                'valencia_island',
            ],
        },
    },
    'Pinkan Paras': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
            ],
        },
    },
    'Parasect': {
        native_region: 'Kanto',
        routes: {
            land: [
                'alola_route_11',
                'natures_pantry',
                'golden_lowlands',
                'cloudpool_ridge',
                'diamond_heath',
                'droning_meadow',
                'windbreak_stand',
                'heavenward_lookout',
                'wayward_wood',
            ],
        },
        dungeons: [
            'cerulean_cave',
        ],
        dungeon_boss: [
            ('flower_paradise', 9900000),
        ],
        evolution: [
            {
                prev: 'Paras',
                level: 24,
            },
        ],
        safari: ['Kanto'],
    },
    'Venonat': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_12',
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'bond_bridge',
                'johto_route_43',
            ],
        },
        dungeons: [
            'berry_forest',
        ],
        safari: ['Johto'],
    },
    'Pinkan Venonat': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
            ],
        },
    },
    'Venomoth': {
        native_region: 'Kanto',
        dungeons: [
            'area_zero',
        ],
        dungeon_boss: [
            ('berry_forest', 101427),
        ],
        evolution: [
            {
                prev: 'Venonat',
                level: 31,
            },
        ],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Diglett': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_48',
                'sinnoh_route_228',
                'rolling_fields',
                'galar_route_4',
                'giants_mirror',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'digletts_cave',
            'galar_mine',
            'inlet_grotto',
        ],
    },
    'Alolan Diglett': {
        native_region: 'Alola',
        dungeons: [
            'verdant_cavern',
            'digletts_tunnel',
        ],
    },
    'Pinkan Diglett': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_plains',
            ],
        },
    },
    'Dugtrio': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_228',
                'kalos_route_13',
                'giants_mirror',
                'giants_cap',
                'lake_of_outrage',
                'hammerlocke_hills',
                'galar_route_6',
            ],
        },
        dungeons: [
            'area_zero_depths',
        ],
        dungeon_boss: [
            ('digletts_cave', 16040),
        ],
        evolution: [
            {
                prev: 'Diglett',
                level: 26,
            },
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Alolan Dugtrio': {
        native_region: 'Alola',
        routes: {
            land: [
                'haina_desert',
                'poni_coast',
            ],
        },
        dungeons: [
            'vast_poni_canyon',
            'resolution_cave',
        ],
        evolution: [
            {
                prev: 'Alolan Diglett',
                level: 26,
            },
        ],
    },
    'Meowth': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_5',
                'kanto_route_6',
                'kanto_route_8',
                'kanto_route_7',
                'treasure_beach',
                'kindle_road',
                'cape_brink',
                'bond_bridge',
                'five_isle_meadow',
                'water_path',
                'ruin_valley',
                'canyon_entrance',
                'sevault_canyon',
                'johto_route_38',
                'johto_route_39',
            ],
        },
        shadow_pokemon: [
            'phenac_city_battles',
        ],
    },
    'Gigantamax Meowth': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Meowth') | make_rule('lair_of_giants2')) & make_rule('max_lair'),
        ],
    },
    'Alolan Meowth': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_2',
            ],
        },
        dungeons: [
            'trainers_school',
            'malie_garden',
        ],
    },
    'Galarian Meowth': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_4',
            ],
        },
    },
    'Meowth (Phanpy)': {
        native_region: 'Kanto',
        special: [
            # below level omited. Fix client code!
            Has('Phanpy') & make_rule('johto_route_42'),
        ],
    },
    'Persian': {
        native_region: 'Kanto',
        routes: {
            land: [
                'treasure_beach',
                'kindle_road',
                'cape_brink',
                'bond_bridge',
                'five_isle_meadow',
                'water_path',
                'ruin_valley',
                'canyon_entrance',
                'sevault_canyon',
            ],
        },
        evolution: [
            {
                prev: 'Meowth',
                level: 28,
            },
        ],
    },
    'Alolan Persian': {
        native_region: 'Alola',
        dungeon_boss: [
            ('malie_garden', 76702881),
        ],
        evolution: [
            {
                prev: 'Alolan Meowth',
                item: 'Soothe Bell',
            },
        ],
    },
    'Psyduck': {
        native_region: 'Kanto',
        routes: {
            land: [
                'treasure_beach',
                'kindle_road',
                'cape_brink',
                'bond_bridge',
                'five_isle_meadow',
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'water_path',
                'green_path',
                'outcast_island',
                'ruin_valley',
                'canyon_entrance',
                'sinnoh_route_210',
                'kalos_route_22',
                'challenge_beach',
                'golden_lowlands',
                'gapejaw_bog',
                'holm_of_trials',
                'bathers_lagoon',
            ],
            water: [
                'kanto_route_22',
                'kanto_route_25',
                'kanto_route_6',
                'kanto_route_23',
                'johto_route_35',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_205',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_214',
                'sinnoh_route_212',
                'sinnoh_route_225',
                'wayward_wood',
                'lonely_spring',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'berry_forest',
            'cerulean_cave',
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
            'oreburgh_gate',
            'lake_valor',
            'lake_verity',
            'lake_acuity',
            'floccesy_ranch',
            'seaward_cave',
            'ten_carat_hill',
            'brooklet_hill',
            'malie_garden',
            'brawlers_cave',
            'heartwood',
        ],
        safari: ['Kanto'],
    },
    'Golduck': {
        native_region: 'Kanto',
        routes: {
            land: [
                'cape_brink',
                'unova_route_14',
                'unova_route_11',
                'unova_route_22',
                'unova_route_23',
                'poni_gauntlet',
                'forest_of_focus',
                'challenge_beach',
                'holm_of_trials',
                'bathers_lagoon',
            ],
            water: [
                'johto_route_35',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_205',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_210',
                'sinnoh_route_214',
                'sinnoh_route_212',
                'sinnoh_route_225',
                'wayward_wood',
                'lonely_spring',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'berry_forest',
            'cerulean_cave',
            'oreburgh_gate',
            'lake_valor',
            'lake_verity',
            'lake_acuity',
            'sendoff_spring',
            'seaside_cave',
            'abundant_shrine',
            'brawlers_cave',
        ],
        evolution: [
            {
                prev: 'Psyduck',
                level: 33,
            },
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Mankey': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_22',
                'kanto_route_3',
                'kanto_route_4',
                'kanto_route_23',
                'johto_route_42',
                'alola_route_3',
            ],
        },
        dungeons: [
            'rock_tunnel',
        ],
        egg: 'Fighting Egg',
        farm_wandering: ['Chople Berry'],
    },
    'Pinkan Mankey': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
            ],
        },
        dungeons: [
            'pinkan_mountain',
        ],
    },
    'Primeape': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_23',
            ],
        },
        dungeons: [
            'victory_road',
            'cerulean_cave',
        ],
        evolution: [
            {
                prev: 'Mankey',
                level: 28,
            },
        ],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Pinkan Primeape': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pinkan_mountain', 7000000),
        ],
        evolution: [
            {
                prev: 'Pinkan Mankey',
                level: 28,
            },
        ],
    },
    'Growlithe': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_8',
                'kanto_route_7',
                'johto_route_36',
                'johto_route_37',
                'johto_route_48',
                'alola_route_2',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'axews_eye',
                'watchtower_ruins',
                'galar_route_3',
                'hammerlocke_hills',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'pokemon_mansion',
        ],
        egg: 'Fire Egg',
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Hisuian Growlithe': {
        native_region: 'Hisui',
        routes: {
            land: [
                'windbreak_stand',
            ],
        },
        dungeon_boss: [
            ('veilstone_cape', 10000000),
        ],
    },
    'Arcanine': {
        native_region: 'Kanto',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        evolution: [
            {
                prev: 'Growlithe',
                item: 'Fire Stone',
            },
        ],
    },
    'Hisuian Arcanine': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Hisuian Growlithe',
                item: 'Fire Stone',
            },
        ],
    },
    'Poliwag': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_31',
            ],
            water: [
                'kanto_route_22',
                'kanto_route_25',
                'kanto_route_6',
                'kanto_route_12',
                'kanto_route_23',
                'cape_brink',
                'ruin_valley',
                'johto_route_30',
                'johto_route_35',
                'johto_route_43',
                'johto_route_44',
                'johto_route_45',
                'johto_route_28',
                'sinnoh_route_227',
                'sinnoh_route_228',
                'kalos_route_14',
                'kalos_route_15',
                'kalos_route_16',
                'kalos_route_19',
                'kalos_route_21',
            ],
        },
        dungeons: [
            'berry_forest',
            'cerulean_cave',
            'icefall_cave',
            'ruins_of_alph',
            'giant_chasm',
            'victory_road_unova',
            'victory_road_kalos',
            'brooklet_hill',
            'brawlers_cave',
        ],
        safari: ['Kanto'],
    },
    'Poliwhirl': {
        native_region: 'Kanto',
        routes: {
            land: [
                'soothing_wetlands',
            ],
            water: [
                'ruin_valley',
                'valencia_island',
                'johto_route_30',
                'johto_route_31',
                'johto_route_44',
                'johto_route_28',
                'sinnoh_route_227',
                'sinnoh_route_228',
                'kalos_route_14',
                'kalos_route_15',
                'kalos_route_16',
                'kalos_route_19',
                'kalos_route_21',
            ],
        },
        dungeons: [
            'icefall_cave',
            'ruins_of_alph',
            'frost_cavern',
            'pokemon_village',
            'victory_road_kalos',
            'malie_garden',
            'ruins_of_hope',
        ],
        evolution: [
            {
                prev: 'Poliwag',
                level: 25,
            },
        ],
    },
    'Pinkan Poliwhirl': {
        native_region: 'Kanto',
        trades: [
            ('pinkan_pokemon_reserve', ['Pinkan Berry']),
        ],
    },
    'Poliwrath': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('brawlers_cave', 135047520),
        ],
        evolution: [
            {
                prev: 'Poliwhirl',
                item: 'Water Stone',
            },
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Abra': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_24',
                'kanto_route_25',
                'johto_route_34',
                'johto_route_35',
                'hoenn_route_116',
                'sinnoh_route_203',
                'sinnoh_route_215',
                'kalos_route_5',
                'alola_route_2',
                'fields_of_honor',
                'sandgem_flats',
                'windswept_run',
            ],
        },
        dungeons: [
            'granite_cave',
            'liberty_garden',
            'trainers_school',
            'ancient_lake_acuity',
        ],
    },
    'Kadabra': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_215',
                'fields_of_honor',
                'soothing_wetlands',
                'sandgem_flats',
            ],
        },
        dungeons: [
            'cave_of_being',
            'ancient_lake_acuity',
        ],
        dungeon_boss: [
            ('cerulean_cave', 183675),
            ('liberty_garden', 14000000),
        ],
        evolution: [
            {
                prev: 'Abra',
                level: 16,
            },
        ],
    },
    'Alakazam': {
        native_region: 'Kanto',
        routes: {
            land: [
                'loop_lagoon',
                'insular_sea',
                'sandgem_flats',
            ],
        },
        evolution: [
            {
                prev: 'Kadabra',
                item: 'Linking Cord',
            },
        ],
    },
    'Mega Alakazam': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Alakazam',
                item: 'Alakazite',
            },
        ],
    },
    'Machop': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_206',
                'sinnoh_route_207',
                'sinnoh_route_210',
                'sinnoh_route_211',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'watchtower_ruins',
                'galar_route_3',
                'giants_mirror',
                'castaway_shore',
                'bolderoll_ravine',
                'arenas_approach',
                'icebound_falls',
                'snowfall_hot_spring',
            ],
        },
        dungeons: [
            'rock_tunnel',
            'mt_ember_summit',
            'victory_road',
            'ruby_path',
            'fiery_path',
            'jagged_pass',
            'mt_coronet_south',
            'mt_coronet_north',
            'glittering_cave',
            'ten_carat_hill',
            'oreburrow_tunnel',
        ],
        egg: 'Fighting Egg',
    },
    'Machoke': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_210',
                'sinnoh_route_211',
                'sinnoh_route_225',
                'sinnoh_route_226',
                'giants_seat',
                'south_lake_miloch',
                'axews_eye',
                'stony_wilderness',
                'hammerlocke_hills',
                'ginkgo_landing',
                'castaway_shore',
                'bolderoll_ravine',
                'arenas_approach',
                'icebound_falls',
                'snowfall_hot_spring',
            ],
        },
        dungeons: [
            'mt_ember_summit',
            'cerulean_cave',
            'ruby_path',
            'spear_pillar',
            'stark_mountain',
            'vast_poni_canyon',
        ],
        dungeon_boss: [
            ('victory_road', 122975),
        ],
        evolution: [
            {
                prev: 'Machop',
                level: 28,
            },
        ],
    },
    'Machamp': {
        native_region: 'Kanto',
        routes: {
            land: [
                'giants_mirror',
                'arenas_approach',
            ],
        },
        evolution: [
            {
                prev: 'Machoke',
                item: 'Linking Cord',
            },
        ],
    },
    'Gigantamax Machamp': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Machamp') | make_rule('lair_of_giants7')) & make_rule('max_lair'),
        ],
    },
    'Bellsprout': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_24',
                'kanto_route_25',
                'kanto_route_5',
                'kanto_route_6',
                'kanto_route_7',
                'kanto_route_12',
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'cape_brink',
                'bond_bridge',
                'water_path',
                'johto_route_31',
                'johto_route_32',
                'johto_route_44',
                'sinnoh_route_224',
                'sinnoh_route_230',
                'alola_route_5',
            ],
        },
        dungeons: [
            'berry_forest',
            'flower_paradise',
        ],
    },
    'Pinkan Bellsprout': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_plains',
            ],
        },
    },
    'Weepinbell': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_12',
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'cape_brink',
                'bond_bridge',
                'water_path',
                'johto_route_44',
                'sinnoh_route_224',
                'sinnoh_route_230',
                'kalos_route_14',
                'kalos_route_16',
                'kalos_route_19',
            ],
        },
        dungeons: [
            'berry_forest',
        ],
        evolution: [
            {
                prev: 'Bellsprout',
                level: 21,
            },
        ],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Valencian Weepinbell': {
        native_region: 'Kanto',
        routes: {
            land: [
                'valencia_island',
            ],
        },
    },
    'Victreebel': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Weepinbell',
                item: 'Leaf Stone',
            },
        ],
    },
    'Tentacool': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_19',
                'kanto_route_20',
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'johto_route_40',
                'johto_route_41',
                'hoenn_route_105',
                'hoenn_route_106',
                'hoenn_route_107',
                'hoenn_route_108',
                'hoenn_route_109',
                'hoenn_route_122',
                'hoenn_route_124',
                'hoenn_route_125',
                'hoenn_route_126',
                'hoenn_route_127',
                'hoenn_route_128',
                'hoenn_route_129',
                'hoenn_route_131',
                'hoenn_route_132',
                'hoenn_route_133',
                'hoenn_route_134',
                'sinnoh_route_219',
                'sinnoh_route_220',
                'melemele_sea',
                'lunkers_lair',
            ],
            water: [
                'kanto_route_4',
                'kanto_route_24',
                'kanto_route_25',
                'kanto_route_11',
                'kanto_route_10',
                'kanto_route_13',
                'kanto_route_21',
                'treasure_beach',
                'kindle_road',
                'bond_bridge',
                'five_isle_meadow',
                'water_path',
                'johto_route_32',
                'johto_route_34',
                'johto_route_47',
                'johto_route_26',
                'johto_route_27',
                'hoenn_route_103',
                'hoenn_route_110',
                'hoenn_route_115',
                'hoenn_route_118',
                'hoenn_route_119',
                'hoenn_route_121',
                'hoenn_route_123',
                'hoenn_route_130',
                'sinnoh_route_205',
                'sinnoh_route_213',
                'sinnoh_route_218',
                'sinnoh_route_221',
                'sinnoh_route_222',
                'kalos_route_8',
                'kalos_route_12',
                'azure_bay',
                'route_1_hauoli_outskirts',
                'kalae_bay',
                'alola_route_7',
                'alola_route_8',
                'fields_of_honor',
                'challenge_beach',
                'loop_lagoon',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
                'seagrass_haven',
            ],
        },
        dungeons: [
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
            'shoal_cave',
            'seafloor_cavern',
            'sealed_chamber',
            'iron_island',
            'brooklet_hill',
            'courageous_cavern',
        ],
    },
    'Tentacruel': {
        native_region: 'Kanto',
        routes: {
            land: [
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'johto_route_40',
                'johto_route_41',
                'sinnoh_route_219',
                'sinnoh_route_220',
                'sinnoh_route_223',
                'alola_route_14',
                'poni_breaker_coast',
                'fields_of_honor',
                'challenge_beach',
                'loop_lagoon',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
                'lunkers_lair',
            ],
            water: [
                'treasure_beach',
                'kindle_road',
                'bond_bridge',
                'five_isle_meadow',
                'water_path',
                'johto_route_32',
                'johto_route_34',
                'johto_route_26',
                'johto_route_27',
                'sinnoh_route_205',
                'sinnoh_route_213',
                'sinnoh_route_218',
                'sinnoh_route_221',
                'sinnoh_route_222',
                'sinnoh_route_224',
                'sinnoh_route_226',
                'sinnoh_route_230',
                'alola_route_15',
                'seagrass_haven',
            ],
        },
        dungeons: [
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
            'iron_island',
            'courageous_cavern',
        ],
        evolution: [
            {
                prev: 'Tentacool',
                level: 30,
            },
        ],
    },
    'Geodude': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kindle_road',
                'sevault_canyon',
                'johto_route_45',
                'johto_route_46',
                'sinnoh_route_206',
                'sinnoh_route_207',
                'sinnoh_route_210',
                'sinnoh_route_214',
                'deertrack_heights',
                'worn_bridge',
                'scarlet_bog',
                'bolderoll_slope',
                'gapejaw_bog',
                'ursas_ring',
                'bolderoll_ravine',
            ],
            headbutt: [
                'hoenn_route_111',
                'hoenn_route_114',
                'deertrack_path',
                'deertrack_heights',
                'windswept_run',
                'natures_pantry',
                'tidewater_dam',
                'golden_lowlands',
                'cloudpool_ridge',
                'diamond_heath',
                'cottonsedge_prairie',
                'droning_meadow',
                'holm_of_trials',
                'crossing_slope',
                'ginkgo_landing',
                'aipom_hill',
                'bathers_lagoon',
                'deadwood_haunt',
                'sands_reach',
                'castaway_shore',
                'tranquility_cove',
            ],
        },
        dungeons: [
            'mt_moon',
            'rock_tunnel',
            'mt_ember_summit',
            'victory_road',
            'ruby_path',
            'union_cave',
            'mt_mortar',
            'team_rockets_hideout',
            'dark_cave',
            'granite_cave',
            'magma_hideout',
            'oreburgh_gate',
            'wayward_cave',
            'mt_coronet_south',
            'solaceon_ruins',
            'iron_island',
            'mt_coronet_north',
            'terminus_cave',
            'victory_road_kalos',
            'oreburrow_tunnel',
            'heartwood',
            'shrouded_ruins',
            'veilstone_cape',
            'clamberclaw_cliffs',
            'celestica_ruins',
            'sacred_plaza',
        ],
        egg: 'Mystery Egg',
    },
    'Alolan Geodude': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_12',
            ],
        },
    },
    'Pinkan Geodude': {
        native_region: 'Kanto',
        trades: [
            ('pinkan_pokemon_reserve', ['Pinkan Berry']),
        ],
    },
    'Graveler': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_45',
                'sinnoh_route_214',
                'sinnoh_route_211',
                'sinnoh_route_216',
                'sinnoh_route_225',
                'sinnoh_route_226',
                'sinnoh_route_227',
                'kalos_route_18',
                'scarlet_bog',
                'bolderoll_slope',
                'gapejaw_bog',
                'ursas_ring',
                'bolderoll_ravine',
            ],
            headbutt: [
                'sevault_canyon',
                'sandgem_flats',
                'ramanas_island',
                'golden_lowlands',
                'cloudpool_ridge',
                'diamond_heath',
                'cottonsedge_prairie',
                'droning_meadow',
                'holm_of_trials',
                'crossing_slope',
                'ginkgo_landing',
                'aipom_hill',
                'bathers_lagoon',
                'hideaway_bay',
                'deadwood_haunt',
                'sands_reach',
                'castaway_shore',
                'windbreak_stand',
                'spring_path',
                'tranquility_cove',
                'tombolo_walk',
                'heavenward_lookout',
                'celestica_trail',
                'fabled_spring',
                'bolderoll_ravine',
                'stonetooth_rows',
            ],
        },
        dungeons: [
            'mt_ember_summit',
            'ruby_path',
            'mt_mortar',
            'dark_cave',
            'victory_road_johto',
            'magma_hideout',
            'iron_island',
            'spear_pillar',
            'victory_road_sinnoh',
            'sendoff_spring',
            'stark_mountain',
            'cave_of_being',
            'terminus_cave',
            'victory_road_kalos',
            'shrouded_ruins',
            'veilstone_cape',
            'firespit_island',
            'clamberclaw_cliffs',
            'celestica_ruins',
            'sacred_plaza',
            'ancient_snowpoint_temple',
            'ancient_lake_valor',
        ],
        dungeon_boss: [
            ('mt_coronet_north', 4960000),
            ('oreburrow_tunnel', 10000000),
        ],
        dungeon_chest: [
            'cerulean_cave',
        ],
        evolution: [
            {
                prev: 'Geodude',
                level: 25,
            },
        ],
    },
    'Alolan Graveler': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_12',
                'alola_route_17',
            ],
        },
        evolution: [
            {
                prev: 'Alolan Geodude',
                level: 25,
            },
        ],
    },
    'Golem': {
        native_region: 'Kanto',
        routes: {
            land: [
                'bolderoll_ravine',
            ],
        },
        evolution: [
            {
                prev: 'Graveler',
                item: 'Linking Cord',
            },
        ],
    },
    'Alolan Golem': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Alolan Graveler',
                item: 'Linking Cord',
            },
        ],
    },
    'Ponyta': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kindle_road',
                'johto_route_26',
                'johto_route_27',
                'johto_route_28',
                'sinnoh_route_206',
                'sinnoh_route_207',
                'sinnoh_route_210',
                'horseshoe_plains',
            ],
        },
        dungeons: [
            'mt_ember_summit',
            'mt_silver',
        ],
    },
    'Galarian Ponyta': {
        native_region: 'Galar',
        routes: {
            land: [
                'old_cemetery',
            ],
        },
        dungeons: [
            'glimwood_tangle',
        ],
    },
    'Rapidash': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kindle_road',
                'johto_route_28',
                'horseshoe_plains',
            ],
        },
        dungeons: [
            'mt_ember_summit',
        ],
        evolution: [
            {
                prev: 'Ponyta',
                level: 40,
            },
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Galarian Rapidash': {
        native_region: 'Galar',
        routes: {
            land: [
                'old_cemetery',
            ],
        },
        dungeon_boss: [
            ('crown_shrine', 161099869),
        ],
        evolution: [
            {
                prev: 'Galarian Ponyta',
                level: 40,
            },
        ],
    },
    'Slowpoke': {
        native_region: 'Kanto',
        routes: {
            land: [
                'treasure_beach',
                'kindle_road',
                'cape_brink',
                'bond_bridge',
                'five_isle_meadow',
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'water_path',
                'green_path',
                'outcast_island',
                'ruin_valley',
                'canyon_entrance',
                'kalos_route_12',
                'azure_bay',
                'route_1_hauoli_outskirts',
                'kalae_bay',
                'alola_route_15',
                'alola_route_16',
            ],
            water: [
                'kanto_route_22',
                'kanto_route_25',
                'kanto_route_6',
                'kanto_route_12',
                'kanto_route_23',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'berry_forest',
            'cerulean_cave',
            'icefall_cave',
            'sunburst_island',
            'slowpoke_well',
            'tohjo_falls',
            'hall_of_origin',
        ],
        egg: 'Water Egg',
        safari: ['Kanto'],
    },
    'Galarian Slowpoke': {
        native_region: 'Galar',
        routes: {
            land: [
                'fields_of_honor',
            ],
        },
    },
    'Slowbro': {
        native_region: 'Kanto',
        routes: {
            land: [
                'cape_brink',
            ],
            water: [
                'kanto_route_12',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'berry_forest',
            'cerulean_cave',
        ],
        evolution: [
            {
                prev: 'Slowpoke',
                level: 37,
            },
        ],
    },
    'Mega Slowbro': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Slowbro',
                item: 'Slowbronite',
            },
        ],
    },
    'Galarian Slowbro': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Galarian Slowpoke',
                item: 'Galarica Cuff',
            },
        ],
    },
    'Magnemite': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_38',
                'johto_route_39',
                'sinnoh_route_222',
                'challenge_beach',
            ],
        },
        dungeons: [
            'power_plant',
            'new_mauville',
            'trainers_school',
        ],
        egg: 'Electric Egg',
        farm_wandering: ['Babiri Berry'],
    },
    'Magneton': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_222',
                'challenge_beach',
                'training_lowlands',
                'challenge_road',
            ],
        },
        dungeons: [
            'power_plant',
            'cerulean_cave',
            'victory_road_sinnoh',
            'p2_laboratory',
            'lost_hotel',
            'glaseado_mountain',
        ],
        dungeon_boss: [
            ('new_mauville', 1650000),
        ],
        evolution: [
            {
                prev: 'Magnemite',
                level: 30,
            },
        ],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Farfetch\'d': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_12',
                'kanto_route_13',
                'johto_route_38',
                'johto_route_39',
                'johto_route_47',
                'johto_route_48',
                'kalos_route_22',
            ],
        },
        farm_wandering: ['Coba Berry'],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Galarian Farfetch\'d': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_5',
                'giants_mirror',
            ],
        },
        egg: 'Fighting Egg',
    },
    'Doduo': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_16',
                'kanto_route_17',
                'kanto_route_18',
                'johto_route_26',
                'johto_route_27',
                'johto_route_28',
                'kalos_route_5',
            ],
        },
        dungeons: [
            'mt_silver',
        ],
        egg: 'Mystery Egg',
    },
    'Dodrio': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_26',
                'johto_route_27',
                'johto_route_28',
            ],
        },
        evolution: [
            {
                prev: 'Doduo',
                level: 31,
            },
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Pinkan Dodrio': {
        native_region: 'Kanto',
        shops: [
            ('tanoby_ruins', 'questPoint'),
        ],
    },
    'Seel': {
        native_region: 'Kanto',
        routes: {
            water: [
                'johto_route_47',
            ],
        },
        dungeons: [
            'icefall_cave',
            'whirl_islands',
            'seaside_cave',
            'giant_chasm',
            'seaward_cave',
        ],
        dungeon_boss: [
            ('seafoam_islands', 86130),
        ],
        shadow_pokemon: [
            'phenac_stadium',
        ],
    },
    'Dewgong': {
        native_region: 'Kanto',
        dungeons: [
            'icefall_cave',
        ],
        dungeon_boss: [
            ('whirl_islands', 400000),
        ],
        evolution: [
            {
                prev: 'Seel',
                level: 34,
            },
        ],
    },
    'Grimer': {
        native_region: 'Kanto',
        dungeons: [
            'pokemon_mansion',
            'fiery_path',
            'castelia_sewers',
        ],
        farm_wandering: ['Kebia Berry'],
        shadow_pokemon: [
            'phenac_stadium',
        ],
    },
    'Alolan Grimer': {
        native_region: 'Alola',
        dungeons: [
            'trainers_school',
        ],
    },
    'Muk': {
        native_region: 'Kanto',
        routes: {
            land: [
                'unova_route_9',
            ],
        },
        dungeons: [
            'pokemon_mansion',
            'castelia_sewers',
        ],
        evolution: [
            {
                prev: 'Grimer',
                level: 38,
            },
        ],
    },
    'Alolan Muk': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Alolan Grimer',
                level: 38,
            },
        ],
        special: [
            Has('Alolan Muk') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Shellder': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_20',
                'johto_route_41',
                'west_lake_axewell',
            ],
            water: [
                'kanto_route_21',
                'johto_route_47',
                'johto_route_26',
                'johto_route_27',
                'sinnoh_route_205',
                'kalos_route_8',
                'kalae_bay',
                'east_lake_axewell',
                'giants_seat',
                'loop_lagoon',
            ],
        },
        dungeons: [
            'icefall_cave',
            'seaside_cave',
            'courageous_cavern',
        ],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Cloyster': {
        native_region: 'Kanto',
        routes: {
            land: [
                'west_lake_axewell',
                'east_lake_axewell',
            ],
            water: [
                'valencia_island',
                'giants_seat',
                'loop_lagoon',
            ],
        },
        dungeons: [
            'courageous_cavern',
        ],
        evolution: [
            {
                prev: 'Shellder',
                item: 'Water Stone',
            },
        ],
    },
    'Gastly': {
        native_region: 'Kanto',
        routes: {
            land: [
                'giants_seat',
                'north_lake_miloch',
                'watchtower_ruins',
                'hammerlocke_hills',
                'golden_lowlands',
                'scarlet_bog',
                'cottonsedge_prairie',
                'droning_meadow',
                'gapejaw_bog',
                'ursas_ring',
                'holm_of_trials',
                'bolderoll_ravine',
                'bonechill_wastes',
                'south_province_area_one',
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'pokemon_tower',
            'lost_cave',
            'sprout_tower',
            'tin_tower',
            'eterna_forest',
            'old_chateau',
            'distortion_world',
            'hauoli_cemetery',
            'memorial_hill',
            'thrifty_megamart',
            'shrouded_ruins',
            'clamberclaw_cliffs',
            'celestica_ruins',
            'sacred_plaza',
        ],
        egg: 'Mystery Egg',
        farm_wandering: ['Kasib Berry'],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_1'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_22'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_2'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_3'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_4'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_24'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_25'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_5'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_6'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_11'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_9'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_10'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_8'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_7'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_12'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_13'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_14'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_15'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_16'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_17'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_18'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_19'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_20'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_21'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('kanto_route_23'),
        ],
    },
    'Haunter': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kalos_route_14',
                'kalos_route_19',
                'rolling_fields',
                'giants_seat',
                'watchtower_ruins',
                'galar_route_8',
                'scarlet_bog',
                'cottonsedge_prairie',
                'droning_meadow',
                'gapejaw_bog',
                'ursas_ring',
                'holm_of_trials',
                'bolderoll_ravine',
                'bonechill_wastes',
            ],
        },
        dungeons: [
            'pokemon_tower',
            'lost_cave',
            'old_chateau',
            'celestial_tower',
            'frost_cavern',
            'victory_road_kalos',
            'thrifty_megamart',
            'shrouded_ruins',
            'clamberclaw_cliffs',
            'celestica_ruins',
            'sacred_plaza',
            'glaseado_mountain',
        ],
        dungeon_boss: [
            ('tin_tower', 380000),
        ],
        evolution: [
            {
                prev: 'Gastly',
                level: 25,
            },
        ],
    },
    'Gengar': {
        native_region: 'Kanto',
        routes: {
            land: [
                'giants_cap',
            ],
        },
        dungeons: [
            'old_chateau',
            'thrifty_megamart',
            'turnback_cave',
        ],
        evolution: [
            {
                prev: 'Haunter',
                item: 'Linking Cord',
            },
        ],
    },
    'Mega Gengar': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Gengar',
                item: 'Gengarite',
            },
        ],
    },
    'Gigantamax Gengar': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Gengar') | make_rule('lair_of_giants8')) & make_rule('max_lair'),
        ],
    },
    'Onix': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sevault_canyon',
                'rolling_fields',
                'east_lake_axewell',
                'giants_seat',
                'motostoke_riverbank',
                'celestica_trail',
            ],
        },
        dungeons: [
            'victory_road',
            'union_cave',
            'victory_road_johto',
            'wayward_cave',
            'iron_island',
            'victory_road_sinnoh',
            'cave_of_being',
            'victory_road_unova',
            'twist_mountain',
            'sea_spirits_den',
        ],
        dungeon_boss: [
            ('rock_tunnel', 20585),
            ('relic_passage', 21000000),
            ('ten_carat_hill', 59489105),
        ],
    },
    'Crystal Onix': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('sunburst_island', 4500000),
        ],
    },
    'Drowzee': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_11',
                'johto_route_34',
                'johto_route_35',
                'alola_route_2',
                'south_province_area_one',
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'berry_forest',
        ],
    },
    'Hypno': {
        native_region: 'Kanto',
        routes: {
            land: [
                'poni_plains',
            ],
        },
        dungeons: [
            'fullmoon_island',
        ],
        dungeon_boss: [
            ('berry_forest', 101427),
        ],
        evolution: [
            {
                prev: 'Drowzee',
                level: 26,
            },
        ],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Krabby': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_19',
                'kanto_route_20',
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'johto_route_40',
                'west_lake_axewell',
                'south_lake_miloch',
                'fields_of_honor',
                'loop_lagoon',
            ],
            water: [
                'kanto_route_4',
                'kanto_route_24',
                'kanto_route_11',
                'kanto_route_10',
                'kanto_route_13',
                'kanto_route_21',
                'treasure_beach',
                'kindle_road',
                'bond_bridge',
                'five_isle_meadow',
                'water_path',
                'johto_route_34',
                'giants_cap',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
            'whirl_islands',
        ],
    },
    'Kingler': {
        native_region: 'Kanto',
        routes: {
            land: [
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'johto_route_40',
                'west_lake_axewell',
                'south_lake_miloch',
                'axews_eye',
                'galar_route_9',
                'fields_of_honor',
                'training_lowlands',
            ],
            water: [
                'five_isle_meadow',
                'water_path',
                'johto_route_34',
            ],
        },
        dungeons: [
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
        ],
        dungeon_boss: [
            ('whirl_islands', 400000),
        ],
        evolution: [
            {
                prev: 'Krabby',
                level: 28,
            },
        ],
    },
    'Gigantamax Kingler': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Kingler') | make_rule('lair_of_giants9')) & make_rule('max_lair'),
        ],
    },
    'Voltorb': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_10',
            ],
        },
        dungeons: [
            'power_plant',
            'team_rockets_hideout',
            'new_mauville',
        ],
        egg: 'Electric Egg',
        shadow_pokemon: [
            'pyrite_cave',
            'relic_cave',
        ],
    },
    'Hisuian Voltorb': {
        native_region: 'Hisui',
        dungeons: [
            'sacred_plaza',
        ],
    },
    'Electrode': {
        native_region: 'Kanto',
        dungeons: [
            'power_plant',
            'cerulean_cave',
            'team_rockets_hideout',
            'lost_hotel',
        ],
        dungeon_boss: [
            ('new_mauville', 1650000),
        ],
        dungeon_chest: [
            'silph_co',
            'aqua_hideout',
        ],
        evolution: [
            {
                prev: 'Voltorb',
                level: 30,
            },
        ],
    },
    'Hisuian Electrode': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Hisuian Voltorb',
                item: 'Leaf Stone',
            },
        ],
    },
    'Exeggcute': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kalos_route_12',
                'azure_bay',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
            ],
            headbutt: [
                'johto_route_29',
                'johto_route_30',
                'johto_route_31',
                'johto_route_32',
                'johto_route_34',
                'johto_route_35',
                'johto_route_36',
                'johto_route_37',
                'johto_route_38',
                'johto_route_39',
                'johto_route_43',
                'johto_route_47',
                'johto_route_48',
                'johto_route_26',
                'johto_route_27',
            ],
        },
        dungeons: [
            'berry_forest',
        ],
        safari: ['Kanto', 'Sinnoh'],
        special: [
            make_rule('exeggutor_island_hill', False) & make_rule('emissary_of_light2'),
        ],
    },
    'Exeggcute (Single)': {
        native_region: 'Kanto',
        special: [
            Has('Exeggcute') & make_rule('region_safari', 'Kanto'),
            Has('Exeggcute') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Exeggutor': {
        native_region: 'Kanto',
        routes: {
            land: [
                'workout_sea',
                'insular_sea',
            ],
        },
        evolution: [
            {
                prev: 'Exeggcute',
                item: 'Leaf Stone',
                region: 'allButAlola',
            },
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Alolan Exeggutor': {
        native_region: 'Alola',
        dungeon_boss: [
            ('exeggutor_island_hill', 78865330),
        ],
        evolution: [
            {
                prev: 'Exeggcute',
                item: 'Leaf Stone',
                region: 'alolaOnly',
            },
        ],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('exeggutor_island_hill', False),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('exeggutor_island_hill', True, 78865330),
        ],
    },
    'Pinkan Exeggutor': {
        native_region: 'Kanto',
        routes: {
            land: [
                'pinkan_forest',
            ],
        },
    },
    'Cubone': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sevault_canyon',
                'forest_of_focus',
            ],
        },
        dungeons: [
            'pokemon_tower',
            'glittering_cave',
            'wela_volcano_park',
            'warm_up_tunnel',
        ],
        safari: ['Kanto'],
    },
    'Marowak': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sevault_canyon',
                'potbottom_desert',
            ],
        },
        dungeons: [
            'victory_road',
        ],
        dungeon_boss: [
            ('pokemon_tower', 37615),
        ],
        evolution: [
            {
                prev: 'Cubone',
                level: 28,
                region: 'allButAlola',
            },
        ],
        safari: ['Kanto', 'Kalos'],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Alolan Marowak': {
        native_region: 'Alola',
        dungeon_boss: [
            ('wela_volcano_park', 64481960),
        ],
        evolution: [
            {
                prev: 'Cubone',
                level: 28,
                time: 'night',
                region: 'alolaOnly',
            },
        ],
    },
    'Totem Marowak': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_symbiotic_relations') & make_rule('wela_volcano_park', True, 82543791),
        ],
    },
    'Hitmonlee': {
        native_region: 'Kanto',
        dungeons: [
            'dusty_bowl',
        ],
        evolution: [
            {
                prev: 'Tyrogue',
                level: 20,
            },
        ],
        egg: 'Fighting Egg',
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Hitmonchan': {
        native_region: 'Kanto',
        dungeons: [
            'dusty_bowl',
        ],
        evolution: [
            {
                prev: 'Tyrogue',
                level: 20,
            },
        ],
        egg: 'Fighting Egg',
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Lickitung': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_44',
                'sinnoh_route_215',
                'unova_route_2',
                'poni_gauntlet',
                'soothing_wetlands',
                'arenas_approach',
                'avalanche_slopes',
                'snowfall_hot_spring',
            ],
        },
        dungeons: [
            'victory_road_kalos',
            'brawlers_cave',
            'shrouded_ruins',
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
        shops: [
            ('celadon_city', 'questPoint'),
        ],
    },
    'Koffing': {
        native_region: 'Kanto',
        routes: {
            land: [
                'motostoke_outskirts',
                'motostoke_riverbank',
                'giants_mirror',
            ],
        },
        dungeons: [
            'pokemon_mansion',
            'burned_tower',
            'team_rockets_hideout',
            'fiery_path',
            'dusty_bowl',
        ],
    },
    'Weezing': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_227',
            ],
        },
        dungeons: [
            'pokemon_mansion',
            'stark_mountain',
            'p2_laboratory',
        ],
        dungeon_boss: [
            ('burned_tower', 320000),
        ],
        evolution: [
            {
                prev: 'Koffing',
                level: 35,
                region: 'allButGalar',
            },
        ],
    },
    'Galarian Weezing': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        dungeon_boss: [
            ('slumbering_weald_shrine', 135047520),
        ],
        evolution: [
            {
                prev: 'Koffing',
                level: 35,
                region: 'galarOnly',
            },
        ],
    },
    'Pinkan Weezing': {
        native_region: 'Kanto',
        trades: [
            ('pinkan_pokemon_reserve', ['Pinkan Berry']),
        ],
    },
    'Rhyhorn': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_214',
                'sinnoh_route_227',
                'motostoke_riverbank',
                'bridge_field',
                'stony_wilderness',
                'giants_mirror',
                'galar_route_8',
                'potbottom_desert',
                'diamond_heath',
                'bolderoll_slope',
                'celestica_trail',
            ],
        },
        dungeons: [
            'victory_road_johto',
            'victory_road_sinnoh',
            'stark_mountain',
            'glittering_cave',
            'shrouded_ruins',
            'sacred_plaza',
        ],
        safari: ['Kanto'],
        farm_wandering: ['Charti Berry'],
    },
    'Pinkan Rhyhorn': {
        native_region: 'Kanto',
        dungeons: [
            'pinkan_mountain',
        ],
    },
    'Rhydon': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_227',
                'sinnoh_route_228',
                'giants_seat',
                'motostoke_riverbank',
                'bridge_field',
                'stony_wilderness',
                'giants_cap',
                'lake_of_outrage',
                'white_hill_station',
                'potbottom_desert',
                'celestica_trail',
            ],
        },
        dungeons: [
            'stark_mountain',
        ],
        dungeon_boss: [
            ('victory_road_johto', 500000),
            ('victory_road_sinnoh', 7000000),
            ('sacred_plaza', 10000000),
        ],
        evolution: [
            {
                prev: 'Rhyhorn',
                level: 42,
            },
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Pinkan Rhydon': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('pinkan_mountain', 7000000),
        ],
        evolution: [
            {
                prev: 'Pinkan Rhyhorn',
                level: 42,
            },
        ],
    },
    'Chansey': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_209',
                'sinnoh_route_210',
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'potbottom_desert',
                'challenge_road',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_island',
                'hideaway_bay',
                'tombolo_walk',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'minas_houseboat',
            'brawlers_cave',
        ],
        safari: ['Kanto'],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Charity Chansey': {
        native_region: 'Kanto',
        shops: [
            ('client_island', 'questPoint'),
        ],
    },
    'Tangela': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_21',
                'treasure_beach',
                'johto_route_44',
                'johto_route_28',
                'unova_route_13',
                'forest_of_focus',
                'gapejaw_bog',
            ],
        },
        dungeons: [
            'mt_silver',
            'flower_paradise',
            'giant_chasm',
        ],
        egg: 'Grass Egg',
        safari: ['Kanto', 'Sinnoh'],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        shadow_pokemon: [
            'cipher_key_lair',
        ],
    },
    'Kangaskhan': {
        native_region: 'Kanto',
        routes: {
            land: [
                'training_lowlands',
            ],
        },
        dungeons: [
            'wela_volcano_park',
        ],
        dungeon_boss: [
            ('warm_up_tunnel', 141260500),
        ],
        safari: ['Kanto', 'Sinnoh'],
        shadow_pokemon: [
            'citadark_isle',
        ],
        special: [
            make_rule('a_beautiful_world3') & make_rule('glittering_cave', True, 63749659),
        ],
    },
    'Mega Kangaskhan': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Kangaskhan',
                item: 'Kangaskhanite',
            },
        ],
    },
    'Baby Kangaskhan': {
        native_region: 'Kanto',
        breeding: ['Kangaskhan', 'Mega Kangaskhan'],
        special: [
            Has('Baby Kangaskhan') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Horsea': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_19',
                'kanto_route_20',
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'hoenn_route_132',
                'hoenn_route_133',
                'hoenn_route_134',
                'kalae_bay',
            ],
            water: [
                'kanto_route_4',
                'kanto_route_24',
                'kanto_route_11',
                'kanto_route_10',
                'kanto_route_13',
                'kanto_route_21',
                'treasure_beach',
                'kindle_road',
                'bond_bridge',
                'five_isle_meadow',
                'water_path',
                'sinnoh_route_226',
                'insular_sea',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
            'whirl_islands',
            'sealed_chamber',
            'p2_laboratory',
        ],
    },
    'Seadra': {
        native_region: 'Kanto',
        routes: {
            land: [
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'honeycalm_sea',
            ],
            water: [
                'five_isle_meadow',
                'water_path',
                'sinnoh_route_226',
            ],
        },
        dungeons: [
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
        ],
        evolution: [
            {
                prev: 'Horsea',
                level: 32,
            },
        ],
    },
    'Goldeen': {
        native_region: 'Kanto',
        routes: {
            water: [
                'kanto_route_22',
                'kanto_route_25',
                'kanto_route_6',
                'kanto_route_12',
                'kanto_route_23',
                'cape_brink',
                'ruin_valley',
                'johto_route_42',
                'hoenn_route_102',
                'hoenn_route_111',
                'hoenn_route_114',
                'hoenn_route_117',
                'hoenn_route_120',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_214',
                'sinnoh_route_212',
                'sinnoh_route_229',
                'kalos_route_3',
                'kalos_route_22',
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'galar_route_4',
                'galar_route_5',
                'bridge_field',
                'giants_cap',
                'galar_route_6',
                'forest_of_focus',
            ],
        },
        dungeons: [
            'berry_forest',
            'cerulean_cave',
            'icefall_cave',
            'union_cave',
            'tohjo_falls',
            'meteor_falls',
            'victory_road_hoenn',
            'lake_valor',
            'lake_verity',
            'lake_acuity',
            'sendoff_spring',
            'abundant_shrine',
            'pinwheel_forest',
            'brooklet_hill',
            'malie_garden',
        ],
        safari: ['Kanto'],
    },
    'Seaking': {
        native_region: 'Kanto',
        routes: {
            land: [
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'bridge_field',
                'lake_of_outrage',
            ],
            water: [
                'johto_route_42',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_214',
                'sinnoh_route_212',
                'sinnoh_route_229',
            ],
        },
        dungeon_boss: [
            ('tohjo_falls', 480000),
            ('sendoff_spring', 10000000),
        ],
        evolution: [
            {
                prev: 'Goldeen',
                level: 33,
            },
        ],
        safari: ['Kanto'],
    },
    'Staryu': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_20',
                'johto_route_40',
            ],
            water: [
                'kanto_route_21',
                'johto_route_34',
                'johto_route_47',
                'unova_route_13',
                'kalos_route_8',
                'alola_route_7',
                'challenge_beach',
                'training_lowlands',
            ],
        },
        dungeons: [
            'icefall_cave',
        ],
        egg: 'Water Egg',
        dream_orbs: ['Orange'],
    },
    'Starmie': {
        native_region: 'Kanto',
        routes: {
            land: [
                'fields_of_honor',
                'challenge_beach',
            ],
        },
        evolution: [
            {
                prev: 'Staryu',
                item: 'Water Stone',
            },
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Mr. Mime': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_218',
                'sandgem_flats',
            ],
        },
        dungeons: [
            'reflection_cave',
        ],
        evolution: [
            {
                prev: 'Mime Jr.',
                level: 32,
                region: 'allButGalar',
            },
        ],
        farm_wandering: ['Payapa Berry'],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
        shops: [
            ('celadon_city', 'questPoint'),
        ],
    },
    'Galarian Mr. Mime': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'white_hill_station',
                'galar_route_10',
            ],
        },
        evolution: [
            {
                prev: 'Mime Jr.',
                level: 32,
                region: 'galarOnly',
            },
        ],
    },
    'Scyther': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_210',
                'sinnoh_route_215',
                'kalos_route_21',
                'training_lowlands',
            ],
        },
        dungeons: [
            'primeval_grotto',
        ],
        dungeon_boss: [
            ('heartwood', 10000000),
        ],
        safari: ['Kanto', 'Johto'],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Pinkan Scyther': {
        native_region: 'Kanto',
        farm_wandering: ['Pinkan Berry'],
        trades: [
            ('pinkan_pokemon_reserve', ['Pinkan Berry']),
        ],
    },
    'Jynx': {
        native_region: 'Kanto',
        routes: {
            land: [
                'slippery_slope',
                'frostpoint_field',
            ],
        },
        dungeons: [
            'ice_path',
            'frost_cavern',
        ],
        dungeon_boss: [
            ('snowpoint_temple', 10000000),
        ],
        evolution: [
            {
                prev: 'Smoochum',
                level: 30,
            },
        ],
        farm_wandering: ['Yache Berry'],
        shops: [
            ('celadon_city', 'questPoint'),
        ],
    },
    'Santa Jynx': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_1'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_22'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_2'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_3'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_4'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_24'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_25'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_5'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_6'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_11'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_9'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_10'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_8'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_7'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_12'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_13'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_14'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_15'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_16'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_17'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_18'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_19'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_20'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_21'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('santa_jynx1') & make_rule('kanto_route_23'),
        ],
    },
    'Electabuzz': {
        native_region: 'Kanto',
        routes: {
            land: [
                'sinnoh_route_222',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'cloudcap_pass',
                'arenas_approach',
                'icebound_falls',
            ],
        },
        dungeons: [
            'hokulani_observatory',
            'ruins_of_conflict',
            'split_decision_ruins',
        ],
        dungeon_boss: [
            ('power_plant', 67535),
        ],
        evolution: [
            {
                prev: 'Elekid',
                level: 30,
            },
        ],
        egg: 'Electric Egg',
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Pinkan Electabuzz': {
        native_region: 'Kanto',
        trades: [
            ('pinkan_pokemon_reserve', ['Pinkan Berry']),
        ],
    },
    'Magmar': {
        native_region: 'Kanto',
        routes: {
            land: [
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'wela_volcano_park',
            'dyna_tree_hill',
            'firespit_island',
        ],
        dungeon_boss: [
            ('pokemon_mansion', 88800),
            ('mt_ember_summit', 101427),
        ],
        evolution: [
            {
                prev: 'Magby',
                level: 30,
            },
        ],
        egg: 'Fire Egg',
        safari: ['Kalos'],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Pinsir': {
        native_region: 'Kanto',
        routes: {
            land: [
                'unova_route_12',
                'kalos_route_12',
                'poni_grove',
                'forest_of_focus',
                'training_lowlands',
                'challenge_road',
            ],
        },
        dungeons: [
            'lush_jungle',
        ],
        dungeon_boss: [
            ('lostlorn_forest', 18000000),
        ],
        safari: ['Kanto', 'Johto'],
        farm_wandering: ['Tanga Berry'],
        shadow_pokemon: [
            'citadark_isle',
        ],
        special: [
            make_rule('emissary_of_light2') & make_rule('exeggutor_island_hill', True, 78865330),
        ],
    },
    'Mega Pinsir': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Pinsir',
                item: 'Pinsirite',
            },
        ],
    },
    'Tauros': {
        native_region: 'Kanto',
        routes: {
            land: [
                'johto_route_38',
                'johto_route_39',
                'johto_route_48',
                'kalos_route_12',
                'poni_plains',
                'training_lowlands',
            ],
        },
        dungeon_boss: [
            ('paniola_ranch', 30278320),
        ],
        safari: ['Kanto'],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Magikarp': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_19',
                'kanto_route_20',
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'johto_route_40',
                'johto_route_41',
                'hoenn_route_105',
                'hoenn_route_106',
                'hoenn_route_107',
                'hoenn_route_108',
                'hoenn_route_109',
                'hoenn_route_122',
                'hoenn_route_124',
                'hoenn_route_125',
                'hoenn_route_126',
                'hoenn_route_127',
                'hoenn_route_128',
                'hoenn_route_129',
                'hoenn_route_131',
                'hoenn_route_132',
                'hoenn_route_133',
                'hoenn_route_134',
                'sinnoh_route_219',
                'sinnoh_route_220',
                'sinnoh_route_223',
                'melemele_sea',
                'alola_route_9',
                'alola_route_13',
                'alola_route_14',
                'poni_breaker_coast',
                'friend_league_bridge',
                'quick_league_bridge',
                'heavy_league_bridge',
                'great_league_bridge',
                'fast_league_bridge',
                'luxury_league_bridge',
                'heal_league_bridge',
                'ultra_league_bridge',
                'elite_four_league_pier',
                'master_league_pier',
            ],
            water: [
                'kanto_route_22',
                'kanto_route_4',
                'kanto_route_24',
                'kanto_route_25',
                'kanto_route_6',
                'kanto_route_11',
                'kanto_route_10',
                'kanto_route_12',
                'kanto_route_13',
                'kanto_route_21',
                'kanto_route_23',
                'treasure_beach',
                'kindle_road',
                'cape_brink',
                'bond_bridge',
                'five_isle_meadow',
                'water_path',
                'ruin_valley',
                'johto_route_30',
                'johto_route_31',
                'johto_route_32',
                'johto_route_34',
                'johto_route_35',
                'johto_route_42',
                'johto_route_43',
                'johto_route_44',
                'johto_route_45',
                'johto_route_47',
                'johto_route_26',
                'johto_route_27',
                'johto_route_28',
                'hoenn_route_102',
                'hoenn_route_103',
                'hoenn_route_104',
                'hoenn_route_110',
                'hoenn_route_111',
                'hoenn_route_114',
                'hoenn_route_115',
                'hoenn_route_117',
                'hoenn_route_118',
                'hoenn_route_119',
                'hoenn_route_120',
                'hoenn_route_121',
                'hoenn_route_123',
                'hoenn_route_130',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_205',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_210',
                'sinnoh_route_214',
                'sinnoh_route_213',
                'sinnoh_route_212',
                'sinnoh_route_218',
                'sinnoh_route_221',
                'sinnoh_route_222',
                'sinnoh_route_224',
                'sinnoh_route_225',
                'sinnoh_route_226',
                'sinnoh_route_227',
                'sinnoh_route_228',
                'sinnoh_route_229',
                'sinnoh_route_230',
                'kalos_route_3',
                'kalos_route_22',
                'kalae_bay',
                'alola_route_7',
                'alola_route_8',
                'akala_outskirts',
                'alola_route_15',
                'poni_gauntlet',
                'galar_route_2',
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'axews_eye',
                'galar_route_4',
                'galar_route_5',
                'bridge_field',
                'galar_route_6',
                'galar_route_2_lakeside',
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
                'giants_bed',
                'giants_foot',
                'frigid_sea',
                'ballimere_lake',
                'snowslide_slope',
                'obsidian_falls',
                'poco_path',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'seafoam_islands',
            'berry_forest',
            'cerulean_cave',
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
            'ruins_of_alph',
            'union_cave',
            'tohjo_falls',
            'meteor_falls',
            'shoal_cave',
            'seafloor_cavern',
            'sealed_chamber',
            'victory_road_hoenn',
            'oreburgh_gate',
            'mt_coronet_south',
            'lake_valor',
            'lake_verity',
            'mt_coronet_north',
            'lake_acuity',
            'sendoff_spring',
            'seaward_cave',
            'brooklet_hill',
            'malie_garden',
            'vast_poni_canyon',
            'poni_meadow',
            'slumbering_weald_shrine',
            'courageous_cavern',
            'roaring_sea_caves',
            'ancient_lake_verity',
        ],
        safari: ['Kanto', 'Sinnoh', 'Alola'],
        shops: [
            ('route_4_pokemon_center', 'money'),
        ],
    },
    'Magikarp Skelly': {
        native_region: 'Kanto',
        special: [
            Has('Quick League Badge') & make_rule('region_safari', 'Alola'),
        ],
    },
    'Magikarp Calico (Orange, White)': {
        native_region: 'Kanto',
        routes: {
            land: [
                'heavy_league_bridge',
                'fast_league_bridge',
                'ultra_league_bridge',
            ],
        },
    },
    'Magikarp Calico (Orange, White, Black)': {
        native_region: 'Kanto',
        routes: {
            land: [
                'fast_league_bridge',
                'luxury_league_bridge',
                'ultra_league_bridge',
            ],
        },
    },
    'Magikarp Calico (White, Orange)': {
        native_region: 'Kanto',
        special: [
            make_rule('region_safari', 'Alola') & make_rule('magikarp_jump_karpen'),
        ],
    },
    'Magikarp Calico (Orange, Gold)': {
        native_region: 'Kanto',
        routes: {
            land: [
                'master_league_pier',
            ],
        },
    },
    'Magikarp Orange Two-Tone': {
        native_region: 'Kanto',
        routes: {
            land: [
                'great_league_bridge',
                'fast_league_bridge',
                'ultra_league_bridge',
            ],
        },
    },
    'Magikarp Orange Orca': {
        native_region: 'Kanto',
        routes: {
            land: [
                'heavy_league_bridge',
            ],
        },
    },
    'Magikarp Orange Dapples': {
        native_region: 'Kanto',
        routes: {
            land: [
                'great_league_bridge',
                'luxury_league_bridge',
                'heal_league_bridge',
            ],
        },
    },
    'Magikarp Pink Two-Tone': {
        native_region: 'Kanto',
        routes: {
            land: [
                'luxury_league_bridge',
            ],
        },
    },
    'Magikarp Pink Orca': {
        native_region: 'Kanto',
        routes: {
            land: [
                'elite_four_league_pier',
            ],
        },
    },
    'Magikarp Pink Dapples': {
        native_region: 'Kanto',
        special: [
            Has('Fast League Badge') & make_rule('region_safari', 'Alola'),
        ],
    },
    'Magikarp Grey Bubbles': {
        native_region: 'Kanto',
        routes: {
            land: [
                'heal_league_bridge',
                'master_league_pier',
            ],
        },
    },
    'Magikarp Grey Diamonds': {
        native_region: 'Kanto',
        special: [
            make_rule('region_safari', 'Alola') & make_rule('magikarp_jump_karpress3'),
        ],
    },
    'Magikarp Grey Patches': {
        native_region: 'Kanto',
        routes: {
            land: [
                'heal_league_bridge',
                'elite_four_league_pier',
            ],
        },
    },
    'Magikarp Purple Bubbles': {
        native_region: 'Kanto',
        special: [
            Has('Heal League Badge') & make_rule('region_safari', 'Alola'),
        ],
    },
    'Magikarp Purple Diamonds': {
        native_region: 'Kanto',
        special: [
            Has('Luxury League Badge') & make_rule('roamer', 'Alola - Magikarp Jump'),
        ],
    },
    'Magikarp Purple Patches': {
        native_region: 'Kanto',
        special: [
            make_rule('region_safari', 'Alola') & make_rule('magikarp_jump_karpella3'),
        ],
    },
    'Magikarp Apricot Tiger': {
        native_region: 'Kanto',
        routes: {
            land: [
                'ultra_league_bridge',
            ],
        },
    },
    'Magikarp Apricot Zebra': {
        native_region: 'Kanto',
        routes: {
            land: [
                'ultra_league_bridge',
            ],
        },
    },
    'Magikarp Apricot Stripes': {
        native_region: 'Kanto',
        special: [
            Has('Heal League Badge') & make_rule('roamer', 'Alola - Magikarp Jump'),
        ],
    },
    'Magikarp Brown Tiger': {
        native_region: 'Kanto',
        special: [
            Has('Ultra League Badge') & make_rule('region_safari', 'Alola'),
        ],
    },
    'Magikarp Brown Zebra': {
        native_region: 'Kanto',
        routes: {
            land: [
                'ultra_league_bridge',
            ],
        },
    },
    'Magikarp Brown Stripes': {
        native_region: 'Kanto',
        shops: [
            ('hoppy_town', 'Water Gems'),
        ],
    },
    'Magikarp Orange Forehead': {
        native_region: 'Kanto',
        special: [
            Has('E4 League Badge') & make_rule('region_safari', 'Alola'),
        ],
    },
    'Magikarp Orange Mask': {
        native_region: 'Kanto',
        routes: {
            land: [
                'master_league_pier',
            ],
        },
    },
    'Magikarp Black Forehead': {
        native_region: 'Kanto',
        routes: {
            land: [
                'elite_four_league_pier',
            ],
        },
    },
    'Magikarp Black Mask': {
        native_region: 'Kanto',
        special: [
            make_rule('region_safari', 'Alola') & make_rule('magikarp_jump_tykarp2'),
        ],
    },
    'Magikarp Blue Raindrops': {
        native_region: 'Kanto',
        shops: [
            ('magikarps_eye', 'diamond'),
        ],
    },
    'Magikarp Saucy Blue': {
        native_region: 'Kanto',
        quest_rewards: [
            'completed_dr_splashs_research_project',
        ],
        special: [
            make_rule('region_safari', 'Alola') & make_rule('completed_dr_splashs_research_project'),
        ],
    },
    'Magikarp Violet Raindrops': {
        native_region: 'Kanto',
        special: [
            Has('Master League Badge') & make_rule('roamer', 'Alola - Magikarp Jump'),
        ],
    },
    'Magikarp Saucy Violet': {
        native_region: 'Kanto',
        shops: [
            ('magikarps_eye', 'money'),
        ],
    },
    'Magikarp (Feebas)': {
        native_region: 'Kanto',
        shops: [
            ('fish_shop', 'battlePoint'),
        ],
    },
    'Gyarados': {
        native_region: 'Kanto',
        routes: {
            land: [
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'sinnoh_route_219',
                'sinnoh_route_220',
                'sinnoh_route_223',
                'south_lake_miloch',
                'north_lake_miloch',
                'challenge_beach',
                'obsidian_falls',
            ],
            water: [
                'five_isle_meadow',
                'water_path',
                'ruin_valley',
                'valencia_island',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_205',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_210',
                'sinnoh_route_214',
                'sinnoh_route_213',
                'sinnoh_route_212',
                'sinnoh_route_218',
                'sinnoh_route_221',
                'sinnoh_route_222',
                'sinnoh_route_224',
                'sinnoh_route_225',
                'sinnoh_route_226',
                'sinnoh_route_227',
                'sinnoh_route_228',
                'sinnoh_route_229',
                'sinnoh_route_230',
                'west_lake_axewell',
                'east_lake_axewell',
                'giants_seat',
                'axews_eye',
                'bridge_field',
                'giants_mirror',
                'giants_cap',
                'lake_of_outrage',
                'galar_route_2_lakeside',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
                'giants_bed',
                'giants_foot',
                'frigid_sea',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'icefall_cave',
            'sunburst_island',
            'tanoby_ruins',
            'lake_acuity',
            'malie_garden',
            'primeval_grotto',
            'ancient_lake_verity',
        ],
        dungeon_boss: [
            ('oreburgh_gate', 3703000),
            ('sendoff_spring', 10000000),
        ],
        evolution: [
            {
                prev: 'Magikarp',
                level: 20,
            },
        ],
        safari: ['Sinnoh'],
    },
    'Mega Gyarados': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Gyarados',
                item: 'Gyaradosite',
            },
        ],
    },
    'Lapras': {
        native_region: 'Kanto',
        routes: {
            land: [
                'poni_breaker_coast',
                'west_lake_axewell',
                'north_lake_miloch',
                'lake_of_outrage',
                'frigid_sea',
            ],
            water: [
                'kalos_route_12',
                'azure_bay',
                'galar_route_2_lakeside',
                'circhester_bay',
            ],
        },
        dungeons: [
            'icefall_cave',
            'sea_spirits_den',
        ],
        egg: 'Water Egg',
        safari: ['Kalos'],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
        special: [
            Has('Fog Badge') & make_rule('union_cave', True, 450000),
            make_rule('silph_co') & make_rule('blue5'),
        ],
    },
    'Gigantamax Lapras': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Lapras') | make_rule('lair_of_giants10')) & make_rule('max_lair'),
        ],
    },
    'Ditto': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kanto_route_13',
                'kanto_route_14',
                'kanto_route_15',
                'johto_route_34',
                'johto_route_35',
                'johto_route_47',
                'mount_hokulani',
                'lake_of_outrage',
                'workout_sea',
            ],
        },
        dungeons: [
            'pokemon_mansion',
            'cerulean_cave',
            'giant_chasm',
        ],
        dungeon_boss: [
            ('pokemon_village', 94836530),
        ],
        dungeon_chest: [
            'hall_of_origin',
        ],
    },
    'Ditto (Magikarp)': {
        native_region: 'Kanto',
        special: [
            make_rule('region_safari', 'Alola') & HasGroupUnique('Magikarp', 6),
        ],
    },
    'Eevee': {
        native_region: 'Kanto',
        routes: {
            land: [
                'kalos_route_10',
                'alola_route_4',
                'alola_route_6',
                'galar_route_4',
                'frostpoint_field',
                'giants_bed',
                'ballimere_lake',
                'horseshoe_plains',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'hall_of_origin',
        ],
        shops: [
            ('celadon_city', 'questPoint'),
        ],
        quest_rewards: [
            'completed_bills_grandpa_treasure_hunt',
        ],
    },
    'Gigantamax Eevee': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Eevee') | make_rule('lair_of_giants2')) & make_rule('max_lair'),
        ],
    },
    'Let\'s Go Eevee': {
        native_region: 'Kanto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto'),
        ],
    },
    'Vaporeon': {
        native_region: 'Kanto',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                item: 'Water Stone',
            },
        ],
    },
    'Jolteon': {
        native_region: 'Kanto',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                item: 'Thunder Stone',
            },
        ],
    },
    'Flareon': {
        native_region: 'Kanto',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                item: 'Fire Stone',
            },
        ],
    },
    'Porygon': {
        native_region: 'Kanto',
        shops: [
            ('celadon_city', 'questPoint'),
        ],
    },
    'Omanyte': {
        native_region: 'Kanto',
        trades: [
            ('cinnabar_island', ['Helix Fossil']),
        ],
        special: [
            Has('Omanyte') & make_rule('giants_foot'),
            Has('Omanyte') & make_rule('roaring_sea_caves', False),
        ],
    },
    'Omastar': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Omanyte',
                level: 40,
            },
        ],
        trades: [
            ('cinnabar_island', ['Helix Fossil']),
        ],
        special: [
            Has('Omastar') & make_rule('roaring_sea_caves', True, 160924440),
        ],
    },
    'Kabuto': {
        native_region: 'Kanto',
        trades: [
            ('cinnabar_island', ['Dome Fossil']),
        ],
        special: [
            Has('Kabuto') & make_rule('giants_foot'),
            Has('Kabuto') & make_rule('roaring_sea_caves', False),
        ],
    },
    'Kabutops': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Kabuto',
                level: 40,
            },
        ],
        trades: [
            ('cinnabar_island', ['Dome Fossil']),
        ],
        special: [
            Has('Kabutops') & make_rule('roaring_sea_caves', True, 160924440),
        ],
    },
    'Aerodactyl': {
        native_region: 'Kanto',
        trades: [
            ('cinnabar_island', ['Old Amber']),
        ],
        special: [
            Has('Aerodactyl') & make_rule('giants_bed'),
            Has('Aerodactyl') & make_rule('rock_peak_ruins', False),
        ],
    },
    'Mega Aerodactyl': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Aerodactyl',
                item: 'Aerodactylite',
            },
        ],
    },
    'Snorlax': {
        native_region: 'Kanto',
        routes: {
            land: [
                'motostoke_riverbank',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'arenas_approach',
                'snowfall_hot_spring',
            ],
        },
        dungeon_boss: [
            ('hall_of_origin', 10000000),
        ],
        evolution: [
            {
                prev: 'Munchlax',
                item: 'Soothe Bell',
            },
        ],
        farm_wandering: ['Chilan Berry'],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
        temporary_battle: [
            'snorlax_route12',
            'snorlax_route16',
        ],
    },
    'Gigantamax Snorlax': {
        native_region: 'Kanto',
        special: [
            (Has('Gigantamax Snorlax') | make_rule('lair_of_giants11')) & make_rule('max_lair'),
        ],
    },
    'Santa Snorlax': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Elf Munchlax',
                item: 'Soothe Bell',
            },
        ],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kanto - Sevii Islands'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Johto'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Hoenn'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Hoenn - Orre'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Sinnoh'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Unova'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kalos'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Alola'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Alola - Magikarp Jump'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Galar - South'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Galar - Isle of Armor'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Galar - Crown Tundra'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Hisui'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Paldea'),
        ],
    },
    'Snorlax (Snowman)': {
        native_region: 'Kanto',
        special: [
            make_rule('seafoam_islands', False) & make_rule('has_script', "Infinite Seasonal Events"),
        ],
    },
    'Articuno': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('seafoam_islands', 129195),
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
        special: [
            make_rule('roamer', 'Kalos') & make_rule('sea_spirits_den', True),
        ],
    },
    'Galarian Articuno': {
        native_region: 'Galar',
        special: [
            make_rule('roamer', 'Galar - Crown Tundra') & make_rule('the_birds_of_the_dyna_tree5'),
        ],
    },
    'Zapdos': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('power_plant', 101302),
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
        special: [
            make_rule('roamer', 'Kalos') & make_rule('sea_spirits_den', True),
        ],
    },
    'Galarian Zapdos': {
        native_region: 'Galar',
        special: [
            make_rule('roamer', 'Galar - South') & make_rule('the_birds_of_the_dyna_tree5'),
        ],
    },
    'Moltres': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('mt_ember_summit', 184462),
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
        special: [
            make_rule('roamer', 'Kalos') & make_rule('sea_spirits_den', True),
        ],
    },
    'Galarian Moltres': {
        native_region: 'Galar',
        special: [
            make_rule('roamer', 'Galar - Isle of Armor') & make_rule('the_birds_of_the_dyna_tree5'),
        ],
    },
    'Dratini': {
        native_region: 'Kanto',
        routes: {
            water: [
                'johto_route_45',
                'kalos_route_21',
                'poni_gauntlet',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'dragonspiral_tower',
            'poni_meadow',
        ],
        egg: 'Dragon Egg',
        farm_wandering: ['Haban Berry'],
        special: [
            Has('Dratini') & make_rule('region_safari', 'Kanto'),
        ],
    },
    'Dragonair': {
        native_region: 'Kanto',
        routes: {
            land: [
                'ballimere_lake',
            ],
            water: [
                'johto_route_45',
                'kalos_route_21',
                'poni_gauntlet',
            ],
        },
        dungeons: [
            'dragonspiral_tower',
        ],
        evolution: [
            {
                prev: 'Dratini',
                level: 30,
            },
        ],
        egg: 'Dragon Egg',
        special: [
            Has('Dragonair') & make_rule('poni_meadow', False),
            Has('Dragonair') & make_rule('region_safari', 'Kanto'),
        ],
    },
    'Dragonite': {
        native_region: 'Kanto',
        routes: {
            land: [
                'ballimere_lake',
            ],
        },
        dungeon_boss: [
            ('dragonspiral_tower', 48000000),
        ],
        evolution: [
            {
                prev: 'Dragonair',
                level: 55,
            },
        ],
        egg: 'Dragon Egg',
        shadow_pokemon: [
            'gateon_port_battles',
        ],
    },
    'Mewtwo': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('cerulean_cave', 255512),
        ],
    },
    'Mega Mewtwo X': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Mewtwo',
                item: 'Mewtwonite X',
                time: 'day',
            },
        ],
    },
    'Mega Mewtwo Y': {
        native_region: 'Kanto',
        evolution: [
            {
                prev: 'Mewtwo',
                item: 'Mewtwonite Y',
                time: 'night',
            },
        ],
    },
    'Armored Mewtwo': {
        native_region: 'Kanto',
        dungeon_boss: [
            ('new_island', 131500),
        ],
    },
    'Mew': {
        native_region: 'Kanto',
        farm_wandering: ['Petaya Berry'],
        roamer: [
            'Kanto',
        ],
    },
    'Chikorita': {
        native_region: 'Johto',
        routes: {
            land: [
                'alola_route_2',
            ],
        },
        egg: 'Grass Egg',
        starter: ['Johto'],
        farm_wandering: ['Rindo Berry'],
    },
    'Bayleef': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Chikorita',
                level: 16,
            },
        ],
        shadow_pokemon: [
            'phenac_city_battles',
            'snagem_hideout',
        ],
    },
    'Meganium': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Bayleef',
                level: 32,
            },
        ],
        special: [
            Has('Meganium') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Cyndaquil': {
        native_region: 'Johto',
        routes: {
            land: [
                'alola_route_3',
            ],
        },
        egg: 'Fire Egg',
        starter: ['Johto'],
        farm_wandering: ['Occa Berry'],
    },
    'Quilava': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Cyndaquil',
                level: 14,
            },
        ],
        shadow_pokemon: [
            'phenac_city_battles',
            'snagem_hideout',
        ],
    },
    'Typhlosion': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Quilava',
                level: 36,
            },
        ],
        special: [
            Has('Typhlosion') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Hisuian Typhlosion': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Quilava',
                level: 36,
            },
        ],
        starter: ['Hisui'],
    },
    'Totodile': {
        native_region: 'Johto',
        dungeon_boss: [
            ('seaward_cave', 59226690),
        ],
        egg: 'Water Egg',
        starter: ['Johto'],
        farm_wandering: ['Passho Berry'],
    },
    'Croconaw': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Totodile',
                level: 18,
            },
        ],
        shadow_pokemon: [
            'phenac_city_battles',
            'snagem_hideout',
        ],
    },
    'Feraligatr': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Croconaw',
                level: 30,
            },
        ],
        special: [
            Has('Feraligatr') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Sentret': {
        native_region: 'Johto',
        routes: {
            land: [
                'five_isle_meadow',
                'water_path',
                'canyon_entrance',
                'johto_route_29',
                'kalos_route_6',
            ],
        },
        dungeons: [
            'liberty_garden',
        ],
    },
    'Furret': {
        native_region: 'Johto',
        dungeons: [
            'pledge_grove',
        ],
        evolution: [
            {
                prev: 'Sentret',
                level: 15,
            },
        ],
        shadow_pokemon: [
            'pyrite_town_battles',
        ],
    },
    'Hoothoot': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_29',
                'johto_route_30',
                'johto_route_31',
                'johto_route_35',
                'johto_route_36',
                'johto_route_37',
                'sinnoh_route_205',
                'sinnoh_route_210',
                'sinnoh_route_211',
                'galar_route_1',
                'galar_route_2',
                'dappled_grove',
            ],
            headbutt: [
                'johto_route_32',
                'johto_route_34',
                'johto_route_38',
                'johto_route_39',
                'johto_route_43',
                'johto_route_47',
                'johto_route_48',
                'johto_route_26',
                'johto_route_27',
            ],
        },
        dungeons: [
            'sprout_tower',
            'ilex_forest',
            'eterna_forest',
            'lush_jungle',
        ],
        safari: ['Sinnoh'],
    },
    'Noctowl': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_43',
                'johto_route_47',
                'sinnoh_route_210',
                'sinnoh_route_211',
                'kalos_route_20',
                'motostoke_outskirts',
                'motostoke_riverbank',
                'bridge_field',
                'giants_cap',
            ],
        },
        dungeons: [
            'mt_coronet_north',
            'spear_pillar',
            'pokemon_village',
        ],
        dungeon_boss: [
            ('ilex_forest', 340000),
        ],
        evolution: [
            {
                prev: 'Hoothoot',
                level: 20,
            },
        ],
        safari: ['Sinnoh'],
        shadow_pokemon: [
            'pyrite_town_battles',
        ],
    },
    'Ledyba': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_30',
                'johto_route_31',
                'johto_route_37',
                'kalos_route_4',
                'alola_route_1',
            ],
            headbutt: [
                'johto_route_29',
                'johto_route_34',
                'johto_route_35',
                'johto_route_36',
                'johto_route_38',
                'johto_route_39',
                'johto_route_47',
                'johto_route_48',
                'johto_route_26',
                'johto_route_27',
            ],
        },
        dungeons: [
            'pattern_bush',
        ],
        safari: ['Johto'],
        farm_wandering: ['Cheri Berry', 'Leppa Berry', 'Razz Berry', 'Figy Berry', 'Pomeg Berry', 'Tamato Berry', 'Spelon Berry', 'Occa Berry', 'Chople Berry', 'Haban Berry', 'Custap Berry', 'Liechi Berry', 'Lansat Berry'],
        shadow_pokemon: [
            'gateon_port_battles',
        ],
    },
    'Ledian': {
        native_region: 'Johto',
        routes: {
            land: [
                'sinnoh_route_229',
                'alola_route_10',
                'alola_route_11',
                'alola_route_17',
            ],
        },
        dungeons: [
            'pledge_grove',
            'malie_garden',
            'ulaula_meadow',
        ],
        evolution: [
            {
                prev: 'Ledyba',
                level: 18,
            },
        ],
        shadow_pokemon: [
            'the_under',
        ],
    },
    'Spinarak': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_30',
                'johto_route_31',
                'johto_route_37',
                'alola_route_1',
            ],
            headbutt: [
                'johto_route_29',
                'johto_route_34',
                'johto_route_35',
                'johto_route_36',
                'johto_route_38',
                'johto_route_39',
                'johto_route_47',
                'johto_route_48',
                'johto_route_26',
                'johto_route_27',
            ],
        },
        dungeons: [
            'pattern_bush',
        ],
        safari: ['Johto'],
        farm_wandering: ['Kebia Berry'],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Ariados': {
        native_region: 'Johto',
        routes: {
            land: [
                'sinnoh_route_229',
                'alola_route_10',
                'alola_route_11',
                'alola_route_17',
            ],
        },
        dungeons: [
            'sky_pillar',
            'malie_garden',
            'ulaula_meadow',
        ],
        evolution: [
            {
                prev: 'Spinarak',
                level: 22,
            },
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Crobat': {
        native_region: 'Johto',
        routes: {
            land: [
                'icebound_falls',
            ],
        },
        dungeon_boss: [
            ('ancient_wayward_cave', 10000000),
        ],
        evolution: [
            {
                prev: 'Golbat',
                item: 'Soothe Bell',
            },
        ],
    },
    'Chinchou': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_41',
                'sinnoh_route_220',
                'undella_bay',
                'west_lake_axewell',
                'east_lake_axewell',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
            water: [
                'johto_route_47',
                'johto_route_26',
                'johto_route_27',
                'azure_bay',
                'alola_route_8',
                'akala_outskirts',
                'giants_mirror',
            ],
        },
        egg: 'Electric Egg',
    },
    'Lanturn': {
        native_region: 'Johto',
        routes: {
            land: [
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
            water: [
                'johto_route_47',
                'johto_route_26',
                'johto_route_27',
                'bridge_field',
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'sea_spirits_den',
        ],
        evolution: [
            {
                prev: 'Chinchou',
                level: 27,
            },
        ],
    },
    'Pichu': {
        native_region: 'Johto',
        routes: {
            land: [
                'alola_route_1',
                'forest_of_focus',
                'natures_pantry',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'pikachu_valley',
            'floaro_gardens',
        ],
        breeding: ['Pikachu', 'Raichu', 'Alolan Raichu'],
    },
    'Spiky-eared Pichu': {
        native_region: 'Johto',
        special: [
            make_rule('ilex_forest', False) & make_rule('unfinished_business7'),
        ],
    },
    'Cleffa': {
        native_region: 'Johto',
        routes: {
            land: [
                'mount_hokulani',
                'fabled_spring',
            ],
        },
        dungeons: [
            'mt_coronet_south',
        ],
        breeding: ['Clefairy', 'Clefable'],
    },
    'Igglybuff': {
        native_region: 'Johto',
        routes: {
            land: [
                'alola_route_4',
                'alola_route_6',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dream_orbs: ['Blue'],
        breeding: ['Jigglypuff', 'Wigglytuff'],
    },
    'Togepi': {
        native_region: 'Johto',
        routes: {
            land: [
                'bridge_field',
                'cottonsedge_prairie',
                'bathers_lagoon',
                'tranquility_cove',
            ],
        },
        farm_wandering: ['Roseli Berry'],
        shadow_pokemon: [
            'phenac_stadium',
        ],
        shops: [
            ('violet_city', 'questPoint'),
        ],
        breeding: ['Togetic', 'Togekiss'],
    },
    'Spooky Togepi': {
        native_region: 'Johto',
        breeding: ['Spooky Togetic', 'Spooky Togekiss'],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_29'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_30'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_31'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_32'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_33'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_34'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_35'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_36'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_37'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_38'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_39'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_40'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_41'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_42'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_43'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_44'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_45'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_46'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_47'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_48'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_26'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_27'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_28'),
        ],
    },
    'Togepi (Flowering Crown)': {
        native_region: 'Johto',
        special: [
            {
                dungeon: 'ruins_of_alph',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('ruins_of_alph', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Togepi (Flowering Crown)',
                            '0',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'slowpoke_well',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('slowpoke_well', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Togepi (Flowering Crown)',
                            '1',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'ilex_forest',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('ilex_forest', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Togepi (Flowering Crown)',
                            '2',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'tin_tower',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('tin_tower', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Togepi (Flowering Crown)',
                            '4',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'whirl_islands',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('whirl_islands', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Togepi (Flowering Crown)',
                            '3',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'ice_path',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('ice_path', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Togepi (Flowering Crown)',
                            '5',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
        ],
    },
    'Togetic': {
        native_region: 'Johto',
        routes: {
            land: [
                'stony_wilderness',
                'tranquility_cove',
            ],
        },
        evolution: [
            {
                prev: 'Togepi',
                item: 'Soothe Bell',
            },
        ],
        shadow_pokemon: [
            'under_colosseum',
        ],
    },
    'Spooky Togetic': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Spooky Togepi',
                item: 'Soothe Bell',
            },
        ],
    },
    'Natu': {
        native_region: 'Johto',
        routes: {
            land: [
                'ruin_valley',
                'akala_outskirts',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'giants_mirror',
            ],
            headbutt: [
                'johto_route_28',
            ],
        },
        dungeons: [
            'ruins_of_alph',
            'solaceon_ruins',
        ],
        farm_wandering: ['Payapa Berry'],
        shadow_pokemon: [
            'phenac_city_battles',
        ],
    },
    'Xatu': {
        native_region: 'Johto',
        routes: {
            land: [
                'east_lake_axewell',
                'giants_seat',
                'north_lake_miloch',
                'giants_mirror',
            ],
        },
        evolution: [
            {
                prev: 'Natu',
                level: 25,
            },
        ],
    },
    'Mareep': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_32',
                'johto_route_42',
                'johto_route_43',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'altering_cave',
            'floccesy_ranch',
            'paniola_ranch',
        ],
        egg: 'Electric Egg',
        shadow_pokemon: [
            'cipher_lab',
            'phenac_stadium',
        ],
    },
    'Flaaffy': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_42',
                'johto_route_43',
            ],
        },
        evolution: [
            {
                prev: 'Mareep',
                level: 15,
            },
        ],
        shadow_pokemon: [
            'pyrite_town_battles',
        ],
    },
    'Ampharos': {
        native_region: 'Johto',
        dungeons: [
            'ruins_of_conflict',
        ],
        evolution: [
            {
                prev: 'Flaaffy',
                level: 30,
            },
        ],
    },
    'Mega Ampharos': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Ampharos',
                item: 'Ampharosite',
            },
        ],
    },
    'Bellossom': {
        native_region: 'Johto',
        routes: {
            land: [
                'giants_mirror',
            ],
        },
        evolution: [
            {
                prev: 'Gloom',
                item: 'Sun Stone',
            },
        ],
    },
    'Marill': {
        native_region: 'Johto',
        routes: {
            land: [
                'ruin_valley',
                'hoenn_route_104',
                'hoenn_route_112',
                'hoenn_route_117',
                'hoenn_route_120',
                'sinnoh_route_215',
                'sinnoh_route_212',
                'unova_route_6',
                'unova_route_11',
                'unova_route_22',
                'fields_of_honor',
                'soothing_wetlands',
                'challenge_beach',
            ],
            water: [
                'hoenn_route_102',
                'hoenn_route_111',
                'hoenn_route_114',
                'kalos_route_3',
            ],
        },
        dungeons: [
            'icefall_cave',
            'mt_mortar',
            'abundant_shrine',
            'victory_road_unova',
            'pinwheel_forest',
        ],
        evolution: [
            {
                prev: 'Azurill',
                item: 'Soothe Bell',
            },
        ],
        egg: 'Water Egg',
        special: [
            make_rule('brooklet_hill', False),
        ],
    },
    'Azumarill': {
        native_region: 'Johto',
        routes: {
            land: [
                'kalos_route_22',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
            ],
        },
        dungeons: [
            'abundant_shrine',
        ],
        dungeon_boss: [
            ('ruins_of_hope', 82177450),
        ],
        evolution: [
            {
                prev: 'Marill',
                level: 18,
            },
        ],
    },
    'Sudowoodo': {
        native_region: 'Johto',
        routes: {
            land: [
                'sinnoh_route_221',
                'motostoke_outskirts',
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'pledge_grove',
        ],
        dungeon_boss: [
            ('celestica_ruins', 10000000),
        ],
        evolution: [
            {
                prev: 'Bonsly',
                level: 32,
            },
        ],
        farm_wandering: ['Charti Berry'],
        shadow_pokemon: [
            'pyrite_cave',
        ],
        temporary_battle: [
            'sudowoodo',
        ],
    },
    'Sudowoodo (Golden)': {
        native_region: 'Johto',
        shops: [
            ('national_park', 'contestToken'),
        ],
    },
    'Politoed': {
        native_region: 'Johto',
        routes: {
            land: [
                'soothing_wetlands',
            ],
            water: [
                'kalos_route_19',
            ],
        },
        dungeon_boss: [
            ('pledge_grove', 50000000),
        ],
        evolution: [
            {
                prev: 'Poliwhirl',
                item: 'Kings Rock',
            },
        ],
    },
    'Hoppip': {
        native_region: 'Johto',
        routes: {
            land: [
                'five_isle_meadow',
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'johto_route_32',
                'johto_route_33',
                'johto_route_48',
                'oasis_poke_spot',
                'poco_path',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'sunburst_island',
        ],
        egg: 'Grass Egg',
    },
    'Hoppip (Chimecho)': {
        native_region: 'Johto',
        shops: [
            ('wind_chime_shop', 'diamond'),
        ],
    },
    'Skiploom': {
        native_region: 'Johto',
        dungeons: [
            'flower_paradise',
        ],
        evolution: [
            {
                prev: 'Hoppip',
                level: 18,
            },
        ],
        shadow_pokemon: [
            'pyrite_town_battles',
        ],
    },
    'Jumpluff': {
        native_region: 'Johto',
        dungeons: [
            'flower_paradise',
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Skiploom',
                level: 27,
            },
        ],
    },
    'Aipom': {
        native_region: 'Johto',
        routes: {
            land: [
                'ramanas_island',
                'aipom_hill',
                'hideaway_bay',
                'whiteout_valley',
                'bonechill_wastes',
                'arenas_approach',
                'avalanche_slopes',
                'hearts_crag',
                'snowfall_hot_spring',
                'glacier_terrace',
            ],
            headbutt: [
                'johto_route_31',
                'johto_route_33',
                'johto_route_42',
                'johto_route_44',
                'johto_route_45',
                'johto_route_46',
                'johto_route_28',
            ],
        },
        dungeons: [
            'altering_cave',
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Sunkern': {
        native_region: 'Johto',
        routes: {
            land: [
                'unova_route_20',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'liberty_garden',
            'lake_of_the_sunne_and_moone',
        ],
        egg: 'Grass Egg',
        special: [
            Has('Sunkern') & Has('Elite Johto Champion Badge') & make_rule('kanto_route_24'),
        ],
    },
    'Sunflora': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Sunkern',
                item: 'Sun Stone',
            },
        ],
        shadow_pokemon: [
            'realgam_tower_battles',
        ],
    },
    'Yanma': {
        native_region: 'Johto',
        routes: {
            land: [
                'ruin_valley',
                'johto_route_35',
                'unova_route_3',
                'droning_meadow',
                'gapejaw_bog',
                'ursas_ring',
                'heavenward_lookout',
            ],
        },
        dungeons: [
            'pinwheel_forest',
            'ancient_solaceon_ruins',
        ],
        egg: 'Mystery Egg',
        safari: ['Johto', 'Sinnoh'],
        shadow_pokemon: [
            'pyrite_building',
        ],
    },
    'Wooper': {
        native_region: 'Johto',
        routes: {
            land: [
                'ruin_valley',
                'johto_route_32',
                'cave_poke_spot',
                'west_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
            ],
            water: [
                'soothing_wetlands',
            ],
        },
        dungeons: [
            'icefall_cave',
            'ruins_of_alph',
            'union_cave',
        ],
        egg: 'Water Egg',
        safari: ['Sinnoh'],
    },
    'Paldean Wooper': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_one',
            ],
        },
    },
    'Quagsire': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_26',
                'johto_route_27',
                'sinnoh_route_212',
                'kalos_route_14',
                'kalos_route_19',
                'west_lake_axewell',
                'giants_seat',
                'giants_cap',
                'lake_of_outrage',
                'soothing_wetlands',
            ],
            water: [
                'johto_route_32',
            ],
        },
        dungeons: [
            'ruins_of_alph',
            'mt_silver',
        ],
        evolution: [
            {
                prev: 'Wooper',
                level: 20,
            },
        ],
        safari: ['Sinnoh'],
        shadow_pokemon: [
            'pyrite_town_battles',
        ],
    },
    'Espeon': {
        native_region: 'Johto',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                item: 'Soothe Bell',
                time: 'day',
            },
        ],
    },
    'Umbreon': {
        native_region: 'Johto',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                item: 'Soothe Bell',
                time: 'night',
            },
        ],
    },
    'Murkrow': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_28',
                'cloudpool_ridge',
                'crossing_slope',
                'ginkgo_landing',
                'aipom_hill',
                'bathers_lagoon',
                'hideaway_bay',
                'castaway_shore',
                'islespy_shore',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'lost_cave',
            'veilstone_cape',
        ],
        farm_wandering: ['Coba Berry'],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Slowking': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Slowpoke',
                item: 'Kings Rock',
            },
        ],
    },
    'Galarian Slowking': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Galarian Slowpoke',
                item: 'Galarica Wreath',
            },
        ],
    },
    'Misdreavus': {
        native_region: 'Johto',
        routes: {
            land: [
                'stonetooth_rows',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'lost_cave',
            'mt_silver',
            'celestial_tower',
            'hauoli_cemetery',
            'poni_meadow',
            'celestica_ruins',
            'sacred_plaza',
            'ice_column_chamber',
            'icepeak_cavern',
        ],
        farm_wandering: ['Kasib Berry'],
        shadow_pokemon: [
            'pyrite_town_battles',
        ],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_29'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_30'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_31'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_32'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_33'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_34'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_35'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_36'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_37'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_38'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_39'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_40'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_41'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_42'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_43'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_44'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_45'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_46'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_47'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_48'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_26'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_27'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('johto_route_28'),
        ],
    },
    'Unown (A)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (B)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (C)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (D)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (E)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (F)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('ruins_of_alph', 280000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (G)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (H)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('ruins_of_alph', 280000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (I)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (J)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (K)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (L)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (M)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (N)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (O)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (P)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('ruins_of_alph', 280000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (Q)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (R)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (S)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (T)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (U)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (V)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (W)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (X)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (Y)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (Z)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ruins_of_alph', 280000),
            ('solaceon_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (!)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Unown (?)': {
        native_region: 'Johto',
        dungeon_boss: [
            ('tanoby_ruins', 4100000),
            ('ancient_solaceon_ruins', 4100000),
        ],
    },
    'Wobbuffet': {
        native_region: 'Johto',
        routes: {
            land: [
                'ruin_valley',
                'galar_route_5',
                'motostoke_riverbank',
                'bridge_field',
                'lake_of_outrage',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'dark_cave',
            'reflection_cave',
        ],
        dungeon_boss: [
            ('ruins_of_life', 82177450),
        ],
        evolution: [
            {
                prev: 'Wynaut',
                level: 15,
            },
        ],
    },
    'Girafarig': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_43',
                'johto_route_48',
                'sinnoh_route_221',
            ],
        },
        dungeons: [
            'area_zero',
        ],
        farm_wandering: ['Chilan Berry'],
    },
    'Pineco': {
        native_region: 'Johto',
        routes: {
            headbutt: [
                'johto_route_29',
                'johto_route_30',
                'johto_route_31',
                'johto_route_32',
                'johto_route_34',
                'johto_route_35',
                'johto_route_36',
                'johto_route_37',
                'johto_route_38',
                'johto_route_39',
                'johto_route_43',
                'johto_route_47',
                'johto_route_48',
                'johto_route_26',
                'johto_route_27',
            ],
        },
        dungeons: [
            'altering_cave',
        ],
        safari: ['Johto'],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        shadow_pokemon: [
            'phenac_city_battles',
        ],
    },
    'Forretress': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Pineco',
                level: 31,
            },
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Dunsparce': {
        native_region: 'Johto',
        routes: {
            land: [
                'kalos_route_3',
                'kalos_route_22',
                'soothing_wetlands',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'area_zero_depths',
        ],
        dungeon_boss: [
            ('dark_cave', 460000),
            ('dreamyard', 48000000),
        ],
        shadow_pokemon: [
            'pyrite_cave',
        ],
    },
    'Gligar': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_45',
                'rock_poke_spot',
                'sinnoh_route_206',
                'unova_route_11',
                'unova_route_23',
                'unova_route_15',
                'arenas_approach',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'primeval_grotto',
            'clamberclaw_cliffs',
            'celestica_ruins',
        ],
        shadow_pokemon: [
            'the_under',
        ],
    },
    'Steelix': {
        native_region: 'Johto',
        routes: {
            land: [
                'giants_seat',
                'giants_mirror',
                'celestica_trail',
            ],
        },
        dungeons: [
            'iron_island',
            'energy_plant',
        ],
        dungeon_boss: [
            ('victory_road_sinnoh', 7000000),
            ('snowpoint_temple', 10000000),
        ],
        evolution: [
            {
                prev: 'Onix',
                item: 'Metal Coat',
            },
        ],
    },
    'Mega Steelix': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Steelix',
                item: 'Steelixite',
            },
        ],
    },
    'Crystal Steelix': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Crystal Onix',
                item: 'Ice Stone',
            },
        ],
    },
    'Snubbull': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_38',
                'kalos_route_10',
            ],
        },
    },
    'Granbull': {
        native_region: 'Johto',
        routes: {
            land: [
                'poni_wilds',
                'ancient_poni_path',
                'poni_gauntlet',
            ],
        },
        dungeon_boss: [
            ('ruins_of_conflict', 82177450),
            ('ruins_of_life', 82177450),
            ('ruins_of_abundance', 82177450),
            ('ruins_of_hope', 82177450),
        ],
        evolution: [
            {
                prev: 'Snubbull',
                level: 23,
            },
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Qwilfish': {
        native_region: 'Johto',
        routes: {
            land: [
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
            ],
            water: [
                'five_isle_meadow',
                'water_path',
                'johto_route_32',
                'bridge_field',
                'lake_of_outrage',
                'galar_route_9',
            ],
        },
        dungeons: [
            'sunburst_island',
            'tanoby_ruins',
            'dusty_bowl',
        ],
        egg: 'Water Egg',
        shadow_pokemon: [
            'pyrite_building',
        ],
    },
    'Hisuian Qwilfish': {
        native_region: 'Hisui',
        routes: {
            land: [
                'lunkers_lair',
            ],
            water: [
                'tranquility_cove',
            ],
        },
    },
    'Scizor': {
        native_region: 'Johto',
        routes: {
            land: [
                'training_lowlands',
                'challenge_road',
            ],
        },
        evolution: [
            {
                prev: 'Scyther',
                item: 'Metal Coat',
            },
        ],
        shadow_pokemon: [
            'phenac_stadium',
        ],
    },
    'Mega Scizor': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Scizor',
                item: 'Scizorite',
            },
        ],
    },
    'Shuckle': {
        native_region: 'Johto',
        routes: {
            land: [
                'watchtower_ruins',
                'stony_wilderness',
                'giants_cap',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'altering_cave',
            'galar_mine_no_2',
        ],
        dungeon_boss: [
            ('burned_tower', 610000),
        ],
        safari: ['Johto', 'Kalos'],
        farm_wandering: ['Tanga Berry'],
        shadow_pokemon: [
            'deep_colosseum',
        ],
        dream_orbs: ['Pink'],
    },
    'Shuckle (Corked)': {
        native_region: 'Johto',
        farm_wandering: ['Tanga Berry'],
    },
    'Heracross': {
        native_region: 'Johto',
        routes: {
            land: [
                'unova_route_12',
                'kalos_route_12',
                'poni_grove',
                'forest_of_focus',
                'training_lowlands',
                'challenge_road',
                'gruelling_grove',
                'wayward_wood',
            ],
            headbutt: [
                'johto_route_31',
                'johto_route_33',
                'johto_route_42',
                'johto_route_44',
                'johto_route_45',
                'johto_route_46',
                'johto_route_47',
                'johto_route_28',
                'sonorous_path',
            ],
        },
        dungeon_boss: [
            ('pattern_bush', 3703000),
            ('lostlorn_forest', 18000000),
        ],
        egg: 'Fighting Egg',
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        shadow_pokemon: [
            'realgam_tower_battles',
        ],
    },
    'Mega Heracross': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Heracross',
                item: 'Heracronite',
            },
        ],
    },
    'Sneasel': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_28',
                'sinnoh_route_216',
                'sinnoh_route_217',
                'kalos_route_17',
                'motostoke_riverbank',
                'bridge_field',
                'stony_wilderness',
                'giants_cap',
                'hammerlocke_hills',
                'steamdrift_way',
                'galar_route_10',
                'slippery_slope',
                'frostpoint_field',
                'frigid_sea',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'icefall_cave',
            'mt_silver',
            'lake_acuity',
            'newmoon_island',
            'snowpoint_temple',
            'giant_chasm',
            'mount_lanakila',
            'glaseado_mountain',
            'area_zero',
        ],
        shadow_pokemon: [
            'the_under',
        ],
    },
    'Hisuian Sneasel': {
        native_region: 'Hisui',
        routes: {
            land: [
                'celestica_trail',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'avaluggs_legacy',
        ],
        dungeon_boss: [
            ('primeval_grotto', 10000000),
        ],
    },
    'Teddiursa': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_45',
                'ursas_ring',
                'sonorous_path',
            ],
        },
        dungeons: [
            'altering_cave',
            'mt_silver',
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Ursaring': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_28',
                'kalos_route_21',
                'ursas_ring',
                'sonorous_path',
            ],
        },
        dungeons: [
            'mt_silver',
            'glaseado_mountain',
        ],
        evolution: [
            {
                prev: 'Teddiursa',
                level: 30,
            },
        ],
        shadow_pokemon: [
            'snagem_hideout',
        ],
    },
    'Slugma': {
        native_region: 'Johto',
        routes: {
            land: [
                'hoenn_route_113',
            ],
        },
        dungeons: [
            'ruby_path',
            'fiery_path',
            'stark_mountain',
        ],
        egg: 'Fire Egg',
        shadow_pokemon: [
            'pyrite_town_battles',
        ],
        special: [
            Has('Slugma') & Has('Elite Johto Champion Badge') & make_rule('kanto_route_16'),
            Has('Slugma') & Has('Elite Johto Champion Badge') & make_rule('kanto_route_17'),
            Has('Slugma') & Has('Elite Johto Champion Badge') & make_rule('kanto_route_18'),
        ],
    },
    'Magcargo': {
        native_region: 'Johto',
        dungeons: [
            'stark_mountain',
        ],
        dungeon_boss: [
            ('ruby_path', 3703000),
        ],
        evolution: [
            {
                prev: 'Slugma',
                level: 38,
            },
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Swinub': {
        native_region: 'Johto',
        routes: {
            land: [
                'sinnoh_route_217',
                'rolling_fields',
                'giants_seat',
                'giants_mirror',
                'slippery_slope',
                'bonechill_wastes',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'icefall_cave',
            'ice_path',
            'avaluggs_legacy',
        ],
        farm_wandering: ['Yache Berry'],
        shadow_pokemon: [
            'phenac_city_battles',
        ],
    },
    'Piloswine': {
        native_region: 'Johto',
        routes: {
            land: [
                'rolling_fields',
                'east_lake_axewell',
                'lake_of_outrage',
                'slippery_slope',
                'bonechill_wastes',
                'arenas_approach',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'giant_chasm',
            'frost_cavern',
            'roaring_sea_caves',
            'avaluggs_legacy',
        ],
        evolution: [
            {
                prev: 'Swinub',
                level: 33,
            },
        ],
        shadow_pokemon: [
            'the_under',
        ],
    },
    'Corsola': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_40',
                'hoenn_route_128',
                'melemele_sea',
                'alola_route_9',
            ],
            water: [
                'johto_route_34',
            ],
        },
    },
    'Galarian Corsola': {
        native_region: 'Galar',
        routes: {
            land: [
                'giants_mirror',
            ],
        },
    },
    'Remoraid': {
        native_region: 'Johto',
        routes: {
            land: [
                'memorial_pillar',
                'water_labyrinth',
                'resort_gorgeous',
                'green_path',
                'outcast_island',
                'sinnoh_route_223',
                'undella_bay',
                'unova_route_21',
                'melemele_sea',
            ],
            water: [
                'five_isle_meadow',
                'water_path',
                'johto_route_44',
                'sinnoh_route_213',
                'sinnoh_route_212',
                'sinnoh_route_222',
                'sinnoh_route_224',
                'sinnoh_route_230',
                'kalos_route_12',
                'azure_bay',
                'kalae_bay',
                'alola_route_8',
                'west_lake_axewell',
                'south_lake_miloch',
                'circhester_bay',
                'fields_of_honor',
                'workout_sea',
                'hideaway_bay',
                'sands_reach',
                'tranquility_cove',
            ],
        },
        dungeons: [
            'sunburst_island',
            'tanoby_ruins',
        ],
        shadow_pokemon: [
            'pyrite_building',
        ],
    },
    'Octillery': {
        native_region: 'Johto',
        routes: {
            land: [
                'sinnoh_route_223',
                'south_lake_miloch',
                'galar_route_9',
                'circhester_bay',
                'challenge_beach',
                'castaway_shore',
            ],
            water: [
                'sinnoh_route_213',
                'sinnoh_route_212',
                'sinnoh_route_222',
                'sinnoh_route_224',
                'sinnoh_route_230',
                'axews_eye',
                'fields_of_honor',
                'workout_sea',
            ],
        },
        dungeons: [
            'seaside_hollow',
        ],
        evolution: [
            {
                prev: 'Remoraid',
                level: 25,
            },
        ],
    },
    'Delibird': {
        native_region: 'Johto',
        routes: {
            land: [
                'unova_route_22',
                'kalos_route_17',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'axews_eye',
                'watchtower_ruins',
                'giants_mirror',
                'giants_cap',
                'steamdrift_way',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'icefall_cave',
            'giant_chasm',
            'iceberg_ruins',
            'glaseado_mountain',
        ],
        dungeon_boss: [
            ('ice_path', 440000),
            ('seaward_cave', 59226690),
        ],
        shadow_pokemon: [
            'realgam_tower_battles',
        ],
    },
    'Mantine': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_41',
            ],
            water: [
                'lake_of_outrage',
                'circhester_bay',
                'tranquility_cove',
            ],
        },
        dungeons: [
            'tanoby_ruins',
        ],
        shadow_pokemon: [
            'pyrite_building',
        ],
    },
    'Skarmory': {
        native_region: 'Johto',
        routes: {
            land: [
                'sevault_canyon',
                'johto_route_45',
                'hoenn_route_113',
                'sinnoh_route_227',
                'alola_route_10',
                'mount_hokulani',
                'training_lowlands',
                'challenge_road',
            ],
        },
        dungeons: [
            'reversal_mountain',
            'hokulani_observatory',
            'vast_poni_canyon',
        ],
        dungeon_boss: [
            ('stark_mountain', 10000000),
        ],
        farm_wandering: ['Babiri Berry'],
        shadow_pokemon: [
            'realgam_tower_battles',
            'snagem_hideout',
        ],
    },
    'Houndour': {
        native_region: 'Johto',
        routes: {
            land: [
                'sinnoh_route_214',
                'kalos_route_10',
            ],
        },
        dungeons: [
            'altering_cave',
            'inlet_grotto',
        ],
        egg: 'Fire Egg',
        farm_wandering: ['Colbur Berry'],
        shadow_pokemon: [
            'cipher_lab',
        ],
        special: [
            Has('Houndour') & Has('Elite Johto Champion Badge') & make_rule('kanto_route_7'),
        ],
    },
    'Houndoom': {
        native_region: 'Johto',
        routes: {
            land: [
                'alola_route_12',
            ],
        },
        dungeons: [
            'firescourge_shrine',
        ],
        dungeon_boss: [
            ('inlet_grotto', 161099869),
        ],
        evolution: [
            {
                prev: 'Houndour',
                level: 24,
            },
        ],
        shadow_pokemon: [
            'realgam_colosseum',
        ],
    },
    'Mega Houndoom': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Houndoom',
                item: 'Houndoominite',
            },
        ],
    },
    'Kingdra': {
        native_region: 'Johto',
        routes: {
            land: [
                'honeycalm_sea',
            ],
        },
        evolution: [
            {
                prev: 'Seadra',
                item: 'Dragon Scale',
            },
        ],
    },
    'Phanpy': {
        native_region: 'Johto',
        routes: {
            land: [
                'canyon_entrance',
                'sevault_canyon',
                'johto_route_45',
                'oasis_poke_spot',
            ],
        },
        dungeons: [
            'mt_silver',
            'area_zero',
        ],
    },
    'Donphan': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_28',
            ],
        },
        dungeons: [
            'mt_silver',
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Phanpy',
                level: 25,
            },
        ],
    },
    'Porygon2': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Porygon',
                item: 'Upgrade',
            },
        ],
    },
    'Stantler': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_36',
                'johto_route_37',
                'deertrack_heights',
                'windbreak_stand',
                'wayward_wood',
            ],
        },
        dungeons: [
            'pledge_grove',
        ],
        dungeon_boss: [
            ('altering_cave', 3703000),
        ],
        egg: 'Mystery Egg',
        shadow_pokemon: [
            'the_under',
        ],
    },
    'Reindeer Stantler': {
        native_region: 'Johto',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Johto'),
        ],
    },
    'Smeargle': {
        native_region: 'Johto',
        routes: {
            land: [
                'kalos_route_7',
                'alola_route_2',
            ],
        },
        dungeons: [
            'ruins_of_alph',
        ],
        dungeon_boss: [
            ('altering_cave', 3703000),
        ],
        shadow_pokemon: [
            'snagem_hideout',
        ],
    },
    'Tyrogue': {
        native_region: 'Johto',
        routes: {
            land: [
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'galar_route_3',
                'stony_wilderness',
            ],
        },
        egg: 'Fighting Egg',
        breeding: ['Hitmonlee', 'Hitmonchan', 'Hitmontop'],
        special: [
            make_rule('mt_mortar', True, 420000),
        ],
    },
    'Hitmontop': {
        native_region: 'Johto',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        evolution: [
            {
                prev: 'Tyrogue',
                level: 20,
            },
        ],
        shadow_pokemon: [
            'relic_cave',
        ],
    },
    'Smoochum': {
        native_region: 'Johto',
        routes: {
            land: [
                'slippery_slope',
                'frostpoint_field',
            ],
        },
        dungeons: [
            'snowpoint_temple',
            'frost_cavern',
            'seaward_cave',
        ],
        dream_orbs: ['Blue'],
        breeding: ['Jynx'],
    },
    'Elekid': {
        native_region: 'Johto',
        routes: {
            land: [
                'mount_hokulani',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'cloudcap_pass',
                'arenas_approach',
                'icebound_falls',
            ],
        },
        dungeons: [
            'hokulani_observatory',
        ],
        egg: 'Electric Egg',
        breeding: ['Electabuzz', 'Electivire'],
    },
    'Magby': {
        native_region: 'Johto',
        routes: {
            land: [
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'wela_volcano_park',
            'firespit_island',
        ],
        egg: 'Fire Egg',
        breeding: ['Magmar', 'Magmortar'],
    },
    'Miltank': {
        native_region: 'Johto',
        routes: {
            land: [
                'johto_route_38',
                'johto_route_39',
                'johto_route_47',
                'kalos_route_12',
                'poni_plains',
                'training_lowlands',
            ],
        },
        dungeon_boss: [
            ('paniola_ranch', 30278320),
        ],
        shadow_pokemon: [
            'realgam_colosseum',
        ],
    },
    'Blissey': {
        native_region: 'Johto',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'potbottom_desert',
                'challenge_road',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_island',
                'avalanche_slopes',
            ],
        },
        dungeon_boss: [
            ('hall_of_origin', 10000000),
        ],
        evolution: [
            {
                prev: 'Chansey',
                item: 'Soothe Bell',
            },
        ],
    },
    'Blessing Blissey': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Charity Chansey',
                item: 'Soothe Bell',
            },
        ],
    },
    'Raikou': {
        native_region: 'Johto',
        shadow_pokemon: [
            'cipher_lab',
        ],
        special: [
            make_rule('roamer', 'Kanto - Sevii Islands') & make_rule('completed_celios_errand'),
            make_rule('roamer', 'Johto') & make_rule('the_legendary_beasts3'),
        ],
    },
    'Entei': {
        native_region: 'Johto',
        shadow_pokemon: [
            'mt_battle',
        ],
        special: [
            make_rule('roamer', 'Kanto - Sevii Islands') & make_rule('completed_celios_errand'),
            make_rule('roamer', 'Johto') & make_rule('the_legendary_beasts3'),
        ],
    },
    'Suicune': {
        native_region: 'Johto',
        shadow_pokemon: [
            'the_under',
        ],
        temporary_battle: [
            'suicune6',
        ],
        special: [
            Has('Suicune') & make_rule('roamer', 'Kanto - Sevii Islands') & make_rule('completed_celios_errand'),
        ],
    },
    'Larvitar': {
        native_region: 'Johto',
        routes: {
            land: [
                'sevault_canyon',
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'terminus_cave',
            'roaring_sea_caves',
        ],
        dungeon_boss: [
            ('mt_silver', 840000),
            ('digletts_tunnel', 66079195),
        ],
        farm_wandering: ['Shuca Berry'],
    },
    'Pupitar': {
        native_region: 'Johto',
        routes: {
            land: [
                'unova_route_15',
                'kalos_route_18',
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'terminus_cave',
        ],
        evolution: [
            {
                prev: 'Larvitar',
                level: 30,
            },
        ],
    },
    'Tyranitar': {
        native_region: 'Johto',
        dungeon_boss: [
            ('dusty_bowl', 114616050),
            ('roaring_sea_caves', 160924440),
        ],
        evolution: [
            {
                prev: 'Pupitar',
                level: 55,
            },
        ],
        shadow_pokemon: [
            'realgam_colosseum',
        ],
    },
    'Mega Tyranitar': {
        native_region: 'Johto',
        evolution: [
            {
                prev: 'Tyranitar',
                item: 'Tyranitarite',
            },
        ],
    },
    'Lugia': {
        native_region: 'Johto',
        dungeon_boss: [
            ('sea_spirits_den', 92375000),
        ],
        special: [
            make_rule('whirl_guardian9') & make_rule('whirl_islands', True, 1410000),
        ],
    },
    'XD001': {
        native_region: 'Johto',
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Ho-Oh': {
        native_region: 'Johto',
        special: [
            make_rule('rainbow_guardian1') & make_rule('tin_tower', True, 1410000),
            make_rule('roamer', 'Hoenn - Orre') & make_rule('completed_shadows_in_the_desert'),
        ],
    },
    'Celebi': {
        native_region: 'Johto',
        special: [
            make_rule('unfinished_business12') & make_rule('ilex_forest', True, 800000),
        ],
    },
    'Flowering Celebi': {
        native_region: 'Johto',
        special: [
            make_rule('glimwood_tangle', False) & make_rule('secrets_of_the_jungle13'),
        ],
    },
    'Grinch Celebi': {
        native_region: 'Johto',
        special: [
            Has('Elite Johto Champion Badge') & make_rule('has_script', "Infinite Seasonal Events") & make_rule('ilex_forest', True, 1600000),
        ],
    },
    'Treecko': {
        native_region: 'Hoenn',
        egg: 'Grass Egg',
        starter: ['Hoenn'],
        farm_wandering: ['Rindo Berry'],
    },
    'Grovyle': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'alola_route_5',
            ],
        },
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Treecko',
                level: 16,
            },
        ],
    },
    'Sceptile': {
        native_region: 'Hoenn',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Grovyle',
                level: 36,
            },
        ],
    },
    'Mega Sceptile': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Sceptile',
                item: 'Sceptilite',
            },
        ],
    },
    'Torchic': {
        native_region: 'Hoenn',
        egg: 'Fire Egg',
        starter: ['Hoenn'],
        farm_wandering: ['Occa Berry'],
    },
    'Torchic (Egg)': {
        native_region: 'Hoenn',
        special: [
            {
                dungeon: 'petalburg_woods',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('petalburg_woods', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Torchic (Egg)',
                            '0',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'rusturf_tunnel',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('rusturf_tunnel', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Torchic (Egg)',
                            '1',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'meteor_falls',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('meteor_falls', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Torchic (Egg)',
                            '2',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'new_mauville',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('new_mauville', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Torchic (Egg)',
                            '3',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'sky_pillar',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('sky_pillar', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Torchic (Egg)',
                            '5',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'sealed_chamber',
                rule: make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_egg_hunt') & make_rule('sealed_chamber', True, 2700000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Torchic (Egg)',
                            '4',
                            '6',
                            '1',
                        ],
                    },
                ],
            },
        ],
    },
    'Combusken': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'alola_route_8',
            ],
        },
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Torchic',
                level: 16,
            },
        ],
    },
    'Blaziken': {
        native_region: 'Hoenn',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Combusken',
                level: 36,
            },
        ],
    },
    'Mega Blaziken': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Blaziken',
                item: 'Blazikenite',
            },
        ],
    },
    'Mudkip': {
        native_region: 'Hoenn',
        egg: 'Water Egg',
        starter: ['Hoenn'],
        farm_wandering: ['Passho Berry'],
    },
    'Marshtomp': {
        native_region: 'Hoenn',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Mudkip',
                level: 16,
            },
        ],
        special: [
            make_rule('brooklet_hill', False),
        ],
    },
    'Swampert': {
        native_region: 'Hoenn',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Marshtomp',
                level: 36,
            },
        ],
    },
    'Mega Swampert': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Swampert',
                item: 'Swampertite',
            },
        ],
    },
    'Poochyena': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_101',
                'hoenn_route_102',
                'hoenn_route_103',
                'hoenn_route_104',
                'hoenn_route_110',
                'hoenn_route_116',
                'hoenn_route_117',
                'hoenn_route_120',
                'hoenn_route_121',
                'hoenn_route_123',
            ],
        },
        dungeons: [
            'petalburg_woods',
        ],
        shadow_pokemon: [
            'gateon_port_battles',
        ],
    },
    'Mightyena': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_120',
                'hoenn_route_121',
                'hoenn_route_123',
                'kalos_route_15',
            ],
        },
        evolution: [
            {
                prev: 'Poochyena',
                level: 18,
            },
        ],
    },
    'Zigzagoon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_101',
                'hoenn_route_102',
                'hoenn_route_103',
                'hoenn_route_118',
                'hoenn_route_119',
                'kalos_route_2',
            ],
        },
    },
    'Galarian Zigzagoon': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_2',
                'galar_route_3',
                'bridge_field',
                'stony_wilderness',
                'galar_route_2_lakeside',
            ],
        },
    },
    'Linoone': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_118',
                'hoenn_route_119',
            ],
        },
        evolution: [
            {
                prev: 'Zigzagoon',
                level: 20,
            },
        ],
    },
    'Galarian Linoone': {
        native_region: 'Galar',
        routes: {
            land: [
                'bridge_field',
                'giants_cap',
                'giants_bed',
                'ballimere_lake',
            ],
        },
        evolution: [
            {
                prev: 'Galarian Zigzagoon',
                level: 20,
            },
        ],
    },
    'Wurmple': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_101',
                'hoenn_route_102',
                'hoenn_route_104',
                'sinnoh_route_204',
                'sinnoh_route_205',
                'horseshoe_plains',
            ],
        },
        dungeons: [
            'petalburg_woods',
            'eterna_forest',
            'floaro_gardens',
            'heartwood',
        ],
        special: [
            Has('Wurmple') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Silcoon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_205',
                'horseshoe_plains',
            ],
        },
        dungeons: [
            'petalburg_woods',
            'eterna_forest',
            'floaro_gardens',
            'heartwood',
        ],
        evolution: [
            {
                prev: 'Wurmple',
                level: 7,
            },
        ],
        special: [
            Has('Silcoon') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Beautifly': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_205',
                'sinnoh_route_224',
                'sinnoh_route_229',
                'gruelling_grove',
                'bathers_lagoon',
            ],
        },
        dungeon_boss: [
            ('eterna_forest', 3950000),
            ('floaro_gardens', 10000000),
            ('heartwood', 10000000),
            ('veilstone_cape', 10000000),
        ],
        evolution: [
            {
                prev: 'Silcoon',
                level: 10,
            },
        ],
        special: [
            Has('Beautifly') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Cascoon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_205',
                'horseshoe_plains',
            ],
        },
        dungeons: [
            'petalburg_woods',
            'eterna_forest',
            'floaro_gardens',
            'heartwood',
        ],
        evolution: [
            {
                prev: 'Wurmple',
                level: 7,
            },
        ],
        special: [
            Has('Cascoon') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Dustox': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_205',
                'sinnoh_route_224',
                'sinnoh_route_229',
                'gruelling_grove',
                'bathers_lagoon',
            ],
        },
        dungeon_boss: [
            ('eterna_forest', 3950000),
            ('floaro_gardens', 10000000),
            ('heartwood', 10000000),
            ('veilstone_cape', 10000000),
        ],
        evolution: [
            {
                prev: 'Cascoon',
                level: 10,
            },
        ],
        special: [
            Has('Dustox') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Lotad': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_102',
                'hoenn_route_114',
                'galar_route_2',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'galar_route_2_lakeside',
            ],
        },
    },
    'Lombre': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_114',
                'dappled_grove',
                'giants_seat',
                'south_lake_miloch',
                'galar_route_5',
                'giants_cap',
            ],
            water: [
                'kalos_route_15',
                'kalos_route_16',
                'kalos_route_21',
            ],
        },
        dungeons: [
            'flower_paradise',
            'pokemon_village',
            'victory_road_kalos',
        ],
        evolution: [
            {
                prev: 'Lotad',
                level: 14,
            },
        ],
    },
    'Ludicolo': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'dappled_grove',
            ],
        },
        evolution: [
            {
                prev: 'Lombre',
                item: 'Water Stone',
            },
        ],
    },
    'Seedot': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_102',
                'hoenn_route_117',
                'hoenn_route_120',
                'galar_route_2',
                'dappled_grove',
                'west_lake_axewell',
                'galar_route_2_lakeside',
            ],
        },
        dungeons: [
            'flower_paradise',
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Nuzleaf': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_114',
                'rolling_fields',
                'dappled_grove',
                'giants_seat',
                'south_lake_miloch',
                'galar_route_5',
                'giants_cap',
            ],
        },
        evolution: [
            {
                prev: 'Seedot',
                level: 14,
            },
        ],
    },
    'Shiftry': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'dappled_grove',
            ],
        },
        dungeons: [
            'grasswither_shrine',
        ],
        evolution: [
            {
                prev: 'Nuzleaf',
                item: 'Leaf Stone',
            },
        ],
    },
    'Taillow': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_104',
                'hoenn_route_115',
                'hoenn_route_116',
            ],
        },
        dungeons: [
            'petalburg_woods',
        ],
    },
    'Swellow': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_115',
            ],
        },
        evolution: [
            {
                prev: 'Taillow',
                level: 22,
            },
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Wingull': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_103',
                'hoenn_route_104',
                'hoenn_route_105',
                'hoenn_route_106',
                'hoenn_route_107',
                'hoenn_route_108',
                'hoenn_route_109',
                'hoenn_route_110',
                'hoenn_route_115',
                'hoenn_route_118',
                'hoenn_route_121',
                'hoenn_route_122',
                'hoenn_route_123',
                'hoenn_route_124',
                'hoenn_route_125',
                'hoenn_route_126',
                'hoenn_route_127',
                'hoenn_route_128',
                'hoenn_route_129',
                'hoenn_route_131',
                'hoenn_route_132',
                'hoenn_route_133',
                'hoenn_route_134',
                'sinnoh_route_213',
                'sinnoh_route_219',
                'sinnoh_route_220',
                'sinnoh_route_222',
                'sinnoh_route_226',
                'sinnoh_route_230',
                'route_1_hauoli_outskirts',
                'melemele_sea',
                'kalae_bay',
                'akala_outskirts',
                'rolling_fields',
                'west_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'watchtower_ruins',
                'loop_lagoon',
                'stepping_stone_sea',
                'insular_sea',
                'poco_path',
                'south_province_area_one',
            ],
            water: [
                'hoenn_route_119',
                'hoenn_route_130',
                'alola_route_7',
                'east_lake_axewell',
                'fields_of_honor',
                'challenge_beach',
                'workout_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
        dungeons: [
            'mt_pyre',
            'iron_island',
            'liberty_garden',
            'trainers_school',
            'brooklet_hill',
            'minas_houseboat',
        ],
    },
    'Pelipper': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_105',
                'hoenn_route_106',
                'hoenn_route_107',
                'hoenn_route_108',
                'hoenn_route_109',
                'hoenn_route_122',
                'hoenn_route_124',
                'hoenn_route_125',
                'hoenn_route_126',
                'hoenn_route_127',
                'hoenn_route_128',
                'hoenn_route_129',
                'hoenn_route_131',
                'hoenn_route_132',
                'hoenn_route_133',
                'hoenn_route_134',
                'sinnoh_route_219',
                'sinnoh_route_220',
                'sinnoh_route_222',
                'sinnoh_route_223',
                'sinnoh_route_230',
                'unova_route_13',
                'unova_route_22',
                'alola_route_14',
                'alola_route_15',
                'alola_route_16',
                'poni_wilds',
                'ancient_poni_path',
                'poni_breaker_coast',
                'poni_plains',
                'poni_gauntlet',
                'rolling_fields',
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'axews_eye',
                'bridge_field',
                'lake_of_outrage',
                'hammerlocke_hills',
                'galar_route_9',
                'fields_of_honor',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
            water: [
                'hoenn_route_103',
                'hoenn_route_104',
                'hoenn_route_110',
                'hoenn_route_115',
                'hoenn_route_118',
                'hoenn_route_119',
                'hoenn_route_121',
                'hoenn_route_123',
                'hoenn_route_130',
                'sinnoh_route_221',
                'sinnoh_route_224',
                'sinnoh_route_226',
            ],
        },
        dungeons: [
            'iron_island',
            'giant_chasm',
            'minas_houseboat',
        ],
        evolution: [
            {
                prev: 'Wingull',
                level: 25,
            },
        ],
        special: [
            make_rule('exeggutor_island_hill', False) & make_rule('emissary_of_light2'),
        ],
    },
    'Ralts': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_102',
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_212',
                'kalos_route_4',
                'alola_route_6',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'watchtower_ruins',
                'fields_of_honor',
                'gapejaw_bog',
                'hearts_crag',
                'south_province_area_one',
            ],
        },
        dungeons: [
            'shrouded_ruins',
            'ancient_snowpoint_temple',
        ],
        farm_wandering: ['Payapa Berry', 'Roseli Berry'],
        shadow_pokemon: [
            'pyrite_building',
        ],
        dream_orbs: ['Orange'],
    },
    'Kirlia': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_212',
                'rolling_fields',
                'dappled_grove',
                'hearts_crag',
            ],
        },
        dungeons: [
            'ancient_solaceon_ruins',
            'shrouded_ruins',
            'ancient_snowpoint_temple',
            'glaseado_mountain',
        ],
        evolution: [
            {
                prev: 'Ralts',
                level: 20,
            },
        ],
    },
    'Gardevoir': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'rolling_fields',
                'dappled_grove',
                'lake_of_outrage',
                'forest_of_focus',
                'training_lowlands',
                'hearts_crag',
            ],
        },
        dungeons: [
            'glaseado_mountain',
        ],
        dungeon_boss: [
            ('ruins_of_life', 82177450),
        ],
        evolution: [
            {
                prev: 'Kirlia',
                level: 30,
            },
        ],
    },
    'Mega Gardevoir': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Gardevoir',
                item: 'Gardevoirite',
            },
        ],
    },
    'Surskit': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_102',
                'hoenn_route_114',
                'hoenn_route_117',
                'hoenn_route_120',
                'oasis_poke_spot',
            ],
            water: [
                'sinnoh_route_229',
                'south_province_area_one',
            ],
        },
        dungeons: [
            'brooklet_hill',
        ],
        special: [
            Has('Surskit') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Masquerain': {
        native_region: 'Hoenn',
        routes: {
            water: [
                'sinnoh_route_229',
                'kalos_route_3',
            ],
        },
        dungeons: [
            'malie_garden',
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Surskit',
                level: 22,
            },
        ],
        special: [
            Has('Masquerain') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Shroomish': {
        native_region: 'Hoenn',
        dungeons: [
            'petalburg_woods',
        ],
        safari: ['Sinnoh'],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Breloom': {
        native_region: 'Hoenn',
        dungeons: [
            'hall_of_origin',
            'pledge_grove',
        ],
        dungeon_boss: [
            ('flower_paradise', 9900000),
        ],
        evolution: [
            {
                prev: 'Shroomish',
                level: 23,
            },
        ],
        safari: ['Kalos'],
    },
    'Slakoth': {
        native_region: 'Hoenn',
        dungeons: [
            'hall_of_origin',
        ],
        special: [
            make_rule('petalburg_woods', True, 860000),
        ],
    },
    'Vigoroth': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'alola_route_11',
            ],
        },
        dungeons: [
            'pinwheel_forest',
            'glaseado_mountain',
        ],
        evolution: [
            {
                prev: 'Slakoth',
                level: 18,
            },
        ],
    },
    'Slaking': {
        native_region: 'Hoenn',
        dungeon_boss: [
            ('hall_of_origin', 10000000),
        ],
        evolution: [
            {
                prev: 'Vigoroth',
                level: 36,
            },
        ],
    },
    'Nincada': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_116',
                'kalos_route_6',
                'west_lake_axewell',
                'south_lake_miloch',
                'galar_route_5',
            ],
        },
        farm_wandering: ['Tanga Berry'],
        special: [
            Has('Nincada') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Ninjask': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'rolling_fields',
                'stony_wilderness',
            ],
        },
        evolution: [
            {
                prev: 'Nincada',
                level: 20,
            },
        ],
    },
    'Shedinja': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Nincada',
                level: 20,
            },
        ],
        farm_wandering: ['Kasib Berry'],
    },
    'Whismur': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_116',
            ],
        },
        dungeons: [
            'rusturf_tunnel',
            'victory_road_hoenn',
            'connecting_cave',
            'brawlers_cave',
        ],
    },
    'Loudred': {
        native_region: 'Hoenn',
        dungeons: [
            'victory_road_hoenn',
            'brawlers_cave',
        ],
        evolution: [
            {
                prev: 'Whismur',
                level: 20,
            },
        ],
    },
    'Exploud': {
        native_region: 'Hoenn',
        dungeon_boss: [
            ('cave_of_origin', 2000000),
        ],
        evolution: [
            {
                prev: 'Loudred',
                level: 40,
            },
        ],
    },
    'Makuhita': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'alola_route_2',
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'granite_cave',
            'victory_road_hoenn',
        ],
        egg: 'Fighting Egg',
        farm_wandering: ['Chople Berry'],
        shadow_pokemon: [
            'phenac_city_battles',
            'pyrite_building',
        ],
    },
    'Hariyama': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalos_route_11',
                'poni_plains',
            ],
        },
        dungeon_boss: [
            ('victory_road_hoenn', 3003000),
        ],
        evolution: [
            {
                prev: 'Makuhita',
                level: 24,
            },
        ],
    },
    'Azurill': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalos_route_3',
                'kalos_route_22',
            ],
            water: [
                'unova_route_20',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'floccesy_ranch',
            'brawlers_cave',
        ],
        breeding: ['Marill', 'Azumarill'],
    },
    'Nosepass': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'akala_outskirts',
            ],
            headbutt: [
                'cloudcap_pass',
            ],
        },
        dungeons: [
            'spear_pillar',
            'chargestone_cave',
            'primeval_grotto',
            'celestica_ruins',
            'sacred_plaza',
        ],
        dungeon_boss: [
            ('granite_cave', 660000),
            ('mt_coronet_south', 4000000),
        ],
        shadow_pokemon: [
            'realgam_colosseum',
        ],
    },
    'Skitty': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_116',
                'kalos_route_4',
            ],
        },
        dungeons: [
            'lake_of_the_sunne_and_moone',
        ],
    },
    'Delcatty': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Skitty',
                item: 'Moon Stone',
            },
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Sableye': {
        native_region: 'Hoenn',
        dungeons: [
            'granite_cave',
            'cave_of_origin',
            'sky_pillar',
            'reflection_cave',
            'lakeside_cave',
            'area_zero_depths',
        ],
        egg: 'Mystery Egg',
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Mega Sableye': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Sableye',
                item: 'Sablenite',
            },
        ],
    },
    'Mawile': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'bridge_field',
            ],
        },
        dungeons: [
            'cave_of_origin',
            'sky_pillar',
            'victory_road_hoenn',
            'ten_carat_hill',
            'energy_plant',
            'lakeside_cave',
        ],
        dungeon_boss: [
            ('granite_cave', 960000),
        ],
        shadow_pokemon: [
            'pyrite_building',
        ],
        special: [
            make_rule('a_beautiful_world3') & make_rule('glittering_cave', True, 61285398),
        ],
    },
    'Mega Mawile': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Mawile',
                item: 'Mawilite',
            },
        ],
    },
    'Aron': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'cave_poke_spot',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'granite_cave',
            'victory_road_hoenn',
            'mistralton_cave',
            'terminus_cave',
            'lakeside_cave',
        ],
        farm_wandering: ['Charti Berry'],
    },
    'Lairon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalos_route_18',
            ],
        },
        dungeons: [
            'victory_road_hoenn',
            'mistralton_cave',
            'terminus_cave',
            'lakeside_cave',
        ],
        evolution: [
            {
                prev: 'Aron',
                level: 32,
            },
        ],
    },
    'Aggron': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'poni_plains',
            ],
        },
        dungeons: [
            'rock_peak_ruins',
        ],
        dungeon_boss: [
            ('lakeside_cave', 166608415),
        ],
        evolution: [
            {
                prev: 'Lairon',
                level: 42,
            },
        ],
    },
    'Mega Aggron': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Aggron',
                item: 'Aggronite',
            },
        ],
    },
    'Meditite': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_210',
                'sinnoh_route_211',
                'sinnoh_route_216',
            ],
        },
        dungeons: [
            'mt_pyre',
            'victory_road_hoenn',
            'mt_coronet_north',
            'connecting_cave',
            'area_zero',
        ],
        dungeon_boss: [
            ('mt_coronet_south', 4000000),
        ],
        egg: 'Fighting Egg',
        shadow_pokemon: [
            'pyrite_cave',
        ],
    },
    'Medicham': {
        native_region: 'Hoenn',
        dungeons: [
            'victory_road_hoenn',
            'spear_pillar',
            'area_zero',
        ],
        dungeon_boss: [
            ('mt_coronet_north', 4960000),
        ],
        evolution: [
            {
                prev: 'Meditite',
                level: 37,
            },
        ],
    },
    'Mega Medicham': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Medicham',
                item: 'Medichamite',
            },
        ],
    },
    'Electrike': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalos_route_10',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'watchtower_ruins',
                'galar_route_4',
            ],
        },
        egg: 'Electric Egg',
        special: [
            Has('Electrike') & make_rule('hoenn_route_110'),
            Has('Electrike') & make_rule('hoenn_route_118'),
        ],
    },
    'Manectric': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'alola_route_12',
                'rolling_fields',
                'giants_seat',
                'axews_eye',
                'giants_cap',
            ],
        },
        evolution: [
            {
                prev: 'Electrike',
                level: 26,
            },
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
        special: [
            Has('Manectric') & make_rule('hoenn_route_118'),
        ],
    },
    'Mega Manectric': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Manectric',
                item: 'Manectite',
            },
        ],
    },
    'Plusle': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_110',
                'kalos_route_5',
            ],
        },
        dungeons: [
            'newmoon_island',
            'pikachu_valley',
        ],
        egg: 'Electric Egg',
        farm_wandering: ['Wacan Berry'],
    },
    'Minun': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_110',
                'kalos_route_5',
            ],
        },
        dungeons: [
            'fullmoon_island',
            'pikachu_valley',
        ],
        egg: 'Electric Egg',
        farm_wandering: ['Wacan Berry'],
    },
    'Volbeat': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_117',
                'sinnoh_route_229',
                'kalos_route_7',
            ],
        },
        dungeons: [
            'newmoon_island',
        ],
        farm_wandering: ['Oran Berry', 'Kelpsy Berry', 'Passho Berry', 'Yache Berry', 'Coba Berry', 'Rowap Berry', 'Maranga Berry', 'Apicot Berry'],
    },
    'Illumise': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_117',
                'sinnoh_route_229',
                'kalos_route_7',
            ],
        },
        dungeons: [
            'fullmoon_island',
        ],
        farm_wandering: ['Chesto Berry', 'Bluk Berry', 'Wiki Berry', 'Cornn Berry', 'Pamtre Berry', 'Belue Berry', 'Payapa Berry', 'Kasib Berry', 'Colbur Berry', 'Ganlon Berry', 'Enigma Berry'],
    },
    'Roselia': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_210',
                'sinnoh_route_212',
                'sinnoh_route_221',
                'sinnoh_route_224',
                'sinnoh_route_229',
                'sinnoh_route_230',
                'unova_route_12',
                'kalos_route_7',
                'rolling_fields',
                'dappled_grove',
                'south_lake_miloch',
                'axews_eye',
                'giants_mirror',
                'cloudpool_ridge',
                'gapejaw_bog',
                'fabled_spring',
            ],
        },
        dungeons: [
            'flower_paradise',
            'lostlorn_forest',
            'victory_road_unova',
        ],
        dungeon_boss: [
            ('ulaula_meadow', 75635260),
        ],
        evolution: [
            {
                prev: 'Budew',
                item: 'Soothe Bell',
                time: 'day',
            },
        ],
        egg: 'Grass Egg',
        shadow_pokemon: [
            'phenac_city_battles',
        ],
        special: [
            Has('Roselia') & make_rule('hoenn_route_117'),
        ],
    },
    'Gulpin': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_110',
                'kalos_route_5',
                'south_province_area_three',
            ],
        },
        safari: ['Sinnoh'],
        farm_wandering: ['Kebia Berry'],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Swalot': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'unova_route_9',
            ],
        },
        evolution: [
            {
                prev: 'Gulpin',
                level: 26,
            },
        ],
    },
    'Carvanha': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'poni_breaker_coast',
            ],
            water: [
                'hoenn_route_118',
                'hoenn_route_119',
                'kalos_route_22',
                'training_lowlands',
            ],
        },
        safari: ['Sinnoh'],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Sharpedo': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_122',
                'hoenn_route_124',
                'hoenn_route_125',
                'hoenn_route_126',
                'hoenn_route_127',
                'hoenn_route_129',
                'hoenn_route_131',
                'hoenn_route_132',
                'hoenn_route_133',
                'hoenn_route_134',
            ],
            water: [
                'hoenn_route_103',
                'hoenn_route_118',
                'hoenn_route_130',
                'sinnoh_route_222',
                'training_lowlands',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
            ],
        },
        evolution: [
            {
                prev: 'Carvanha',
                level: 30,
            },
        ],
    },
    'Mega Sharpedo': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Sharpedo',
                item: 'Sharpedonite',
            },
        ],
    },
    'Wailmer': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_105',
                'hoenn_route_106',
                'hoenn_route_107',
                'hoenn_route_108',
                'hoenn_route_109',
                'hoenn_route_122',
                'hoenn_route_124',
                'hoenn_route_125',
                'hoenn_route_126',
                'hoenn_route_127',
                'hoenn_route_128',
                'hoenn_route_129',
                'hoenn_route_131',
                'hoenn_route_132',
                'hoenn_route_133',
                'hoenn_route_134',
                'sinnoh_route_223',
                'undella_bay',
                'poni_breaker_coast',
            ],
            water: [
                'hoenn_route_103',
                'hoenn_route_110',
                'hoenn_route_115',
                'hoenn_route_121',
                'hoenn_route_123',
                'hoenn_route_130',
                'sinnoh_route_230',
                'kalos_route_8',
                'motostoke_riverbank',
                'circhester_bay',
                'honeycalm_sea',
                'honeycalm_island',
                'frigid_sea',
            ],
        },
        dungeons: [
            'shoal_cave',
            'seafloor_cavern',
            'sealed_chamber',
        ],
    },
    'Wailord': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_129',
                'sinnoh_route_223',
            ],
            water: [
                'sinnoh_route_230',
                'circhester_bay',
                'workout_sea',
            ],
        },
        evolution: [
            {
                prev: 'Wailmer',
                level: 40,
            },
        ],
    },
    'Numel': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_112',
                'sinnoh_route_227',
            ],
        },
        dungeons: [
            'fiery_path',
            'jagged_pass',
            'stark_mountain',
            'reversal_mountain',
            'area_zero',
        ],
        egg: 'Fire Egg',
        farm_wandering: ['Shuca Berry'],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Camerupt': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_227',
            ],
        },
        dungeons: [
            'reversal_mountain',
            'area_zero',
        ],
        dungeon_boss: [
            ('stark_mountain', 10000000),
        ],
        evolution: [
            {
                prev: 'Numel',
                level: 33,
            },
        ],
    },
    'Mega Camerupt': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Camerupt',
                item: 'Cameruptite',
            },
        ],
    },
    'Torkoal': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalos_route_18',
                'alola_route_12',
                'motostoke_riverbank',
                'giants_mirror',
                'giants_cap',
                'galar_route_6',
                'potbottom_desert',
            ],
        },
        dungeons: [
            'magma_hideout',
            'warm_up_tunnel',
        ],
        dungeon_boss: [
            ('fiery_path', 1200000),
        ],
    },
    'Spoink': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalos_route_8',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'jagged_pass',
            'reversal_mountain',
        ],
        egg: 'Mystery Egg',
    },
    'Grumpig': {
        native_region: 'Hoenn',
        dungeons: [
            'reversal_mountain',
            'glaseado_mountain',
        ],
        evolution: [
            {
                prev: 'Spoink',
                level: 32,
            },
        ],
    },
    'Spinda': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_113',
                'kalos_route_21',
            ],
        },
        dungeon_boss: [
            ('ten_carat_hill', 59489105),
        ],
    },
    'Trapinch': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_111',
                'rock_poke_spot',
                'desert_resort',
                'kalos_route_13',
                'haina_desert',
                'hammerlocke_hills',
                'galar_route_6',
            ],
        },
        dungeons: [
            'reversal_mountain',
        ],
        egg: 'Mystery Egg',
    },
    'Vibrava': {
        native_region: 'Hoenn',
        dungeon_boss: [
            ('reversal_mountain', 24000000),
        ],
        evolution: [
            {
                prev: 'Trapinch',
                level: 35,
            },
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Flygon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        dungeon_boss: [
            ('dusty_bowl', 114616050),
        ],
        evolution: [
            {
                prev: 'Vibrava',
                level: 45,
            },
        ],
    },
    'Cacnea': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_111',
                'sinnoh_route_228',
            ],
        },
    },
    'Cacturne': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_228',
            ],
        },
        dungeons: [
            'grasswither_shrine',
        ],
        dungeon_boss: [
            ('reversal_mountain', 24000000),
        ],
        evolution: [
            {
                prev: 'Cacnea',
                level: 32,
            },
        ],
    },
    'Swablu': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_114',
                'hoenn_route_115',
                'sinnoh_route_210',
                'unova_route_14',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'path_to_the_peak',
            ],
        },
        dungeons: [
            'sky_pillar',
            'abundant_shrine',
            'area_zero',
        ],
        farm_wandering: ['Chilan Berry'],
        shadow_pokemon: [
            'pyrite_cave',
        ],
        dream_orbs: ['Pink'],
    },
    'Altaria': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'unova_route_14',
                'kalos_route_21',
                'giants_bed',
                'giants_foot',
                'frigid_sea',
                'ballimere_lake',
                'path_to_the_peak',
            ],
        },
        dungeons: [
            'victory_road_unova',
            'area_zero',
        ],
        dungeon_boss: [
            ('sky_pillar', 3200000),
            ('abundant_shrine', 38000000),
            ('split_decision_ruins', 156135635),
        ],
        evolution: [
            {
                prev: 'Swablu',
                level: 35,
            },
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Zangoose': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_114',
                'unova_route_7',
                'unova_route_11',
                'kalos_route_8',
            ],
        },
        shadow_pokemon: [
            'gateon_port_battles',
        ],
    },
    'Seviper': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_114',
                'unova_route_7',
                'unova_route_11',
                'kalos_route_8',
            ],
        },
    },
    'Lunatone': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'unova_route_13',
                'unova_route_22',
                'galar_route_8',
            ],
        },
        dungeons: [
            'near_space',
            'giant_chasm',
            'glittering_cave',
            'lake_of_the_sunne_and_moone',
        ],
        dungeon_boss: [
            ('meteor_falls', 1240000),
            ('fullmoon_island', 11000000),
            ('newmoon_island', 9900000),
        ],
        shadow_pokemon: [
            'phenac_stadium',
        ],
    },
    'Solrock': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'unova_route_13',
                'unova_route_22',
                'galar_route_8',
            ],
        },
        dungeons: [
            'near_space',
            'giant_chasm',
            'glittering_cave',
            'lake_of_the_sunne_and_moone',
        ],
        dungeon_boss: [
            ('meteor_falls', 1240000),
        ],
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Barboach': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'stony_wilderness',
            ],
            water: [
                'hoenn_route_111',
                'hoenn_route_114',
                'hoenn_route_120',
                'sinnoh_route_205',
                'sinnoh_route_208',
                'sinnoh_route_210',
                'sinnoh_route_225',
                'sinnoh_route_227',
                'sinnoh_route_228',
                'kalos_route_14',
                'kalos_route_19',
                'poni_gauntlet',
                'south_lake_miloch',
                'north_lake_miloch',
                'soothing_wetlands',
                'giants_bed',
                'giants_foot',
                'ballimere_lake',
                'gapejaw_bog',
            ],
        },
        dungeons: [
            'meteor_falls',
            'victory_road_hoenn',
            'oreburgh_gate',
            'mt_coronet_south',
            'mt_coronet_north',
            'moor_of_icirrus',
            'vast_poni_canyon',
            'poni_meadow',
            'slumbering_weald_shrine',
            'galar_mine_no_2',
            'brawlers_cave',
            'roaring_sea_caves',
            'ancient_wayward_cave',
            'ancient_lake_valor',
        ],
        dungeon_boss: [
            ('seaward_cave', 59226690),
        ],
        safari: ['Sinnoh'],
    },
    'Whiscash': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'south_lake_miloch',
                'north_lake_miloch',
            ],
            water: [
                'sinnoh_route_205',
                'sinnoh_route_208',
                'sinnoh_route_210',
                'sinnoh_route_225',
                'sinnoh_route_227',
                'sinnoh_route_228',
                'soothing_wetlands',
                'giants_bed',
                'giants_foot',
                'ballimere_lake',
                'gapejaw_bog',
            ],
        },
        dungeons: [
            'slumbering_weald_shrine',
            'courageous_cavern',
            'brawlers_cave',
            'ancient_wayward_cave',
            'ancient_lake_valor',
        ],
        dungeon_boss: [
            ('victory_road_hoenn', 3003000),
            ('oreburgh_gate', 3703000),
            ('moor_of_icirrus', 48000000),
        ],
        evolution: [
            {
                prev: 'Barboach',
                level: 30,
            },
        ],
        safari: ['Sinnoh'],
    },
    'Corphish': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'south_lake_miloch',
                'soothing_wetlands',
            ],
            water: [
                'hoenn_route_102',
                'hoenn_route_117',
                'giants_cap',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
            ],
        },
        dungeons: [
            'vast_poni_canyon',
            'galar_mine_no_2',
        ],
    },
    'Crawdaunt': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'giants_seat',
                'south_lake_miloch',
                'axews_eye',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
            ],
        },
        evolution: [
            {
                prev: 'Corphish',
                level: 30,
            },
        ],
    },
    'Baltoy': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_111',
                'haina_desert',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'axews_eye',
                'bridge_field',
                'stony_wilderness',
                'giants_cap',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'relic_castle',
        ],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Claydol': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'dappled_grove',
                'axews_eye',
                'bridge_field',
                'stony_wilderness',
                'lake_of_outrage',
                'giants_foot',
                'three_point_pass',
            ],
        },
        dungeon_boss: [
            ('sky_pillar', 3200000),
        ],
        evolution: [
            {
                prev: 'Baltoy',
                level: 36,
            },
        ],
    },
    'Lileep': {
        native_region: 'Hoenn',
        trades: [
            ('rustboro_city', ['Root Fossil']),
        ],
        special: [
            Has('Lileep') & make_rule('giants_bed'),
            Has('Lileep') & make_rule('giants_foot'),
        ],
    },
    'Cradily': {
        native_region: 'Hoenn',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Lileep',
                level: 40,
            },
        ],
        trades: [
            ('rustboro_city', ['Root Fossil']),
        ],
    },
    'Anorith': {
        native_region: 'Hoenn',
        trades: [
            ('rustboro_city', ['Claw Fossil']),
        ],
        special: [
            Has('Anorith') & make_rule('ballimere_lake'),
        ],
    },
    'Armaldo': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Anorith',
                level: 40,
            },
        ],
        trades: [
            ('rustboro_city', ['Claw Fossil']),
        ],
        special: [
            Has('Armaldo') & make_rule('ballimere_lake'),
        ],
    },
    'Feebas': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'giants_bed',
                'giants_foot',
            ],
            water: [
                'galar_route_2_lakeside',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'brooklet_hill',
            'roaring_sea_caves',
        ],
        dungeon_boss: [
            ('mt_coronet_north', 4960000),
        ],
        egg: 'Water Egg',
    },
    'Milotic': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'south_lake_miloch',
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Feebas',
                item: 'Prism Scale',
            },
        ],
    },
    'Castform': {
        native_region: 'Hoenn',
        special: [
            make_rule('weather_institute', True, 1820000),
        ],
    },
    'Castform (Sunny)': {
        native_region: 'Hoenn',
        special: [
            Has('Castform') & make_rule('weather_institute', True, 1820000),
        ],
    },
    'Castform (Rainy)': {
        native_region: 'Hoenn',
        special: [
            Has('Castform') & make_rule('weather_institute', True, 1820000),
        ],
    },
    'Castform (Snowy)': {
        native_region: 'Hoenn',
        special: [
            Has('Castform') & make_rule('weather_institute', True, 1820000),
        ],
    },
    'Kecleon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_118',
                'hoenn_route_119',
                'hoenn_route_120',
                'hoenn_route_121',
                'hoenn_route_123',
                'kalos_route_6',
            ],
        },
        safari: ['Sinnoh'],
        temporary_battle: [
            'kecleon1',
        ],
    },
    'Shuppet': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_121',
                'hoenn_route_123',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'mt_pyre',
            'thrifty_megamart',
        ],
        dungeon_boss: [
            ('mt_pyre', 1880000),
        ],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_101'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_102'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_103'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_104'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_105'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_106'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_107'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_108'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_109'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_110'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_111'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_112'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_113'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_114'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_115'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_116'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_117'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_118'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_119'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_120'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_121'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_122'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_123'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_124'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_125'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_126'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_127'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_128'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_129'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_130'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_131'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_132'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_133'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_134'),
        ],
    },
    'Banette': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_225',
                'sinnoh_route_226',
            ],
        },
        dungeons: [
            'sky_pillar',
            'victory_road_unova',
            'thrifty_megamart',
        ],
        dungeon_chest: [
            'distortion_world',
            'pokemon_village',
        ],
        evolution: [
            {
                prev: 'Shuppet',
                level: 37,
            },
        ],
        shadow_pokemon: [
            'citadark_isle',
        ],
    },
    'Mega Banette': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Banette',
                item: 'Banettite',
            },
        ],
    },
    'Duskull': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_209',
                'giants_seat',
                'watchtower_ruins',
                'motostoke_riverbank',
                'giants_cap',
                'galar_route_6',
                'deadwood_haunt',
                'arenas_approach',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'mt_pyre',
            'distortion_world',
        ],
        dungeon_boss: [
            ('mt_pyre', 1890000),
        ],
        shadow_pokemon: [
            'pyrite_building',
        ],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_101'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_102'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_103'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_104'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_105'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_106'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_107'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_108'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_109'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_110'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_111'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_112'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_113'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_114'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_115'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_116'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_117'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_118'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_119'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_120'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_121'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_122'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_123'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_124'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_125'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_126'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_127'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_128'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_129'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_130'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_131'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_132'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_133'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('hoenn_route_134'),
        ],
    },
    'Dusclops': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'giants_seat',
                'watchtower_ruins',
                'galar_route_8',
                'deadwood_haunt',
                'arenas_approach',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'distortion_world',
            'turnback_cave',
        ],
        dungeon_boss: [
            ('sky_pillar', 3200000),
            ('sendoff_spring', 10000000),
        ],
        evolution: [
            {
                prev: 'Duskull',
                level: 37,
            },
        ],
    },
    'Tropius': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_119',
                'unova_route_18',
            ],
        },
        egg: 'Grass Egg',
        safari: ['Sinnoh'],
        farm_wandering: ['Coba Berry'],
        shadow_pokemon: [
            'realgam_colosseum',
        ],
        special: [
            make_rule('emissary_of_light2') & make_rule('exeggutor_island_hill', True, 78865330),
        ],
    },
    'Chimecho': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'celestica_trail',
            ],
        },
        dungeons: [
            'spear_pillar',
            'distortion_world',
            'ruins_of_life',
            'sacred_plaza',
            'ancient_lake_acuity',
        ],
        dungeon_boss: [
            ('mt_pyre', 1880000),
            ('liberty_garden', 14000000),
        ],
        evolution: [
            {
                prev: 'Chingling',
                item: 'Soothe Bell',
                time: 'night',
            },
        ],
    },
    'Absol': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_120',
                'unova_route_13',
                'unova_route_14',
                'kalos_route_8',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'snowslide_slope',
                'path_to_the_peak',
            ],
        },
        dungeons: [
            'spear_pillar',
            'hall_of_origin',
            'dyna_tree_hill',
        ],
        dungeon_boss: [
            ('newmoon_island', 9900000),
            ('mount_lanakila', 81064250),
        ],
        farm_wandering: ['Colbur Berry'],
        shadow_pokemon: [
            'realgam_colosseum',
        ],
    },
    'Mega Absol': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Absol',
                item: 'Absolite',
            },
        ],
    },
    'Wynaut': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_130',
            ],
        },
        breeding: ['Wobbuffet'],
    },
    'Snorunt': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'sinnoh_route_216',
                'sinnoh_route_217',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'watchtower_ruins',
                'giants_cap',
                'hammerlocke_hills',
                'steamdrift_way',
                'giants_bed',
                'giants_foot',
                'snowslide_slope',
                'whiteout_valley',
                'bonechill_wastes',
                'avalanche_slopes',
            ],
            headbutt: [
                'arenas_approach',
                'icebound_falls',
                'hearts_crag',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'lake_acuity',
            'mount_lanakila',
            'tunnel_to_the_top',
        ],
        dungeon_boss: [
            ('shoal_cave', 1900000),
        ],
        shadow_pokemon: [
            'phenac_city_battles',
        ],
    },
    'Glalie': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'giants_seat',
                'watchtower_ruins',
                'giants_cap',
                'lake_of_outrage',
                'galar_route_9',
                'white_hill_station',
                'slippery_slope',
                'giants_bed',
                'snowslide_slope',
                'bonechill_wastes',
                'avalanche_slopes',
            ],
            headbutt: [
                'arenas_approach',
                'icebound_falls',
                'hearts_crag',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'split_decision_ruins',
            'dyna_tree_hill',
            'avaluggs_legacy',
            'ancient_snowpoint_temple',
        ],
        dungeon_boss: [
            ('mount_lanakila', 81064250),
            ('iceberg_ruins', 149662240),
        ],
        evolution: [
            {
                prev: 'Snorunt',
                level: 42,
            },
        ],
        special: [
            make_rule('icy_boulder') & make_rule('shoal_cave', True, 61614300),
        ],
    },
    'Mega Glalie': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Glalie',
                item: 'Glalitite',
            },
        ],
    },
    'Spheal': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'undella_bay',
                'unova_route_21',
                'alola_route_7',
                'ginkgo_landing',
                'hideaway_bay',
            ],
            water: [
                'frigid_sea',
            ],
        },
        dungeons: [
            'shoal_cave',
        ],
        farm_wandering: ['Yache Berry'],
        shadow_pokemon: [
            'cipher_lab',
        ],
    },
    'Sealeo': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hideaway_bay',
                'islespy_shore',
            ],
            water: [
                'sinnoh_route_230',
                'frigid_sea',
            ],
        },
        evolution: [
            {
                prev: 'Spheal',
                level: 32,
            },
        ],
    },
    'Walrein': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'frigid_sea',
                'ginkgo_landing',
                'islespy_shore',
            ],
        },
        evolution: [
            {
                prev: 'Sealeo',
                level: 44,
            },
        ],
    },
    'Clamperl': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_124',
                'hoenn_route_126',
                'sinnoh_route_219',
                'melemele_sea',
            ],
            water: [
                'sinnoh_route_221',
                'kalos_route_12',
                'alola_route_15',
            ],
        },
        dungeons: [
            'ruins_of_hope',
        ],
        egg: 'Water Egg',
    },
    'Huntail': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Clamperl',
                item: 'Deepsea Tooth',
            },
        ],
    },
    'Gorebyss': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Clamperl',
                item: 'Deepsea Scale',
            },
        ],
    },
    'Relicanth': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_124',
                'hoenn_route_126',
                'poni_breaker_coast',
            ],
            water: [
                'sinnoh_route_226',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'split_decision_ruins',
        ],
        dungeon_boss: [
            ('rock_peak_ruins', 149662240),
        ],
    },
    'Luvdisc': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'hoenn_route_128',
                'unova_route_21',
                'melemele_sea',
                'alola_route_9',
            ],
            water: [
                'sinnoh_route_224',
                'kalos_route_8',
                'azure_bay',
            ],
        },
        dungeons: [
            'fullmoon_island',
            'newmoon_island',
            'seaside_cave',
        ],
    },
    'Bagon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalos_route_8',
                'alola_route_3',
                'kalae_bay',
            ],
        },
        dungeons: [
            'tunnel_to_the_top',
        ],
        egg: 'Dragon Egg',
        farm_wandering: ['Haban Berry'],
        special: [
            Has('Bagon') & make_rule('meteor_falls', False),
        ],
    },
    'Shelgon': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'kalae_bay',
            ],
        },
        evolution: [
            {
                prev: 'Bagon',
                level: 30,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Salamence': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'path_to_the_peak',
            ],
        },
        dungeon_boss: [
            ('tunnel_to_the_top', 167825980),
        ],
        evolution: [
            {
                prev: 'Shelgon',
                level: 50,
            },
        ],
        egg: 'Dragon Egg',
        shadow_pokemon: [
            'citadark_isle_dome',
        ],
    },
    'Mega Salamence': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Salamence',
                item: 'Salamencite',
            },
        ],
    },
    'Beldum': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'mount_hokulani',
                'snowslide_slope',
            ],
        },
        farm_wandering: ['Babiri Berry'],
        shops: [
            ('mossdeep_city', 'questPoint'),
        ],
    },
    'Metang': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'snowslide_slope',
            ],
        },
        dungeons: [
            'giant_chasm',
        ],
        evolution: [
            {
                prev: 'Beldum',
                level: 20,
            },
        ],
    },
    'Metagross': {
        native_region: 'Hoenn',
        routes: {
            land: [
                'snowslide_slope',
            ],
        },
        dungeons: [
            'split_decision_ruins',
        ],
        dungeon_boss: [
            ('iron_ruins', 149662240),
        ],
        evolution: [
            {
                prev: 'Metang',
                level: 45,
            },
        ],
        shadow_pokemon: [
            'realgam_colosseum',
        ],
    },
    'Mega Metagross': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Metagross',
                item: 'Metagrossite',
            },
        ],
    },
    'Regirock': {
        native_region: 'Hoenn',
        special: [
            make_rule('the_three_golems8') & make_rule('sealed_chamber', True, 4500000),
            make_rule('the_ancient_golems4') & make_rule('rock_peak_ruins', True, 157539200),
        ],
    },
    'Regice': {
        native_region: 'Hoenn',
        special: [
            make_rule('the_three_golems8') & make_rule('sealed_chamber', True, 4500000),
            make_rule('the_ancient_golems4') & make_rule('iceberg_ruins', True, 157539200),
        ],
    },
    'Registeel': {
        native_region: 'Hoenn',
        special: [
            make_rule('the_three_golems8') & make_rule('sealed_chamber', True, 4500000),
            make_rule('the_ancient_golems4') & make_rule('iron_ruins', True, 157539200),
        ],
    },
    'Latias': {
        native_region: 'Hoenn',
        dungeon_boss: [
            ('dreamyard', 48000000),
        ],
        temporary_battle: [
            'latias',
        ],
        special: [
            make_rule('roamer', 'Hoenn') & make_rule('the_eon_duo3'),
        ],
    },
    'Mega Latias': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Latias',
                item: 'Latiasite',
            },
        ],
    },
    'Latios': {
        native_region: 'Hoenn',
        dungeon_boss: [
            ('dreamyard', 48000000),
        ],
        temporary_battle: [
            'latios',
        ],
        special: [
            make_rule('roamer', 'Hoenn') & make_rule('the_eon_duo3'),
        ],
    },
    'Mega Latios': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Latios',
                item: 'Latiosite',
            },
        ],
    },
    'Kyogre': {
        native_region: 'Hoenn',
        special: [
            Has('Elite Hoenn Champion Badge') & make_rule('the_weather_trio5') & make_rule('cave_of_origin', True, 4700000),
        ],
    },
    'Primal Kyogre': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Kyogre',
                item: 'Blue Orb',
            },
        ],
        special: [
            make_rule('completed_primal_reversion') & make_rule('cave_of_origin', True, 95743340),
        ],
    },
    'Groudon': {
        native_region: 'Hoenn',
        special: [
            Has('Elite Hoenn Champion Badge') & make_rule('the_weather_trio5') & make_rule('cave_of_origin', True, 4700000),
        ],
    },
    'Primal Groudon': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Groudon',
                item: 'Red Orb',
            },
        ],
        special: [
            make_rule('completed_primal_reversion') & make_rule('cave_of_origin', True, 95743340),
        ],
    },
    'Meta Groudon': {
        native_region: 'Hoenn',
        special: [
            make_rule('a_meta_discovery3') & make_rule('mt_chimney_crater', True, 1820000),
        ],
    },
    'Rayquaza': {
        native_region: 'Hoenn',
        special: [
            make_rule('the_weather_trio5') & make_rule('sky_pillar', True, 5824002),
        ],
    },
    'Mega Rayquaza': {
        native_region: 'Hoenn',
        evolution: [
            {
                prev: 'Rayquaza',
                item: 'Meteorite',
            },
        ],
    },
    'Jirachi': {
        native_region: 'Hoenn',
        farm_wandering: ['Starf Berry'],
        special: [
            make_rule('roamer', 'Hoenn') & make_rule('wish_maker8'),
        ],
    },
    'Deoxys': {
        native_region: 'Hoenn',
        dungeon_boss: [
            ('near_space', 95743340),
        ],
        special: [
            make_rule('battle_frontier', 100) & make_rule('mystery_of_deoxys2'),
        ],
    },
    'Deoxys (Attack)': {
        native_region: 'Hoenn',
        special: [
            Has('Deoxys (Attack)') & make_rule('near_space', True, 95743340),
            Has('Deoxys') & make_rule('battle_frontier', 151),
        ],
    },
    'Deoxys (Defense)': {
        native_region: 'Hoenn',
        special: [
            Has('Deoxys (Defense)') & make_rule('near_space', True, 95743340),
            Has('Deoxys') & make_rule('battle_frontier', 251),
        ],
    },
    'Deoxys (Speed)': {
        native_region: 'Hoenn',
        special: [
            Has('Deoxys (Speed)') & make_rule('near_space', True, 95743340),
            Has('Deoxys') & make_rule('battle_frontier', 386),
        ],
    },
    'Deoxys (Green Core)': {
        native_region: 'Hoenn',
        special: [
            Has('Deoxys (Green Core)') & make_rule('near_space', True, 95743340),
            Has('Deoxys (Green Core)') & make_rule('battle_frontier') & make_rule('destiny_deoxys8'),
        ],
    },
    'Deoxys (Clone)': {
        native_region: 'Hoenn',
        shops: [
            ('battle_frontier', 'Psychic Gems'),
        ],
    },
    'Turtwig': {
        native_region: 'Sinnoh',
        egg: 'Grass Egg',
        starter: ['Sinnoh'],
        farm_wandering: ['Rindo Berry'],
    },
    'Grotle': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('ulaula_meadow', 75635260),
        ],
        evolution: [
            {
                prev: 'Turtwig',
                level: 18,
            },
        ],
    },
    'Grotle (Acorn)': {
        native_region: 'Sinnoh',
        trades: [
            ('secret_berry_shop', ['Snover Berry']),
        ],
    },
    'Torterra': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'holm_of_trials',
            ],
        },
        evolution: [
            {
                prev: 'Grotle',
                level: 32,
            },
        ],
    },
    'Chimchar': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'deertrack_heights',
                'ramanas_island',
            ],
        },
        egg: 'Fire Egg',
        starter: ['Sinnoh'],
        farm_wandering: ['Occa Berry'],
    },
    'Monferno': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'alola_route_11',
                'deertrack_heights',
                'ramanas_island',
            ],
        },
        evolution: [
            {
                prev: 'Chimchar',
                level: 14,
            },
        ],
    },
    'Infernape': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'ramanas_island',
            ],
        },
        evolution: [
            {
                prev: 'Monferno',
                level: 36,
            },
        ],
    },
    'Piplup': {
        native_region: 'Sinnoh',
        egg: 'Water Egg',
        starter: ['Sinnoh'],
        farm_wandering: ['Passho Berry'],
    },
    'Prinplup': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'alola_route_16',
            ],
        },
        evolution: [
            {
                prev: 'Piplup',
                level: 16,
            },
        ],
    },
    'Empoleon': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'islespy_shore',
            ],
        },
        evolution: [
            {
                prev: 'Prinplup',
                level: 36,
            },
        ],
    },
    'Starly': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_201',
                'sinnoh_route_202',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'aspiration_hill',
                'horseshoe_plains',
                'deertrack_path',
                'deertrack_heights',
                'windswept_run',
                'natures_pantry',
                'tidewater_dam',
                'ramanas_island',
                'crossing_slope',
                'bathers_lagoon',
                'deadwood_haunt',
                'sands_reach',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'lake_verity',
        ],
    },
    'Staravia': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_209',
                'sinnoh_route_210',
                'sinnoh_route_215',
                'sinnoh_route_212',
                'kalos_route_11',
                'alola_route_10',
                'sandgem_flats',
                'deertrack_heights',
                'windswept_run',
                'natures_pantry',
                'tidewater_dam',
                'ramanas_island',
                'crossing_slope',
                'bathers_lagoon',
                'deadwood_haunt',
                'sands_reach',
                'tranquility_cove',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'lake_valor',
            'sendoff_spring',
        ],
        evolution: [
            {
                prev: 'Starly',
                level: 14,
            },
        ],
    },
    'Staraptor': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'deadwood_haunt',
                'tranquility_cove',
                'south_province_area_three',
            ],
        },
        dungeon_boss: [
            ('hall_of_origin', 10000000),
        ],
        evolution: [
            {
                prev: 'Staravia',
                level: 34,
            },
        ],
    },
    'Bidoof': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_201',
                'sinnoh_route_202',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_205',
                'sinnoh_route_208',
                'sinnoh_route_211',
                'kalos_route_3',
                'kalos_route_22',
                'aspiration_hill',
                'horseshoe_plains',
                'tidewater_dam',
                'droning_meadow',
                'gapejaw_bog',
            ],
        },
        dungeons: [
            'eterna_forest',
            'lake_verity',
        ],
    },
    'Bibarel': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_208',
                'sinnoh_route_209',
                'sinnoh_route_210',
                'kalos_route_22',
                'tidewater_dam',
                'droning_meadow',
                'gapejaw_bog',
                'spring_path',
            ],
        },
        dungeons: [
            'lake_valor',
            'lake_acuity',
            'sendoff_spring',
            'avaluggs_legacy',
            'temple_of_sinnoh',
        ],
        evolution: [
            {
                prev: 'Bidoof',
                level: 15,
            },
        ],
        safari: ['Sinnoh'],
    },
    'Kricketot': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_201',
                'sinnoh_route_202',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'sinnoh_route_205',
                'sinnoh_route_207',
                'deertrack_path',
                'windswept_run',
                'natures_pantry',
                'tidewater_dam',
                'golden_lowlands',
                'cloudpool_ridge',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'eterna_forest',
        ],
        special: [
            Has('Kricketot') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Kricketune': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_206',
                'windswept_run',
                'natures_pantry',
                'tidewater_dam',
                'golden_lowlands',
                'cloudpool_ridge',
            ],
        },
        evolution: [
            {
                prev: 'Kricketot',
                level: 10,
            },
        ],
        special: [
            Has('Kricketune') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Shinx': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_202',
                'sinnoh_route_203',
                'sinnoh_route_204',
                'challenge_beach',
                'training_lowlands',
                'potbottom_desert',
                'challenge_road',
                'aspiration_hill',
                'deertrack_heights',
                'sonorous_path',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'floaro_gardens',
        ],
        egg: 'Electric Egg',
    },
    'Luxio': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_222',
                'alola_route_8',
                'fields_of_honor',
                'soothing_wetlands',
                'loop_lagoon',
                'training_lowlands',
                'sandgem_flats',
                'heavenward_lookout',
                'sonorous_path',
                'cloudcap_pass',
            ],
        },
        dungeons: [
            'floaro_gardens',
            'sacred_plaza',
            'ancient_lake_verity',
        ],
        evolution: [
            {
                prev: 'Shinx',
                level: 15,
            },
        ],
    },
    'Luxray': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'soothing_wetlands',
                'forest_of_focus',
                'loop_lagoon',
                'training_lowlands',
                'sandgem_flats',
                'heavenward_lookout',
                'sonorous_path',
                'cloudcap_pass',
            ],
        },
        dungeons: [
            'ancient_lake_verity',
        ],
        dungeon_boss: [
            ('ruins_of_conflict', 82177450),
            ('sacred_plaza', 10000000),
        ],
        evolution: [
            {
                prev: 'Luxio',
                level: 30,
            },
        ],
    },
    'Budew': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_204',
                'sinnoh_route_205',
                'sinnoh_route_208',
                'kalos_route_4',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'galar_route_4',
                'giants_mirror',
                'golden_lowlands',
                'gapejaw_bog',
                'fabled_spring',
            ],
        },
        dungeons: [
            'eterna_forest',
        ],
        egg: 'Grass Egg',
        breeding: ['Roselia', 'Roserade'],
    },
    'Roserade': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'hammerlocke_hills',
                'cloudpool_ridge',
            ],
        },
        dungeons: [
            'crown_shrine',
        ],
        evolution: [
            {
                prev: 'Roselia',
                item: 'Shiny Stone',
            },
        ],
    },
    'Cranidos': {
        native_region: 'Sinnoh',
        trades: [
            ('oreburgh_city', ['Skull Fossil']),
        ],
    },
    'Rampardos': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Cranidos',
                level: 30,
            },
        ],
        trades: [
            ('oreburgh_city', ['Skull Fossil']),
        ],
    },
    'Shieldon': {
        native_region: 'Sinnoh',
        trades: [
            ('oreburgh_city', ['Armor Fossil']),
        ],
    },
    'Bastiodon': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Shieldon',
                level: 30,
            },
        ],
        trades: [
            ('oreburgh_city', ['Armor Fossil']),
        ],
    },
    'Burmy (Plant)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_3',
            ],
            headbutt: [
                'deertrack_path',
                'deertrack_heights',
                'windswept_run',
                'natures_pantry',
                'worn_bridge',
                'gruelling_grove',
                'tidewater_dam',
                'obsidian_falls',
            ],
        },
        evolution: [
            {
                prev: 'Burmy (Sand)',
                level: 1,
                environment: 'PlantCloak',
            },
            {
                prev: 'Burmy (Trash)',
                level: 1,
                environment: 'PlantCloak',
            },
        ],
        farm_wandering: ['Rawst Berry', 'Wepear Berry', 'Aguav Berry', 'Lum Berry', 'Hondew Berry', 'Rabuta Berry', 'Durin Berry', 'Rindo Berry', 'Kebia Berry', 'Tanga Berry', 'Babiri Berry', 'Snover Berry', 'Micle Berry', 'Salac Berry', 'Starf Berry'],
        shops: [
            ('pal_park', 'questPoint'),
        ],
    },
    'Burmy (Sand)': {
        native_region: 'Sinnoh',
        routes: {
            headbutt: [
                'golden_lowlands',
                'cloudpool_ridge',
                'bolderoll_slope',
                'gapejaw_bog',
                'ursas_ring',
                'holm_of_trials',
                'heavenward_lookout',
                'fabled_spring',
                'stonetooth_rows',
                'cloudcap_pass',
            ],
        },
        dungeons: [
            'shrouded_ruins',
            'clamberclaw_cliffs',
            'celestica_ruins',
            'sacred_plaza',
        ],
        evolution: [
            {
                prev: 'Burmy (Plant)',
                level: 1,
                environment: 'SandyCloak',
            },
            {
                prev: 'Burmy (Trash)',
                level: 1,
                environment: 'SandyCloak',
            },
        ],
    },
    'Burmy (Trash)': {
        native_region: 'Sinnoh',
        routes: {
            headbutt: [
                'crossing_slope',
                'ginkgo_landing',
                'aipom_hill',
                'bathers_lagoon',
                'hideaway_bay',
                'sands_reach',
                'castaway_shore',
                'spring_path',
                'tranquility_cove',
                'lunkers_lair',
                'seagrass_haven',
                'tombolo_walk',
                'whiteout_valley',
                'bonechill_wastes',
                'arenas_approach',
                'avalanche_slopes',
                'icebound_falls',
                'hearts_crag',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'veilstone_cape',
            'ancient_lake_acuity',
        ],
        evolution: [
            {
                prev: 'Burmy (Plant)',
                level: 1,
                environment: 'TrashCloak',
            },
            {
                prev: 'Burmy (Sand)',
                level: 1,
                environment: 'TrashCloak',
            },
        ],
    },
    'Burmy (No Coat)': {
        native_region: 'Sinnoh',
        farm_wandering: ['Custap Berry'],
    },
    'Wormadam (Plant)': {
        native_region: 'Sinnoh',
        routes: {
            headbutt: [
                'sandgem_flats',
                'gruelling_grove',
            ],
        },
        dungeons: [
            'ancient_lake_verity',
        ],
        evolution: [
            {
                prev: 'Burmy (Plant)',
                level: 20,
            },
        ],
    },
    'Wormadam (Sand)': {
        native_region: 'Sinnoh',
        routes: {
            headbutt: [
                'heavenward_lookout',
                'fabled_spring',
                'stonetooth_rows',
                'cloudcap_pass',
            ],
        },
        dungeons: [
            'clamberclaw_cliffs',
            'sacred_plaza',
        ],
        dungeon_boss: [
            ('celestica_ruins', 10000000),
        ],
        evolution: [
            {
                prev: 'Burmy (Sand)',
                level: 20,
            },
        ],
    },
    'Wormadam (Trash)': {
        native_region: 'Sinnoh',
        routes: {
            headbutt: [
                'crossing_slope',
                'ginkgo_landing',
                'aipom_hill',
                'bathers_lagoon',
                'hideaway_bay',
                'sands_reach',
                'castaway_shore',
                'windbreak_stand',
                'spring_path',
                'tranquility_cove',
                'lunkers_lair',
                'seagrass_haven',
                'tombolo_walk',
                'whiteout_valley',
                'bonechill_wastes',
                'arenas_approach',
                'avalanche_slopes',
                'icebound_falls',
                'hearts_crag',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'veilstone_cape',
            'ancient_lake_acuity',
        ],
        evolution: [
            {
                prev: 'Burmy (Trash)',
                level: 20,
            },
        ],
    },
    'Mothim': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'gruelling_grove',
                'aipom_hill',
                'spring_path',
                'wayward_wood',
            ],
        },
        dungeons: [
            'veilstone_cape',
        ],
        evolution: [
            {
                prev: 'Burmy (Plant)',
                level: 20,
            },
            {
                prev: 'Burmy (Sand)',
                level: 20,
            },
            {
                prev: 'Burmy (Trash)',
                level: 20,
            },
        ],
        farm_wandering: ['Tanga Berry'],
    },
    'Combee': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'unova_route_12',
                'kalos_route_4',
                'rolling_fields',
                'honeycalm_island',
                'gruelling_grove',
                'cloudpool_ridge',
                'aipom_hill',
                'south_province_area_one',
                'south_province_area_two',
            ],
            headbutt: [
                'ramanas_island',
                'cottonsedge_prairie',
                'droning_meadow',
            ],
        },
        dungeons: [
            'lostlorn_forest',
            'heartwood',
        ],
        farm_wandering: ['Aspear Berry', 'Sitrus Berry', 'Pinap Berry', 'Iapapa Berry', 'Grepa Berry', 'Nomel Berry', 'Wacan Berry', 'Shuca Berry', 'Charti Berry', 'Chilan Berry', 'Jaboca Berry', 'Kee Berry'],
        shops: [
            ('pal_park', 'questPoint'),
        ],
        special: [
            Has('Combee') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Vespiquen': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'unova_route_12',
                'rolling_fields',
                'south_province_area_two',
            ],
            headbutt: [
                'cottonsedge_prairie',
                'droning_meadow',
            ],
        },
        evolution: [
            {
                prev: 'Combee',
                level: 21,
            },
        ],
        special: [
            Has('Vespiquen') & make_rule('lostlorn_forest', False),
            Has('Vespiquen') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Pachirisu': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_12',
                'cottonsedge_prairie',
                'south_province_area_one',
            ],
            headbutt: [
                'droning_meadow',
                'gapejaw_bog',
                'ursas_ring',
                'holm_of_trials',
            ],
        },
        dungeons: [
            'pikachu_valley',
        ],
        egg: 'Electric Egg',
        farm_wandering: ['Wacan Berry'],
    },
    'Buizel': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_205',
                'sinnoh_route_213',
                'sinnoh_route_212',
                'horseshoe_plains',
                'windswept_run',
                'ginkgo_landing',
                'aipom_hill',
                'bathers_lagoon',
                'poco_path',
                'south_province_area_one',
            ],
            water: [
                'unova_route_14',
                'unova_route_11',
                'unova_route_23',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'victory_road_unova',
        ],
        egg: 'Water Egg',
    },
    'Floatzel': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_218',
                'sinnoh_route_221',
                'sinnoh_route_222',
                'sinnoh_route_224',
                'sinnoh_route_230',
                'kalos_route_16',
                'kalos_route_21',
                'ginkgo_landing',
                'aipom_hill',
                'bathers_lagoon',
            ],
            water: [
                'kalos_route_15',
            ],
        },
        dungeons: [
            'victory_road_sinnoh',
            'frost_cavern',
            'victory_road_kalos',
            'temple_of_sinnoh',
        ],
        evolution: [
            {
                prev: 'Buizel',
                level: 26,
            },
        ],
    },
    'Cherubi': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'galar_route_3',
            ],
            headbutt: [
                'rolling_fields',
                'dappled_grove',
                'giants_seat',
                'north_lake_miloch',
                'axews_eye',
                'watchtower_ruins',
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
                'giants_cap',
                'lake_of_outrage',
                'lonely_spring',
                'bolderoll_ravine',
            ],
        },
        dungeons: [
            'primeval_grotto',
        ],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        shops: [
            ('pal_park', 'questPoint'),
        ],
    },
    'Cherrim (Overcast)': {
        native_region: 'Sinnoh',
        routes: {
            headbutt: [
                'lonely_spring',
                'bolderoll_ravine',
            ],
        },
        dungeons: [
            'primeval_grotto',
        ],
        evolution: [
            {
                prev: 'Cherubi',
                level: 25,
            },
        ],
        special: [
            Has('Cherrim (Overcast)') & make_rule('unova_route_12'),
        ],
    },
    'Cherrim (Sunshine)': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Cherrim (Overcast)',
                level: 1,
                weather: ['Harsh Sunlight'],
            },
        ],
        special: [
            Has('Cherrim (Sunshine)') & make_rule('unova_route_12'),
        ],
    },
    'Shellos (West)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_205',
                'sinnoh_route_221',
                'sandgem_flats',
                'ramanas_island',
            ],
            water: [
                'sinnoh_route_218',
            ],
        },
    },
    'Shellos (East)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_213',
                'sinnoh_route_212',
                'motostoke_riverbank',
                'bridge_field',
                'stony_wilderness',
                'giants_mirror',
                'giants_cap',
                'tranquility_cove',
                'seagrass_haven',
            ],
        },
        dungeons: [
            'galar_mine_no_2',
        ],
    },
    'Gastrodon (West)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_218',
                'sinnoh_route_221',
                'sandgem_flats',
                'ramanas_island',
            ],
            water: [
                'sinnoh_route_205',
            ],
        },
        evolution: [
            {
                prev: 'Shellos (West)',
                level: 30,
            },
        ],
    },
    'Gastrodon (East)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_222',
                'sinnoh_route_224',
                'poni_wilds',
                'ancient_poni_path',
                'poni_breaker_coast',
                'giants_mirror',
                'galar_route_9',
                'circhester_bay',
                'seagrass_haven',
            ],
            water: [
                'sinnoh_route_213',
                'sinnoh_route_212',
            ],
        },
        dungeon_boss: [
            ('galar_mine_no_2', 106473200),
        ],
        evolution: [
            {
                prev: 'Shellos (East)',
                level: 30,
            },
        ],
        special: [
            make_rule('exeggutor_island_hill', False) & make_rule('emissary_of_light2'),
        ],
    },
    'Ambipom': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'poni_plains',
                'aipom_hill',
                'avalanche_slopes',
                'hearts_crag',
            ],
        },
        evolution: [
            {
                prev: 'Aipom',
                level: 32,
            },
        ],
    },
    'Drifloon': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_8',
                'south_lake_miloch',
                'north_lake_miloch',
                'watchtower_ruins',
                'galar_route_5',
                'fields_of_honor',
                'challenge_beach',
                'loop_lagoon',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
                'aspiration_hill',
                'horseshoe_plains',
                'deertrack_path',
                'windswept_run',
                'ramanas_island',
                'crossing_slope',
                'ginkgo_landing',
                'bathers_lagoon',
                'deadwood_haunt',
                'sands_reach',
                'tranquility_cove',
                'lunkers_lair',
                'bonechill_wastes',
                'hearts_crag',
                'glacier_terrace',
                'south_province_area_three',
            ],
            water: [
                'seagrass_haven',
            ],
        },
        dungeons: [
            'floaro_gardens',
            'avaluggs_legacy',
        ],
        dungeon_boss: [
            ('hauoli_cemetery', 28968625),
        ],
        farm_wandering: ['Kasib Berry'],
        dream_orbs: ['Green'],
        special: [
            make_rule('valley_windworks', True, 3803000),
        ],
    },
    'Drifblim': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'unova_route_13',
                'unova_route_14',
                'south_lake_miloch',
                'north_lake_miloch',
                'axews_eye',
                'watchtower_ruins',
                'challenge_beach',
                'training_lowlands',
                'challenge_road',
                'sandgem_flats',
                'ramanas_island',
                'crossing_slope',
                'bathers_lagoon',
                'deadwood_haunt',
                'sands_reach',
                'tranquility_cove',
                'lunkers_lair',
                'bonechill_wastes',
                'hearts_crag',
                'glacier_terrace',
            ],
            water: [
                'seagrass_haven',
            ],
        },
        dungeons: [
            'reversal_mountain',
            'avaluggs_legacy',
            'ancient_lake_verity',
            'turnback_cave',
        ],
        evolution: [
            {
                prev: 'Drifloon',
                level: 28,
            },
        ],
    },
    'Buneary': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'alola_route_1',
                'poni_grove',
                'fields_of_honor',
                'challenge_beach',
                'bonechill_wastes',
                'arenas_approach',
                'snowfall_hot_spring',
            ],
        },
        dungeons: [
            'eterna_forest',
            'heartwood',
        ],
    },
    'Lopunny': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'challenge_beach',
                'bonechill_wastes',
                'arenas_approach',
                'snowfall_hot_spring',
            ],
        },
        evolution: [
            {
                prev: 'Buneary',
                item: 'Soothe Bell',
            },
        ],
    },
    'Mega Lopunny': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Lopunny',
                item: 'Lopunnite',
            },
        ],
    },
    'Mismagius': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'stonetooth_rows',
            ],
        },
        dungeon_boss: [
            ('turnback_cave', 10000000),
        ],
        evolution: [
            {
                prev: 'Misdreavus',
                item: 'Dusk Stone',
            },
        ],
    },
    'Mismagius (Illusion)': {
        native_region: 'Sinnoh',
        special: [
            Has('Mismagius') & make_rule('battle_frontier', 2000),
            Has('Mismagius (Illusion)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Honchkrow': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'cloudpool_ridge',
            ],
        },
        evolution: [
            {
                prev: 'Murkrow',
                item: 'Dusk Stone',
            },
        ],
    },
    'Glameow': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_218',
                'sinnoh_route_222',
                'crossing_slope',
            ],
        },
        dungeons: [
            'veilstone_cape',
        ],
    },
    'Purugly': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_222',
                'sinnoh_route_229',
                'crossing_slope',
            ],
        },
        dungeon_boss: [
            ('veilstone_cape', 10000000),
        ],
        evolution: [
            {
                prev: 'Glameow',
                level: 38,
            },
        ],
    },
    'Chingling': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_211',
                'kalos_route_11',
            ],
        },
        dungeons: [
            'mt_coronet_south',
            'mt_coronet_north',
            'spear_pillar',
            'distortion_world',
            'sendoff_spring',
            'reflection_cave',
            'sacred_plaza',
            'ancient_lake_acuity',
        ],
        farm_wandering: ['Payapa Berry'],
        breeding: ['Chimecho'],
    },
    'Stunky': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_206',
                'sinnoh_route_214',
                'sinnoh_route_221',
                'kalos_route_11',
                'dappled_grove',
                'south_lake_miloch',
                'north_lake_miloch',
                'galar_route_3',
                'giants_cap',
                'scarlet_bog',
            ],
        },
        dungeons: [
            'ancient_solaceon_ruins',
            'ancient_quarry',
        ],
        egg: 'Mystery Egg',
        farm_wandering: ['Colbur Berry'],
    },
    'Skuntank': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_221',
                'sinnoh_route_225',
                'south_lake_miloch',
                'north_lake_miloch',
                'lake_of_outrage',
                'scarlet_bog',
            ],
        },
        dungeons: [
            'ancient_quarry',
        ],
        evolution: [
            {
                prev: 'Stunky',
                level: 34,
            },
        ],
    },
    'Bronzor': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_211',
                'giants_seat',
                'south_lake_miloch',
                'bridge_field',
                'stony_wilderness',
                'giants_foot',
                'three_point_pass',
                'stonetooth_rows',
                'south_province_area_two',
                'south_province_area_three',
            ],
            headbutt: [
                'wayward_wood',
                'lonely_spring',
                'sonorous_path',
            ],
        },
        dungeons: [
            'solaceon_ruins',
            'mt_coronet_north',
            'distortion_world',
            'abundant_shrine',
            'ancient_quarry',
            'primeval_grotto',
            'clamberclaw_cliffs',
            'ancient_snowpoint_temple',
        ],
        dungeon_boss: [
            ('wayward_cave', 4400000),
            ('mt_coronet_south', 4000000),
        ],
        egg: 'Mystery Egg',
        farm_wandering: ['Babiri Berry'],
        dream_orbs: ['Green'],
    },
    'Bronzong': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'east_lake_axewell',
                'giants_seat',
                'axews_eye',
                'bridge_field',
                'stony_wilderness',
                'lake_of_outrage',
                'galar_route_8',
                'giants_bed',
                'giants_foot',
                'three_point_pass',
                'stonetooth_rows',
            ],
        },
        dungeons: [
            'spear_pillar',
            'distortion_world',
            'energy_plant',
            'iron_ruins',
            'split_decision_ruins',
            'ancient_snowpoint_temple',
            'temple_of_sinnoh',
        ],
        dungeon_boss: [
            ('abundant_shrine', 38000000),
            ('ancient_quarry', 10000000),
            ('clamberclaw_cliffs', 10000000),
        ],
        evolution: [
            {
                prev: 'Bronzor',
                level: 33,
            },
        ],
    },
    'Bonsly': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'alola_route_5',
                'bridge_field',
                'stony_wilderness',
                'south_province_area_one',
                'south_province_area_two',
            ],
            headbutt: [
                'diamond_heath',
            ],
        },
        dungeons: [
            'lush_jungle',
            'celestica_ruins',
        ],
        farm_wandering: ['Charti Berry'],
        breeding: ['Sudowoodo'],
        special: [
            make_rule('roamer', 'Hoenn - Orre') & make_rule('completed_gale_of_darkness'),
        ],
    },
    'Mime Jr.': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'rolling_fields',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
                'horseshoe_plains',
                'sandgem_flats',
            ],
        },
        dungeons: [
            'reflection_cave',
            'trainers_school',
        ],
        breeding: ['Mr. Mime', 'Galarian Mr. Mime', 'Mr. Rime'],
    },
    'Happiny': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'challenge_road',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_island',
                'hideaway_bay',
                'tombolo_walk',
                'avalanche_slopes',
                'south_province_area_one',
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'oreburrow_tunnel',
        ],
        breeding: ['Chansey', 'Blissey'],
    },
    'Handout Happiny': {
        native_region: 'Sinnoh',
        breeding: ['Charity Chansey', 'Blessing Blissey'],
        special: [
            Has('Handout Happiny') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Chatot': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_213',
                'sinnoh_route_218',
                'sinnoh_route_222',
                'sinnoh_route_224',
                'kalos_route_12',
                'azure_bay',
                'deadwood_haunt',
            ],
        },
        farm_wandering: ['Coba Berry'],
    },
    'Spiritomb': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('shrouded_ruins', 10000000),
            ('glaseado_mountain', 161099869),
        ],
        trades: [
            ('solaceon_town', ['Odd Keystone']),
        ],
        special: [
            Has('Spiritomb') & make_rule('ballimere_lake'),
        ],
    },
    'Gible': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_13',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'tunnel_to_the_top',
            'ancient_wayward_cave',
            'clamberclaw_cliffs',
            'area_zero_depths',
        ],
        egg: 'Dragon Egg',
        farm_wandering: ['Haban Berry'],
        special: [
            Has('Gible') & make_rule('wayward_cave', False),
        ],
    },
    'Gabite': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'haina_desert',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'turnback_cave',
            'area_zero_depths',
        ],
        dungeon_boss: [
            ('clamberclaw_cliffs', 10000000),
        ],
        evolution: [
            {
                prev: 'Gible',
                level: 24,
            },
        ],
        egg: 'Dragon Egg',
        special: [
            Has('Gabite') & make_rule('victory_road_sinnoh', False),
        ],
    },
    'Garchomp': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'path_to_the_peak',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'hall_of_origin',
            'temple_of_sinnoh',
        ],
        dungeon_boss: [
            ('tunnel_to_the_top', 167825980),
            ('turnback_cave', 10000000),
        ],
        evolution: [
            {
                prev: 'Gabite',
                level: 48,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Mega Garchomp': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Garchomp',
                item: 'Garchompite',
            },
        ],
    },
    'Munchlax': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'motostoke_riverbank',
                'deertrack_path',
                'arenas_approach',
                'snowfall_hot_spring',
            ],
            headbutt: [
                'ballimere_lake',
            ],
        },
        farm_wandering: ['Chilan Berry'],
        breeding: ['Snorlax', 'Gigantamax Snorlax'],
    },
    'Elf Munchlax': {
        native_region: 'Sinnoh',
        trades: [
            ('sandgem_town', ['Meadow Plate', 'Pixie Plate']),
        ],
    },
    'Riolu': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_22',
                'poni_grove',
                'giants_cap',
                'arenas_approach',
                'icebound_falls',
                'snowfall_hot_spring',
            ],
        },
        dungeons: [
            'roaring_sea_caves',
        ],
        dungeon_boss: [
            ('floccesy_ranch', 13000000),
        ],
        egg: 'Fighting Egg',
        farm_wandering: ['Chople Berry'],
        dream_orbs: ['Pink'],
        breeding: ['Lucario', 'Mega Lucario'],
    },
    'Lucario': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'north_lake_miloch',
                'arenas_approach',
                'icebound_falls',
                'snowfall_hot_spring',
            ],
        },
        dungeons: [
            'temple_of_sinnoh',
        ],
        dungeon_boss: [
            ('roaring_sea_caves', 160924440),
        ],
        evolution: [
            {
                prev: 'Riolu',
                item: 'Soothe Bell',
                time: 'day',
            },
        ],
    },
    'Mega Lucario': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Lucario',
                item: 'Lucarionite',
            },
        ],
    },
    'Hippopotas': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_9',
                'galar_route_6',
                'scarlet_bog',
                'gapejaw_bog',
                'celestica_trail',
            ],
        },
        dungeons: [
            'solaceon_ruins',
        ],
        farm_wandering: ['Shuca Berry'],
    },
    'Hippowdon': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_228',
                'giants_mirror',
                'lake_of_outrage',
                'galar_route_8',
                'scarlet_bog',
                'gapejaw_bog',
                'celestica_trail',
            ],
        },
        evolution: [
            {
                prev: 'Hippopotas',
                level: 34,
            },
        ],
    },
    'Skorupi': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_14',
                'kalos_route_15',
                'kalos_route_16',
                'motostoke_riverbank',
                'giants_mirror',
                'galar_route_6',
                'soothing_wetlands',
                'ginkgo_landing',
                'castaway_shore',
            ],
        },
        dungeons: [
            'reversal_mountain',
        ],
        safari: ['Sinnoh'],
        farm_wandering: ['Kebia Berry'],
    },
    'Drapion': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_19',
                'motostoke_riverbank',
                'bridge_field',
                'lake_of_outrage',
                'galar_route_8',
                'soothing_wetlands',
                'challenge_beach',
                'training_lowlands',
                'castaway_shore',
            ],
        },
        evolution: [
            {
                prev: 'Skorupi',
                level: 40,
            },
        ],
        safari: ['Sinnoh'],
    },
    'Croagunk': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_212',
                'unova_route_8',
                'kalos_route_7',
                'motostoke_outskirts',
                'bridge_field',
                'stony_wilderness',
                'giants_cap',
                'soothing_wetlands',
                'forest_of_focus',
                'scarlet_bog',
                'gapejaw_bog',
                'holm_of_trials',
            ],
        },
        dungeons: [
            'moor_of_icirrus',
            'galar_mine_no_2',
            'ancient_solaceon_ruins',
            'ancient_quarry',
        ],
        egg: 'Fighting Egg',
        safari: ['Sinnoh'],
    },
    'Toxicroak': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'training_lowlands',
                'challenge_road',
                'holm_of_trials',
                'spring_path',
            ],
        },
        dungeons: [
            'pinwheel_forest',
            'ancient_quarry',
        ],
        evolution: [
            {
                prev: 'Croagunk',
                level: 37,
            },
        ],
        safari: ['Sinnoh'],
    },
    'Carnivine': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'unova_route_18',
                'kalos_route_14',
                'kalos_route_19',
                'golden_lowlands',
                'cloudpool_ridge',
                'gapejaw_bog',
                'holm_of_trials',
                'lonely_spring',
            ],
        },
        dungeons: [
            'ancient_solaceon_ruins',
            'shrouded_ruins',
        ],
        safari: ['Sinnoh'],
    },
    'Finneon': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_219',
                'sinnoh_route_220',
                'melemele_sea',
                'alola_route_14',
            ],
            water: [
                'sinnoh_route_205',
                'sinnoh_route_218',
                'sinnoh_route_221',
                'route_1_hauoli_outskirts',
                'kalae_bay',
                'alola_route_7',
                'alola_route_8',
                'alola_route_15',
                'seagrass_haven',
            ],
        },
        dungeons: [
            'iron_island',
            'p2_laboratory',
            'brooklet_hill',
        ],
        egg: 'Water Egg',
    },
    'Lumineon': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_219',
                'sinnoh_route_220',
                'poni_breaker_coast',
            ],
            water: [
                'sinnoh_route_205',
                'sinnoh_route_218',
                'sinnoh_route_221',
                'seagrass_haven',
            ],
        },
        dungeons: [
            'temple_of_sinnoh',
        ],
        dungeon_boss: [
            ('ruins_of_hope', 82177450),
        ],
        evolution: [
            {
                prev: 'Finneon',
                level: 31,
            },
        ],
    },
    'Mantyke': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_223',
                'undella_bay',
                'unova_route_21',
                'melemele_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
            water: [
                'kalos_route_12',
                'azure_bay',
                'route_1_hauoli_outskirts',
                'kalae_bay',
                'alola_route_8',
                'motostoke_riverbank',
                'lake_of_outrage',
                'galar_route_9',
                'circhester_bay',
                'fields_of_honor',
                'workout_sea',
                'tranquility_cove',
            ],
        },
        breeding: ['Mantine'],
    },
    'Snover': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'sinnoh_route_216',
                'sinnoh_route_217',
                'kalos_route_17',
                'dappled_grove',
                'east_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'axews_eye',
                'watchtower_ruins',
                'giants_mirror',
                'giants_cap',
                'steamdrift_way',
                'white_hill_station',
                'galar_route_10',
                'frostpoint_field',
                'bonechill_wastes',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'mt_coronet_north',
            'lake_acuity',
            'spear_pillar',
        ],
        egg: 'Grass Egg',
        farm_wandering: ['Yache Berry'],
    },
    'Snover (Berry)': {
        native_region: 'Sinnoh',
        farm_wandering: ['Snover Berry'],
    },
    'Abomasnow': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'kalos_route_17',
                'giants_seat',
                'axews_eye',
                'giants_mirror',
                'lake_of_outrage',
                'hammerlocke_hills',
                'galar_route_10',
                'slippery_slope',
                'frostpoint_field',
                'bonechill_wastes',
                'glacier_terrace',
            ],
        },
        dungeons: [
            'spear_pillar',
        ],
        dungeon_boss: [
            ('crown_shrine', 161099869),
        ],
        evolution: [
            {
                prev: 'Snover',
                level: 40,
            },
        ],
        special: [
            make_rule('a_beautiful_world17') & make_rule('frost_cavern', True, 85376500),
        ],
    },
    'Mega Abomasnow': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Abomasnow',
                item: 'Abomasite',
            },
        ],
    },
    'Weavile': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'bridge_field',
                'slippery_slope',
                'frostpoint_field',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'iceberg_ruins',
            'icerend_shrine',
            'area_zero',
        ],
        dungeon_boss: [
            ('crown_shrine', 161099869),
        ],
        evolution: [
            {
                prev: 'Sneasel',
                item: 'Razor Claw',
                time: 'night',
            },
        ],
    },
    'Magnezone': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'challenge_beach',
                'loop_lagoon',
                'insular_sea',
            ],
        },
        dungeons: [
            'temple_of_sinnoh',
        ],
        evolution: [
            {
                prev: 'Magneton',
                level: 20,
                environment: 'MagneticField',
            },
            {
                prev: 'Magneton',
                item: 'Thunder Stone',
                region: 'galarOnly',
            },
        ],
        special: [
            make_rule('p2_laboratory', True, 58000000),
        ],
    },
    'Lickilicky': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'soothing_wetlands',
                'avalanche_slopes',
            ],
        },
        dungeon_boss: [
            ('shrouded_ruins', 10000000),
        ],
        evolution: [
            {
                prev: 'Lickitung',
                level: 33,
            },
        ],
    },
    'Rhyperior': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'potbottom_desert',
            ],
        },
        dungeons: [
            'rock_peak_ruins',
        ],
        evolution: [
            {
                prev: 'Rhydon',
                item: 'Protector',
            },
        ],
    },
    'Tangrowth': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'forest_of_focus',
                'gapejaw_bog',
            ],
        },
        evolution: [
            {
                prev: 'Tangela',
                level: 33,
            },
        ],
        special: [
            make_rule('ghetsis2') & make_rule('giant_chasm', True, 30000000),
        ],
    },
    'Electivire': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'giants_bed',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'cloudcap_pass',
            ],
        },
        dungeon_boss: [
            ('split_decision_ruins', 156135635),
        ],
        evolution: [
            {
                prev: 'Electabuzz',
                item: 'Electirizer',
            },
        ],
    },
    'Magmortar': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'slippery_slope',
                'giants_bed',
                'frigid_sea',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        evolution: [
            {
                prev: 'Magmar',
                item: 'Magmarizer',
            },
        ],
    },
    'Togekiss': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'poni_gauntlet',
            ],
        },
        dungeons: [
            'ancient_lake_verity',
        ],
        evolution: [
            {
                prev: 'Togetic',
                item: 'Shiny Stone',
            },
        ],
    },
    'Spooky Togekiss': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Spooky Togetic',
                item: 'Dusk Stone',
            },
        ],
    },
    'Yanmega': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'unova_route_3',
                'heavenward_lookout',
            ],
        },
        evolution: [
            {
                prev: 'Yanma',
                level: 33,
            },
        ],
        special: [
            Has('Yanmega') & make_rule('pinwheel_forest', False),
            Has('Yanmega') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Leafeon': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                level: 20,
                environment: 'MossRock',
            },
            {
                prev: 'Eevee',
                item: 'Leaf Stone',
                region: 'galarOnly',
            },
        ],
    },
    'Glaceon': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                level: 20,
                environment: 'IceRock',
            },
            {
                prev: 'Eevee',
                item: 'Ice Stone',
                region: 'galarOnly',
            },
        ],
    },
    'Gliscor': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('primeval_grotto', 10000000),
        ],
        evolution: [
            {
                prev: 'Gligar',
                item: 'Razor Fang',
                time: 'night',
            },
        ],
    },
    'Mamoswine': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'slippery_slope',
            ],
        },
        dungeons: [
            'crown_shrine',
        ],
        dungeon_boss: [
            ('avaluggs_legacy', 10000000),
        ],
        evolution: [
            {
                prev: 'Piloswine',
                level: 53,
            },
        ],
        special: [
            make_rule('ghetsis2') & make_rule('giant_chasm', True, 32000000),
        ],
    },
    'Porygon-Z': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Porygon2',
                item: 'Dubious Disc',
            },
        ],
    },
    'Gallade': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'bridge_field',
                'challenge_road',
            ],
        },
        dungeon_boss: [
            ('ancient_snowpoint_temple', 10000000),
        ],
        evolution: [
            {
                prev: 'Kirlia',
                item: 'Dawn Stone',
            },
        ],
    },
    'Mega Gallade': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Gallade',
                item: 'Galladite',
            },
        ],
    },
    'Probopass': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('primeval_grotto', 10000000),
        ],
        evolution: [
            {
                prev: 'Nosepass',
                level: 20,
                environment: 'MagneticField',
            },
        ],
    },
    'Dusknoir': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'stony_wilderness',
                'deadwood_haunt',
            ],
        },
        dungeon_boss: [
            ('turnback_cave', 10000000),
        ],
        evolution: [
            {
                prev: 'Dusclops',
                item: 'Reaper Cloth',
            },
        ],
    },
    'Froslass': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'slippery_slope',
                'giants_bed',
                'old_cemetery',
                'snowslide_slope',
                'bonechill_wastes',
                'avalanche_slopes',
            ],
        },
        dungeons: [
            'iceberg_ruins',
            'avaluggs_legacy',
            'ancient_snowpoint_temple',
        ],
        dungeon_boss: [
            ('tunnel_to_the_top', 167825980),
            ('ice_column_chamber', 10000000),
            ('turnback_cave', 10000000),
        ],
        evolution: [
            {
                prev: 'Snorunt',
                item: 'Dawn Stone',
            },
        ],
    },
    'Rotom': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'poni_gauntlet',
                'lake_of_outrage',
                'workout_sea',
                'stonetooth_rows',
            ],
        },
        dungeons: [
            'sacred_plaza',
            'turnback_cave',
        ],
        dungeon_boss: [
            ('old_chateau', 4200000),
            ('lost_hotel', 82376500),
        ],
        dream_orbs: ['Orange'],
    },
    'Rotom (Heat)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'workout_sea',
            ],
        },
        dungeon_chest: [
            'lost_hotel',
        ],
        special: [
            Has('Rotom') & make_rule('team_galactic_eterna_building', True, 4300000),
        ],
    },
    'Rotom (Wash)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'workout_sea',
            ],
        },
        dungeon_chest: [
            'lost_hotel',
        ],
        special: [
            Has('Rotom') & make_rule('team_galactic_eterna_building', True, 4300000),
        ],
    },
    'Rotom (Frost)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'workout_sea',
            ],
        },
        dungeon_chest: [
            'lost_hotel',
        ],
        special: [
            Has('Rotom') & make_rule('team_galactic_eterna_building', True, 4300000),
        ],
    },
    'Rotom (Fan)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'workout_sea',
            ],
        },
        dungeon_chest: [
            'lost_hotel',
        ],
        special: [
            Has('Rotom') & make_rule('team_galactic_eterna_building', True, 4300000),
        ],
    },
    'Rotom (Mow)': {
        native_region: 'Sinnoh',
        routes: {
            land: [
                'workout_sea',
            ],
        },
        dungeon_chest: [
            'lost_hotel',
        ],
        special: [
            Has('Rotom') & make_rule('team_galactic_eterna_building', True, 4300000),
        ],
    },
    'Rotom (Discord)': {
        native_region: 'Sinnoh',
        special: [
            Has('Rotom (Discord)') & make_rule('workout_sea'),
            Has('Rotom') & Has('Rotom (Discord)') & make_rule('team_galactic_eterna_building', True, 4300000),
            make_rule('lost_hotel', False) & Has('Rotom (Discord)'),
        ],
    },
    'Uxie': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('cave_of_being', 35000000),
        ],
        special: [
            make_rule('completed_a_new_world') & make_rule('lake_acuity', True, 10070000),
            {
                dungeon: 'ancient_lake_acuity',
                rule: make_rule('ancient_lake_acuity', True, 10000000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
        ],
    },
    'Mesprit': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('cave_of_being', 35000000),
        ],
        special: [
            {
                dungeon: 'ancient_lake_verity',
                rule: make_rule('ancient_lake_verity', True, 10000000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
            make_rule('roamer', 'Sinnoh') & make_rule('distortion_world', True),
        ],
    },
    'Azelf': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('cave_of_being', 35000000),
        ],
        special: [
            make_rule('completed_a_new_world') & make_rule('lake_valor', True, 10060000),
            {
                dungeon: 'ancient_lake_valor',
                rule: make_rule('ancient_lake_valor', True, 10000000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
        ],
    },
    'Dialga': {
        native_region: 'Sinnoh',
        special: [
            Has('Elite Sinnoh Champion Badge') & make_rule('spear_pillar', True, 11880000),
        ],
    },
    'Dialga (Origin)': {
        native_region: 'Hisui',
        special: [
            {
                dungeon: 'temple_of_sinnoh',
                rule: make_rule('temple_of_sinnoh', True, 11880000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
        ],
    },
    'Palkia': {
        native_region: 'Sinnoh',
        special: [
            Has('Elite Sinnoh Champion Badge') & make_rule('spear_pillar', True, 11880000),
        ],
    },
    'Palkia (Origin)': {
        native_region: 'Hisui',
        special: [
            {
                dungeon: 'temple_of_sinnoh',
                rule: make_rule('temple_of_sinnoh', True, 11880000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
        ],
    },
    'Heatran': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('stark_mountain', 11000000),
        ],
        special: [
            Has('Elite Unova Champion Badge') & make_rule('reversal_mountain', True, 30000000),
            {
                dungeon: 'firespit_island',
                rule: make_rule('firespit_island', True, 10000000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
        ],
    },
    'Regigigas': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('snowpoint_temple', 11000000),
            ('twist_mountain', 50000000),
        ],
        temporary_battle: [
            'regigigas',
        ],
        special: [
            {
                dungeon: 'ancient_snowpoint_temple',
                rule: make_rule('ancient_snowpoint_temple', True, 10000000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
        ],
    },
    'Giratina (Altered)': {
        native_region: 'Sinnoh',
        special: [
            make_rule('zeros_ambition13') & make_rule('distortion_world', True, 11880000),
        ],
    },
    'Giratina (Origin)': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('turnback_cave', 10000000),
        ],
        evolution: [
            {
                prev: 'Giratina (Altered)',
                level: 70,
                item: 'Griseous Orb',
            },
        ],
    },
    'Cresselia': {
        native_region: 'Sinnoh',
        special: [
            {
                dungeon: 'fullmoon_island',
                rule: make_rule('fullmoon_island', True, 11000000),
                requirements: [
                    {
                        type: 'CustomRequirement',
                        args: [
                            'ko.pureComputed(() => cresseliaDungeonMoonReq.isCompleted())',
                            'true',
                            'Cresselia lives on the island around New Moon, and roams Sinnoh during other moon phases.',
                        ],
                    },
                ],
            },
            make_rule('roamer', 'Sinnoh') & make_rule('fullmoon_island', True),
        ],
    },
    'Phione': {
        native_region: 'Sinnoh',
        dungeons: [
            'seaside_hollow',
        ],
        breeding: ['Manaphy'],
    },
    'Manaphy': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('seaside_hollow', 10000000),
        ],
        farm_wandering: ['Liechi Berry'],
        temporary_battle: [
            'manaphy_egg_protectors',
        ],
        special: [
            make_rule('roamer', 'Sinnoh') & make_rule('completed_recover_the_precious_egg'),
        ],
    },
    'Darkrai': {
        native_region: 'Sinnoh',
        special: [
            {
                dungeon: 'newmoon_island',
                rule: make_rule('newmoon_island', True, 11000000),
                requirements: [
                    {
                        type: 'CustomRequirement',
                        args: [
                            'ko.pureComputed(() => darkraiDungeonMoonReq.isCompleted())',
                            'true',
                            'Darkrai roams Sinnoh around New Moon, and lives on the island during other moon phases.',
                        ],
                    },
                ],
            },
            {
                dungeon: 'clamberclaw_cliffs',
                rule: make_rule('clamberclaw_cliffs', True, 10000000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
            make_rule('roamer', 'Sinnoh') & make_rule('newmoon_island', True),
        ],
    },
    'Shaymin (Land)': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('flower_paradise', 11000000),
        ],
        special: [
            {
                dungeon: 'floaro_gardens',
                rule: make_rule('floaro_gardens', True, 10000000),
                requirements: [
                    {
                        type: 'DevelopmentRequirement',
                        args: [
                        ],
                    },
                ],
            },
        ],
    },
    'Shaymin (Sky)': {
        native_region: 'Sinnoh',
        evolution: [
            {
                prev: 'Shaymin (Land)',
                level: 20,
                item: 'Gracidea',
            },
        ],
        special: [
            Has('Shaymin (Sky)') & make_rule('flower_paradise', True, 11000000),
        ],
    },
    'Arceus (Normal)': {
        native_region: 'Sinnoh',
        dungeon_boss: [
            ('hall_of_origin', 13000000),
        ],
    },
    'Victini': {
        native_region: 'Unova',
        dungeon_boss: [
            ('liberty_garden', 14000000),
        ],
    },
    'Snivy': {
        native_region: 'Unova',
        egg: 'Grass Egg',
        starter: ['Unova'],
        farm_wandering: ['Rindo Berry'],
    },
    'Servine': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Snivy',
                level: 17,
            },
        ],
        special: [
            Has('Servine') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Serperior': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Servine',
                level: 36,
            },
        ],
        special: [
            make_rule('emissary_of_light2') & make_rule('exeggutor_island_hill', True, 78865330),
        ],
    },
    'Tepig': {
        native_region: 'Unova',
        egg: 'Fire Egg',
        starter: ['Unova'],
        farm_wandering: ['Occa Berry'],
    },
    'Pignite': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Tepig',
                level: 17,
            },
        ],
        special: [
            Has('Pignite') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Emboar': {
        native_region: 'Unova',
        routes: {
            land: [
                'ancient_poni_path',
            ],
        },
        evolution: [
            {
                prev: 'Pignite',
                level: 36,
            },
        ],
    },
    'Oshawott': {
        native_region: 'Unova',
        egg: 'Water Egg',
        starter: ['Unova'],
        farm_wandering: ['Passho Berry'],
    },
    'Dewott': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Oshawott',
                level: 17,
            },
        ],
        special: [
            Has('Dewott') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Samurott': {
        native_region: 'Unova',
        routes: {
            land: [
                'poni_wilds',
            ],
        },
        evolution: [
            {
                prev: 'Dewott',
                level: 36,
            },
        ],
    },
    'Hisuian Samurott': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Dewott',
                level: 36,
            },
        ],
        starter: ['Hisui'],
    },
    'Patrat': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_19',
                'unova_route_20',
            ],
        },
        dungeons: [
            'floccesy_ranch',
        ],
    },
    'Watchog': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_7',
                'unova_route_3',
                'unova_route_2',
                'unova_route_1',
                'unova_route_18',
                'kalos_route_15',
            ],
        },
        dungeons: [
            'dreamyard',
            'p2_laboratory',
        ],
        evolution: [
            {
                prev: 'Patrat',
                level: 20,
            },
        ],
    },
    'Lillipup': {
        native_region: 'Unova',
        routes: {
            land: [
                'alola_route_4',
                'alola_route_5',
                'alola_route_6',
                'training_lowlands',
            ],
        },
        dungeons: [
            'floccesy_ranch',
            'paniola_ranch',
        ],
    },
    'Herdier': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_3',
                'unova_route_2',
                'unova_route_1',
                'training_lowlands',
            ],
        },
        dungeons: [
            'p2_laboratory',
        ],
        evolution: [
            {
                prev: 'Lillipup',
                level: 16,
            },
        ],
    },
    'Stoutland': {
        native_region: 'Unova',
        routes: {
            land: [
                'training_lowlands',
            ],
        },
        evolution: [
            {
                prev: 'Herdier',
                level: 32,
            },
        ],
        special: [
            make_rule('p2_laboratory', True, 58000000),
        ],
    },
    'Purrloin': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_19',
                'unova_route_20',
                'unova_route_3',
                'galar_route_2',
                'west_lake_axewell',
                'east_lake_axewell',
                'north_lake_miloch',
                'watchtower_ruins',
                'motostoke_riverbank',
                'galar_route_2_lakeside',
            ],
        },
    },
    'Liepard': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_5',
                'unova_route_16',
                'unova_route_9',
                'unova_route_2',
                'kalos_route_15',
                'giants_seat',
                'north_lake_miloch',
                'axews_eye',
                'bridge_field',
                'giants_cap',
                'galar_route_7',
                'outer_spikemuth',
            ],
        },
        dungeons: [
            'dreamyard',
        ],
        evolution: [
            {
                prev: 'Purrloin',
                level: 20,
            },
        ],
    },
    'Pansage': {
        native_region: 'Unova',
        dungeons: [
            'santalune_forest',
        ],
        egg: 'Grass Egg',
    },
    'Simisage': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Pansage',
                item: 'Leaf Stone',
            },
        ],
    },
    'Pansear': {
        native_region: 'Unova',
        dungeons: [
            'santalune_forest',
        ],
        egg: 'Fire Egg',
    },
    'Simisear': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Pansear',
                item: 'Fire Stone',
            },
        ],
    },
    'Panpour': {
        native_region: 'Unova',
        dungeons: [
            'santalune_forest',
        ],
        egg: 'Water Egg',
    },
    'Simipour': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Panpour',
                item: 'Water Stone',
            },
        ],
    },
    'Munna': {
        native_region: 'Unova',
        routes: {
            land: [
                'rolling_fields',
                'dappled_grove',
                'east_lake_axewell',
                'giants_seat',
                'axews_eye',
                'bridge_field',
                'stony_wilderness',
                'giants_cap',
            ],
        },
        dungeons: [
            'dreamyard',
            'ruins_of_life',
            'slumbering_weald_shrine',
        ],
        dream_orbs: ['Pink'],
    },
    'Musharna': {
        native_region: 'Unova',
        routes: {
            land: [
                'giants_seat',
                'bridge_field',
            ],
        },
        evolution: [
            {
                prev: 'Munna',
                item: 'Moon Stone',
            },
        ],
    },
    'Pidove': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_20',
                'rolling_fields',
                'east_lake_axewell',
                'north_lake_miloch',
                'watchtower_ruins',
            ],
        },
        dungeons: [
            'floccesy_ranch',
            'liberty_garden',
        ],
    },
    'Tranquill': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
                'unova_route_7',
                'unova_route_12',
                'unova_route_3',
                'giants_seat',
                'bridge_field',
                'stony_wilderness',
                'giants_mirror',
            ],
        },
        dungeons: [
            'victory_road_unova',
            'dragonspiral_tower',
        ],
        evolution: [
            {
                prev: 'Pidove',
                level: 21,
            },
        ],
    },
    'Unfezant': {
        native_region: 'Unova',
        routes: {
            land: [
                'axews_eye',
                'stony_wilderness',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'victory_road_unova',
        ],
        dungeon_boss: [
            ('pledge_grove', 50000000),
        ],
        evolution: [
            {
                prev: 'Tranquill',
                level: 32,
            },
        ],
    },
    'Blitzle': {
        native_region: 'Unova',
        egg: 'Electric Egg',
        special: [
            Has('Blitzle') & make_rule('unova_route_3'),
        ],
    },
    'Zebstrika': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Blitzle',
                level: 27,
            },
        ],
        special: [
            Has('Zebstrika') & make_rule('unova_route_7'),
            Has('Zebstrika') & make_rule('unova_route_3'),
        ],
    },
    'Roggenrola': {
        native_region: 'Unova',
        routes: {
            land: [
                'rolling_fields',
                'motostoke_outskirts',
                'challenge_road',
            ],
        },
        dungeons: [
            'relic_passage',
            'reflection_cave',
            'ten_carat_hill',
            'galar_mine',
        ],
    },
    'Boldore': {
        native_region: 'Unova',
        routes: {
            land: [
                'stony_wilderness',
                'giants_mirror',
                'giants_cap',
                'lake_of_outrage',
                'galar_route_8',
            ],
        },
        dungeons: [
            'chargestone_cave',
            'mistralton_cave',
            'reversal_mountain',
            'seaside_cave',
            'victory_road_unova',
            'twist_mountain',
            'vast_poni_canyon',
        ],
        evolution: [
            {
                prev: 'Roggenrola',
                level: 25,
            },
        ],
    },
    'Gigalith': {
        native_region: 'Unova',
        dungeons: [
            'rock_peak_ruins',
        ],
        dungeon_boss: [
            ('dusty_bowl', 114616050),
            ('brawlers_cave', 135047520),
        ],
        evolution: [
            {
                prev: 'Boldore',
                item: 'Linking Cord',
            },
        ],
    },
    'Woobat': {
        native_region: 'Unova',
        routes: {
            land: [
                'watchtower_ruins',
                'bridge_field',
                'giants_mirror',
            ],
        },
        dungeons: [
            'relic_passage',
            'mistralton_cave',
            'reversal_mountain',
            'seaside_cave',
            'cave_of_being',
            'twist_mountain',
            'sea_spirits_den',
            'galar_mine',
            'brawlers_cave',
        ],
        safari: ['Kalos'],
    },
    'Swoobat': {
        native_region: 'Unova',
        routes: {
            land: [
                'challenge_beach',
                'training_lowlands',
            ],
        },
        dungeons: [
            'courageous_cavern',
            'brawlers_cave',
        ],
        evolution: [
            {
                prev: 'Woobat',
                item: 'Soothe Bell',
            },
        ],
    },
    'Drilbur': {
        native_region: 'Unova',
        routes: {
            land: [
                'stony_wilderness',
                'giants_mirror',
                'giants_cap',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'galar_mine',
        ],
        dungeon_boss: [
            ('relic_passage', 21000000),
            ('chargestone_cave', 22000000),
            ('mistralton_cave', 23000000),
        ],
        egg: 'Mystery Egg',
    },
    'Excadrill': {
        native_region: 'Unova',
        routes: {
            land: [
                'giants_mirror',
                'giants_cap',
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'iron_ruins',
        ],
        dungeon_boss: [
            ('reversal_mountain', 26000000),
        ],
        evolution: [
            {
                prev: 'Drilbur',
                level: 31,
            },
        ],
    },
    'Audino': {
        native_region: 'Unova',
        routes: {
            land: [
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
                'path_to_the_peak',
            ],
        },
        dungeons: [
            'p2_laboratory',
            'roaring_sea_caves',
            'lakeside_cave',
            'tunnel_to_the_top',
        ],
        dungeon_boss: [
            ('victory_road_unova', 45000000),
            ('dreamyard', 48000000),
        ],
        farm_wandering: ['Chilan Berry'],
        special: [
            make_rule('ghetsis2') & make_rule('giant_chasm', True, 32000000),
        ],
    },
    'Mega Audino': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Audino',
                item: 'Audinite',
            },
        ],
    },
    'Timburr': {
        native_region: 'Unova',
        dungeons: [
            'relic_passage',
            'galar_mine',
        ],
    },
    'Gurdurr': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_18',
                'stony_wilderness',
                'galar_route_8',
                'giants_bed',
                'giants_foot',
            ],
        },
        dungeons: [
            'cave_of_being',
            'victory_road_unova',
            'twist_mountain',
            'pinwheel_forest',
            'victory_road_kalos',
            'dusty_bowl',
        ],
        evolution: [
            {
                prev: 'Timburr',
                level: 25,
            },
        ],
    },
    'Conkeldurr': {
        native_region: 'Unova',
        routes: {
            land: [
                'poni_plains',
                'motostoke_riverbank',
                'giants_bed',
                'giants_foot',
            ],
        },
        evolution: [
            {
                prev: 'Gurdurr',
                item: 'Linking Cord',
            },
        ],
    },
    'Tympole': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_8',
                'dappled_grove',
                'west_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'watchtower_ruins',
            ],
        },
        dungeons: [
            'pinwheel_forest',
        ],
        egg: 'Water Egg',
    },
    'Palpitoad': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_8',
                'west_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'bridge_field',
                'giants_mirror',
                'giants_cap',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'moor_of_icirrus',
            'pinwheel_forest',
        ],
        evolution: [
            {
                prev: 'Tympole',
                level: 25,
            },
        ],
    },
    'Seismitoad': {
        native_region: 'Unova',
        routes: {
            land: [
                'dappled_grove',
                'north_lake_miloch',
                'axews_eye',
                'bridge_field',
                'giants_mirror',
                'giants_cap',
                'lake_of_outrage',
                'galar_route_7',
            ],
        },
        dungeon_boss: [
            ('moor_of_icirrus', 48000000),
            ('pinwheel_forest', 48000000),
        ],
        evolution: [
            {
                prev: 'Palpitoad',
                level: 36,
            },
        ],
    },
    'Throh': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_11',
                'motostoke_outskirts',
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
                'steamdrift_way',
            ],
        },
        egg: 'Fighting Egg',
        special: [
            Has('Throh') & make_rule('unova_route_23'),
            Has('Throh') & make_rule('unova_route_15'),
            Has('Throh') & make_rule('unova_route_18'),
            Has('Throh') & make_rule('victory_road_unova', False),
            Has('Throh') & make_rule('pinwheel_forest', False),
        ],
    },
    'Sawk': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_11',
                'motostoke_outskirts',
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
                'steamdrift_way',
            ],
        },
        egg: 'Fighting Egg',
        special: [
            Has('Sawk') & make_rule('unova_route_23'),
            Has('Sawk') & make_rule('unova_route_15'),
            Has('Sawk') & make_rule('unova_route_18'),
            Has('Sawk') & make_rule('victory_road_unova', False),
            Has('Sawk') & make_rule('pinwheel_forest', False),
        ],
    },
    'Sewaddle': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_20',
                'unova_route_12',
            ],
        },
        dungeons: [
            'lostlorn_forest',
        ],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        special: [
            Has('Sewaddle') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Swadloon': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
            ],
        },
        dungeons: [
            'pinwheel_forest',
        ],
        evolution: [
            {
                prev: 'Sewaddle',
                level: 20,
            },
        ],
        special: [
            Has('Swadloon') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Leavanny': {
        native_region: 'Unova',
        dungeon_boss: [
            ('poni_meadow', 83299840),
        ],
        evolution: [
            {
                prev: 'Swadloon',
                item: 'Soothe Bell',
            },
        ],
        special: [
            Has('Leavanny') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Venipede': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_20',
                'alola_route_4',
                'forest_of_focus',
            ],
        },
        dungeons: [
            'lostlorn_forest',
        ],
        special: [
            Has('Venipede') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Whirlipede': {
        native_region: 'Unova',
        dungeons: [
            'pinwheel_forest',
        ],
        evolution: [
            {
                prev: 'Venipede',
                level: 22,
            },
        ],
        special: [
            Has('Whirlipede') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Scolipede': {
        native_region: 'Unova',
        routes: {
            land: [
                'forest_of_focus',
            ],
        },
        dungeon_boss: [
            ('pinwheel_forest', 48000000),
        ],
        evolution: [
            {
                prev: 'Whirlipede',
                level: 30,
            },
        ],
        special: [
            Has('Scolipede') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Cottonee': {
        native_region: 'Unova',
        routes: {
            land: [
                'poni_plains',
                'stony_wilderness',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'lostlorn_forest',
            'abundant_shrine',
            'victory_road_unova',
            'pinwheel_forest',
            'melemele_meadow',
            'malie_garden',
            'ulaula_meadow',
            'ruins_of_abundance',
            'poni_meadow',
        ],
    },
    'Whimsicott': {
        native_region: 'Unova',
        routes: {
            land: [
                'ballimere_lake',
            ],
        },
        evolution: [
            {
                prev: 'Cottonee',
                item: 'Sun Stone',
            },
        ],
    },
    'Petilil': {
        native_region: 'Unova',
        routes: {
            land: [
                'poni_plains',
                'honeycalm_island',
                'cottonsedge_prairie',
                'holm_of_trials',
            ],
        },
        dungeons: [
            'lostlorn_forest',
            'abundant_shrine',
            'victory_road_unova',
            'pinwheel_forest',
            'melemele_meadow',
            'malie_garden',
            'ulaula_meadow',
            'ruins_of_abundance',
            'poni_meadow',
        ],
    },
    'Lilligant': {
        native_region: 'Unova',
        routes: {
            land: [
                'soothing_wetlands',
                'training_lowlands',
                'honeycalm_island',
            ],
        },
        evolution: [
            {
                prev: 'Petilil',
                item: 'Sun Stone',
                region: 'allButHisui',
            },
        ],
    },
    'Hisuian Lilligant': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Petilil',
                item: 'Sun Stone',
                region: 'hisuiOnly',
            },
        ],
    },
    'Basculin (Red-Striped)': {
        native_region: 'Unova',
        routes: {
            water: [
                'unova_route_19',
                'unova_route_20',
                'unova_route_6',
                'unova_route_13',
                'unova_route_14',
                'unova_route_11',
                'unova_route_22',
                'unova_route_23',
                'unova_route_1',
                'kalos_route_15',
                'kalos_route_16',
                'kalos_route_21',
                'north_lake_miloch',
                'motostoke_riverbank',
                'giants_bed',
                'giants_foot',
                'frigid_sea',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'giant_chasm',
            'abundant_shrine',
            'victory_road_unova',
            'dragonspiral_tower',
            'pinwheel_forest',
            'frost_cavern',
            'victory_road_kalos',
            'brooklet_hill',
            'malie_garden',
            'vast_poni_canyon',
            'roaring_sea_caves',
        ],
    },
    'Basculin (Blue-Striped)': {
        native_region: 'Unova',
        routes: {
            water: [
                'unova_route_19',
                'unova_route_20',
                'unova_route_6',
                'unova_route_13',
                'unova_route_14',
                'unova_route_11',
                'unova_route_22',
                'unova_route_23',
                'unova_route_1',
                'kalos_route_15',
                'kalos_route_16',
                'north_lake_miloch',
                'motostoke_riverbank',
                'giants_bed',
                'giants_foot',
                'frigid_sea',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'giant_chasm',
            'abundant_shrine',
            'victory_road_unova',
            'dragonspiral_tower',
            'pinwheel_forest',
            'frost_cavern',
            'victory_road_kalos',
            'brooklet_hill',
            'malie_garden',
            'vast_poni_canyon',
            'roaring_sea_caves',
        ],
    },
    'Basculin (White-Striped)': {
        native_region: 'Hisui',
        routes: {
            water: [
                'tranquility_cove',
                'fabled_spring',
                'hearts_crag',
            ],
        },
        dungeons: [
            'ancient_lake_acuity',
        ],
    },
    'Sandile': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_4',
                'desert_resort',
                'kalos_route_9',
                'potbottom_desert',
            ],
        },
        dungeons: [
            'relic_castle',
        ],
    },
    'Krokorok': {
        native_region: 'Unova',
        routes: {
            land: [
                'haina_desert',
                'potbottom_desert',
            ],
        },
        dungeons: [
            'relic_castle',
        ],
        evolution: [
            {
                prev: 'Sandile',
                level: 29,
            },
        ],
    },
    'Krookodile': {
        native_region: 'Unova',
        routes: {
            land: [
                'potbottom_desert',
            ],
        },
        dungeons: [
            'groundblight_shrine',
        ],
        evolution: [
            {
                prev: 'Krokorok',
                level: 40,
            },
        ],
    },
    'Darumaka': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_4',
                'desert_resort',
            ],
        },
        egg: 'Fire Egg',
    },
    'Galarian Darumaka': {
        native_region: 'Galar',
        routes: {
            land: [
                'steamdrift_way',
                'white_hill_station',
                'galar_route_10',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'iceberg_ruins',
        ],
    },
    'Darmanitan': {
        native_region: 'Unova',
        dungeon_boss: [
            ('relic_castle', 21000000),
        ],
        evolution: [
            {
                prev: 'Darumaka',
                level: 35,
            },
        ],
    },
    'Darmanitan (Zen)': {
        native_region: 'Unova',
        dungeon_chest: [
            'relic_castle',
        ],
    },
    'Galarian Darmanitan': {
        native_region: 'Galar',
        routes: {
            land: [
                'snowslide_slope',
            ],
        },
        evolution: [
            {
                prev: 'Galarian Darumaka',
                item: 'Ice Stone',
            },
        ],
    },
    'Galarian Darmanitan (Zen)': {
        native_region: 'Galar',
        dungeon_chest: [
            'crown_shrine',
        ],
    },
    'Maractus': {
        native_region: 'Unova',
        routes: {
            land: [
                'desert_resort',
                'bridge_field',
                'stony_wilderness',
                'hammerlocke_hills',
                'galar_route_6',
            ],
        },
        dungeon_boss: [
            ('ruins_of_abundance', 82177450),
        ],
        egg: 'Grass Egg',
        safari: ['Kalos'],
    },
    'Dwebble': {
        native_region: 'Unova',
        routes: {
            land: [
                'desert_resort',
                'rolling_fields',
                'west_lake_axewell',
                'east_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'watchtower_ruins',
                'stony_wilderness',
                'hammerlocke_hills',
                'loop_lagoon',
            ],
        },
        dungeons: [
            'sea_spirits_den',
            'courageous_cavern',
        ],
        special: [
            Has('Dwebble') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Crustle': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_18',
                'rolling_fields',
                'south_lake_miloch',
                'axews_eye',
                'stony_wilderness',
                'galar_route_8',
                'training_lowlands',
                'challenge_road',
            ],
        },
        dungeons: [
            'courageous_cavern',
            'rock_peak_ruins',
        ],
        dungeon_boss: [
            ('seaside_cave', 28000000),
        ],
        evolution: [
            {
                prev: 'Dwebble',
                level: 34,
            },
        ],
    },
    'Scraggy': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_4',
                'desert_resort',
                'alola_route_16',
                'alola_route_17',
                'motostoke_outskirts',
                'bridge_field',
                'stony_wilderness',
                'giants_cap',
                'soothing_wetlands',
                'potbottom_desert',
                'challenge_road',
            ],
        },
        dungeons: [
            'galar_mine_no_2',
        ],
        egg: 'Fighting Egg',
        farm_wandering: ['Chople Berry'],
    },
    'Scrafty': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_1',
                'unova_route_18',
                'training_lowlands',
                'challenge_road',
            ],
        },
        dungeons: [
            'p2_laboratory',
        ],
        evolution: [
            {
                prev: 'Scraggy',
                level: 39,
            },
        ],
    },
    'Sigilyph': {
        native_region: 'Unova',
        routes: {
            land: [
                'desert_resort',
                'kalos_route_10',
                'motostoke_riverbank',
                'stony_wilderness',
                'lake_of_outrage',
            ],
        },
        dungeon_boss: [
            ('dusty_bowl', 114616050),
        ],
        dream_orbs: ['Green'],
    },
    'Yamask': {
        native_region: 'Unova',
        dungeons: [
            'relic_castle',
        ],
    },
    'Galarian Yamask': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_6',
            ],
        },
    },
    'Cofagrigus': {
        native_region: 'Unova',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Yamask',
                level: 34,
            },
        ],
    },
    'Tirtouga': {
        native_region: 'Unova',
        trades: [
            ('nacrene_city', ['Cover Fossil']),
        ],
        special: [
            Has('Tirtouga') & make_rule('frigid_sea'),
        ],
    },
    'Carracosta': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Tirtouga',
                level: 37,
            },
        ],
        trades: [
            ('nacrene_city', ['Cover Fossil']),
        ],
        special: [
            Has('Carracosta') & make_rule('frigid_sea'),
        ],
    },
    'Archen': {
        native_region: 'Unova',
        trades: [
            ('nacrene_city', ['Plume Fossil']),
        ],
        special: [
            Has('Archen') & make_rule('giants_foot'),
        ],
    },
    'Archeops': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Archen',
                level: 37,
            },
        ],
        trades: [
            ('nacrene_city', ['Plume Fossil']),
        ],
        special: [
            Has('Archeops') & make_rule('path_to_the_peak'),
        ],
    },
    'Trubbish': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_4',
                'unova_route_5',
                'unova_route_16',
                'galar_route_3',
            ],
        },
        dungeons: [
            'castelia_sewers',
        ],
        dungeon_chest: [
            'lost_hotel',
        ],
    },
    'Garbodor': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_9',
                'east_lake_axewell',
                'bridge_field',
                'lake_of_outrage',
            ],
        },
        dungeon_chest: [
            'lost_hotel',
            'pokemon_village',
        ],
        evolution: [
            {
                prev: 'Trubbish',
                level: 36,
            },
        ],
    },
    'Gigantamax Garbodor': {
        native_region: 'Unova',
        special: [
            (Has('Gigantamax Garbodor') | make_rule('lair_of_giants12')) & make_rule('max_lair'),
        ],
    },
    'Zorua': {
        native_region: 'Unova',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
            ],
        },
        dungeons: [
            'trainers_school',
        ],
        farm_wandering: ['Colbur Berry'],
        shops: [
            ('driftveil_city', 'questPoint'),
        ],
    },
    'Hisuian Zorua': {
        native_region: 'Hisui',
        dungeons: [
            'icepeak_cavern',
            'turnback_cave',
        ],
    },
    'Zoroark': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_20',
                'poni_grove',
                'loop_lagoon',
                'insular_sea',
            ],
        },
        dungeon_boss: [
            ('pokemon_village', 95743340),
        ],
        dungeon_chest: [
            'victory_road_unova',
        ],
        evolution: [
            {
                prev: 'Zorua',
                level: 30,
            },
        ],
        special: [
            make_rule('lostlorn_forest', False) & make_rule('lostlorn_forest', True),
        ],
    },
    'Hisuian Zoroark': {
        native_region: 'Hisui',
        dungeon_boss: [
            ('icepeak_cavern', 10000000),
            ('ancient_lake_acuity', 10000000),
        ],
        evolution: [
            {
                prev: 'Hisuian Zorua',
                level: 30,
            },
        ],
    },
    'Minccino': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_4',
                'unova_route_5',
                'unova_route_16',
                'unova_route_9',
                'rolling_fields',
                'east_lake_axewell',
                'galar_route_5',
                'giants_cap',
            ],
        },
    },
    'Cinccino': {
        native_region: 'Unova',
        routes: {
            land: [
                'giants_cap',
            ],
        },
        evolution: [
            {
                prev: 'Minccino',
                item: 'Shiny Stone',
            },
        ],
    },
    'Gothita': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_5',
                'unova_route_16',
                'alola_route_6',
                'giants_cap',
                'slippery_slope',
                'frostpoint_field',
            ],
        },
    },
    'Gothorita': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_9',
                'kalos_route_20',
                'slippery_slope',
                'frostpoint_field',
            ],
        },
        dungeons: [
            'pokemon_village',
        ],
        evolution: [
            {
                prev: 'Gothita',
                level: 32,
            },
        ],
    },
    'Gothitelle': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
                'slippery_slope',
                'frostpoint_field',
            ],
        },
        evolution: [
            {
                prev: 'Gothorita',
                level: 41,
            },
        ],
    },
    'Solosis': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_5',
                'unova_route_16',
                'giants_cap',
                'slippery_slope',
                'frostpoint_field',
            ],
        },
        dungeons: [
            'reflection_cave',
        ],
    },
    'Duosion': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_9',
                'alola_route_16',
                'slippery_slope',
                'frostpoint_field',
            ],
        },
        evolution: [
            {
                prev: 'Solosis',
                level: 32,
            },
        ],
    },
    'Reuniclus': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
                'slippery_slope',
                'frostpoint_field',
            ],
        },
        dungeons: [
            'crown_shrine',
        ],
        evolution: [
            {
                prev: 'Duosion',
                level: 41,
            },
        ],
    },
    'Ducklett': {
        native_region: 'Unova',
        routes: {
            land: [
                'undella_bay',
                'kalos_route_7',
            ],
        },
    },
    'Swanna': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_15',
            ],
        },
        evolution: [
            {
                prev: 'Ducklett',
                level: 35,
            },
        ],
    },
    'Vanillite': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
                'giants_cap',
                'hammerlocke_hills',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'frost_cavern',
        ],
        egg: 'Mystery Egg',
    },
    'Vanillish': {
        native_region: 'Unova',
        routes: {
            land: [
                'dappled_grove',
                'north_lake_miloch',
                'axews_eye',
                'steamdrift_way',
                'white_hill_station',
                'galar_route_10',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'giant_chasm',
            'dragonspiral_tower',
        ],
        evolution: [
            {
                prev: 'Vanillite',
                level: 35,
            },
        ],
    },
    'Vanilluxe': {
        native_region: 'Unova',
        routes: {
            land: [
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'bridge_field',
                'lake_of_outrage',
                'white_hill_station',
                'frostpoint_field',
                'giants_bed',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'iceberg_ruins',
        ],
        dungeon_boss: [
            ('mount_lanakila', 81064250),
        ],
        evolution: [
            {
                prev: 'Vanillish',
                level: 47,
            },
        ],
    },
    'Deerling (Spring)': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
            ],
        },
    },
    'Deerling (Summer)': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_7',
            ],
        },
    },
    'Deerling (Autumn)': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
            ],
        },
    },
    'Deerling (Winter)': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_7',
            ],
        },
    },
    'Sawsbuck (Spring)': {
        native_region: 'Unova',
        dungeons: [
            'dragonspiral_tower',
            'pledge_grove',
        ],
        evolution: [
            {
                prev: 'Deerling (Spring)',
                level: 34,
            },
        ],
    },
    'Sawsbuck (Summer)': {
        native_region: 'Unova',
        dungeons: [
            'dragonspiral_tower',
            'pledge_grove',
        ],
        evolution: [
            {
                prev: 'Deerling (Summer)',
                level: 34,
            },
        ],
    },
    'Sawsbuck (Autumn)': {
        native_region: 'Unova',
        dungeons: [
            'dragonspiral_tower',
            'pledge_grove',
        ],
        evolution: [
            {
                prev: 'Deerling (Autumn)',
                level: 34,
            },
        ],
    },
    'Sawsbuck (Winter)': {
        native_region: 'Unova',
        dungeons: [
            'dragonspiral_tower',
            'pledge_grove',
        ],
        evolution: [
            {
                prev: 'Deerling (Winter)',
                level: 34,
            },
        ],
    },
    'Emolga': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_10',
            ],
            headbutt: [
                'forest_of_focus',
            ],
        },
        dungeons: [
            'pikachu_valley',
        ],
        dungeon_boss: [
            ('lostlorn_forest', 19000000),
        ],
        farm_wandering: ['Wacan Berry'],
    },
    'Karrablast': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
                'unova_route_11',
                'unova_route_8',
                'kalos_route_14',
                'kalos_route_19',
                'motostoke_riverbank',
                'bridge_field',
                'giants_cap',
                'hammerlocke_hills',
                'galar_route_7',
                'forest_of_focus',
                'training_lowlands',
                'old_cemetery',
            ],
        },
        dungeons: [
            'moor_of_icirrus',
        ],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
    },
    'Escavalier': {
        native_region: 'Unova',
        routes: {
            land: [
                'forest_of_focus',
                'training_lowlands',
            ],
        },
        evolution: [
            {
                prev: 'Karrablast',
                item: 'Linking Cord',
            },
        ],
    },
    'Foongus': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
                'unova_route_7',
                'kalos_route_15',
                'kalos_route_16',
                'forest_of_focus',
            ],
        },
        dungeon_chest: [
            'lostlorn_forest',
        ],
    },
    'Amoonguss': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_11',
                'unova_route_22',
                'unova_route_23',
                'kalos_route_20',
                'forest_of_focus',
            ],
        },
        dungeons: [
            'pokemon_village',
        ],
        dungeon_chest: [
            'giant_chasm',
            'abundant_shrine',
            'pinwheel_forest',
        ],
        evolution: [
            {
                prev: 'Foongus',
                level: 39,
            },
        ],
    },
    'Frillish': {
        native_region: 'Unova',
        routes: {
            land: [
                'undella_bay',
                'unova_route_17',
                'alola_route_14',
                'west_lake_axewell',
                'east_lake_axewell',
                'bridge_field',
                'giants_mirror',
            ],
            water: [
                'unova_route_4',
                'unova_route_13',
                'unova_route_18',
                'north_lake_miloch',
                'stepping_stone_sea',
            ],
        },
        dungeons: [
            'seaside_cave',
            'p2_laboratory',
        ],
    },
    'Jellicent': {
        native_region: 'Unova',
        routes: {
            land: [
                'undella_bay',
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'bridge_field',
                'lake_of_outrage',
                'galar_route_9',
                'outer_spikemuth',
                'challenge_beach',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
        dungeons: [
            'thrifty_megamart',
        ],
        evolution: [
            {
                prev: 'Frillish',
                level: 40,
            },
        ],
    },
    'Alomomola': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_17',
            ],
            water: [
                'unova_route_18',
            ],
        },
        dungeons: [
            'brooklet_hill',
        ],
    },
    'Joltik': {
        native_region: 'Unova',
        routes: {
            land: [
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'galar_route_4',
                'giants_mirror',
                'giants_cap',
            ],
        },
        dungeons: [
            'chargestone_cave',
        ],
        egg: 'Electric Egg',
    },
    'Galvantula': {
        native_region: 'Unova',
        routes: {
            land: [
                'giants_seat',
                'south_lake_miloch',
                'giants_cap',
                'lake_of_outrage',
                'galar_route_7',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'three_point_pass',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'split_decision_ruins',
        ],
        evolution: [
            {
                prev: 'Joltik',
                level: 36,
            },
        ],
    },
    'Ferroseed': {
        native_region: 'Unova',
        routes: {
            land: [
                'galar_route_4',
                'motostoke_riverbank',
                'bridge_field',
                'stony_wilderness',
            ],
        },
        dungeons: [
            'chargestone_cave',
            'lakeside_cave',
        ],
    },
    'Ferrothorn': {
        native_region: 'Unova',
        routes: {
            land: [
                'bridge_field',
            ],
        },
        dungeons: [
            'dusty_bowl',
            'iron_ruins',
        ],
        evolution: [
            {
                prev: 'Ferroseed',
                level: 40,
            },
        ],
    },
    'Klink': {
        native_region: 'Unova',
        routes: {
            land: [
                'dappled_grove',
                'west_lake_axewell',
                'south_lake_miloch',
                'north_lake_miloch',
                'axews_eye',
                'galar_route_3',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'chargestone_cave',
        ],
    },
    'Klang': {
        native_region: 'Unova',
        routes: {
            land: [
                'hammerlocke_hills',
                'white_hill_station',
            ],
        },
        dungeons: [
            'p2_laboratory',
            'dusty_bowl',
        ],
        evolution: [
            {
                prev: 'Klink',
                level: 38,
            },
        ],
    },
    'Klinklang': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
                'hammerlocke_hills',
            ],
        },
        evolution: [
            {
                prev: 'Klang',
                level: 49,
            },
        ],
        special: [
            make_rule('p2_laboratory', True, 58000000),
        ],
    },
    'Tynamo': {
        native_region: 'Unova',
        dungeons: [
            'seaside_cave',
        ],
        dungeon_boss: [
            ('chargestone_cave', 22000000),
        ],
    },
    'Eelektrik': {
        native_region: 'Unova',
        dungeon_boss: [
            ('seaside_cave', 28000000),
        ],
        evolution: [
            {
                prev: 'Tynamo',
                level: 39,
            },
        ],
    },
    'Eelektross': {
        native_region: 'Unova',
        routes: {
            land: [
                'poni_grove',
            ],
        },
        evolution: [
            {
                prev: 'Eelektrik',
                item: 'Thunder Stone',
            },
        ],
    },
    'Elgyem': {
        native_region: 'Unova',
        routes: {
            land: [
                'mount_hokulani',
                'motostoke_riverbank',
                'bridge_field',
            ],
        },
        dungeons: [
            'near_space',
            'celestial_tower',
        ],
    },
    'Beheeyem': {
        native_region: 'Unova',
        routes: {
            land: [
                'bridge_field',
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'near_space',
        ],
        evolution: [
            {
                prev: 'Elgyem',
                level: 42,
            },
        ],
    },
    'Litwick': {
        native_region: 'Unova',
        routes: {
            land: [
                'motostoke_riverbank',
                'bridge_field',
            ],
        },
        dungeons: [
            'lost_hotel',
        ],
        dungeon_boss: [
            ('celestial_tower', 25000000),
            ('hauoli_cemetery', 28968625),
        ],
    },
    'Lampent': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
                'old_cemetery',
            ],
        },
        evolution: [
            {
                prev: 'Litwick',
                level: 41,
            },
        ],
    },
    'Chandelure': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Lampent',
                item: 'Dusk Stone',
            },
        ],
    },
    'Axew': {
        native_region: 'Unova',
        routes: {
            land: [
                'mount_hokulani',
                'axews_eye',
                'hammerlocke_hills',
                'galar_route_6',
            ],
        },
        dungeon_boss: [
            ('mistralton_cave', 24000000),
            ('connecting_cave', 59867590),
        ],
    },
    'Fraxure': {
        native_region: 'Unova',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Axew',
                level: 38,
            },
        ],
    },
    'Haxorus': {
        native_region: 'Unova',
        routes: {
            land: [
                'axews_eye',
                'lake_of_outrage',
            ],
        },
        evolution: [
            {
                prev: 'Fraxure',
                level: 48,
            },
        ],
    },
    'Cubchoo': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_7',
                'bridge_field',
                'stony_wilderness',
                'giants_mirror',
                'hammerlocke_hills',
                'white_hill_station',
                'galar_route_10',
            ],
        },
        dungeons: [
            'frost_cavern',
        ],
    },
    'Beartic': {
        native_region: 'Unova',
        routes: {
            land: [
                'bridge_field',
                'giants_cap',
                'galar_route_10',
                'frigid_sea',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'twist_mountain',
            'dragonspiral_tower',
            'frost_cavern',
            'iceberg_ruins',
            'dyna_tree_hill',
        ],
        evolution: [
            {
                prev: 'Cubchoo',
                level: 37,
            },
        ],
    },
    'Cryogonal': {
        native_region: 'Unova',
        routes: {
            land: [
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'frost_cavern',
            'iceberg_ruins',
            'split_decision_ruins',
            'dyna_tree_hill',
        ],
        dungeon_boss: [
            ('twist_mountain', 48000000),
        ],
    },
    'Shelmet': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_6',
                'unova_route_11',
                'unova_route_8',
                'kalos_route_14',
                'kalos_route_19',
                'motostoke_riverbank',
                'bridge_field',
                'giants_cap',
                'hammerlocke_hills',
                'galar_route_7',
                'soothing_wetlands',
                'forest_of_focus',
                'training_lowlands',
                'giants_bed',
            ],
        },
        dungeons: [
            'moor_of_icirrus',
        ],
    },
    'Accelgor': {
        native_region: 'Unova',
        routes: {
            land: [
                'forest_of_focus',
                'training_lowlands',
            ],
        },
        evolution: [
            {
                prev: 'Shelmet',
                item: 'Linking Cord',
            },
        ],
    },
    'Stunfisk': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_8',
            ],
            water: [
                'kalos_route_14',
                'kalos_route_19',
            ],
        },
        dungeons: [
            'moor_of_icirrus',
        ],
        egg: 'Electric Egg',
        safari: ['Kalos'],
    },
    'Galarian Stunfisk': {
        native_region: 'Galar',
        dungeons: [
            'slumbering_weald_shrine',
            'energy_plant',
        ],
        dungeon_boss: [
            ('galar_mine_no_2', 106473200),
        ],
        dungeon_chest: [
            'galar_mine_no_2',
        ],
    },
    'Mienfoo': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_14',
                'unova_route_22',
                'unova_route_23',
                'kalos_route_8',
                'challenge_road',
            ],
        },
        dungeons: [
            'dragonspiral_tower',
            'vast_poni_canyon',
        ],
    },
    'Mienshao': {
        native_region: 'Unova',
        routes: {
            land: [
                'challenge_road',
            ],
        },
        dungeons: [
            'dragonspiral_tower',
        ],
        evolution: [
            {
                prev: 'Mienfoo',
                level: 50,
            },
        ],
    },
    'Druddigon': {
        native_region: 'Unova',
        routes: {
            land: [
                'three_point_pass',
                'snowslide_slope',
                'path_to_the_peak',
            ],
        },
        dungeons: [
            'victory_road_unova',
            'victory_road_kalos',
            'resolution_cave',
            'tunnel_to_the_top',
        ],
        dungeon_boss: [
            ('dragonspiral_tower', 48000000),
            ('courageous_cavern', 133520620),
            ('brawlers_cave', 135047520),
        ],
        farm_wandering: ['Haban Berry'],
    },
    'Golett': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_10',
                'haina_desert',
                'rolling_fields',
                'dappled_grove',
                'giants_seat',
                'north_lake_miloch',
                'watchtower_ruins',
                'stony_wilderness',
                'giants_cap',
                'galar_route_8',
            ],
        },
        dungeons: [
            'dragonspiral_tower',
        ],
    },
    'Golurk': {
        native_region: 'Unova',
        routes: {
            land: [
                'giants_seat',
                'watchtower_ruins',
                'stony_wilderness',
                'lake_of_outrage',
                'three_point_pass',
            ],
        },
        dungeons: [
            'dragonspiral_tower',
        ],
        dungeon_boss: [
            ('victory_road_unova', 44000000),
        ],
        evolution: [
            {
                prev: 'Golett',
                level: 43,
            },
        ],
        safari: ['Kalos'],
    },
    'Pawniard': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_9',
                'kalos_route_15',
                'motostoke_outskirts',
                'motostoke_riverbank',
                'stony_wilderness',
                'giants_mirror',
                'giants_cap',
                'galar_route_8',
                'soothing_wetlands',
                'forest_of_focus',
                'potbottom_desert',
                'challenge_road',
            ],
        },
        dungeons: [
            'lost_hotel',
            'area_zero',
        ],
    },
    'Bisharp': {
        native_region: 'Unova',
        routes: {
            land: [
                'alola_route_17',
                'giants_seat',
                'lake_of_outrage',
                'training_lowlands',
                'challenge_road',
            ],
        },
        dungeons: [
            'energy_plant',
            'iron_ruins',
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Pawniard',
                level: 52,
            },
        ],
    },
    'Bouffalant': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_23',
                'soothing_wetlands',
            ],
        },
    },
    'Rufflet': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_23',
                'alola_route_3',
                'bridge_field',
                'galar_route_8',
                'potbottom_desert',
                'hearts_crag',
            ],
        },
        dungeons: [
            'ancient_lake_acuity',
        ],
    },
    'Braviary': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
                'potbottom_desert',
                'challenge_road',
            ],
        },
        dungeons: [
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Rufflet',
                level: 54,
            },
        ],
    },
    'Hisuian Braviary': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Rufflet',
                level: 54,
            },
        ],
    },
    'Vullaby': {
        native_region: 'Unova',
        routes: {
            land: [
                'unova_route_23',
                'alola_route_3',
                'galar_route_8',
                'potbottom_desert',
            ],
        },
    },
    'Mandibuzz': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
                'potbottom_desert',
                'challenge_road',
            ],
        },
        evolution: [
            {
                prev: 'Vullaby',
                level: 54,
            },
        ],
    },
    'Heatmor': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_18',
                'giants_mirror',
                'lake_of_outrage',
                'galar_route_6',
                'giants_bed',
                'old_cemetery',
                'three_point_pass',
            ],
        },
        dungeon_boss: [
            ('twist_mountain', 48000000),
        ],
    },
    'Durant': {
        native_region: 'Unova',
        routes: {
            land: [
                'kalos_route_18',
                'giants_mirror',
                'lake_of_outrage',
                'galar_route_6',
                'giants_bed',
                'old_cemetery',
                'three_point_pass',
            ],
        },
        dungeons: [
            'terminus_cave',
            'energy_plant',
        ],
        dungeon_boss: [
            ('twist_mountain', 48000000),
        ],
        special: [
            Has('Durant') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Deino': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'roaring_sea_caves',
        ],
        dungeon_boss: [
            ('ten_carat_hill', 59489105),
        ],
        egg: 'Dragon Egg',
        special: [
            Has('Deino') & make_rule('victory_road_unova', False),
        ],
    },
    'Zweilous': {
        native_region: 'Unova',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'victory_road_kalos',
            'area_zero_depths',
        ],
        evolution: [
            {
                prev: 'Deino',
                level: 50,
            },
        ],
        egg: 'Dragon Egg',
        special: [
            Has('Zweilous') & make_rule('victory_road_unova', False),
        ],
    },
    'Hydreigon': {
        native_region: 'Unova',
        dungeon_boss: [
            ('roaring_sea_caves', 160924440),
        ],
        evolution: [
            {
                prev: 'Zweilous',
                level: 64,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Larvesta': {
        native_region: 'Unova',
        routes: {
            land: [
                'forest_of_focus',
                'loop_lagoon',
            ],
        },
        breeding: ['Volcarona'],
    },
    'Volcarona': {
        native_region: 'Unova',
        routes: {
            land: [
                'challenge_beach',
                'potbottom_desert',
                'insular_sea',
            ],
        },
        dungeons: [
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Larvesta',
                level: 59,
            },
        ],
        special: [
            make_rule('relic_passage', True) & make_rule('relic_castle', True, 21000000),
        ],
    },
    'Cobalion': {
        native_region: 'Unova',
        special: [
            make_rule('swords_of_justice21') & make_rule('mistralton_cave', True, 25000000),
        ],
    },
    'Terrakion': {
        native_region: 'Unova',
        special: [
            make_rule('swords_of_justice21') & make_rule('victory_road_unova', True, 45000000),
        ],
    },
    'Virizion': {
        native_region: 'Unova',
        special: [
            make_rule('swords_of_justice21') & make_rule('pinwheel_forest', True, 48000000),
        ],
    },
    'Tornadus': {
        native_region: 'Unova',
        special: [
            Has('Legend Badge') & make_rule('roamer', 'Unova'),
            make_rule('roamer', 'Hisui') & make_rule('incarnate_forces_of_hisui1'),
        ],
    },
    'Tornadus (Therian)': {
        native_region: 'Unova',
        dream_orbs: ['Pink'],
    },
    'Thundurus': {
        native_region: 'Unova',
        special: [
            Has('Legend Badge') & make_rule('roamer', 'Unova'),
            make_rule('roamer', 'Hisui') & make_rule('incarnate_forces_of_hisui1'),
        ],
    },
    'Thundurus (Therian)': {
        native_region: 'Unova',
        dream_orbs: ['Green'],
    },
    'Reshiram': {
        native_region: 'Unova',
        dungeon_boss: [
            ('dragonspiral_tower', 50000000),
        ],
    },
    'Zekrom': {
        native_region: 'Unova',
        dungeon_boss: [
            ('dragonspiral_tower', 50000000),
        ],
    },
    'Landorus': {
        native_region: 'Unova',
        dungeon_boss: [
            ('abundant_shrine', 42000000),
        ],
        special: [
            make_rule('roamer', 'Hisui') & make_rule('incarnate_forces_of_hisui1'),
        ],
    },
    'Landorus (Therian)': {
        native_region: 'Unova',
        dream_orbs: ['Orange'],
    },
    'Kyurem': {
        native_region: 'Unova',
        special: [
            Has('Elite Unova Champion Badge') & make_rule('completed_hollow_truth_and_ideals') & make_rule('completed_swords_of_justice') & make_rule('giant_chasm', True, 35000000),
        ],
    },
    'Kyurem (White)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Kyurem',
                item: 'White Dna',
            },
        ],
    },
    'Kyurem (Black)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Kyurem',
                item: 'Black Dna',
            },
        ],
    },
    'Keldeo': {
        native_region: 'Unova',
        special: [
            make_rule('completed_swords_of_justice') & make_rule('moor_of_icirrus', True, 50000000),
        ],
    },
    'Keldeo (Resolute)': {
        native_region: 'Unova',
        dungeon_boss: [
            ('pledge_grove', 52000000),
        ],
    },
    'Meloetta (Aria)': {
        native_region: 'Unova',
        special: [
            Has('Elite Unova Champion Badge') & make_rule('roamer', 'Unova'),
        ],
    },
    'Meloetta (Pirouette)': {
        native_region: 'Unova',
        shops: [
            ('anville_town', 'questPoint'),
        ],
    },
    'Genesect': {
        native_region: 'Unova',
        special: [
            make_rule('the_legend_awakened7') & make_rule('p2_laboratory', True, 62000000),
        ],
    },
    'Genesect (Burn)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect',
                level: 70,
                item: 'Burn Drive',
            },
        ],
        special: [
            {
                dungeon: 'p2_laboratory',
                rule: Has('Genesect (Burn)') & make_rule('p2_laboratory', True, 62000000),
                requirements: [
                    {
                        type: 'MoonCyclePhaseRequirement',
                        args: [
                            ['MoonCyclePhase.NewMoon', 'MoonCyclePhase.FullMoon'],
                        ],
                    },
                ],
            },
        ],
    },
    'Genesect (Chill)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect',
                level: 70,
                item: 'Chill Drive',
            },
        ],
        special: [
            {
                dungeon: 'p2_laboratory',
                rule: Has('Genesect (Chill)') & make_rule('p2_laboratory', True, 62000000),
                requirements: [
                    {
                        type: 'MoonCyclePhaseRequirement',
                        args: [
                            ['MoonCyclePhase.FirstQuarter', 'MoonCyclePhase.ThirdQuarter'],
                        ],
                    },
                ],
            },
        ],
    },
    'Genesect (Douse)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect',
                level: 70,
                item: 'Douse Drive',
            },
        ],
        special: [
            {
                dungeon: 'p2_laboratory',
                rule: Has('Genesect (Douse)') & make_rule('p2_laboratory', True, 62000000),
                requirements: [
                    {
                        type: 'MoonCyclePhaseRequirement',
                        args: [
                            ['MoonCyclePhase.WaxingCrescent', 'MoonCyclePhase.WaningGibbous'],
                        ],
                    },
                ],
            },
        ],
    },
    'Genesect (Shock)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect',
                level: 70,
                item: 'Shock Drive',
            },
        ],
        special: [
            {
                dungeon: 'p2_laboratory',
                rule: Has('Genesect (Shock)') & make_rule('p2_laboratory', True, 62000000),
                requirements: [
                    {
                        type: 'MoonCyclePhaseRequirement',
                        args: [
                            ['MoonCyclePhase.WaxingGibbous', 'MoonCyclePhase.WaningCrescent'],
                        ],
                    },
                ],
            },
        ],
    },
    'Genesect (High-Speed)': {
        native_region: 'Unova',
        special: [
            make_rule('roamer', 'Unova') & make_rule('completed_the_legend_awakened'),
        ],
    },
    'Genesect (High-Speed Burn)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect (High-Speed)',
                level: 70,
                item: 'Burn Drive',
            },
        ],
        special: [
            {
                dungeon: 'liberty_garden',
                rule: Has('Genesect (High-Speed Burn)') & make_rule('liberty_garden', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Burn)',
                            '0',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'relic_castle',
                rule: Has('Genesect (High-Speed Burn)') & make_rule('relic_castle', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Burn)',
                            '1',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'celestial_tower',
                rule: Has('Genesect (High-Speed Burn)') & make_rule('celestial_tower', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Burn)',
                            '2',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'twist_mountain',
                rule: Has('Genesect (High-Speed Burn)') & make_rule('twist_mountain', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Burn)',
                            '3',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
        ],
    },
    'Genesect (High-Speed Chill)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect (High-Speed)',
                level: 70,
                item: 'Chill Drive',
            },
        ],
        special: [
            {
                dungeon: 'mistralton_cave',
                rule: Has('Genesect (High-Speed Chill)') & make_rule('mistralton_cave', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Chill)',
                            '0',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'giant_chasm',
                rule: Has('Genesect (High-Speed Chill)') & make_rule('giant_chasm', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Chill)',
                            '1',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'twist_mountain',
                rule: Has('Genesect (High-Speed Chill)') & make_rule('twist_mountain', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Chill)',
                            '2',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'dreamyard',
                rule: Has('Genesect (High-Speed Chill)') & make_rule('dreamyard', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Chill)',
                            '3',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
        ],
    },
    'Genesect (High-Speed Douse)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect (High-Speed)',
                level: 70,
                item: 'Douse Drive',
            },
        ],
        special: [
            {
                dungeon: 'floccesy_ranch',
                rule: Has('Genesect (High-Speed Douse)') & make_rule('floccesy_ranch', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Douse)',
                            '0',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'castelia_sewers',
                rule: Has('Genesect (High-Speed Douse)') & make_rule('castelia_sewers', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Douse)',
                            '1',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'seaside_cave',
                rule: Has('Genesect (High-Speed Douse)') & make_rule('seaside_cave', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Douse)',
                            '2',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'pinwheel_forest',
                rule: Has('Genesect (High-Speed Douse)') & make_rule('pinwheel_forest', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Douse)',
                            '3',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
        ],
    },
    'Genesect (High-Speed Shock)': {
        native_region: 'Unova',
        evolution: [
            {
                prev: 'Genesect (High-Speed)',
                level: 70,
                item: 'Shock Drive',
            },
        ],
        special: [
            {
                dungeon: 'castelia_sewers',
                rule: Has('Genesect (High-Speed Shock)') & make_rule('castelia_sewers', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Shock)',
                            '0',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'chargestone_cave',
                rule: Has('Genesect (High-Speed Shock)') & make_rule('chargestone_cave', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Shock)',
                            '1',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'reversal_mountain',
                rule: Has('Genesect (High-Speed Shock)') & make_rule('reversal_mountain', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Shock)',
                            '2',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
            {
                dungeon: 'dragonspiral_tower',
                rule: Has('Genesect (High-Speed Shock)') & make_rule('dragonspiral_tower', True, 62000000),
                requirements: [
                    {
                        type: 'PokemonDefeatedSelectNRequirement',
                        args: [
                            'Genesect (High-Speed Shock)',
                            '3',
                            '4',
                            '1',
                        ],
                    },
                ],
            },
        ],
    },
    'Chespin': {
        native_region: 'Kalos',
        egg: 'Grass Egg',
        starter: ['Kalos'],
        farm_wandering: ['Rindo Berry'],
    },
    'Quilladin': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Chespin',
                level: 16,
            },
        ],
        special: [
            Has('Quilladin') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Chesnaught': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Quilladin',
                level: 36,
            },
        ],
        special: [
            make_rule('emissary_of_light2') & make_rule('exeggutor_island_hill', True, 78865330),
        ],
    },
    'Fennekin': {
        native_region: 'Kalos',
        egg: 'Fire Egg',
        starter: ['Kalos'],
        farm_wandering: ['Occa Berry'],
    },
    'Braixen': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Fennekin',
                level: 16,
            },
        ],
        special: [
            Has('Braixen') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Delphox': {
        native_region: 'Kalos',
        routes: {
            land: [
                'ancient_poni_path',
            ],
        },
        evolution: [
            {
                prev: 'Braixen',
                level: 36,
            },
        ],
    },
    'Froakie': {
        native_region: 'Kalos',
        egg: 'Water Egg',
        starter: ['Kalos'],
        farm_wandering: ['Passho Berry'],
    },
    'Frogadier': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Froakie',
                level: 16,
            },
        ],
        special: [
            Has('Frogadier') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Greninja': {
        native_region: 'Kalos',
        routes: {
            land: [
                'poni_wilds',
            ],
        },
        evolution: [
            {
                prev: 'Frogadier',
                level: 36,
            },
        ],
    },
    'Ash-Greninja': {
        native_region: 'Kalos',
        special: [
            make_rule('roamer', 'Kalos') & make_rule('ash_ketchum_kalos'),
        ],
    },
    'Bunnelby': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_1',
                'kalos_route_2',
                'kalos_route_3',
                'kalos_route_22',
                'kalos_route_5',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'north_lake_miloch',
            ],
        },
    },
    'Diggersby': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_22',
                'rolling_fields',
                'west_lake_axewell',
                'giants_seat',
                'north_lake_miloch',
                'axews_eye',
                'bridge_field',
                'giants_mirror',
                'giants_cap',
            ],
        },
        evolution: [
            {
                prev: 'Bunnelby',
                level: 20,
            },
        ],
    },
    'Fletchling': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_1',
                'kalos_route_2',
                'kalos_route_3',
                'alola_route_8',
                'loop_lagoon',
                'potbottom_desert',
                'challenge_road',
                'poco_path',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'santalune_forest',
            'wela_volcano_park',
        ],
    },
    'Fletchinder': {
        native_region: 'Kalos',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'loop_lagoon',
                'training_lowlands',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
        evolution: [
            {
                prev: 'Fletchling',
                level: 17,
            },
        ],
    },
    'Talonflame': {
        native_region: 'Kalos',
        routes: {
            land: [
                'soothing_wetlands',
                'loop_lagoon',
                'training_lowlands',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Fletchinder',
                level: 35,
            },
        ],
    },
    'Scatterbug': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_2',
                'poco_path',
                'south_province_area_one',
            ],
        },
        dungeons: [
            'santalune_forest',
        ],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        special: [
            Has('Scatterbug') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Spewpa': {
        native_region: 'Kalos',
        routes: {
            land: [
                'south_province_area_one',
            ],
        },
        evolution: [
            {
                prev: 'Scatterbug',
                level: 9,
            },
        ],
        farm_wandering: ['Pecha Berry', 'Persim Berry', 'Nanab Berry', 'Mago Berry', 'Qualot Berry', 'Magost Berry', 'Watmel Berry', 'Pinkan Berry', 'Roseli Berry', 'Petaya Berry'],
        special: [
            Has('Spewpa') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Vivillon (Meadow)': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Spewpa',
                level: 12,
            },
        ],
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kalos'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Alola'),
        ],
    },
    'Vivillon (Icy Snow)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Icy Snow)') | make_rule('the_great_vivillon_hunt32')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('frost_cavern', True, 96662023),
        ],
    },
    'Vivillon (Polar)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Polar)') | make_rule('the_great_vivillon_hunt22')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('sky_pillar', True, 96662023),
        ],
    },
    'Vivillon (Tundra)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Tundra)') | make_rule('the_great_vivillon_hunt8')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('poke_ball_factory', True, 96662023),
        ],
    },
    'Vivillon (Continental)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Continental)') | make_rule('the_great_vivillon_hunt18')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('new_mauville', True, 96662023),
        ],
    },
    'Vivillon (Garden)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Garden)') | make_rule('the_great_vivillon_hunt26')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('flower_paradise', True, 96662023),
        ],
    },
    'Vivillon (Elegant)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Elegant)') | make_rule('the_great_vivillon_hunt14')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('lost_hotel', True, 96662023),
        ],
    },
    'Vivillon (Modern)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Modern)') | make_rule('the_great_vivillon_hunt2')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('cerulean_cave', True, 96662023),
        ],
    },
    'Vivillon (Marine)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Marine)') | make_rule('the_great_vivillon_hunt0')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('lake_valor', True, 96662023),
            (Has('Vivillon (Marine)') | make_rule('the_great_vivillon_hunt0')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('lake_verity', True, 96662023),
            (Has('Vivillon (Marine)') | make_rule('the_great_vivillon_hunt0')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('lake_acuity', True, 96662023),
        ],
    },
    'Vivillon (Archipelago)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Archipelago)') | make_rule('the_great_vivillon_hunt12')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('sprout_tower', True, 96662023),
        ],
    },
    'Vivillon (High Plains)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (High Plains)') | make_rule('the_great_vivillon_hunt28')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('mt_moon', True, 96662023),
        ],
    },
    'Vivillon (Sandstorm)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Sandstorm)') | make_rule('the_great_vivillon_hunt24')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('relic_castle', True, 96662023),
        ],
    },
    'Vivillon (River)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (River)') | make_rule('the_great_vivillon_hunt20')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('eterna_forest', True, 96662023),
        ],
    },
    'Vivillon (Monsoon)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Monsoon)') | make_rule('the_great_vivillon_hunt6')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('dark_cave', True, 96662023),
        ],
    },
    'Vivillon (Savanna)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Savanna)') | make_rule('the_great_vivillon_hunt30')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('dragonspiral_tower', True, 96662023),
        ],
    },
    'Vivillon (Sun)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Sun)') | make_rule('the_great_vivillon_hunt10')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('mt_chimney_crater', True, 96662023),
        ],
    },
    'Vivillon (Ocean)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Ocean)') | make_rule('the_great_vivillon_hunt16')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('dreamyard', True, 96662023),
        ],
    },
    'Vivillon (Jungle)': {
        native_region: 'Kalos',
        special: [
            (Has('Vivillon (Jungle)') | make_rule('the_great_vivillon_hunt4')) & make_rule('has_script', "Infinite Seasonal Events") & make_rule('has_script', 'Infinite Seasonal Events') & make_rule('moor_of_icirrus', True, 96662023),
        ],
    },
    'Vivillon (Poké Ball)': {
        native_region: 'Kalos',
        special: [
            Has('Vivillon (Poké Ball)') & make_rule('has_script', "Infinite Seasonal Events") & make_rule('completed_child_of_the_stars') & make_rule('thrifty_megamart', True, 96662023),
            make_rule('battle_frontier', 666) & make_rule('the_great_vivillon_hunt34'),
        ],
    },
    'Vivillon (Fancy)': {
        native_region: 'Kalos',
        special: [
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Kalos'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Galar - South'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Galar - Isle of Armor'),
            make_rule('has_script', "Infinite Seasonal Events") & make_rule('roamer', 'Galar - Crown Tundra'),
        ],
    },
    'Litleo': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_22',
            ],
        },
        egg: 'Fire Egg',
    },
    'Pyroar': {
        native_region: 'Kalos',
        routes: {
            land: [
                'poni_plains',
            ],
        },
        evolution: [
            {
                prev: 'Litleo',
                level: 35,
            },
        ],
    },
    'Flabébé (Red)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_4',
                'south_province_area_two',
            ],
        },
        dungeon_boss: [
            ('melemele_meadow', 58846350),
        ],
        farm_wandering: ['Cheri Berry', 'Leppa Berry', 'Razz Berry', 'Figy Berry', 'Pomeg Berry', 'Tamato Berry', 'Spelon Berry', 'Occa Berry', 'Chople Berry', 'Haban Berry', 'Custap Berry', 'Liechi Berry', 'Lansat Berry'],
    },
    'Flabébé (Yellow)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'south_province_area_two',
            ],
        },
        farm_wandering: ['Aspear Berry', 'Sitrus Berry', 'Pinap Berry', 'Iapapa Berry', 'Grepa Berry', 'Nomel Berry', 'Wacan Berry', 'Shuca Berry', 'Charti Berry', 'Chilan Berry', 'Jaboca Berry', 'Kee Berry'],
    },
    'Flabébé (Orange)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_4',
                'kalos_route_7',
                'south_province_area_two',
            ],
        },
        farm_wandering: ['Hopo Berry'],
    },
    'Flabébé (Blue)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'south_province_area_two',
            ],
        },
        farm_wandering: ['Oran Berry', 'Kelpsy Berry', 'Passho Berry', 'Yache Berry', 'Coba Berry', 'Rowap Berry', 'Maranga Berry', 'Apicot Berry'],
    },
    'Flabébé (White)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_4',
                'kalos_route_7',
                'south_province_area_two',
            ],
        },
    },
    'Floette (Red)': {
        native_region: 'Kalos',
        dungeon_boss: [
            ('ulaula_meadow', 75635260),
        ],
        evolution: [
            {
                prev: 'Flabébé (Red)',
                level: 19,
            },
        ],
    },
    'Floette (Yellow)': {
        native_region: 'Kalos',
        dungeons: [
            'ruins_of_conflict',
        ],
        evolution: [
            {
                prev: 'Flabébé (Yellow)',
                level: 19,
            },
        ],
    },
    'Floette (Orange)': {
        native_region: 'Kalos',
        dungeons: [
            'ruins_of_abundance',
        ],
        evolution: [
            {
                prev: 'Flabébé (Orange)',
                level: 19,
            },
        ],
    },
    'Floette (Blue)': {
        native_region: 'Kalos',
        dungeons: [
            'ruins_of_hope',
        ],
        dungeon_boss: [
            ('poni_meadow', 83299840),
        ],
        evolution: [
            {
                prev: 'Flabébé (Blue)',
                level: 19,
            },
        ],
    },
    'Floette (White)': {
        native_region: 'Kalos',
        dungeons: [
            'ruins_of_life',
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Flabébé (White)',
                level: 19,
            },
        ],
    },
    'Floette (Eternal)': {
        native_region: 'Kalos',
        special: [
            make_rule('lumiose_city') & make_rule('completed_a_beautiful_world'),
            Has('Floette (Eternal)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Florges (Red)': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Floette (Red)',
                item: 'Shiny Stone',
            },
        ],
    },
    'Florges (Yellow)': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Floette (Yellow)',
                item: 'Shiny Stone',
            },
        ],
    },
    'Florges (Orange)': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Floette (Orange)',
                item: 'Shiny Stone',
            },
        ],
    },
    'Florges (Blue)': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Floette (Blue)',
                item: 'Shiny Stone',
            },
        ],
    },
    'Florges (White)': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Floette (White)',
                item: 'Shiny Stone',
            },
        ],
    },
    'Skiddo': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_5',
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
        egg: 'Grass Egg',
    },
    'Gogoat': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Skiddo',
                level: 32,
            },
        ],
        special: [
            Has('Gogoat') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Pancham': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_5',
                'alola_route_10',
                'alola_route_11',
                'rolling_fields',
                'west_lake_axewell',
                'east_lake_axewell',
                'galar_route_3',
            ],
        },
        egg: 'Fighting Egg',
    },
    'Pangoro': {
        native_region: 'Kalos',
        routes: {
            land: [
                'rolling_fields',
                'dappled_grove',
                'bridge_field',
                'lake_of_outrage',
            ],
        },
        evolution: [
            {
                prev: 'Pancham',
                level: 32,
            },
        ],
    },
    'Furfrou': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_5',
                'alola_route_2',
                'poni_wilds',
                'ancient_poni_path',
            ],
        },
        dungeons: [
            'trainers_school',
        ],
    },
    'Furfrou (Star)': {
        native_region: 'Kalos',
        trades: [
            ('parfum_palace', ['Red Shard', 'Yellow Shard', 'Green Shard', 'Blue Shard', 'Grey Shard', 'Purple Shard', 'Ochre Shard', 'Black Shard', 'Crimson Shard', 'Lime Shard', 'White Shard', 'Pink Shard']),
        ],
    },
    'Furfrou (Diamond)': {
        native_region: 'Kalos',
        shops: [
            ('lumiose_city', 'diamond'),
        ],
    },
    'Furfrou (Debutante)': {
        native_region: 'Kalos',
        shops: [
            ('lumiose_city', 'money'),
        ],
    },
    'Furfrou (Matron)': {
        native_region: 'Kalos',
        shops: [
            ('lumiose_city', 'farmPoint'),
        ],
    },
    'Furfrou (Dandy)': {
        native_region: 'Kalos',
        shops: [
            ('lumiose_city', 'questPoint'),
        ],
    },
    'Furfrou (La Reine)': {
        native_region: 'Kalos',
        shops: [
            ('parfum_palace', 'Normal Gems'),
        ],
    },
    'Furfrou (Kabuki)': {
        native_region: 'Kalos',
        shops: [
            ('lumiose_city', 'battlePoint'),
        ],
    },
    'Furfrou (Pharaoh)': {
        native_region: 'Kalos',
        shops: [
            ('lumiose_city', 'dungeonToken'),
        ],
    },
    'Espurr': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_6',
                'galar_route_5',
                'motostoke_riverbank',
                'hammerlocke_hills',
            ],
        },
    },
    'Meowstic': {
        native_region: 'Kalos',
        routes: {
            land: [
                'galar_route_7',
            ],
        },
        dungeons: [
            'dusty_bowl',
        ],
        evolution: [
            {
                prev: 'Espurr',
                level: 25,
            },
        ],
    },
    'Honedge': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_6',
                'akala_outskirts',
                'hammerlocke_hills',
            ],
        },
        egg: 'Mystery Egg',
    },
    'Doublade': {
        native_region: 'Kalos',
        routes: {
            land: [
                'giants_cap',
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'energy_plant',
        ],
        evolution: [
            {
                prev: 'Honedge',
                level: 35,
            },
        ],
    },
    'Aegislash (Shield)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'giants_cap',
            ],
        },
        evolution: [
            {
                prev: 'Doublade',
                item: 'Dusk Stone',
            },
        ],
    },
    'Aegislash (Blade)': {
        native_region: 'Kalos',
        special: [
            Has('Aegislash (Blade)') & make_rule('shalour_city') & make_rule('princess_diancie4'),
            Has('Aegislash (Blade)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Spritzee': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_7',
                'galar_route_5',
                'stony_wilderness',
                'giants_mirror',
            ],
        },
        dungeons: [
            'minas_houseboat',
            'glimwood_tangle',
        ],
    },
    'Aromatisse': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Spritzee',
                item: 'Sachet',
            },
        ],
    },
    'Swirlix': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_7',
                'galar_route_5',
                'stony_wilderness',
                'giants_mirror',
            ],
        },
        dungeons: [
            'minas_houseboat',
            'glimwood_tangle',
        ],
    },
    'Slurpuff': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Swirlix',
                item: 'Whipped Dream',
            },
        ],
    },
    'Inkay': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_8',
                'azure_bay',
                'route_1_hauoli_outskirts',
                'poni_wilds',
                'ancient_poni_path',
                'poni_gauntlet',
                'giants_mirror',
                'hammerlocke_hills',
                'galar_route_7',
                'circhester_bay',
                'fields_of_honor',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
            ],
            water: [
                'bridge_field',
            ],
        },
    },
    'Inkay (Pikachu)': {
        native_region: 'Kalos',
        shops: [
            ('disguised_shop', 'dungeonToken'),
        ],
    },
    'Malamar': {
        native_region: 'Kalos',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
            ],
        },
        evolution: [
            {
                prev: 'Inkay',
                level: 30,
            },
        ],
    },
    'Binacle': {
        native_region: 'Kalos',
        routes: {
            land: [
                'motostoke_riverbank',
                'bridge_field',
            ],
        },
        dungeons: [
            'sea_spirits_den',
            'galar_mine_no_2',
        ],
    },
    'Barbaracle': {
        native_region: 'Kalos',
        routes: {
            land: [
                'lake_of_outrage',
                'circhester_bay',
            ],
        },
        dungeons: [
            'dusty_bowl',
            'rock_peak_ruins',
        ],
        evolution: [
            {
                prev: 'Binacle',
                level: 39,
            },
        ],
    },
    'Skrelp': {
        native_region: 'Kalos',
        routes: {
            water: [
                'kalos_route_8',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
        egg: 'Water Egg',
    },
    'Dragalge': {
        native_region: 'Kalos',
        routes: {
            water: [
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
        evolution: [
            {
                prev: 'Skrelp',
                level: 48,
            },
        ],
    },
    'Clauncher': {
        native_region: 'Kalos',
        routes: {
            water: [
                'kalos_route_8',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
        egg: 'Water Egg',
    },
    'Clawitzer': {
        native_region: 'Kalos',
        routes: {
            water: [
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
        evolution: [
            {
                prev: 'Clauncher',
                level: 37,
            },
        ],
    },
    'Helioptile': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_9',
                'giants_mirror',
                'galar_route_6',
            ],
        },
        dungeons: [
            'lake_of_the_sunne_and_moone',
        ],
        egg: 'Electric Egg',
    },
    'Heliolisk': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Helioptile',
                item: 'Sun Stone',
            },
        ],
    },
    'Tyrunt': {
        native_region: 'Kalos',
        trades: [
            ('ambrette_town', ['Jaw Fossil']),
        ],
        special: [
            Has('Tyrunt') & make_rule('ballimere_lake'),
        ],
    },
    'Tyrantrum': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Tyrunt',
                level: 39,
                time: 'day',
            },
        ],
        trades: [
            ('ambrette_town', ['Jaw Fossil']),
        ],
        special: [
            Has('Tyrantrum') & make_rule('ballimere_lake'),
        ],
    },
    'Amaura': {
        native_region: 'Kalos',
        trades: [
            ('ambrette_town', ['Sail Fossil']),
        ],
        special: [
            Has('Amaura') & make_rule('slippery_slope'),
            Has('Amaura') & make_rule('frostpoint_field'),
            Has('Amaura') & make_rule('snowslide_slope'),
        ],
    },
    'Aurorus': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Amaura',
                level: 39,
                time: 'night',
            },
        ],
        trades: [
            ('ambrette_town', ['Sail Fossil']),
        ],
        special: [
            Has('Aurorus') & make_rule('snowslide_slope'),
            Has('Aurorus') & make_rule('iceberg_ruins', False),
        ],
    },
    'Sylveon': {
        native_region: 'Kalos',
        routes: {
            land: [
                'lake_of_outrage',
                'giants_bed',
            ],
        },
        evolution: [
            {
                prev: 'Eevee',
                level: 29,
            },
        ],
    },
    'Hawlucha': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_10',
                'alola_route_3',
                'hammerlocke_hills',
                'galar_route_6',
            ],
        },
        egg: 'Fighting Egg',
    },
    'Dedenne': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_11',
                'challenge_beach',
            ],
        },
        dungeons: [
            'pikachu_valley',
            'hokulani_observatory',
        ],
        dungeon_boss: [
            ('ruins_of_conflict', 82177450),
        ],
        egg: 'Electric Egg',
        farm_wandering: ['Wacan Berry'],
    },
    'Carbink': {
        native_region: 'Kalos',
        dungeons: [
            'reflection_cave',
            'vast_poni_canyon',
            'roaring_sea_caves',
            'lakeside_cave',
            'tunnel_to_the_top',
        ],
        dungeon_boss: [
            ('ten_carat_hill', 59489105),
        ],
        egg: 'Mystery Egg',
    },
    'Goomy': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_14',
                'lake_of_outrage',
                'soothing_wetlands',
                'forest_of_focus',
                'holm_of_trials',
            ],
        },
        dungeons: [
            'ancient_quarry',
        ],
        egg: 'Dragon Egg',
    },
    'Sliggoo': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_19',
                'lake_of_outrage',
            ],
        },
        evolution: [
            {
                prev: 'Goomy',
                level: 40,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Hisuian Sliggoo': {
        native_region: 'Hisui',
        routes: {
            land: [
                'holm_of_trials',
            ],
        },
        dungeons: [
            'turnback_cave',
        ],
        dungeon_boss: [
            ('ancient_quarry', 10000000),
        ],
        evolution: [
            {
                prev: 'Goomy',
                level: 40,
            },
        ],
    },
    'Goodra': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Sliggoo',
                level: 50,
                weather: ['Rain', 'Fog', 'Thunderstorm'],
            },
        ],
        egg: 'Dragon Egg',
        special: [
            Has('Goodra') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Hisuian Goodra': {
        native_region: 'Hisui',
        dungeon_boss: [
            ('ancient_lake_verity', 10000000),
        ],
        evolution: [
            {
                prev: 'Hisuian Sliggoo',
                level: 50,
                weather: ['Rain', 'Fog', 'Thunderstorm'],
            },
        ],
    },
    'Klefki': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_15',
                'kalos_route_16',
                'fields_of_honor',
            ],
        },
        dungeons: [
            'lost_hotel',
            'thrifty_megamart',
        ],
        safari: ['Kalos'],
    },
    'Phantump': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_16',
                'slippery_slope',
                'old_cemetery',
                'giants_foot',
                'three_point_pass',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'memorial_hill',
            'glimwood_tangle',
        ],
        egg: 'Grass Egg',
    },
    'Trevenant': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_20',
                'slippery_slope',
                'old_cemetery',
                'snowslide_slope',
            ],
        },
        dungeon_boss: [
            ('crown_shrine', 161099869),
        ],
        evolution: [
            {
                prev: 'Phantump',
                item: 'Linking Cord',
            },
        ],
    },
    'Pumpkaboo (Average)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_16',
                'galar_route_4',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
    },
    'Pumpkaboo (Small)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_16',
                'galar_route_4',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
    },
    'Pumpkaboo (Large)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_16',
                'galar_route_4',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
    },
    'Pumpkaboo (Super Size)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'kalos_route_16',
                'galar_route_4',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
    },
    'Gourgeist (Average)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'hammerlocke_hills',
            ],
        },
        evolution: [
            {
                prev: 'Pumpkaboo (Average)',
                item: 'Linking Cord',
            },
        ],
    },
    'Gourgeist (Small)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'hammerlocke_hills',
            ],
        },
        evolution: [
            {
                prev: 'Pumpkaboo (Small)',
                item: 'Linking Cord',
            },
        ],
    },
    'Gourgeist (Large)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'hammerlocke_hills',
            ],
        },
        evolution: [
            {
                prev: 'Pumpkaboo (Large)',
                item: 'Linking Cord',
            },
        ],
    },
    'Gourgeist (Super Size)': {
        native_region: 'Kalos',
        routes: {
            land: [
                'hammerlocke_hills',
            ],
        },
        evolution: [
            {
                prev: 'Pumpkaboo (Super Size)',
                item: 'Linking Cord',
            },
        ],
    },
    'Bergmite': {
        native_region: 'Kalos',
        routes: {
            land: [
                'lake_of_outrage',
                'circhester_bay',
                'outer_spikemuth',
                'frigid_sea',
                'three_point_pass',
                'bonechill_wastes',
                'arenas_approach',
            ],
            headbutt: [
                'arenas_approach',
            ],
        },
        dungeons: [
            'frost_cavern',
            'avaluggs_legacy',
            'ice_column_chamber',
            'icepeak_cavern',
        ],
    },
    'Avalugg': {
        native_region: 'Kalos',
        routes: {
            land: [
                'lake_of_outrage',
                'three_point_pass',
            ],
            water: [
                'frigid_sea',
            ],
        },
        evolution: [
            {
                prev: 'Bergmite',
                level: 37,
            },
        ],
    },
    'Hisuian Avalugg': {
        native_region: 'Hisui',
        dungeon_boss: [
            ('avaluggs_legacy', 10000000),
        ],
        evolution: [
            {
                prev: 'Bergmite',
                level: 37,
            },
        ],
    },
    'Noibat': {
        native_region: 'Kalos',
        routes: {
            land: [
                'watchtower_ruins',
                'bridge_field',
            ],
        },
        dungeons: [
            'victory_road_kalos',
            'verdant_cavern',
            'galar_mine_no_2',
        ],
    },
    'Noivern': {
        native_region: 'Kalos',
        routes: {
            land: [
                'bridge_field',
                'lake_of_outrage',
                'ballimere_lake',
            ],
        },
        dungeon_boss: [
            ('resolution_cave', 85572310),
            ('lakeside_cave', 166608415),
        ],
        evolution: [
            {
                prev: 'Noibat',
                level: 48,
            },
        ],
    },
    'Xerneas': {
        native_region: 'Kalos',
        special: [
            make_rule('a_beautiful_world31') & make_rule('team_flare_secret_hq', True, 93659460),
        ],
    },
    'Xerneas (Active)': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Xerneas',
                attack: '100',
                attackIsPercent: 'true',
            },
        ],
        special: [
            Has('Xerneas (Active)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Yveltal': {
        native_region: 'Kalos',
        special: [
            make_rule('a_beautiful_world31') & make_rule('team_flare_secret_hq', True, 93659450),
        ],
    },
    'Zygarde': {
        native_region: 'Kalos',
        dungeon_boss: [
            ('resolution_cave', 88406970),
        ],
        special: [
            Has('Elite Kalos Champion Badge') & make_rule('terminus_cave', True, 92485360),
        ],
    },
    'Diancie': {
        native_region: 'Kalos',
        special: [
            make_rule('princess_diancie7') & make_rule('reflection_cave', True, 69694200),
        ],
    },
    'Mega Diancie': {
        native_region: 'Kalos',
        evolution: [
            {
                prev: 'Diancie',
                item: 'Diancite',
            },
        ],
    },
    'Hoopa': {
        native_region: 'Kalos',
        farm_wandering: ['Micle Berry'],
        special: [
            Has('Elite Kalos Champion Badge') & make_rule('roamer', 'Kalos'),
        ],
    },
    'Hoopa (Unbound)': {
        native_region: 'Kalos',
        temporary_battle: [
            'hoopa6',
        ],
        special: [
            Has('Hoopa (Unbound)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Volcanion': {
        native_region: 'Kalos',
        special: [
            Has('Elite Kalos Champion Badge') & make_rule('kalos_power_plant', True, 83945700),
        ],
    },
    'Rowlet': {
        native_region: 'Alola',
        egg: 'Grass Egg',
        starter: ['Alola'],
        farm_wandering: ['Rindo Berry'],
    },
    'Dartrix': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Rowlet',
                level: 17,
            },
        ],
        special: [
            Has('Dartrix') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Decidueye': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Dartrix',
                level: 34,
            },
        ],
        special: [
            Has('Decidueye') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Hisuian Decidueye': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Dartrix',
                level: 36,
            },
        ],
        starter: ['Hisui'],
    },
    'Litten': {
        native_region: 'Alola',
        egg: 'Fire Egg',
        starter: ['Alola'],
        farm_wandering: ['Occa Berry'],
    },
    'Torracat': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Litten',
                level: 17,
            },
        ],
        special: [
            Has('Torracat') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Incineroar': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Torracat',
                level: 34,
            },
        ],
        special: [
            Has('Incineroar') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Popplio': {
        native_region: 'Alola',
        egg: 'Water Egg',
        starter: ['Alola'],
        farm_wandering: ['Passho Berry'],
    },
    'Brionne': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Popplio',
                level: 17,
            },
        ],
        special: [
            Has('Brionne') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Primarina': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Brionne',
                level: 34,
            },
        ],
        special: [
            Has('Primarina') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Pikipek': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_1',
                'alola_route_4',
                'alola_route_5',
                'alola_route_6',
            ],
        },
    },
    'Trumbeak': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_5',
                'alola_route_8',
                'alola_route_11',
                'poni_grove',
                'poni_plains',
            ],
        },
        dungeons: [
            'lush_jungle',
        ],
        evolution: [
            {
                prev: 'Pikipek',
                level: 14,
            },
        ],
    },
    'Toucannon': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_11',
                'poni_grove',
                'poni_plains',
            ],
        },
        evolution: [
            {
                prev: 'Trumbeak',
                level: 28,
            },
        ],
    },
    'Yungoos': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_1',
                'alola_route_2',
                'kalae_bay',
                'alola_route_4',
                'alola_route_6',
                'alola_route_8',
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
        dungeons: [
            'verdant_cavern',
            'inlet_grotto',
        ],
    },
    'Gumshoos': {
        native_region: 'Alola',
        routes: {
            land: [
                'akala_outskirts',
                'alola_route_10',
                'alola_route_15',
                'alola_route_16',
                'alola_route_17',
                'poni_plains',
            ],
        },
        dungeons: [
            'mount_lanakila',
        ],
        dungeon_boss: [
            ('verdant_cavern', 57978365),
        ],
        evolution: [
            {
                prev: 'Yungoos',
                level: 20,
                time: 'day',
            },
        ],
    },
    'Totem Gumshoos': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_welcome_to_paradise_cousin') & make_rule('verdant_cavern', True, 82543791),
        ],
    },
    'Grubbin': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_1',
                'alola_route_4',
                'alola_route_5',
                'alola_route_6',
                'galar_route_1',
                'dappled_grove',
                'east_lake_axewell',
                'north_lake_miloch',
                'watchtower_ruins',
            ],
        },
        dungeons: [
            'hokulani_observatory',
        ],
        special: [
            Has('Grubbin') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Charjabug': {
        native_region: 'Alola',
        routes: {
            land: [
                'axews_eye',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'hokulani_observatory',
        ],
        evolution: [
            {
                prev: 'Grubbin',
                level: 20,
            },
        ],
        special: [
            Has('Charjabug') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Vikavolt': {
        native_region: 'Alola',
        routes: {
            land: [
                'giants_seat',
                'giants_mirror',
            ],
        },
        dungeon_boss: [
            ('hokulani_observatory', 69418380),
        ],
        evolution: [
            {
                prev: 'Charjabug',
                level: 20,
                environment: 'MagneticField',
            },
            {
                prev: 'Charjabug',
                item: 'Thunder Stone',
                region: 'galarOnly',
            },
        ],
        special: [
            Has('Vikavolt') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Totem Vikavolt': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_child_of_the_stars') & make_rule('hokulani_observatory', True, 82543791),
        ],
    },
    'Crabrawler': {
        native_region: 'Alola',
        egg: 'Fighting Egg',
        farm_wandering: ['Chople Berry'],
    },
    'Crabominable': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Crabrawler',
                level: 20,
                dungeon_evolution: 'mount_lanakila',
            },
        ],
        special: [
            Has('Crabominable') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Oricorio (Baile)': {
        native_region: 'Alola',
        routes: {
            land: [
                'south_province_area_three',
            ],
        },
        dungeon_boss: [
            ('ulaula_meadow', 75635260),
        ],
        farm_wandering: ['Cheri Berry', 'Leppa Berry', 'Razz Berry', 'Figy Berry', 'Pomeg Berry', 'Tamato Berry', 'Spelon Berry', 'Occa Berry', 'Chople Berry', 'Haban Berry', 'Custap Berry', 'Liechi Berry', 'Lansat Berry'],
    },
    'Oricorio (Pom-Pom)': {
        native_region: 'Alola',
        routes: {
            land: [
                'south_province_area_one',
            ],
        },
        dungeon_boss: [
            ('melemele_meadow', 58846350),
        ],
        farm_wandering: ['Aspear Berry', 'Sitrus Berry', 'Pinap Berry', 'Iapapa Berry', 'Grepa Berry', 'Nomel Berry', 'Wacan Berry', 'Shuca Berry', 'Charti Berry', 'Chilan Berry', 'Jaboca Berry', 'Kee Berry'],
    },
    'Oricorio (Pa\'u)': {
        native_region: 'Alola',
        farm_wandering: ['Pecha Berry', 'Persim Berry', 'Nanab Berry', 'Mago Berry', 'Qualot Berry', 'Magost Berry', 'Watmel Berry', 'Pinkan Berry', 'Roseli Berry', 'Petaya Berry'],
    },
    'Oricorio (Sensu)': {
        native_region: 'Alola',
        dungeon_boss: [
            ('poni_meadow', 83299840),
        ],
        farm_wandering: ['Chesto Berry', 'Bluk Berry', 'Wiki Berry', 'Cornn Berry', 'Pamtre Berry', 'Belue Berry', 'Payapa Berry', 'Kasib Berry', 'Colbur Berry', 'Ganlon Berry', 'Enigma Berry'],
    },
    'Cutiefly': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_2',
                'alola_route_3',
                'galar_route_4',
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
            ],
        },
        dungeons: [
            'melemele_meadow',
            'minas_houseboat',
        ],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        special: [
            Has('Cutiefly') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Ribombee': {
        native_region: 'Alola',
        routes: {
            land: [
                'motostoke_riverbank',
                'bridge_field',
                'stony_wilderness',
            ],
        },
        dungeons: [
            'ulaula_meadow',
            'poni_meadow',
        ],
        dungeon_boss: [
            ('minas_houseboat', 81087060),
        ],
        evolution: [
            {
                prev: 'Cutiefly',
                level: 25,
            },
        ],
    },
    'Totem Ribombee': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_eater_of_light') & make_rule('minas_houseboat', True, 82543791),
        ],
    },
    'Rockruff': {
        native_region: 'Alola',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'loop_lagoon',
                'challenge_road',
                'south_province_area_two',
            ],
        },
        dungeon_boss: [
            ('ten_carat_hill', 59489105),
        ],
        egg: 'Mystery Egg',
        farm_wandering: ['Charti Berry'],
    },
    'Lycanroc (Midday)': {
        native_region: 'Alola',
        routes: {
            land: [
                'challenge_road',
            ],
        },
        dungeons: [
            'vast_poni_canyon',
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Rockruff',
                level: 25,
                dayCyclePart: ['Day'],
            },
        ],
    },
    'Lycanroc (Midnight)': {
        native_region: 'Alola',
        routes: {
            land: [
                'challenge_road',
            ],
        },
        dungeons: [
            'vast_poni_canyon',
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Rockruff',
                level: 25,
                dayCyclePart: ['Night'],
            },
        ],
    },
    'Lycanroc (Dusk)': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Rockruff',
                level: 25,
                dayCyclePart: ['Dusk'],
            },
            {
                prev: 'Rockruff',
                level: 25,
                dayCyclePart: ['Dawn'],
            },
        ],
        special: [
            Has('Lycanroc (Dusk)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Wishiwashi (Solo)': {
        native_region: 'Alola',
        routes: {
            land: [
                'melemele_sea',
                'alola_route_9',
                'alola_route_13',
                'alola_route_14',
            ],
            water: [
                'kalae_bay',
                'alola_route_7',
                'alola_route_8',
                'akala_outskirts',
                'alola_route_15',
                'west_lake_axewell',
                'east_lake_axewell',
                'axews_eye',
                'galar_route_9',
                'challenge_beach',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_sea',
                'honeycalm_island',
            ],
        },
    },
    'Wishiwashi (School)': {
        native_region: 'Alola',
        dungeon_boss: [
            ('brooklet_hill', 60690300),
        ],
        evolution: [
            {
                prev: 'Wishiwashi (Solo)',
                level: 20,
            },
        ],
    },
    'Totem Wishiwashi': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_symbiotic_relations') & make_rule('brooklet_hill', True, 82543791),
        ],
    },
    'Mareanie': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_9',
                'galar_route_9',
                'outer_spikemuth',
                'loop_lagoon',
            ],
            water: [
                'motostoke_riverbank',
                'giants_mirror',
            ],
        },
        egg: 'Water Egg',
    },
    'Toxapex': {
        native_region: 'Alola',
        routes: {
            land: [
                'circhester_bay',
                'outer_spikemuth',
                'fields_of_honor',
                'challenge_beach',
                'loop_lagoon',
            ],
        },
        evolution: [
            {
                prev: 'Mareanie',
                level: 38,
            },
        ],
    },
    'Mudbray': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_4',
                'alola_route_6',
                'alola_route_12',
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'giants_seat',
                'south_lake_miloch',
                'north_lake_miloch',
                'galar_route_3',
                'giants_cap',
            ],
        },
        dungeons: [
            'paniola_ranch',
        ],
        egg: 'Mystery Egg',
    },
    'Mudsdale': {
        native_region: 'Alola',
        routes: {
            land: [
                'poni_plains',
                'rolling_fields',
                'dappled_grove',
                'east_lake_axewell',
                'giants_seat',
                'axews_eye',
            ],
        },
        evolution: [
            {
                prev: 'Mudbray',
                level: 30,
            },
        ],
    },
    'Dewpider': {
        native_region: 'Alola',
        routes: {
            land: [
                'galar_route_5',
                'motostoke_riverbank',
                'stony_wilderness',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'brooklet_hill',
        ],
        special: [
            Has('Dewpider') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Araquanid': {
        native_region: 'Alola',
        routes: {
            land: [
                'stony_wilderness',
                'lake_of_outrage',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'malie_garden',
        ],
        dungeon_boss: [
            ('brooklet_hill', 60690300),
        ],
        evolution: [
            {
                prev: 'Dewpider',
                level: 22,
            },
        ],
        special: [
            Has('Araquanid') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Totem Araquanid': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_symbiotic_relations') & make_rule('brooklet_hill', True, 82543791),
        ],
    },
    'Fomantis': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_5',
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
            ],
        },
        dungeons: [
            'lush_jungle',
        ],
        egg: 'Grass Egg',
    },
    'Lurantis': {
        native_region: 'Alola',
        routes: {
            land: [
                'forest_of_focus',
            ],
        },
        dungeon_boss: [
            ('lush_jungle', 65451660),
        ],
        evolution: [
            {
                prev: 'Fomantis',
                level: 34,
                time: 'day',
            },
        ],
    },
    'Totem Lurantis': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_symbiotic_relations') & make_rule('lush_jungle', True, 82543791),
        ],
    },
    'Morelull': {
        native_region: 'Alola',
        routes: {
            land: [
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
        egg: 'Grass Egg',
        special: [
            Has('Morelull') & make_rule('brooklet_hill', False),
            Has('Morelull') & make_rule('lush_jungle', False),
        ],
    },
    'Shiinotic': {
        native_region: 'Alola',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'glimwood_tangle',
        ],
        dungeon_boss: [
            ('ruins_of_abundance', 82177450),
        ],
        evolution: [
            {
                prev: 'Morelull',
                level: 24,
            },
        ],
        special: [
            Has('Shiinotic') & make_rule('alola_route_11'),
        ],
    },
    'Salandit': {
        native_region: 'Alola',
        routes: {
            land: [
                'motostoke_outskirts',
                'motostoke_riverbank',
                'stony_wilderness',
                'challenge_road',
            ],
        },
        dungeons: [
            'wela_volcano_park',
        ],
        egg: 'Fire Egg',
        farm_wandering: ['Kebia Berry'],
        special: [
            Has('Salandit') & make_rule('alola_route_8'),
        ],
    },
    'Salazzle': {
        native_region: 'Alola',
        routes: {
            land: [
                'challenge_road',
            ],
        },
        dungeon_boss: [
            ('wela_volcano_park', 64481960),
        ],
        evolution: [
            {
                prev: 'Salandit',
                level: 33,
            },
        ],
    },
    'Totem Salazzle': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_symbiotic_relations') & make_rule('wela_volcano_park', True, 82543791),
        ],
    },
    'Stufful': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_8',
                'akala_outskirts',
                'dappled_grove',
                'east_lake_axewell',
                'giants_seat',
                'north_lake_miloch',
                'galar_route_5',
                'bridge_field',
                'hammerlocke_hills',
            ],
        },
        egg: 'Fighting Egg',
    },
    'Bewear': {
        native_region: 'Alola',
        routes: {
            land: [
                'poni_gauntlet',
                'dappled_grove',
                'giants_seat',
                'axews_eye',
                'bridge_field',
                'lake_of_outrage',
            ],
        },
        evolution: [
            {
                prev: 'Stufful',
                level: 27,
            },
        ],
    },
    'Bounsweet': {
        native_region: 'Alola',
        routes: {
            land: [
                'rolling_fields',
                'dappled_grove',
                'west_lake_axewell',
                'east_lake_axewell',
                'watchtower_ruins',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'lush_jungle',
        ],
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
    },
    'Steenee': {
        native_region: 'Alola',
        routes: {
            land: [
                'axews_eye',
            ],
        },
        dungeons: [
            'lush_jungle',
        ],
        evolution: [
            {
                prev: 'Bounsweet',
                level: 18,
            },
        ],
    },
    'Tsareena': {
        native_region: 'Alola',
        routes: {
            land: [
                'stony_wilderness',
            ],
        },
        evolution: [
            {
                prev: 'Steenee',
                level: 29,
            },
        ],
    },
    'Comfey': {
        native_region: 'Alola',
        routes: {
            land: [
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
                'insular_sea',
                'honeycalm_island',
            ],
        },
        dungeons: [
            'lush_jungle',
            'minas_houseboat',
            'ruins_of_conflict',
            'ruins_of_life',
            'ruins_of_abundance',
            'ruins_of_hope',
        ],
    },
    'Oranguru': {
        native_region: 'Alola',
        routes: {
            land: [
                'forest_of_focus',
            ],
        },
        dungeons: [
            'lush_jungle',
            'glimwood_tangle',
        ],
    },
    'Passimian': {
        native_region: 'Alola',
        routes: {
            land: [
                'forest_of_focus',
            ],
        },
        dungeons: [
            'lush_jungle',
            'glimwood_tangle',
        ],
    },
    'Wimpod': {
        native_region: 'Alola',
        routes: {
            land: [
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
                'hammerlocke_hills',
            ],
        },
        dungeons: [
            'galar_mine_no_2',
        ],
        egg: 'Water Egg',
        special: [
            Has('Wimpod') & make_rule('alola_route_8'),
            Has('Wimpod') & make_rule('poni_breaker_coast'),
            Has('Wimpod') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Golisopod': {
        native_region: 'Alola',
        routes: {
            land: [
                'bridge_field',
                'giants_cap',
                'lake_of_outrage',
                'challenge_beach',
            ],
        },
        dungeons: [
            'energy_plant',
        ],
        dungeon_boss: [
            ('courageous_cavern', 133520620),
        ],
        evolution: [
            {
                prev: 'Wimpod',
                level: 30,
            },
        ],
        special: [
            Has('Golisopod') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Sandygast': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_15',
                'loop_lagoon',
            ],
        },
    },
    'Palossand': {
        native_region: 'Alola',
        routes: {
            land: [
                'loop_lagoon',
            ],
        },
        evolution: [
            {
                prev: 'Sandygast',
                level: 42,
            },
        ],
    },
    'Pyukumuku': {
        native_region: 'Alola',
        routes: {
            land: [
                'galar_route_9',
            ],
            water: [
                'alola_route_7',
                'giants_seat',
                'south_lake_miloch',
            ],
        },
    },
    'Type: Null': {
        native_region: 'Alola',
        shops: [
            ('aether_paradise', 'questPoint'),
        ],
    },
    'Silvally (Normal)': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Type: Null',
                item: 'Soothe Bell',
            },
        ],
    },
    'Silvally (Fire)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Fire Gems'),
        ],
    },
    'Silvally (Water)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Water Gems'),
        ],
    },
    'Silvally (Electric)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Electric Gems'),
        ],
    },
    'Silvally (Grass)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Grass Gems'),
        ],
    },
    'Silvally (Ice)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Ice Gems'),
        ],
    },
    'Silvally (Fighting)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Fighting Gems'),
        ],
    },
    'Silvally (Poison)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Poison Gems'),
        ],
    },
    'Silvally (Ground)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Ground Gems'),
        ],
    },
    'Silvally (Flying)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Flying Gems'),
        ],
    },
    'Silvally (Psychic)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Psychic Gems'),
        ],
    },
    'Silvally (Bug)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Bug Gems'),
        ],
    },
    'Silvally (Rock)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Rock Gems'),
        ],
    },
    'Silvally (Ghost)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Ghost Gems'),
        ],
    },
    'Silvally (Dragon)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Dragon Gems'),
        ],
    },
    'Silvally (Dark)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Dark Gems'),
        ],
    },
    'Silvally (Steel)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Steel Gems'),
        ],
    },
    'Silvally (Fairy)': {
        native_region: 'Alola',
        shops: [
            ('aether_foundation', 'Fairy Gems'),
        ],
    },
    'Minior (Meteor)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
        special: [
            Has('Cosmoem') & make_rule('lake_of_the_sunne_and_moone', True, 82177450),
        ],
    },
    'Minior (Red Core)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
    },
    'Minior (Orange Core)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
    },
    'Minior (Yellow Core)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
        special: [
            Has('Solgaleo') & Has('Necrozma') & make_rule('lake_of_the_sunne_and_moone', True, 82177450),
        ],
    },
    'Minior (Green Core)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
    },
    'Minior (Blue Core)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
    },
    'Minior (Indigo Core)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
    },
    'Minior (Violet Core)': {
        native_region: 'Alola',
        routes: {
            land: [
                'mount_hokulani',
            ],
        },
        special: [
            Has('Lunala') & Has('Necrozma') & make_rule('lake_of_the_sunne_and_moone', True, 82177450),
        ],
    },
    'Komala': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_11',
            ],
        },
    },
    'Turtonator': {
        native_region: 'Alola',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        egg: 'Dragon Egg',
    },
    'Togedemaru': {
        native_region: 'Alola',
        routes: {
            land: [
                'lake_of_outrage',
                'galar_route_8',
            ],
        },
        dungeon_boss: [
            ('hokulani_observatory', 69418380),
        ],
        egg: 'Electric Egg',
        farm_wandering: ['Wacan Berry'],
    },
    'Totem Togedemaru': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_child_of_the_stars') & make_rule('hokulani_observatory', True, 82543791),
        ],
    },
    'Mimikyu': {
        native_region: 'Alola',
        routes: {
            land: [
                'bridge_field',
                'giants_mirror',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
                'snowslide_slope',
            ],
        },
        dungeon_boss: [
            ('thrifty_megamart', 73527110),
        ],
    },
    'Totem Mimikyu': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_child_of_the_stars') & make_rule('thrifty_megamart', True, 82543791),
        ],
    },
    'Bruxish': {
        native_region: 'Alola',
        routes: {
            land: [
                'alola_route_13',
                'alola_route_14',
            ],
            water: [
                'alola_route_15',
            ],
        },
    },
    'Drampa': {
        native_region: 'Alola',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        egg: 'Dragon Egg',
        farm_wandering: ['Haban Berry'],
    },
    'Dhelmise': {
        native_region: 'Alola',
        routes: {
            land: [
                'circhester_bay',
                'outer_spikemuth',
            ],
            water: [
                'challenge_beach',
                'frigid_sea',
            ],
        },
        dungeons: [
            'minas_houseboat',
            'crown_shrine',
        ],
    },
    'Jangmo-o': {
        native_region: 'Alola',
        routes: {
            land: [
                'lake_of_outrage',
                'training_lowlands',
                'potbottom_desert',
                'challenge_road',
            ],
        },
        dungeons: [
            'vast_poni_canyon',
        ],
        egg: 'Dragon Egg',
    },
    'Hakamo-o': {
        native_region: 'Alola',
        routes: {
            land: [
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'vast_poni_canyon',
        ],
        evolution: [
            {
                prev: 'Jangmo-o',
                level: 35,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Kommo-o': {
        native_region: 'Alola',
        dungeon_boss: [
            ('vast_poni_canyon', 79960220),
        ],
        evolution: [
            {
                prev: 'Hakamo-o',
                level: 45,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Totem Kommo-o': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('completed_emissary_of_light') & make_rule('vast_poni_canyon', True, 82543791),
        ],
    },
    'Tapu Koko': {
        native_region: 'Alola',
        dungeon_boss: [
            ('ruins_of_conflict', 82543791),
        ],
    },
    'Tapu Lele': {
        native_region: 'Alola',
        dungeon_boss: [
            ('ruins_of_life', 82543791),
        ],
    },
    'Tapu Bulu': {
        native_region: 'Alola',
        dungeon_boss: [
            ('ruins_of_abundance', 82543791),
        ],
    },
    'Tapu Fini': {
        native_region: 'Alola',
        dungeon_boss: [
            ('ruins_of_hope', 82543791),
        ],
    },
    'Cosmog': {
        native_region: 'Alola',
        dungeon_boss: [
            ('lake_of_the_sunne_and_moone', 82177450),
        ],
    },
    'Cosmoem': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Cosmog',
                level: 43,
            },
        ],
        special: [
            Has('Cosmoem') & make_rule('lake_of_the_sunne_and_moone', True, 82177450),
        ],
    },
    'Solgaleo': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Cosmoem',
                level: 53,
            },
        ],
        temporary_battle: [
            'lillie',
        ],
        special: [
            Has('Solgaleo') & Has('Necrozma') & make_rule('lake_of_the_sunne_and_moone', True, 90673816),
        ],
    },
    'Solgaleo (Radiant Sun)': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Solgaleo',
                item: 'Solar Light',
            },
        ],
    },
    'Lunala': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Cosmoem',
                level: 53,
            },
        ],
        temporary_battle: [
            'lillie',
        ],
        special: [
            Has('Lunala') & Has('Necrozma') & make_rule('lake_of_the_sunne_and_moone', True, 90673816),
        ],
    },
    'Lunala (Full Moon)': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Lunala',
                item: 'Lunar Light',
            },
        ],
    },
    'Nihilego': {
        native_region: 'Alola',
        special: [
            make_rule('wela_volcano_park', False) & make_rule('ultra_beast_hunt3'),
            make_rule('digletts_tunnel', False) & make_rule('ultra_beast_hunt3'),
        ],
    },
    'Buzzwole': {
        native_region: 'Alola',
        special: [
            make_rule('melemele_meadow', False) & make_rule('ultra_beast_hunt5'),
        ],
    },
    'Pheromosa': {
        native_region: 'Alola',
        special: [
            make_rule('verdant_cavern', False) & make_rule('ultra_beast_hunt5'),
        ],
    },
    'Xurkitree': {
        native_region: 'Alola',
        special: [
            make_rule('lush_jungle', False) & make_rule('ultra_beast_hunt9'),
            make_rule('memorial_hill', False) & make_rule('ultra_beast_hunt9'),
        ],
    },
    'Celesteela': {
        native_region: 'Alola',
        special: [
            make_rule('haina_desert') & make_rule('ultra_beast_hunt11'),
            make_rule('malie_garden', False) & make_rule('ultra_beast_hunt11'),
        ],
    },
    'Kartana': {
        native_region: 'Alola',
        special: [
            make_rule('alola_route_17') & make_rule('ultra_beast_hunt11'),
            make_rule('malie_garden', False) & make_rule('ultra_beast_hunt11'),
        ],
    },
    'Guzzlord': {
        native_region: 'Alola',
        dungeon_boss: [
            ('resolution_cave', 90673816),
        ],
    },
    'Necrozma': {
        native_region: 'Alola',
        special: [
            {
                dungeon: 'ten_carat_hill',
                rule: make_rule('ten_carat_hill', False) & make_rule('completed_ultra_beast_hunt'),
                requirements: [
                    {
                        type: 'StatisticRequirement',
                        args: [
                            ['pokemonEncountered', 'PokemonHelper.getPokemonByName(\'Necrozma\').id'],
                            '1',
                            'Must have encountered Necrozma before.',
                        ],
                    },
                ],
            },
            Has('Champion Stamp Badge') & make_rule('eater_of_light5') & make_rule('mount_lanakila', True, 83527125),
        ],
    },
    'Necrozma (Dusk Mane)': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Necrozma',
                item: 'Solar Light',
            },
        ],
    },
    'Necrozma (Dawn Wings)': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Necrozma',
                item: 'Lunar Light',
            },
        ],
    },
    'Ultra Necrozma': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Necrozma (Dusk Mane)',
                item: 'Pure Light',
            },
            {
                prev: 'Necrozma (Dawn Wings)',
                item: 'Pure Light',
            },
        ],
    },
    'Magearna': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('roamer', 'Alola'),
        ],
    },
    'Magearna (Original Color)': {
        native_region: 'Alola',
        special: [
            {
                route: 'postwick',
                requirements: [
                    {
                        type: 'CustomRequirement',
                        args: [
                            'ko.pureComputed(() => +magearnaGiftReq.isCompleted())',
                            '1',
                            'Complete all regional Shiny Master achievements from Kanto through Galar.',
                        ],
                    },
                ],
            },
            Has('Magearna (Original Color)') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Marshadow': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('roamer', 'Alola'),
        ],
    },
    'Marshadow (Zenith)': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Marshadow',
                item: 'Crystallized Shadow',
            },
        ],
    },
    'Poipole': {
        native_region: 'Alola',
        shops: [
            ('altar_of_the_sunne_and_moone', 'questPoint'),
        ],
    },
    'Naganadel': {
        native_region: 'Alola',
        evolution: [
            {
                prev: 'Poipole',
                level: 41,
            },
        ],
        special: [
            Has('Naganadel') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Stakataka': {
        native_region: 'Alola',
        special: [
            make_rule('poni_grove') & make_rule('ultra_beast_hunt15'),
        ],
    },
    'Blacephalon': {
        native_region: 'Alola',
        special: [
            make_rule('poni_grove') & make_rule('ultra_beast_hunt15'),
        ],
    },
    'Zeraora': {
        native_region: 'Alola',
        special: [
            Has('Champion Stamp Badge') & make_rule('roamer', 'Alola'),
        ],
    },
    'Meltan': {
        special: [
            make_rule('any_alola_route') & make_rule('lets_go_meltan9'),
        ],
    },
    'Melmetal': {
        quest_rewards: [
            'completed_lets_go_meltan',
        ],
        special: [
            Has('Melmetal') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Gigantamax Melmetal': {
        special: [
            (Has('Gigantamax Melmetal') | make_rule('lair_of_giants13')) & make_rule('max_lair'),
        ],
    },
    'Grookey': {
        native_region: 'Galar',
        egg: 'Grass Egg',
        starter: ['Galar'],
        farm_wandering: ['Rindo Berry'],
    },
    'Thwackey': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Grookey',
                level: 16,
            },
        ],
        special: [
            Has('Thwackey') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Rillaboom': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Thwackey',
                level: 35,
            },
        ],
        special: [
            Has('Rillaboom') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Gigantamax Rillaboom': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Rillaboom') | make_rule('lair_of_giants14')) & make_rule('max_lair'),
        ],
    },
    'Scorbunny': {
        native_region: 'Galar',
        egg: 'Fire Egg',
        starter: ['Galar'],
        farm_wandering: ['Occa Berry'],
    },
    'Raboot': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Scorbunny',
                level: 16,
            },
        ],
        special: [
            Has('Raboot') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Cinderace': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Raboot',
                level: 35,
            },
        ],
        special: [
            Has('Cinderace') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Gigantamax Cinderace': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Cinderace') | make_rule('lair_of_giants15')) & make_rule('max_lair'),
        ],
    },
    'Sobble': {
        native_region: 'Galar',
        egg: 'Water Egg',
        starter: ['Galar'],
        farm_wandering: ['Passho Berry'],
    },
    'Drizzile': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Sobble',
                level: 16,
            },
        ],
        special: [
            Has('Drizzile') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Inteleon': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Drizzile',
                level: 35,
            },
        ],
        special: [
            Has('Inteleon') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Gigantamax Inteleon': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Inteleon') | make_rule('lair_of_giants16')) & make_rule('max_lair'),
        ],
    },
    'Skwovet': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_1',
                'galar_route_2',
                'south_province_area_one',
                'south_province_area_two',
            ],
            headbutt: [
                'rolling_fields',
                'dappled_grove',
                'north_lake_miloch',
                'watchtower_ruins',
                'galar_route_3',
                'galar_route_4',
                'galar_route_5',
                'motostoke_riverbank',
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'giants_foot',
                'ballimere_lake',
            ],
        },
        farm_wandering: ['Chilan Berry'],
    },
    'Greedent': {
        native_region: 'Galar',
        routes: {
            headbutt: [
                'giants_seat',
                'axews_eye',
                'motostoke_riverbank',
                'bridge_field',
                'giants_mirror',
                'giants_cap',
                'lake_of_outrage',
                'galar_route_6',
                'galar_route_7',
                'circhester_bay',
                'outer_spikemuth',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'giants_foot',
                'ballimere_lake',
            ],
        },
        dungeon_boss: [
            ('dyna_tree_hill', 166608415),
        ],
        evolution: [
            {
                prev: 'Skwovet',
                level: 24,
            },
        ],
    },
    'Rookidee': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_1',
                'galar_route_2',
                'galar_route_3',
                'motostoke_riverbank',
                'south_province_area_three',
            ],
        },
    },
    'Corvisquire': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_3',
                'motostoke_riverbank',
                'giants_mirror',
                'hammerlocke_hills',
                'ballimere_lake',
            ],
        },
        evolution: [
            {
                prev: 'Rookidee',
                level: 18,
            },
        ],
    },
    'Corviknight': {
        native_region: 'Galar',
        routes: {
            land: [
                'north_lake_miloch',
                'watchtower_ruins',
                'giants_cap',
                'lake_of_outrage',
                'hammerlocke_hills',
                'galar_route_7',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'iron_ruins',
            'area_zero',
        ],
        dungeon_boss: [
            ('slumbering_weald_shrine', 135047520),
        ],
        evolution: [
            {
                prev: 'Corvisquire',
                level: 38,
            },
        ],
    },
    'Gigantamax Corviknight': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Corviknight') | make_rule('lair_of_giants17')) & make_rule('max_lair'),
        ],
    },
    'Blipbug': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_1',
                'galar_route_2',
                'galar_route_2_lakeside',
                'fields_of_honor',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'challenge_road',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
                'honeycalm_island',
            ],
        },
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
        special: [
            Has('Blipbug') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Dottler': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_5',
                'stony_wilderness',
                'giants_mirror',
                'giants_cap',
            ],
        },
        evolution: [
            {
                prev: 'Blipbug',
                level: 10,
            },
        ],
        special: [
            Has('Dottler') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Orbeetle': {
        native_region: 'Galar',
        routes: {
            land: [
                'dappled_grove',
                'giants_cap',
                'lake_of_outrage',
            ],
        },
        dungeons: [
            'slumbering_weald_shrine',
        ],
        evolution: [
            {
                prev: 'Dottler',
                level: 30,
            },
        ],
        special: [
            Has('Orbeetle') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Gigantamax Orbeetle': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Orbeetle') | make_rule('lair_of_giants18')) & make_rule('max_lair'),
        ],
    },
    'Nickit': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_1',
                'galar_route_2',
                'stony_wilderness',
                'giants_mirror',
                'galar_route_2_lakeside',
            ],
        },
    },
    'Thievul': {
        native_region: 'Galar',
        routes: {
            land: [
                'south_lake_miloch',
                'bridge_field',
                'stony_wilderness',
                'hammerlocke_hills',
                'galar_route_7',
                'outer_spikemuth',
            ],
        },
        evolution: [
            {
                prev: 'Nickit',
                level: 18,
            },
        ],
    },
    'Gossifleur': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_3',
                'motostoke_riverbank',
                'galar_route_2_lakeside',
                'ballimere_lake',
            ],
        },
        egg: 'Grass Egg',
        farm_wandering: ['Cheri Berry', 'Chesto Berry', 'Pecha Berry', 'Rawst Berry', 'Aspear Berry', 'Leppa Berry', 'Oran Berry', 'Sitrus Berry', 'Persim Berry', 'Razz Berry', 'Bluk Berry', 'Nanab Berry', 'Wepear Berry', 'Pinap Berry', 'Figy Berry', 'Wiki Berry', 'Mago Berry', 'Aguav Berry', 'Iapapa Berry', 'Lum Berry', 'Pomeg Berry', 'Kelpsy Berry', 'Qualot Berry', 'Hondew Berry', 'Grepa Berry', 'Tamato Berry', 'Cornn Berry', 'Magost Berry', 'Rabuta Berry', 'Nomel Berry', 'Spelon Berry', 'Pamtre Berry', 'Watmel Berry', 'Durin Berry', 'Belue Berry', 'Pinkan Berry', 'Occa Berry', 'Passho Berry', 'Wacan Berry', 'Rindo Berry', 'Yache Berry', 'Chople Berry', 'Kebia Berry', 'Shuca Berry', 'Coba Berry', 'Payapa Berry', 'Tanga Berry', 'Charti Berry', 'Kasib Berry', 'Haban Berry', 'Colbur Berry', 'Babiri Berry', 'Chilan Berry', 'Roseli Berry', 'Snover Berry', 'Micle Berry', 'Custap Berry', 'Jaboca Berry', 'Rowap Berry', 'Kee Berry', 'Maranga Berry', 'Liechi Berry', 'Ganlon Berry', 'Salac Berry', 'Petaya Berry', 'Apicot Berry', 'Lansat Berry', 'Starf Berry', 'Enigma Berry', 'Hopo Berry'],
    },
    'Eldegoss': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_5',
                'motostoke_riverbank',
                'stony_wilderness',
                'giants_cap',
                'ballimere_lake',
            ],
        },
        evolution: [
            {
                prev: 'Gossifleur',
                level: 20,
            },
        ],
    },
    'Wooloo': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_1',
                'galar_route_4',
                'motostoke_riverbank',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'three_point_pass',
                'snowslide_slope',
            ],
        },
    },
    'Dubwool': {
        native_region: 'Galar',
        routes: {
            land: [
                'rolling_fields',
                'motostoke_riverbank',
                'hammerlocke_hills',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'three_point_pass',
                'snowslide_slope',
            ],
        },
        dungeons: [
            'dyna_tree_hill',
        ],
        evolution: [
            {
                prev: 'Wooloo',
                level: 24,
            },
        ],
    },
    'Chewtle': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_2',
                'motostoke_outskirts',
                'motostoke_riverbank',
                'giants_mirror',
                'galar_route_2_lakeside',
            ],
            water: [
                'galar_route_4',
                'galar_route_5',
                'soothing_wetlands',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        dungeons: [
            'galar_mine_no_2',
            'courageous_cavern',
        ],
        egg: 'Water Egg',
    },
    'Drednaw': {
        native_region: 'Galar',
        routes: {
            land: [
                'giants_cap',
                'fields_of_honor',
                'soothing_wetlands',
                'challenge_beach',
                'loop_lagoon',
            ],
            water: [
                'west_lake_axewell',
                'bridge_field',
                'giants_mirror',
                'galar_route_6',
                'galar_route_2_lakeside',
            ],
        },
        dungeon_boss: [
            ('galar_mine_no_2', 106473200),
            ('courageous_cavern', 133520620),
        ],
        evolution: [
            {
                prev: 'Chewtle',
                level: 22,
            },
        ],
    },
    'Gigantamax Drednaw': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Drednaw') | make_rule('lair_of_giants19')) & make_rule('max_lair'),
        ],
    },
    'Yamper': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_2',
                'galar_route_4',
                'motostoke_riverbank',
                'stony_wilderness',
                'giants_mirror',
                'galar_route_2_lakeside',
                'ballimere_lake',
            ],
        },
    },
    'Boltund': {
        native_region: 'Galar',
        routes: {
            land: [
                'north_lake_miloch',
                'motostoke_riverbank',
                'lake_of_outrage',
                'ballimere_lake',
            ],
        },
        evolution: [
            {
                prev: 'Yamper',
                level: 25,
            },
        ],
    },
    'Rolycoly': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_3',
                'motostoke_riverbank',
                'giants_cap',
            ],
        },
        dungeons: [
            'galar_mine',
        ],
        egg: 'Mystery Egg',
    },
    'Carkol': {
        native_region: 'Galar',
        routes: {
            land: [
                'bridge_field',
                'stony_wilderness',
                'giants_cap',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'lakeside_cave',
        ],
        dungeon_boss: [
            ('galar_mine', 103839200),
        ],
        dungeon_chest: [
            'galar_mine',
        ],
        evolution: [
            {
                prev: 'Rolycoly',
                level: 18,
            },
        ],
    },
    'Coalossal': {
        native_region: 'Galar',
        routes: {
            land: [
                'giants_cap',
                'lake_of_outrage',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'rock_peak_ruins',
        ],
        dungeon_boss: [
            ('lakeside_cave', 166608415),
        ],
        evolution: [
            {
                prev: 'Carkol',
                level: 34,
            },
        ],
    },
    'Gigantamax Coalossal': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Coalossal') | make_rule('lair_of_giants20')) & make_rule('max_lair'),
        ],
    },
    'Applin': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_5',
                'stony_wilderness',
                'giants_mirror',
                'south_province_area_two',
            ],
            headbutt: [
                'fields_of_honor',
                'soothing_wetlands',
                'forest_of_focus',
                'challenge_beach',
                'loop_lagoon',
                'training_lowlands',
                'workout_sea',
                'stepping_stone_sea',
                'insular_sea',
            ],
        },
        dungeons: [
            'dusty_bowl',
        ],
        egg: 'Grass Egg',
        farm_wandering: ['Haban Berry'],
    },
    'Exposed Applin': {
        native_region: 'Galar',
        farm_wandering: ['Haban Berry'],
    },
    'Flapple': {
        native_region: 'Galar',
        routes: {
            headbutt: [
                'stepping_stone_sea',
            ],
        },
        evolution: [
            {
                prev: 'Applin',
                item: 'Tart Apple',
            },
        ],
    },
    'Gigantamax Flapple': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Flapple') | make_rule('lair_of_giants21')) & make_rule('max_lair'),
        ],
    },
    'Appletun': {
        native_region: 'Galar',
        routes: {
            headbutt: [
                'stepping_stone_sea',
            ],
        },
        evolution: [
            {
                prev: 'Applin',
                item: 'Sweet Apple',
            },
        ],
    },
    'Gigantamax Appletun': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Appletun') | make_rule('lair_of_giants22')) & make_rule('max_lair'),
        ],
    },
    'Silicobra': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_6',
                'forest_of_focus',
                'training_lowlands',
                'potbottom_desert',
                'challenge_road',
            ],
        },
    },
    'Sandaconda': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'galar_route_8',
                'potbottom_desert',
            ],
        },
        evolution: [
            {
                prev: 'Silicobra',
                level: 36,
            },
        ],
    },
    'Gigantamax Sandaconda': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Sandaconda') | make_rule('lair_of_giants23')) & make_rule('max_lair'),
        ],
    },
    'Cramorant': {
        native_region: 'Galar',
        routes: {
            land: [
                'axews_eye',
                'galar_route_9',
                'circhester_bay',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
            ],
        },
    },
    'Cramorant (Gulping)': {
        native_region: 'Galar',
        routes: {
            land: [
                'axews_eye',
                'bridge_field',
                'stony_wilderness',
                'lake_of_outrage',
                'galar_route_9',
                'circhester_bay',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
            ],
        },
    },
    'Cramorant (Gorging)': {
        native_region: 'Galar',
        routes: {
            land: [
                'axews_eye',
                'galar_route_9',
                'circhester_bay',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
            ],
        },
    },
    'Arrokuda': {
        native_region: 'Galar',
        routes: {
            water: [
                'galar_route_2',
                'motostoke_riverbank',
                'galar_route_2_lakeside',
                'forest_of_focus',
                'challenge_beach',
                'training_lowlands',
                'poco_path',
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
        egg: 'Water Egg',
    },
    'Barraskewda': {
        native_region: 'Galar',
        routes: {
            land: [
                'challenge_beach',
                'training_lowlands',
            ],
            water: [
                'motostoke_riverbank',
                'lake_of_outrage',
                'galar_route_2_lakeside',
            ],
        },
        evolution: [
            {
                prev: 'Arrokuda',
                level: 26,
            },
        ],
    },
    'Toxel': {
        native_region: 'Galar',
        egg: 'Electric Egg',
        farm_wandering: ['Kebia Berry'],
        breeding: ['Toxtricity (Amped)', 'Toxtricity (Low Key)', 'Gigantamax Toxtricity'],
        special: [
            Has('Toxel') & make_rule('motostoke_riverbank'),
            Has('Toxel') & make_rule('bridge_field'),
            Has('Toxel') & make_rule('stony_wilderness'),
            Has('Toxel') & make_rule('giants_cap'),
            Has('Toxel') & make_rule('hammerlocke_hills'),
            Has('Toxel') & make_rule('galar_route_7'),
        ],
    },
    'Toxtricity (Amped)': {
        native_region: 'Galar',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Toxel',
                level: 30,
            },
        ],
    },
    'Toxtricity (Low Key)': {
        native_region: 'Galar',
        dungeons: [
            'max_lair',
        ],
        evolution: [
            {
                prev: 'Toxel',
                level: 30,
            },
        ],
    },
    'Gigantamax Toxtricity': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Toxtricity') | make_rule('lair_of_giants24')) & make_rule('max_lair'),
        ],
    },
    'Sizzlipede': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_3',
                'giants_foot',
            ],
        },
        egg: 'Fire Egg',
        farm_wandering: ['Tanga Berry'],
        special: [
            Has('Sizzlipede') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Centiskorch': {
        native_region: 'Galar',
        routes: {
            land: [
                'giants_foot',
            ],
        },
        evolution: [
            {
                prev: 'Sizzlipede',
                level: 28,
            },
        ],
    },
    'Gigantamax Centiskorch': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Centiskorch') | make_rule('lair_of_giants25')) & make_rule('max_lair'),
        ],
    },
    'Clobbopus': {
        native_region: 'Galar',
        egg: 'Fighting Egg',
        special: [
            Has('Clobbopus') & make_rule('galar_route_9'),
            Has('Clobbopus') & make_rule('circhester_bay'),
            Has('Clobbopus') & make_rule('outer_spikemuth'),
            Has('Clobbopus') & make_rule('loop_lagoon'),
            Has('Clobbopus') & make_rule('courageous_cavern', False),
        ],
    },
    'Grapploct': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Clobbopus',
                level: 35,
            },
        ],
        special: [
            Has('Grapploct') & make_rule('west_lake_axewell'),
            Has('Grapploct') & make_rule('lake_of_outrage'),
            Has('Grapploct') & make_rule('circhester_bay'),
            Has('Grapploct') & make_rule('loop_lagoon'),
        ],
    },
    'Sinistea': {
        native_region: 'Galar',
        routes: {
            land: [
                'old_cemetery',
            ],
        },
        dungeons: [
            'glimwood_tangle',
        ],
    },
    'Polteageist': {
        native_region: 'Galar',
        routes: {
            land: [
                'old_cemetery',
            ],
        },
        evolution: [
            {
                prev: 'Sinistea',
                item: 'Cracked Pot',
            },
        ],
    },
    'Hatenna': {
        native_region: 'Galar',
        routes: {
            land: [
                'motostoke_outskirts',
                'stony_wilderness',
                'hammerlocke_hills',
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
            ],
        },
    },
    'Hattrem': {
        native_region: 'Galar',
        routes: {
            land: [
                'slippery_slope',
                'frostpoint_field',
                'giants_bed',
                'old_cemetery',
                'giants_foot',
                'frigid_sea',
                'three_point_pass',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'dusty_bowl',
        ],
        dungeon_boss: [
            ('glimwood_tangle', 118824240),
        ],
        evolution: [
            {
                prev: 'Hatenna',
                level: 32,
            },
        ],
    },
    'Hatterene': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'frostpoint_field',
                'giants_bed',
                'frigid_sea',
                'ballimere_lake',
            ],
        },
        dungeons: [
            'crown_shrine',
        ],
        evolution: [
            {
                prev: 'Hattrem',
                level: 42,
            },
        ],
    },
    'Gigantamax Hatterene': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Hatterene') | make_rule('lair_of_giants26')) & make_rule('max_lair'),
        ],
    },
    'Impidimp': {
        native_region: 'Galar',
        routes: {
            land: [
                'motostoke_outskirts',
                'stony_wilderness',
                'giants_mirror',
                'hammerlocke_hills',
                'slippery_slope',
            ],
        },
        dungeons: [
            'glimwood_tangle',
        ],
        farm_wandering: ['Colbur Berry'],
    },
    'Morgrem': {
        native_region: 'Galar',
        routes: {
            land: [
                'giants_bed',
                'giants_foot',
                'snowslide_slope',
            ],
        },
        dungeon_boss: [
            ('glimwood_tangle', 118824240),
        ],
        evolution: [
            {
                prev: 'Impidimp',
                level: 32,
            },
        ],
    },
    'Grimmsnarl': {
        native_region: 'Galar',
        routes: {
            land: [
                'stony_wilderness',
                'lake_of_outrage',
                'slippery_slope',
                'giants_bed',
                'snowslide_slope',
            ],
        },
        evolution: [
            {
                prev: 'Morgrem',
                level: 42,
            },
        ],
    },
    'Gigantamax Grimmsnarl': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Grimmsnarl') | make_rule('lair_of_giants27')) & make_rule('max_lair'),
        ],
    },
    'Obstagoon': {
        native_region: 'Galar',
        routes: {
            land: [
                'bridge_field',
                'lake_of_outrage',
                'galar_route_2_lakeside',
                'giants_bed',
                'ballimere_lake',
            ],
        },
        evolution: [
            {
                prev: 'Galarian Linoone',
                level: 35,
                time: 'night',
            },
        ],
    },
    'Perrserker': {
        native_region: 'Galar',
        routes: {
            land: [
                'giants_mirror',
                'lake_of_outrage',
                'galar_route_7',
                'outer_spikemuth',
            ],
        },
        dungeons: [
            'iron_ruins',
        ],
        evolution: [
            {
                prev: 'Galarian Meowth',
                level: 28,
            },
        ],
    },
    'Cursola': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Galarian Corsola',
                level: 38,
            },
        ],
        special: [
            Has('Cursola') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Sirfetch\'d': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Galarian Farfetch\'d',
                level: 20,
                item: 'Leek',
            },
        ],
        special: [
            Has('Sirfetch\'d') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Mr. Rime': {
        native_region: 'Galar',
        dungeons: [
            'crown_shrine',
        ],
        evolution: [
            {
                prev: 'Galarian Mr. Mime',
                level: 42,
            },
        ],
    },
    'Runerigus': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Galarian Yamask',
                level: 34,
                dungeon_evolution: 'dusty_bowl',
            },
        ],
        special: [
            Has('Runerigus') & make_rule('region_safari', 'Kalos'),
        ],
    },
    'Milcery': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_4',
                'bridge_field',
                'giants_mirror',
            ],
        },
        egg: 'Mystery Egg',
    },
    'Milcery (Cheesy)': {
        native_region: 'Galar',
        battle_cafe: [
            (3600, 'any', 'any'),
        ],
    },
    'Alcremie (Strawberry Vanilla)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Strawberry Ruby Cream)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Strawberry Caramel)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Strawberry Ruby Swirl)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Strawberry Matcha)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Strawberry Salted)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Strawberry Lemon)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Strawberry Mint)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Strawberry Rainbow)': {
        native_region: 'Galar',
        battle_cafe: [
            (11, 'counterclockwise', 'dusk'),
        ],
    },
    'Alcremie (Berry Vanilla)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Berry Ruby Cream)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Berry Caramel)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Berry Ruby Swirl)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Berry Matcha)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Berry Salted)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Berry Lemon)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Berry Mint)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Berry Rainbow)': {
        native_region: 'Galar',
        battle_cafe: [
            (11, 'counterclockwise', 'dusk'),
        ],
    },
    'Alcremie (Love Vanilla)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Love Ruby Cream)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Love Caramel)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Love Ruby Swirl)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Love Matcha)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Love Salted)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Love Lemon)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Love Mint)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Love Rainbow)': {
        native_region: 'Galar',
        battle_cafe: [
            (11, 'counterclockwise', 'dusk'),
        ],
    },
    'Alcremie (Star Vanilla)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Star Ruby Cream)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Star Caramel)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Star Ruby Swirl)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Star Matcha)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Star Salted)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Star Lemon)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Star Mint)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Star Rainbow)': {
        native_region: 'Galar',
        battle_cafe: [
            (11, 'counterclockwise', 'dusk'),
        ],
    },
    'Alcremie (Clover Vanilla)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Clover Ruby Cream)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Clover Caramel)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Clover Ruby Swirl)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Clover Matcha)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Clover Salted)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Clover Lemon)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Clover Mint)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Clover Rainbow)': {
        native_region: 'Galar',
        battle_cafe: [
            (11, 'counterclockwise', 'dusk'),
        ],
    },
    'Alcremie (Flower Vanilla)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Flower Ruby Cream)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Flower Caramel)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Flower Ruby Swirl)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Flower Matcha)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Flower Salted)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Flower Lemon)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Flower Mint)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Flower Rainbow)': {
        native_region: 'Galar',
        battle_cafe: [
            (11, 'counterclockwise', 'dusk'),
        ],
    },
    'Alcremie (Ribbon Vanilla)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Ribbon Ruby Cream)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Ribbon Caramel)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'day'),
        ],
    },
    'Alcremie (Ribbon Ruby Swirl)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'day'),
        ],
    },
    'Alcremie (Ribbon Matcha)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Ribbon Salted)': {
        native_region: 'Galar',
        battle_cafe: [
            (1, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Ribbon Lemon)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'clockwise', 'night'),
        ],
    },
    'Alcremie (Ribbon Mint)': {
        native_region: 'Galar',
        battle_cafe: [
            (5, 'counterclockwise', 'night'),
        ],
    },
    'Alcremie (Ribbon Rainbow)': {
        native_region: 'Galar',
        battle_cafe: [
            (11, 'counterclockwise', 'dusk'),
        ],
    },
    'Gigantamax Alcremie': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Alcremie') | make_rule('lair_of_giants28')) & make_rule('max_lair'),
        ],
    },
    'Falinks': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'galar_route_8',
            ],
        },
        egg: 'Fighting Egg',
    },
    'Pincurchin': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_9',
                'circhester_bay',
                'loop_lagoon',
                'frigid_sea',
            ],
        },
        dungeons: [
            'courageous_cavern',
        ],
        egg: 'Electric Egg',
    },
    'Snom': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'steamdrift_way',
                'white_hill_station',
                'galar_route_10',
                'slippery_slope',
                'snowslide_slope',
                'path_to_the_peak',
            ],
        },
        farm_wandering: ['Yache Berry'],
        special: [
            Has('Snom') & make_rule('region_safari', 'Johto'),
        ],
    },
    'Frosmoth': {
        native_region: 'Galar',
        routes: {
            land: [
                'path_to_the_peak',
            ],
        },
        dungeons: [
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Snom',
                item: 'Soothe Bell',
                time: 'night',
            },
        ],
    },
    'Stonjourner': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'galar_route_10',
                'giants_bed',
                'giants_foot',
            ],
        },
        dungeons: [
            'rock_peak_ruins',
            'split_decision_ruins',
        ],
    },
    'Eiscue (Ice Face)': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'galar_route_10',
                'frigid_sea',
            ],
        },
    },
    'Eiscue (Noice Face)': {
        native_region: 'Galar',
        routes: {
            land: [
                'galar_route_10',
                'frigid_sea',
            ],
        },
    },
    'Indeedee (Male)': {
        native_region: 'Galar',
        routes: {
            land: [
                'ballimere_lake',
            ],
        },
        dungeon_boss: [
            ('glimwood_tangle', 118824240),
        ],
    },
    'Indeedee (Female)': {
        native_region: 'Galar',
        routes: {
            land: [
                'ballimere_lake',
            ],
        },
        dungeon_boss: [
            ('glimwood_tangle', 118824240),
        ],
    },
    'Morpeko': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'galar_route_7',
                'outer_spikemuth',
                'challenge_beach',
                'ballimere_lake',
            ],
        },
        egg: 'Electric Egg',
    },
    'Morpeko (Hangry)': {
        native_region: 'Galar',
        farm_wandering: ['Wacan Berry'],
    },
    'Cufant': {
        native_region: 'Galar',
        routes: {
            land: [
                'bridge_field',
                'giants_foot',
            ],
        },
        farm_wandering: ['Babiri Berry'],
    },
    'Copperajah': {
        native_region: 'Galar',
        routes: {
            land: [
                'lake_of_outrage',
                'hammerlocke_hills',
                'giants_foot',
            ],
        },
        dungeons: [
            'iron_ruins',
        ],
        evolution: [
            {
                prev: 'Cufant',
                level: 34,
            },
        ],
    },
    'Gigantamax Copperajah': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Copperajah') | make_rule('lair_of_giants29')) & make_rule('max_lair'),
        ],
    },
    'Dracozolt': {
        native_region: 'Galar',
        trades: [
            ('stow_on_side', ['Fossilized Bird', 'Fossilized Drake', 'questPoint']),
        ],
    },
    'Arctozolt': {
        native_region: 'Galar',
        trades: [
            ('stow_on_side', ['Fossilized Bird', 'Fossilized Dino', 'questPoint']),
        ],
    },
    'Dracovish': {
        native_region: 'Galar',
        trades: [
            ('stow_on_side', ['Fossilized Fish', 'Fossilized Drake', 'questPoint']),
        ],
    },
    'Arctovish': {
        native_region: 'Galar',
        trades: [
            ('stow_on_side', ['Fossilized Fish', 'Fossilized Dino', 'questPoint']),
        ],
    },
    'Duraludon': {
        native_region: 'Galar',
        routes: {
            land: [
                'giants_seat',
                'lake_of_outrage',
                'galar_route_10',
            ],
        },
        dungeons: [
            'iron_ruins',
        ],
        egg: 'Dragon Egg',
    },
    'Gigantamax Duraludon': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Duraludon') | make_rule('lair_of_giants30')) & make_rule('max_lair'),
        ],
    },
    'Dreepy': {
        native_region: 'Galar',
        dungeons: [
            'area_zero_depths',
        ],
        egg: 'Dragon Egg',
        special: [
            Has('Dreepy') & make_rule('lake_of_outrage'),
        ],
    },
    'Drakloak': {
        native_region: 'Galar',
        routes: {
            land: [
                'old_cemetery',
            ],
        },
        dungeons: [
            'area_zero_depths',
        ],
        evolution: [
            {
                prev: 'Dreepy',
                level: 50,
            },
        ],
        egg: 'Dragon Egg',
        special: [
            Has('Drakloak') & make_rule('lake_of_outrage'),
        ],
    },
    'Dragapult': {
        native_region: 'Galar',
        routes: {
            land: [
                'old_cemetery',
                'three_point_pass',
            ],
        },
        evolution: [
            {
                prev: 'Drakloak',
                level: 60,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Zacian (Battle Hero)': {
        native_region: 'Galar',
        special: [
            make_rule('sword_and_shield18') & make_rule('energy_plant', True, 169578810),
        ],
    },
    'Zacian (Crowned Sword)': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Zacian (Battle Hero)',
                level: 100,
                item: 'Rusted Sword',
            },
        ],
        special: [
            Has('Zacian (Crowned Sword)') & make_rule('slumbering_weald_shrine', True, 169578810),
        ],
    },
    'Zamazenta (Battle Hero)': {
        native_region: 'Galar',
        special: [
            make_rule('sword_and_shield18') & make_rule('energy_plant', True, 169578810),
        ],
    },
    'Zamazenta (Crowned Shield)': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Zamazenta (Battle Hero)',
                level: 100,
                item: 'Rusted Shield',
            },
        ],
        special: [
            Has('Zamazenta (Crowned Shield)') & make_rule('slumbering_weald_shrine', True, 169578810),
        ],
    },
    'Eternatus': {
        native_region: 'Galar',
        special: [
            make_rule('the_lair_of_giants36') & make_rule('energy_plant', True, 169578810),
            Has('Eternatus') & make_rule('energy_plant') & make_rule('the_darkest_day'),
        ],
    },
    'Eternamax Eternatus': {
        native_region: 'Galar',
        special: [
            make_rule('completed_the_lair_of_giants') & make_rule('max_lair', True, 176361964),
        ],
    },
    'Kubfu': {
        native_region: 'Galar',
        dungeons: [
            'tower_of_darkness',
            'tower_of_waters',
        ],
        temporary_battle: [
            'kubfu',
        ],
    },
    'Urshifu (Single Strike)': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Kubfu',
                level: 34,
                dungeon_evolution: 'tower_of_darkness',
            },
        ],
        special: [
            Has('Urshifu (Single Strike)') & make_rule('tower_of_darkness', True, 160924440),
        ],
    },
    'Urshifu (Rapid Strike)': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Kubfu',
                level: 34,
                dungeon_evolution: 'tower_of_waters',
            },
        ],
        special: [
            Has('Urshifu (Rapid Strike)') & make_rule('tower_of_waters', True, 160924440),
        ],
    },
    'Gigantamax Urshifu (Single Strike)': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Urshifu (Single Strike)') | make_rule('lair_of_giants31')) & make_rule('max_lair'),
        ],
    },
    'Gigantamax Urshifu (Rapid Strike)': {
        native_region: 'Galar',
        special: [
            (Has('Gigantamax Urshifu (Rapid Strike)') | make_rule('lair_of_giants32')) & make_rule('max_lair'),
        ],
    },
    'Zarude': {
        native_region: 'Galar',
        special: [
            make_rule('roamer', 'Galar - Isle of Armor') & make_rule('secrets_of_the_jungle1'),
        ],
    },
    'Zarude (Dada)': {
        native_region: 'Galar',
        shops: [
            ('glimwood_tangle', 'questPoint'),
        ],
    },
    'Regieleki': {
        native_region: 'Galar',
        dungeon_boss: [
            ('split_decision_ruins', 164353300),
        ],
    },
    'Regidrago': {
        native_region: 'Galar',
        dungeon_boss: [
            ('split_decision_ruins', 164353300),
        ],
    },
    'Glastrier': {
        native_region: 'Galar',
        special: [
            make_rule('roamer', 'Galar - Crown Tundra') & make_rule('the_crown_of_galar6'),
        ],
    },
    'Spectrier': {
        native_region: 'Galar',
        special: [
            make_rule('roamer', 'Galar - Crown Tundra') & make_rule('the_crown_of_galar6'),
        ],
    },
    'Calyrex': {
        native_region: 'Galar',
        special: [
            make_rule('the_crown_of_galar8') & make_rule('crown_shrine', True, 169578810),
        ],
    },
    'Ice Rider Calyrex': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Calyrex',
                item: 'White Mane Hair',
            },
        ],
    },
    'Shadow Rider Calyrex': {
        native_region: 'Galar',
        evolution: [
            {
                prev: 'Calyrex',
                item: 'Black Mane Hair',
            },
        ],
    },
    'Wyrdeer': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Stantler',
                level: 31,
                item: 'Agile Scroll',
            },
        ],
    },
    'Kleavor': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Scyther',
                item: 'Black Augurite',
            },
        ],
    },
    'Ursaluna': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Ursaring',
                item: 'Peat Block',
                time: 'night',
            },
        ],
    },
    'Basculegion (Male)': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Basculin (White-Striped)',
                level: 45,
            },
        ],
    },
    'Basculegion (Female)': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Basculin (White-Striped)',
                level: 45,
            },
        ],
    },
    'Sneasler': {
        native_region: 'Hisui',
        evolution: [
            {
                prev: 'Hisuian Sneasel',
                item: 'Razor Claw',
                time: 'day',
            },
        ],
    },
    'Overqwil': {
        native_region: 'Hisui',
        dungeon_boss: [
            ('ancient_lake_valor', 10000000),
        ],
        evolution: [
            {
                prev: 'Hisuian Qwilfish',
                level: 25,
                item: 'Strong Scroll',
            },
        ],
    },
    'Enamorus': {
        native_region: 'Hisui',
        special: [
            make_rule('roamer', 'Hisui') & make_rule('incarnate_forces_of_hisui3'),
        ],
    },
    'Enamorus (Therian)': {
        native_region: 'Hisui',
        dream_orbs: ['Blue'],
    },
    'Sprigatito': {
        native_region: 'Paldea',
        egg: 'Grass Egg',
        starter: ['Paldea'],
        farm_wandering: ['Rindo Berry'],
    },
    'Floragato': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Sprigatito',
                level: 16,
            },
        ],
    },
    'Meowscarada': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Floragato',
                level: 36,
            },
        ],
    },
    'Fuecoco': {
        native_region: 'Paldea',
        egg: 'Fire Egg',
        starter: ['Paldea'],
        farm_wandering: ['Occa Berry'],
    },
    'Crocalor': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Fuecoco',
                level: 16,
            },
        ],
    },
    'Skeledirge': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Crocalor',
                level: 36,
            },
        ],
    },
    'Quaxly': {
        native_region: 'Paldea',
        egg: 'Water Egg',
        starter: ['Paldea'],
        farm_wandering: ['Passho Berry'],
    },
    'Quaxwell': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Quaxly',
                level: 16,
            },
        ],
    },
    'Quaquaval': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Quaxwell',
                level: 36,
            },
        ],
    },
    'Lechonk': {
        native_region: 'Paldea',
        routes: {
            land: [
                'poco_path',
                'south_province_area_one',
            ],
        },
    },
    'Oinkologne (Male)': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Lechonk',
                level: 18,
            },
        ],
    },
    'Oinkologne (Female)': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Lechonk',
                level: 18,
            },
        ],
    },
    'Tarountula': {
        native_region: 'Paldea',
        routes: {
            land: [
                'poco_path',
                'south_province_area_one',
            ],
        },
    },
    'Spidops': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Tarountula',
                level: 15,
            },
        ],
    },
    'Nymble': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_three',
            ],
        },
    },
    'Lokix': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Nymble',
                level: 24,
            },
        ],
    },
    'Pawmi': {
        native_region: 'Paldea',
        routes: {
            land: [
                'poco_path',
                'south_province_area_one',
                'south_province_area_three',
            ],
        },
        farm_wandering: ['Wacan Berry'],
    },
    'Pawmo': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Pawmi',
                level: 18,
            },
        ],
    },
    'Tandemaus': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_three',
            ],
        },
    },
    'Maushold (Family of Four)': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Tandemaus',
                level: 25,
            },
        ],
    },
    'Fidough': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
    },
    'Dachsbun': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Fidough',
                level: 26,
            },
        ],
    },
    'Smoliv': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
            ],
        },
    },
    'Dolliv': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Smoliv',
                level: 25,
            },
        ],
    },
    'Arboliva': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Dolliv',
                level: 35,
            },
        ],
    },
    'Squawkabilly (Green)': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
    },
    'Squawkabilly (Blue)': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
    },
    'Squawkabilly (Yellow)': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
    },
    'Squawkabilly (White)': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
    },
    'Nacli': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
    },
    'Naclstack': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Nacli',
                level: 24,
            },
        ],
    },
    'Garganacl': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
        evolution: [
            {
                prev: 'Naclstack',
                level: 38,
            },
        ],
    },
    'Charcadet': {
        native_region: 'Paldea',
        egg: 'Fire Egg',
    },
    'Armarouge': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Charcadet',
                item: 'Auspicious Armor',
            },
        ],
    },
    'Ceruledge': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Charcadet',
                item: 'Malicious Armor',
            },
        ],
    },
    'Tadbulb': {
        native_region: 'Paldea',
        routes: {
            water: [
                'south_province_area_two',
            ],
        },
        dungeons: [
            'area_zero',
        ],
    },
    'Bellibolt': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Tadbulb',
                item: 'Thunder Stone',
            },
        ],
    },
    'Kilowattrel': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Wattrel',
                level: 25,
            },
        ],
    },
    'Maschiff': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
            ],
        },
    },
    'Mabosstiff': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Maschiff',
                level: 30,
            },
        ],
    },
    'Shroodle': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_one',
                'south_province_area_two',
            ],
        },
    },
    'Grafaiai': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Shroodle',
                level: 28,
            },
        ],
    },
    'Toedscruel': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Toedscool',
                level: 30,
            },
        ],
    },
    'Klawf': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_three',
            ],
        },
    },
    'Scovillain': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Capsakid',
                item: 'Fire Stone',
            },
        ],
    },
    'Espathra': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero_depths',
        ],
        evolution: [
            {
                prev: 'Flittle',
                level: 35,
            },
        ],
    },
    'Tinkatink': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
    },
    'Tinkatuff': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Tinkatink',
                level: 38,
            },
        ],
    },
    'Tinkaton': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Tinkatuff',
                level: 38,
            },
        ],
    },
    'Wiglett': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_one',
            ],
        },
    },
    'Wugtrio': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Wiglett',
                level: 26,
            },
        ],
    },
    'Palafin (Zero)': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Finizen',
                level: 38,
            },
        ],
    },
    'Revavroom': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Varoom',
                level: 40,
            },
        ],
    },
    'Glimmet': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero_depths',
        ],
    },
    'Glimmora': {
        native_region: 'Paldea',
        dungeon_boss: [
            ('area_zero', 161099869),
            ('area_zero_depths', 161099869),
        ],
        evolution: [
            {
                prev: 'Glimmet',
                level: 35,
            },
        ],
    },
    'Greavard': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero_depths',
        ],
    },
    'Houndstone': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero_depths',
        ],
        evolution: [
            {
                prev: 'Greavard',
                level: 30,
            },
        ],
    },
    'Flamigo': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_one',
            ],
        },
        dungeons: [
            'area_zero',
        ],
    },
    'Cetitan': {
        native_region: 'Paldea',
        dungeon_boss: [
            ('glaseado_mountain', 161099869),
        ],
        evolution: [
            {
                prev: 'Cetoddle',
                item: 'Ice Stone',
            },
        ],
    },
    'Annihilape': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Primeape',
                level: 35,
            },
        ],
    },
    'Clodsire': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Paldean Wooper',
                level: 20,
            },
        ],
    },
    'Farigiraf': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
        ],
        evolution: [
            {
                prev: 'Girafarig',
                level: 32,
            },
        ],
    },
    'Dudunsparce (Two-Segment)': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero_depths',
        ],
        evolution: [
            {
                prev: 'Dunsparce',
                level: 32,
            },
        ],
    },
    'Kingambit': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Bisharp',
                item: 'Leaders Crest',
            },
        ],
    },
    'Great Tusk': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero_depths',
        ],
    },
    'Scream Tail': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Brute Bonnet': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Flutter Mane': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Slither Wing': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Sandy Shocks': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Iron Treads': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero_depths',
        ],
    },
    'Iron Bundle': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Iron Hands': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Iron Jugulis': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Iron Moth': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Iron Thorns': {
        native_region: 'Paldea',
        dungeons: [
            'area_zero',
            'area_zero_depths',
        ],
    },
    'Frigibax': {
        native_region: 'Paldea',
        egg: 'Dragon Egg',
    },
    'Arctibax': {
        native_region: 'Paldea',
        dungeon_boss: [
            ('glaseado_mountain', 161099869),
        ],
        evolution: [
            {
                prev: 'Frigibax',
                level: 35,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Baxcalibur': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Arctibax',
                level: 54,
            },
        ],
        egg: 'Dragon Egg',
    },
    'Gimmighoul (Chest)': {
        native_region: 'Paldea',
        routes: {
            land: [
                'south_province_area_one',
                'south_province_area_two',
                'south_province_area_three',
            ],
        },
    },
    'Gimmighoul (Roaming)': {
        native_region: 'Paldea',
        roamer: [
            'Paldea',
        ],
    },
    'Gholdengo': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Gimmighoul (Chest)',
                item: 'Gimmighoul Coin',
            },
        ],
    },
    'Wo-Chien': {
        native_region: 'Paldea',
        dungeon_boss: [
            ('grasswither_shrine', 161099869),
        ],
    },
    'Chien-Pao': {
        native_region: 'Paldea',
        dungeon_boss: [
            ('icerend_shrine', 161099869),
        ],
    },
    'Ting-Lu': {
        native_region: 'Paldea',
        dungeon_boss: [
            ('groundblight_shrine', 161099869),
        ],
    },
    'Chi-Yu': {
        native_region: 'Paldea',
        dungeon_boss: [
            ('firescourge_shrine', 161099869),
        ],
    },
    'Roaring Moon': {
        native_region: 'Paldea',
        special: [
            make_rule('paradise_protection_protocol') & make_rule('area_zero', True, 161099869),
        ],
    },
    'Iron Valiant': {
        native_region: 'Paldea',
        special: [
            make_rule('paradise_protection_protocol') & make_rule('area_zero', True, 161099869),
        ],
    },
    'Koraidon': {
        native_region: 'Paldea',
        special: [
            make_rule('paradise_protection_protocol') & make_rule('area_zero_depths', True, 161099869),
        ],
    },
    'Miraidon': {
        native_region: 'Paldea',
        special: [
            make_rule('paradise_protection_protocol') & make_rule('area_zero_depths', True, 161099869),
        ],
    },
    'Dipplin': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Applin',
                item: 'Syrupy Apple',
            },
        ],
    },
    'Sinistcha': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Poltchageist',
                item: 'Unremarkable Teacup',
            },
        ],
    },
    'Ogerpon (Wellspring Mask)': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Ogerpon (Teal Mask)',
                level: 70,
                item: 'Wellspring Mask',
            },
        ],
    },
    'Ogerpon (Hearthflame Mask)': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Ogerpon (Teal Mask)',
                level: 70,
                item: 'Hearthflame Mask',
            },
        ],
    },
    'Ogerpon (Cornerstone Mask)': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Ogerpon (Teal Mask)',
                level: 70,
                item: 'Cornerstone Mask',
            },
        ],
    },
    'Archaludon': {
        native_region: 'Paldea',
        evolution: [
            {
                prev: 'Duraludon',
                item: 'Metal Alloy',
            },
        ],
    },
}
