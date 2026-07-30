from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from . import Helpers

if TYPE_CHECKING:
    from .world import PokeclickerWorld

class ItemData:
    def __init__(self, item_id, classification, groups, count=1):
        self.groups = groups
        self.classification = classification
        self.id = item_id
        self.count = count


item_table = {
    "Town Map": ItemData(1, ItemClassification.progression, ['Key Items']),
    "Dungeon Ticket": ItemData(2, ItemClassification.progression, ['Key Items']),
    "Mystery Egg": ItemData(3, ItemClassification.progression, ['Key Items']),
    "Wailmer Pail": ItemData(4, ItemClassification.progression, ['Key Items']),
    "Super Rod": ItemData(5, ItemClassification.progression, ['Key Items']),
    "Safari Ticket": ItemData(6, ItemClassification.progression, ['Key Items']),
    "Explorer Kit": ItemData(7, ItemClassification.progression, ['Key Items']),
    "Gem Case": ItemData(8, ItemClassification.useful, ['Key Items']),
    "Holo Caster": ItemData(9, ItemClassification.useful, ['Key Items']),

    "Magic Ball": ItemData(101, ItemClassification.useful, ['Oak Items']),
    "Amulet Coin": ItemData(102, ItemClassification.useful, ['Oak Items']),
    "Rocky Helmet": ItemData(103, ItemClassification.useful, ['Oak Items']),
    "EXP Share": ItemData(104, ItemClassification.useful, ['Oak Items']),
    "Sprayduck": ItemData(105, ItemClassification.useful, ['Oak Items']),
    "Shiny Charm": ItemData(106, ItemClassification.useful, ['Oak Items']),
    "Magma Stone": ItemData(107, ItemClassification.useful, ['Oak Items']),
    "Cell Battery": ItemData(108, ItemClassification.useful, ['Oak Items']),
    "Explosive Charge": ItemData(109, ItemClassification.useful, ['Oak Items']),
    "Treasure Scanner": ItemData(110, ItemClassification.useful, ['Oak Items']),

    "Auto Battle Items": ItemData(201, ItemClassification.useful, ['Scripts']),
    "Catch Filter Fantasia": ItemData(202, ItemClassification.useful, ['Scripts']),
    "Enhanced Auto Clicker": ItemData(203, ItemClassification.useful, ['Scripts', 'Not Progressive Auto Clicker']),
    "Enhanced Auto Clicker (Progressive Clicks/Second)": ItemData(204, ItemClassification.useful, ['Scripts', 'Progressive Auto Clicker'], 5),
    "Enhanced Auto Hatchery": ItemData(205, ItemClassification.useful, ['Scripts']),
    "Enhanced Auto Mine": ItemData(206, ItemClassification.progression, ['Scripts']),
    "Simple Auto Farmer": ItemData(207, ItemClassification.useful, ['Scripts']),
    "Auto Quest Completer": ItemData(208, ItemClassification.useful, ['Scripts']),
    "Auto Safari Zone": ItemData(209, ItemClassification.progression, ['Scripts', 'Not Progressive Safari Zone']),
    "Auto Safari Zone (Progressive Fast Animations)": ItemData(210, ItemClassification.progression, ['Scripts', 'Progressive Safari Zone'], 5),
    "Catch Speed Adjuster": ItemData(211, ItemClassification.useful, ['Scripts']),
    "Infinite Seasonal Events": ItemData(212, ItemClassification.progression, ['Scripts', 'Seasonal Events']),
    "Oak Items Unlimited": ItemData(213, ItemClassification.useful, ['Scripts']),
    "Simple Weather Changer": ItemData(214, ItemClassification.useful, ['Scripts']),

    "Boulder Badge": ItemData(301, ItemClassification.progression, ['Badges']),
    "Cascade Badge": ItemData(302, ItemClassification.progression, ['Badges']),
    "Thunder Badge": ItemData(303, ItemClassification.progression, ['Badges']),
    "Rainbow Badge": ItemData(304, ItemClassification.progression, ['Badges']),
    "Marsh Badge": ItemData(305, ItemClassification.progression, ['Badges']),
    "Soul Badge": ItemData(306, ItemClassification.progression, ['Badges']),
    "Volcano Badge": ItemData(307, ItemClassification.progression, ['Badges']),
    "Earth Badge": ItemData(308, ItemClassification.progression, ['Badges']),
    "Kanto Elite Lorelei Badge": ItemData(309, ItemClassification.progression, ['Badges', 'Kanto Elite Badges']),
    "Kanto Elite Bruno Badge": ItemData(310, ItemClassification.progression, ['Badges', 'Kanto Elite Badges']),
    "Kanto Elite Agatha Badge": ItemData(311, ItemClassification.progression, ['Badges', 'Kanto Elite Badges']),
    "Kanto Elite Lance Badge": ItemData(312, ItemClassification.progression, ['Badges', 'Kanto Elite Badges']),
    "Kanto Elite Champion Badge": ItemData(313, ItemClassification.progression, ['Badges', 'Kanto Elite Badges']),

    "Progressive Pokeball": ItemData(501, ItemClassification.progression, ['Shop', 'Not Implemented'], 3),
    "Extra Egg Slot": ItemData(502, ItemClassification.useful, ['Extra Slots'], 4),
    "Primary Egg Slot": ItemData(503, ItemClassification.useful, ['Extra Slots', 'Not Implemented']),
    "Palaeontologist Token": ItemData(504, ItemClassification.progression, ['Palaeontologist']),

    "Tutorial Complete": ItemData(1001, ItemClassification.progression, ['Event']),

    "Bulbasaur": ItemData(2001, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Ivysaur": ItemData(2002, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Venusaur": ItemData(2003, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Charmander": ItemData(2004, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Charmeleon": ItemData(2005, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Charizard": ItemData(2006, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Squirtle": ItemData(2007, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Wartortle": ItemData(2008, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Blastoise": ItemData(2009, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Caterpie": ItemData(2010, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Metapod": ItemData(2011, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Butterfree": ItemData(2012, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Weedle": ItemData(2013, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Kakuna": ItemData(2014, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Beedrill": ItemData(2015, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Pidgey": ItemData(2016, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Pidgeotto": ItemData(2017, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Pidgeot": ItemData(2018, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Rattata": ItemData(2019, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Raticate": ItemData(2020, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Spearow": ItemData(2021, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Fearow": ItemData(2022, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Ekans": ItemData(2023, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Arbok": ItemData(2024, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Pikachu": ItemData(2025, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Raichu": ItemData(2026, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Sandshrew": ItemData(2027, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Sandslash": ItemData(2028, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Nidoran (F)": ItemData(2029, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Nidorina": ItemData(2030, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Nidoqueen": ItemData(2031, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Nidoran (M)": ItemData(2032, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Nidorino": ItemData(2033, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Nidoking": ItemData(2034, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Clefairy": ItemData(2035, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Clefable": ItemData(2036, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Vulpix": ItemData(2037, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Ninetails": ItemData(2038, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Jigglypuff": ItemData(2039, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Wigglytuff": ItemData(2040, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Zubat": ItemData(2041, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Golbat": ItemData(2042, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Oddish": ItemData(2043, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Gloom": ItemData(2044, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Vileplume": ItemData(2045, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Paras": ItemData(2046, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Parasect": ItemData(2047, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Venonat": ItemData(2048, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Venomoth": ItemData(2049, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Diglett": ItemData(2050, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Dugtrio": ItemData(2051, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Meowth": ItemData(2052, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Persian": ItemData(2053, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Psyduck": ItemData(2054, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Golduck": ItemData(2055, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Mankey": ItemData(2056, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Primape": ItemData(2057, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Growlithe": ItemData(2058, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Arcanine": ItemData(2059, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Poliwag": ItemData(2060, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Poliwhirl": ItemData(2061, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Poliwrath": ItemData(2062, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Abra": ItemData(2063, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Kadabra": ItemData(2064, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Alakazam": ItemData(2065, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Machop": ItemData(2066, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Machoke": ItemData(2067, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Machamp": ItemData(2068, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Bellsprout": ItemData(2069, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Weepinbell": ItemData(2070, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Victreebel": ItemData(2071, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Tentacool": ItemData(2072, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Tentacruel": ItemData(2073, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Geodude": ItemData(2074, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Graveler": ItemData(2075, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Golem": ItemData(2076, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Ponyta": ItemData(2077, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Rapidash": ItemData(2078, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Slowpoke": ItemData(2079, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Slowbro": ItemData(2080, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Magnemite": ItemData(2081, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Magneton": ItemData(2082, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Farfetch'd": ItemData(2083, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Doduo": ItemData(2084, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Dodrio": ItemData(2085, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Seel": ItemData(2086, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Dewgong": ItemData(2087, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Grimer": ItemData(2088, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Muk": ItemData(2089, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Shellder": ItemData(2090, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Cloyster": ItemData(2091, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Gastly": ItemData(2092, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Haunter": ItemData(2093, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Gengar": ItemData(2094, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Onix": ItemData(2095, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Drowzee": ItemData(2096, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Hypno": ItemData(2097, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Krabby": ItemData(2098, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Kingler": ItemData(2099, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Voltorb": ItemData(2100, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Electrode": ItemData(2101, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Exeggcute": ItemData(2102, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Exeggutor": ItemData(2103, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Cubone": ItemData(2104, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Marowak": ItemData(2105, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Hitmonlee": ItemData(2106, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Hitmonchan": ItemData(2107, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Lickitung": ItemData(2108, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Koffing": ItemData(2109, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Weezing": ItemData(2110, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Rhyhorn": ItemData(2111, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Rhydon": ItemData(2112, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Chansey": ItemData(2113, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Tangela": ItemData(2114, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Kangaskhan": ItemData(2115, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Horsea": ItemData(2116, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Seadra": ItemData(2117, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Goldeen": ItemData(2118, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Seaking": ItemData(2119, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Staryu": ItemData(2120, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Starmie": ItemData(2121, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Mr. Mime": ItemData(2122, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Scyther": ItemData(2123, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Jynx": ItemData(2124, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Electabuzz": ItemData(2125, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Magmar": ItemData(2126, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Pinsir": ItemData(2127, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Tauros": ItemData(2128, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Magikarp": ItemData(2129, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Gyarados": ItemData(2130, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Lapras": ItemData(2131, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Ditto": ItemData(2132, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Eevee": ItemData(2133, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Vaporeon": ItemData(2134, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Jolteon": ItemData(2135, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Flareon": ItemData(2136, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Porygon": ItemData(2137, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Omanyte": ItemData(2138, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Omastar": ItemData(2139, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Kabuto": ItemData(2140, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Kabutops": ItemData(2141, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Aerodactyl": ItemData(2142, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Snorlax": ItemData(2143, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Articuno": ItemData(2144, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Zapdos": ItemData(2145, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Moltres": ItemData(2146, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Dratini": ItemData(2147, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Dragonair": ItemData(2148, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Dragonite": ItemData(2149, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Mewtwo": ItemData(2150, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon']),
    "Mew": ItemData(2151, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Kanto Pokemon', 'Roaming Pokemon']),

    "Chikorita": ItemData(2152, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Bayleef": ItemData(2153, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Meganium": ItemData(2154, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Cyndaquil": ItemData(2155, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Quilava": ItemData(2156, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Typhlosion": ItemData(2157, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Totodile": ItemData(2158, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Croconaw": ItemData(2159, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Feraligatr": ItemData(2160, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Sentret": ItemData(2161, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Furret": ItemData(2162, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Hoothoot": ItemData(2163, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Noctowl": ItemData(2164, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Ledyba": ItemData(2165, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Ledian": ItemData(2166, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Spinarak": ItemData(2167, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Ariados": ItemData(2168, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Crobat": ItemData(2169, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Chinchou": ItemData(2170, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Lanturn": ItemData(2171, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Pichu": ItemData(2172, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Cleffa": ItemData(2173, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Igglybuff": ItemData(2174, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Togepi": ItemData(2175, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Togetic": ItemData(2176, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Natu": ItemData(2177, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Xatu": ItemData(2178, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Mareep": ItemData(2179, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Flaaffy": ItemData(2180, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Ampharos": ItemData(2181, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Bellossom": ItemData(2182, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Marill": ItemData(2183, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Azumarill": ItemData(2184, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Sudowoodo": ItemData(2185, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Politoed": ItemData(2186, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Hoppip": ItemData(2187, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Skiploom": ItemData(2188, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Jumpluff": ItemData(2189, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Aipom": ItemData(2190, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Sunkern": ItemData(2191, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Sunflora": ItemData(2192, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Yanma": ItemData(2193, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Wooper": ItemData(2194, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Quagsire": ItemData(2195, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Espeon": ItemData(2196, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Umbreon": ItemData(2197, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Murkrow": ItemData(2198, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Slowking": ItemData(2199, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Misdreavus": ItemData(2200, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Unown (A)": ItemData(2201, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Wobbuffet": ItemData(2202, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Girafarig": ItemData(2203, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Pineco": ItemData(2204, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Forretress": ItemData(2205, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Dunsparce": ItemData(2206, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Gligar": ItemData(2207, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Steelix": ItemData(2208, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Snubbull": ItemData(2209, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Granbull": ItemData(2210, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Qwilfish": ItemData(2211, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Scizor": ItemData(2212, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Shuckle": ItemData(2213, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Heracross": ItemData(2214, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Sneasel": ItemData(2215, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Teddiursa": ItemData(2216, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Ursaring": ItemData(2217, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Slugma": ItemData(2218, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Magcargo": ItemData(2219, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Swinub": ItemData(2220, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Piloswine": ItemData(2221, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Corsola": ItemData(2222, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Remoraid": ItemData(2223, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Octillery": ItemData(2224, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Delibird": ItemData(2225, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Mantine": ItemData(2226, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Skarmory": ItemData(2227, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Houndour": ItemData(2228, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Houndoom": ItemData(2229, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Kingdra": ItemData(2230, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Phanpy": ItemData(2231, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Donphan": ItemData(2232, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Porygon2": ItemData(2233, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Stantler": ItemData(2234, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Smeargle": ItemData(2235, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Tyrogue": ItemData(2236, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Hitmontop": ItemData(2237, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Smoochum": ItemData(2238, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Elekid": ItemData(2239, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Magby": ItemData(2240, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Miltank": ItemData(2241, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Blissey": ItemData(2242, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Raikou": ItemData(2243, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon', 'Roaming Pokemon']),
    "Entei": ItemData(2244, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon', 'Roaming Pokemon']),
    "Suicune": ItemData(2245, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Larvitar": ItemData(2246, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Pupitar": ItemData(2247, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Tyranitar": ItemData(2248, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Lugia": ItemData(2249, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Ho-Oh": ItemData(2250, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),
    "Celebi": ItemData(2251, ItemClassification.progression, ['Pokemon', 'Base Pokemon', 'Johto Pokemon']),

    "Bulbasaur (Clone)": ItemData(5101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Spooky Bulbasaur": ItemData(5102, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Halloween']),
    "Bulbasaur (Rose)": ItemData(5103, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Sinnoh Pokemon', 'Seasonal Events', 'Golden Week', 'Not Implemented']),
    "Ivysaur (Clone)": ItemData(5201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Spooky Ivysaur": ItemData(5202, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Halloween']),
    "Ivysaur (Rose)": ItemData(5203, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Sinnoh Pokemon', 'Seasonal Events', 'Golden Week', 'Not Implemented']),
    "Mega Venusaur": ItemData(5301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Gigantamax Venusaur": ItemData(5302, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Venusaur (Clone)": ItemData(5303, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Spooky Venusaur": ItemData(5304, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Halloween']),
    "Venusaur (Rose)": ItemData(5305, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Sinnoh Pokemon', 'Seasonal Events', 'Golden Week', 'Not Implemented']),
    "Charmander (Clone)": ItemData(5401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Charmeleon (Clone)": ItemData(5501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Mega Charizard X": ItemData(5601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Mega Charizard Y": ItemData(5602, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Gigantamax Charizard": ItemData(5603, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Charizard (Clone)": ItemData(5604, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Squirtle (Clone)": ItemData(5701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Squad Leader Squirtle": ItemData(5702, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Wartortle (Clone)": ItemData(5801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Mega Blastoise": ItemData(5901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Gigantamax Blastoise": ItemData(5902, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Blastoise (Clone)": ItemData(5903, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Pinkan Caterpie": ItemData(6001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Gigantamax Butterfree": ItemData(6201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Valencian Butterfree": ItemData(6202, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pink Butterfree": ItemData(6203, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Roaming Pokemon', 'Not Implemented']),
    "Ash's Butterfree": ItemData(6204, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Roaming Pokemon', 'Not Implemented']),
    "Pinkan Weedle": ItemData(6301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Mega Beedrill": ItemData(6501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Pinkan Pidgey": ItemData(6601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Pidgeotto": ItemData(6701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Mega Pidgeot": ItemData(6801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Alolan Rattata": ItemData(6901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pinkan Rattata": ItemData(6902, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Alolan Raticate": ItemData(7001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Totem Raticate": ItemData(7002, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Valencian Raticate": ItemData(7003, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Red Spearow": ItemData(7101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', 'Flying Pikachu Event']),
    "Pinkan Arbok": ItemData(7401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pikachu (Original Cap)": ItemData(7501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pikachu (Hoenn Cap)": ItemData(7502, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pikachu (Sinnoh Cap)": ItemData(7503, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pikachu (Unova Cap)": ItemData(7504, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pikachu (Kalos Cap)": ItemData(7505, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pikachu (Alola Cap)": ItemData(7506, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pikachu (World Cap)": ItemData(7507, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Pikachu (Partner Cap)": ItemData(7508, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Gigantamax Pikachu": ItemData(7509, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Flying Pikachu": ItemData(7510, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', 'Flying Pikachu Event']),
    "Surfing Pikachu": ItemData(7511, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Redeemable Code', 'Codes']),
    "Pikachu (Gengar)": ItemData(7512, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Let's Go Pikachu": ItemData(7513, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', "Let's Go"]),
    "Pinkan Pikachu": ItemData(7514, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Not Implemented']),
    "Detective Pikachu": ItemData(7515, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Wanderer', 'Not Implemented']),
    "Pikachu (Clone)": ItemData(7516, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Pikachu (Rock Star)": ItemData(7517, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Pikachu (Belle)": ItemData(7518, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Pikachu (Pop Star)": ItemData(7519, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Pikachu (Ph. D.)": ItemData(7520, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Pikachu (Libre)": ItemData(7521, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Pikachu (Easter)": ItemData(7522, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Not Implemented']),
    "Pikachu (Palaeontologist)": ItemData(7523, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon']),
    "Alolan Raichu": ItemData(7601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Detective Raichu": ItemData(7602, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Wanderer', 'Not Implemented']),
    "Alolan Sandshrew": ItemData(7701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Alolan Sandslash": ItemData(7801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pinkan Nidoran(F)": ItemData(7901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Nidoran(M)": ItemData(8201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Nidoking": ItemData(8401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Alolan Vulpix": ItemData(8701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Alolan Ninetales": ItemData(8801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pinkan Oddish": ItemData(9301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Valencian Vileplume": ItemData(9501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Vileplume": ItemData(9502, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Valencian Paras": ItemData(9601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Paras": ItemData(9602, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Venonat": ItemData(9801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Alolan Diglett": ItemData(10001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pinkan Diglett": ItemData(10002, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Alolan Dugtrio": ItemData(10101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Dugtrio (Punk)": ItemData(10102, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Gigantamax Meowth": ItemData(10201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Alolan Meowth": ItemData(10202, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Galarian Meowth": ItemData(10203, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Meowth (Phanpy)": ItemData(10204, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Not Implemented']),
    "Alolan Persian": ItemData(10301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Psyduck (Dark Mage)": ItemData(10401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Not Implemented']),
    "Pinkan Mankey": ItemData(10601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Primeape": ItemData(10701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Hisuian Growlithe": ItemData(10801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Hisuian Arcanine": ItemData(10901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Noble Arcanine": ItemData(10902, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Pinkan Poliwhirl": ItemData(11101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Mega Alakazam": ItemData(11501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Gigantamax Machamp": ItemData(11801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Pinkan Bellsprout": ItemData(11901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Valencian Weepinbell": ItemData(12001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Weepinbell (Fancy)": ItemData(12002, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Alolan Geodude": ItemData(12401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pinkan Geodude": ItemData(12402, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Alolan Graveler": ItemData(12501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Alolan Golem": ItemData(12601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Galarian Ponyta": ItemData(12701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Galarian Rapidash": ItemData(12801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Galarian Slowpoke": ItemData(12901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Mega Slowbro": ItemData(13001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Galarian Slowbro": ItemData(13002, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Galarian Farfetch'd": ItemData(13301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Pinkan Dodrio": ItemData(13501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Alolan Grimer": ItemData(13801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Alolan Muk": ItemData(13901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Mega Gengar": ItemData(14401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Gigantamax Gengar": ItemData(14402, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Gengar (Punk)": ItemData(14403, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Crystal Onix": ItemData(14501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Onix (Rocker)": ItemData(14502, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Gigantamax Kingler": ItemData(14901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Hisuian Voltorb": ItemData(15001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Hisuian Electrode": ItemData(15101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Noble Electrode": ItemData(15102, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Exeggcute (Single)": ItemData(15201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon']),
    "Alolan Exeggutor": ItemData(15301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Pinkan Exeggutor": ItemData(15302, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Alolan Marowak": ItemData(15501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Totem Marowak": ItemData(15502, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Galarian Weezing": ItemData(16001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Pinkan Weezing": ItemData(16002, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Rhyhorn": ItemData(16101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Pinkan Rhydon": ItemData(16201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Charity Chansey": ItemData(16301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon']),
    "Tangela (Pom-pom)": ItemData(16401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Mega Kangaskhan": ItemData(16501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Baby Kangaskhan": ItemData(16502, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon']),
    "Goldeen (Diva)": ItemData(16801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Unobtainable', 'Not Implemented']),
    "Galarian Mr. Mime": ItemData(17201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Pinkan Scyther": ItemData(17301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Santa Jynx": ItemData(17401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Merry Christmas']),
    "Pinkan Electabuzz": ItemData(17501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Mega Pinsir": ItemData(17701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Paldean Tauros (Combat)": ItemData(17801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Paldea Pokemon', 'Not Implemented']),
    "Paldean Tauros (Blaze)": ItemData(17802, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Paldea Pokemon', 'Not Implemented']),
    "Paldean Tauros (Aqua)": ItemData(17803, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Paldea Pokemon', 'Not Implemented']),
    "Magikarp Skelly": ItemData(17901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Calico (Orange, White)": ItemData(17902, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Calico (Orange, White, Black)": ItemData(17903, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Calico (White, Orange)": ItemData(17904, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Calico (Orange, Gold)": ItemData(17905, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Orange Two-Tone": ItemData(17906, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Orange Orca": ItemData(17907, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Orange Dapples": ItemData(17908, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Pink Two-Tone": ItemData(17909, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Pink Orca": ItemData(17910, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Pink Dapples": ItemData(17911, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Grey Bubbles": ItemData(17912, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Grey Diamonds": ItemData(17913, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Grey Patches": ItemData(17914, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Purple Bubbles": ItemData(17915, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Purple Diamonds": ItemData(17916, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Roaming Pokemon', 'Not Implemented']),
    "Magikarp Purple Patches": ItemData(17917, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Apricot Tiger": ItemData(17918, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Apricot Zebra": ItemData(17919, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Apricot Stripes": ItemData(17920, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Brown Tiger": ItemData(17921, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Brown Zebra": ItemData(17922, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Brown Stripes": ItemData(17923, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Orange Forehead": ItemData(17924, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Orange Mask": ItemData(17925, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Black Forehead": ItemData(17926, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Black Mask": ItemData(17927, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Blue Raindrops": ItemData(17928, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Saucy Blue": ItemData(17929, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Magikarp Violet Raindrops": ItemData(17930, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Roaming Pokemon', 'Not Implemented']),
    "Magikarp Saucy Violet": ItemData(17931, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Not Implemented']),
    "Magikarp (Feebas)": ItemData(17932, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Mega Gyarados": ItemData(18001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Gigantamax Lapras": ItemData(18101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Ditto (Magikarp)": ItemData(18201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Alola Pokemon', 'Not Implemented']),
    "Gigantamax Eevee": ItemData(18301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Let's Go Eevee": ItemData(18302, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', "Let's Go"]),
    "Mega Aerodactyl": ItemData(19201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Gigantamax Snorlax": ItemData(19301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Santa Snorlax": ItemData(19302, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Roaming Pokemon', 'Seasonal Events', 'Merry Christmas']),
    "Snorlax (Snowman)": ItemData(19303, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Merry Christmas']),
    "Galarian Articuno": ItemData(19401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Galarian Zapdos": ItemData(19501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Galarian Moltres": ItemData(19601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Mega Mewtwo X": ItemData(20001, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Mega Mewtwo Y": ItemData(20002, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Armored Mewtwo": ItemData(20003, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kanto Pokemon', 'Seasonal Events', 'Mewtwo Strikes Back']),
    
    "Hisuian Typhlosion": ItemData(20701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Spiky-eared Pichu": ItemData(22201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Spooky Togepi": ItemData(22501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Seasonal Events', 'Halloween']),
    "Togepi (Flowering Crown)": ItemData(22502, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Seasonal Events', 'Easter']),
    "Spooky Togetic": ItemData(22601, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Seasonal Events', 'Halloween']),
    "Mega Ampharos": ItemData(23101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Sudowoodo (Golden)": ItemData(23501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Hoppip (Chimecho)": ItemData(23701, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Paldean Wooper": ItemData(24401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Paldea Pokemon', 'Not Implemented']),
    "Galarian Slowking": ItemData(24901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Unown (B)": ItemData(25101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (C)": ItemData(25102, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Redeemable Code']),
    "Unown (D)": ItemData(25103, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Redeemable Code']),
    "Unown (E)": ItemData(25104, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Sinnoh Pokemon', 'Not Implemented']),
    "Unown (F)": ItemData(25105, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (G)": ItemData(25106, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (H)": ItemData(25107, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (I)": ItemData(25108, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Redeemable Code']),
    "Unown (J)": ItemData(25109, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (K)": ItemData(25110, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (L)": ItemData(25111, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (M)": ItemData(25112, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (N)": ItemData(25113, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (O)": ItemData(25114, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Redeemable Code']),
    "Unown (P)": ItemData(25115, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (Q)": ItemData(25116, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (R)": ItemData(25117, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Redeemable Code']),
    "Unown (S)": ItemData(25118, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Redeemable Code']),
    "Unown (T)": ItemData(25119, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (U)": ItemData(25120, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (V)": ItemData(25121, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (W)": ItemData(25122, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (X)": ItemData(25123, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (Y)": ItemData(25124, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (Z)": ItemData(25125, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Unown (!)": ItemData(25126, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Unown (?)": ItemData(25127, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Mega Steelix": ItemData(25801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Crystal Steelix": ItemData(25802, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Hisuian Qwilfish": ItemData(26101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Mega Scizor": ItemData(26201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Shuckle (Corked)": ItemData(26301, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Mega Heracross": ItemData(26401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Hisuian Sneasel": ItemData(26501, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hisui Pokemon', 'Not Implemented']),
    "Galarian Corsola": ItemData(27201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Mega Houndoom": ItemData(27901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "Reindeer Stantler": ItemData(28401, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Seasonal Events', 'Merry Christmas']),
    "Blessing Blissey": ItemData(29201, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon']),
    "Mega Tyranitar": ItemData(29801, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Kalos Pokemon', 'Not Implemented']),
    "XD001": ItemData(29901, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Hoenn Pokemon', 'Not Implemented']),
    "Flowering Celebi": ItemData(30101, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Galar Pokemon', 'Not Implemented']),
    "Grinch Celebi": ItemData(30102, ItemClassification.progression, ['Pokemon', 'Alt Pokemon', 'Johto Pokemon', 'Seasonal Events', 'Merry Christmas']),
    
    "Kanto Route 1": ItemData(110001, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Kanto Route 22": ItemData(110002, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 2": ItemData(110003, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 3": ItemData(110004, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 4": ItemData(110005, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 24": ItemData(110006, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 25": ItemData(110007, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 5": ItemData(110008, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 6": ItemData(110009, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 11": ItemData(110010, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 9": ItemData(110011, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 10": ItemData(110012, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 8": ItemData(110013, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 7": ItemData(110014, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 12": ItemData(110015, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 13": ItemData(110016, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 14": ItemData(110017, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 15": ItemData(110018, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 16": ItemData(110019, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 17": ItemData(110020, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 18": ItemData(110021, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 19": ItemData(110022, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 20": ItemData(110023, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 21": ItemData(110024, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kanto Route 23": ItemData(110025, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Treasure Beach": ItemData(110026, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Kindle Road": ItemData(110027, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Cape Brink": ItemData(110028, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Bond Bridge": ItemData(110029, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Five Isle Meadow": ItemData(110030, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Memorial Pillar": ItemData(110031, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Water Labyrinth": ItemData(110032, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Resort Gorgeous": ItemData(110033, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Water Path": ItemData(110034, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Green Path": ItemData(110035, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Outcast Island": ItemData(110036, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Ruin Valley": ItemData(110037, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Canyon Entrance": ItemData(110038, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Sevault Canyon": ItemData(110039, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Valencia Island": ItemData(110040, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pinkan Forest": ItemData(110041, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pinkan Plains": ItemData(110042, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pallet Town": ItemData(110043, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Viridian City": ItemData(110044, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pewter City": ItemData(110045, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Kanto Route 4 Pokemon Center": ItemData(110046, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Cerulean City": ItemData(110047, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Bill's House": ItemData(110048, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Vermilion City": ItemData(110049, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Lavender Town": ItemData(110050, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Celadon City": ItemData(110051, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Saffron City": ItemData(110052, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Fuchsia City": ItemData(110053, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Safari Zone": ItemData(110054, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Cinnabar Island": ItemData(110055, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Indigo Plateau Kanto": ItemData(110056, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "One Island": ItemData(110057, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Mt. Ember": ItemData(110058, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Two Island": ItemData(110059, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Three Island": ItemData(110060, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Professor Ivy's Lab": ItemData(110061, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Client Island": ItemData(110062, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Four Island": ItemData(110063, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Five Island": ItemData(110064, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Rocket Warehouse": ItemData(110065, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Six Island": ItemData(110066, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Dotted Hole": ItemData(110067, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Seven Island": ItemData(110068, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Mikan Island": ItemData(110069, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Navel Island": ItemData(110070, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Trovita Island": ItemData(110071, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Kumquat Island": ItemData(110072, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pummelo Island": ItemData(110073, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Valencia Pokemon Center": ItemData(110074, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pinkan Pokemon Reserve": ItemData(110075, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Viridian Forest": ItemData(110076, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Mt. Moon": ItemData(110077, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Diglett's Cave": ItemData(110078, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Rock Tunnel": ItemData(110079, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Rocket Game Corner": ItemData(110080, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Pokemon Tower": ItemData(110081, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Silph Co.": ItemData(110082, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Power Plant": ItemData(110083, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Seafoam Islands": ItemData(110084, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Pokemon Mansion": ItemData(110085, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Mt. Ember Summit": ItemData(110086, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Berry Forest": ItemData(110087, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "New Island": ItemData(110088, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Seasonal Events', 'Mewtwo Strikes Back']),
    "Victory Road": ItemData(110089, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Cerulean Cave": ItemData(110090, ItemClassification.progression, ['Kanto', 'Mapsanity']),
    "Ruby Path": ItemData(110091, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Icefall Cave": ItemData(110092, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Sunburst Island": ItemData(110093, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Lost Cave": ItemData(110094, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pattern Bush": ItemData(110095, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Altering Cave": ItemData(110096, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Tanoby Ruins": ItemData(110097, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),
    "Pinkan Mountain": ItemData(110098, ItemClassification.progression, ['Kanto', 'Mapsanity', 'Not Implemented']),

    "Farming-Quick-Start Code": ItemData(112001, ItemClassification.filler, ['Codes']),
    "Shiny-Charmer Code": ItemData(112002, ItemClassification.useful, ['Codes']),
    "Great-Balls Code": ItemData(112003, ItemClassification.filler, ['Codes']),
    "Everstone Code": ItemData(112004, ItemClassification.useful, ['Codes']),
    "Typed-Held-Item Code": ItemData(112005, ItemClassification.useful, ['Codes', 'Not Implemented']),
    "Eon-Ticket Code": ItemData(112006, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Ampharosite Code": ItemData(112007, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Rare-Candy Code": ItemData(112009, ItemClassification.filler, ['Codes']),
    "Surfing Pikachu Code": ItemData(112101, ItemClassification.progression, ['Codes']),
    "Rotom (Discord) Code": ItemData(112102, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Unown (D) Code": ItemData(112103, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Unown (I) Code": ItemData(112104, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Unown (S) Code": ItemData(112105, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Unown (C) Code": ItemData(112106, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Unown (O) Code": ItemData(112107, ItemClassification.progression, ['Codes', 'Not Implemented']),
    "Unown (R) Code": ItemData(112108, ItemClassification.progression, ['Codes', 'Not Implemented']),

    "Victory!": ItemData(1000000, ItemClassification.progression, ['Victory']),
}

item_groups = {}
for item, data in item_table.items():
    for group in data.groups:
        item_groups[group] = item_groups.get(group, []) + [item]
    
filler_items = [
    "Protein",
    "100000 Pokedollars",
    "10000 Dungeon Tokens",
    "1000 Quest Points",
    "100 Diamonds",
    "1000 Farm Points"
]

FILLER_ID_START = 1000001
item_name_to_id = {name: data.id for name, data in item_table.items()}
for item in filler_items:
    item_name_to_id[item] = FILLER_ID_START + filler_items.index(item)

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
# ITEM_NAME_TO_ID = {
#     "Key": 1,
#     "Sword": 2,
#     "Shield": 3,
#     "Hammer": 4,
#     "Health Upgrade": 5,
#     "Confetti Cannon": 6,
#     "Math Trap": 7,
# }

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
# DEFAULT_ITEM_CLASSIFICATIONS = {
#     "Key": ItemClassification.progression,
#     "Sword": ItemClassification.progression | ItemClassification.useful,  # Items can have multiple classifications.
#     "Shield": ItemClassification.progression,
#     "Hammer": ItemClassification.progression,
#     "Health Upgrade": ItemClassification.useful,
#     "Confetti Cannon": ItemClassification.filler,
#     "Math Trap": ItemClassification.trap,
# }


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class PokeclickerItem(Item):
    game = "Pokeclicker"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: PokeclickerWorld) -> str:
    return world.random.choice(filler_items)


def create_item_with_correct_classification(world: PokeclickerWorld, name: str) -> PokeclickerItem:
    if name in filler_items:
        classification = ItemClassification.filler
        id = FILLER_ID_START + filler_items.index(name)
    else:
        item = item_table[name]
        classification = item.classification
        id = item.id

    return PokeclickerItem(name, classification, id, world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: PokeclickerWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = []

    for name, item in item_table.items():
        if item.id is None:
            continue
        make_item = True
        for group in item.groups:
            if Helpers.is_category_enabled(world, group) == False:
                make_item = False
                break
        if not make_item:
            continue

        id = item.id
        classification = item.classification
        itempool.append(PokeclickerItem(name, classification, id, world.player))

    # # Some items may only exist if the player enables certain options.
    # # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # # Otherwise, we add a filler Confetti Cannon.
    # if world.options.hammer:
    #     # Once again, it is important to stress that even though the Hammer doesn't always exist,
    #     # it must be present in the worlds item_name_to_id.
    #     # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
    #     itempool.append(world.create_item("Hammer"))

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    # itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    for _ in range(needed_number_of_filler_items):
        name = get_random_filler_item_name(world)
        id = FILLER_ID_START + filler_items.index(name)
        classification = ItemClassification.filler
        itempool.append(PokeclickerItem(name, classification, id, world.player))

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # # Sometimes, you might want the player to start with certain items already in their inventory.
    # # These items are called "precollected items".
    # # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # # Players can add precollected items themselves via the generic "start_inventory" option.
    # # If you want to add your own precollected items, you can do so via world.push_precollected().
    # if world.options.start_with_one_confetti_cannon:
    #     # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
    #     starting_confetti_cannon = world.create_item("Confetti Cannon")
    #     world.push_precollected(starting_confetti_cannon)
