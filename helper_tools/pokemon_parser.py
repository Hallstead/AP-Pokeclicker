from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent / "AP-Pokeclicker"
POKEMON_PATH = PROJECT_DIR / "src" / "modules" / "pokemons" / "PokemonList.ts"
GAME_CONSTANTS_PATH = PROJECT_DIR / "src" / "modules" / "GameConstants.ts"
DISCORD_PATH = PROJECT_DIR / "src" / "scripts" / "discord" / "Discord.ts"
DREAM_ORB_PATH = PROJECT_DIR / "src" / "scripts" / "towns" / "DreamOrbController.ts"
BATTLE_CAFE_PATH = PROJECT_DIR / "src" / "scripts" / "towns" / "BattleCafe.ts"
TEMPORARY_BATTLE_PATH = PROJECT_DIR / "src" / "scripts" / "temporaryBattle" / "TemporaryBattleList.ts"
GYM_LIST_PATH = PROJECT_DIR / "src" / "scripts" / "gym" / "GymList.ts"
QUEST_LINE_HELPER_PATH = PROJECT_DIR / "src" / "scripts" / "quests" / "QuestLineHelper.ts"
ROUTES_PATH = PROJECT_DIR / "src" / "modules" / "routes" / "RouteData.ts"
DUNGEONS_PATH = PROJECT_DIR / "src" / "scripts" / "dungeons" / "Dungeon.ts"
BATTLE_FRONTIER_MILESTONES_PATH = PROJECT_DIR / "src" / "scripts" / "battleFrontier" / "BattleFrontierMilestones.ts"
ROAMING_PATH = PROJECT_DIR / "src" / "modules" / "pokemons" / "RoamingPokemonList.ts"
BERRY_PATH = PROJECT_DIR / "src" / "scripts" / "farming" / "Berry.ts"
FARMING_PATH = PROJECT_DIR / "src" / "scripts" / "farming" / "Farming.ts"
BERRY_DEAL_PATH = PROJECT_DIR / "src" / "scripts" / "farming" / "BerryDeal.ts"
TOWN_LIST_PATH = PROJECT_DIR / "src" / "scripts" / "towns" / "TownList.ts"
ITEM_LIST_PATH = PROJECT_DIR / "src" / "modules" / "items" / "ItemList.ts"
GEM_DEAL_PATH = PROJECT_DIR / "src" / "modules" / "gems" / "GemDealList.ts"
GENERIC_DEAL_PATH = PROJECT_DIR / "src" / "modules" / "deal" / "GenericDeal.ts"
SHARD_DEAL_PATH = PROJECT_DIR / "src" / "modules" / "underground" / "ShardDeal.ts"
BREEDING_PATH = PROJECT_DIR / "src" / "scripts" / "breeding" / "Breeding.ts"
SAFARI_ITEM_PATH = PROJECT_DIR / "src" / "scripts" / "safari" / "SafariItem.ts"
SAFARI_POKEMON_PATH = PROJECT_DIR / "src" / "scripts" / "safari" / "SafariPokemonList.ts"
OUTPUT_PATH = SCRIPT_DIR / "output.txt"


def functionify(text):
    text = text.strip().replace("é", "e").replace(" ", "_").replace("-", "_")
    text = text.replace("\\'", "'").replace(".", "_").replace("'", "").replace("(", "").replace(")", "").lower()
    while "__" in text:
        text = text.replace("__", "_")
    return text.rstrip("_")

def read_source(path):
    text = Path(path).read_text(encoding="utf-8")
    result = []
    index = 0
    in_string = False
    escaped = False

    while index < len(text):
        char = text[index]
        next_char = text[index + 1] if index + 1 < len(text) else ""

        if in_string:
            result.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "'":
                in_string = False
            index += 1
        elif char == "'":
            in_string = True
            result.append(char)
            index += 1
        elif char == "/" and next_char == "/":
            newline = text.find("\n", index + 2)
            index = len(text) if newline == -1 else newline
        elif char == "/" and next_char == "*":
            end = text.find("*/", index + 2)
            index = len(text) if end == -1 else end + 2
        else:
            result.append(char)
            index += 1

    return "".join(result)

def compile_pokemon_dictionary():
    import re

    pokemon = {}

    def add_pokemon(name, route, method):
        if name not in pokemon:
            pokemon[name] = {"land": [], "water": [], "headbutt": []}

        if route not in pokemon[name][method]:
            pokemon[name][method].append(route)

    def extract_bracket_content(text, start_pos):
        """
        Given text and the position of an opening '[',
        return the contents inside the matching ']'.
        Handles nested brackets and quoted strings.
        """
        depth = 0
        in_string = False
        escaped = False

        for i in range(start_pos, len(text)):
            char = text[i]

            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "'":
                    in_string = False
                continue

            if char == "'":
                in_string = True
                continue

            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
                if depth == 0:
                    return text[start_pos + 1:i]

        return ""

    def extract_region_routes(text):
        """
        Extract each complete new RegionRoute(...) block.
        """
        routes = []
        marker = "new RegionRoute("
        search_pos = 0

        while True:
            start = text.find(marker, search_pos)
            if start == -1:
                break

            open_pos = start + len(marker) - 1
            depth = 0
            in_string = False
            escaped = False
            end_pos = None

            for i in range(open_pos, len(text)):
                char = text[i]

                if in_string:
                    if escaped:
                        escaped = False
                    elif char == "\\":
                        escaped = True
                    elif char == "'":
                        in_string = False
                    continue

                if char == "'":
                    in_string = True
                    continue

                if char == "(":
                    depth += 1
                elif char == ")":
                    depth -= 1
                    if depth == 0:
                        end_pos = i
                        break

            if end_pos is None:
                break

            routes.append(text[start:end_pos + 1])
            search_pos = end_pos + 1

        return routes

    def extract_pokemon_names(text):
        """
        Extract quoted Pokemon names from a list such as:

        ['Spearow', 'Mankey', 'Farfetch\\'d']
        """
        names = re.findall(r"'((?:\\'|[^'])*)'", text)
        return [name.replace("\\'", "'") for name in names]

    def extract_pokemon_order(pokemon_ts_path):
        """
        Read pokemon.ts directly (it's plain text, no TS compilation needed)
        and pull out the Pokemon names in the order they're defined, using
        the fact that every entry's 'id' line is immediately followed by
        its 'name' line.
        """
        text = read_source(pokemon_ts_path)

        pairs = re.findall(r"'id':\s*[\d.]+,\s*\n\s*'name':\s*'((?:\\'|[^'])*)'", text)
        return [name.replace("\\'", "'") for name in pairs]

    def extract_pokemon_id_map(pokemon_ts_path):
        """Return {pokemon_id: pokemon_name} from the TS list."""
        text = read_source(pokemon_ts_path)

        pairs = re.findall(
            r"'id':\s*([\d.]+),\s*\n\s*'name':\s*'((?:\\'|[^'])*)'",
            text,
        )
        pokemon_by_id = {}
        for raw_id, raw_name in pairs:
            pokemon_id = float(raw_id)
            pokemon_by_id[pokemon_id] = raw_name.replace("\\'", "'")
        return pokemon_by_id

    def extract_pokemon_regions(pokemon_ts_path, game_constants_path):
        pokemon_text = read_source(pokemon_ts_path)
        constants_text = read_source(game_constants_path)

        region_enum = re.search(r"export enum Region\s*\{(.*?)\}", constants_text, re.DOTALL)
        regions = {
            name: int(index)
            for name, index in re.findall(r"(\w+)\s*=\s*(-?\d+)", region_enum.group(1))
        } if region_enum else {}
        region_names = {
            index: name.title()
            for name, index in regions.items()
            if name not in ("none", "final")
        }
        max_ids_match = re.search(r"MaxIDPerRegion\s*=\s*\[(.*?)\]", constants_text, re.DOTALL)
        max_ids = [int(value) for value in re.findall(r"\b\d+\b", max_ids_match.group(1))] if max_ids_match else []
        max_region_match = re.search(r"MAX_AVAILABLE_REGION\s*=\s*Region\.(\w+)", constants_text)
        max_region = regions.get(max_region_match.group(1), -1) if max_region_match else -1

        array_marker = "export const pokemonList = createPokemonArray("
        array_start = pokemon_text.find(array_marker)
        array_open = pokemon_text.find("(", array_start)
        array_content, _ = extract_matching(pokemon_text, array_open, "(", ")")
        pokemon_regions = {}
        search_pos = 0

        while True:
            object_start = array_content.find("{", search_pos)
            if object_start == -1:
                break

            object_content, object_end = extract_matching(array_content, object_start, "{", "}")
            id_match = re.search(r"'id':\s*([\d.]+)", object_content)
            name_match = re.search(r"'name':\s*'((?:\\'|[^'])*)'", object_content)
            if id_match and name_match:
                native_region_match = re.search(r"'nativeRegion':\s*Region\.(\w+)", object_content)
                if native_region_match:
                    native_region = regions.get(native_region_match.group(1), -1)
                else:
                    pokemon_id = int(float(id_match.group(1)))
                    native_region = next(
                        (index for index, max_id in enumerate(max_ids) if pokemon_id <= max_id),
                        -1,
                    )
                pokemon_regions[name_match.group(1).replace("\\'", "'")] = native_region

            search_pos = object_end + 1

        return pokemon_regions, max_region, region_names

    def extract_regional_starters(game_constants_path):
        """Return {pokemon_id: [region_name, ...]} from RegionalStarters."""
        text = read_source(game_constants_path)
        starter_match = re.search(r"export const RegionalStarters\s*=\s*(\[[\s\S]*?\]);", text)
        if not starter_match:
            return {}

        region_names = [
            "Kanto", "Johto", "Hoenn", "Sinnoh", "Unova", "Kalos",
            "Alola", "Galar", "Hisui", "Paldea",
        ]

        starter_regions = {}
        starter_block = starter_match.group(1)
        region_entries = re.findall(r"\[(.*?)\]", starter_block, re.DOTALL)

        for region_index, region_entry in enumerate(region_entries):
            region_name = region_names[region_index] if region_index < len(region_names) else str(region_index)
            for pokemon_id_text in re.findall(r"\b\d+(?:\.\d+)?\b", region_entry):
                pokemon_id = float(pokemon_id_text)
                starter_regions.setdefault(pokemon_id, []).append(region_name)

        return starter_regions

    def extract_discord_pokemon(discord_ts_path, pokemon_ts_path, game_constants_path):
        discord_text = read_source(discord_ts_path)
        pokemon_text = read_source(pokemon_ts_path)
        constants_text = read_source(game_constants_path)

        region_enum = re.search(r"export enum Region\s*\{(.*?)\}", constants_text, re.DOTALL)
        regions_by_index = {
            int(index): name
            for name, index in re.findall(r"(\w+)\s*=\s*(-?\d+)", region_enum.group(1))
            if name not in ("none", "final")
        } if region_enum else {}

        max_ids_match = re.search(r"MaxIDPerRegion\s*=\s*\[(.*?)\]", constants_text, re.DOTALL)
        max_ids = [int(value) for value in re.findall(r"\b\d+\b", max_ids_match.group(1))] if max_ids_match else []

        pokemon_regions = {}
        array_marker = "export const pokemonList = createPokemonArray("
        array_start = pokemon_text.find(array_marker)
        array_open = pokemon_text.find("(", array_start)
        array_content, _ = extract_matching(pokemon_text, array_open, "(", ")")
        search_pos = 0

        while True:
            obj_start = array_content.find("{", search_pos)
            if obj_start == -1:
                break

            obj_content, obj_end = extract_matching(array_content, obj_start, "{", "}")
            id_match = re.search(r"'id':\s*([\d.]+)", obj_content)
            name_match = re.search(r"'name':\s*'((?:\\'|[^'])*)'", obj_content)
            if id_match and name_match:
                name = name_match.group(1).replace("\\'", "'")
                region_match = re.search(r"'nativeRegion':\s*Region\.(\w+)", obj_content)
                if region_match:
                    region = region_match.group(1)
                else:
                    pokemon_id = int(float(id_match.group(1)))
                    region_index = next(
                        (index for index, max_id in enumerate(max_ids) if pokemon_id <= max_id),
                        -1,
                    )
                    region = regions_by_index.get(region_index)

                if region:
                    pokemon_regions[name] = region

            search_pos = obj_end + 1

        discord_pokemon = {}
        for match in re.finditer(
            r"new\s+DiscordPokemonCode\(\s*pokemonMap\[['\"]((?:\\'|[^'\"])+)['\"]\]",
            discord_text,
        ):
            name = match.group(1).replace("\\'", "'")
            region = pokemon_regions.get(name)
            if region:
                region = region.title()
                discord_pokemon.setdefault(name, [])
                if region not in discord_pokemon[name]:
                    discord_pokemon[name].append(region)

        return discord_pokemon

    def extract_dream_orb_pokemon(dream_orb_ts_path, pokemon_names):
        text = read_source(dream_orb_ts_path)
        dream_orbs = {}
        marker = "new DreamOrb("
        search_pos = 0

        while True:
            orb_start = text.find(marker, search_pos)
            if orb_start == -1:
                break

            orb_open = orb_start + len(marker) - 1
            orb_args_text, orb_close = extract_matching(text, orb_open, "(", ")")
            if orb_close == -1:
                break

            orb_args = split_top_level(orb_args_text)
            if len(orb_args) >= 3:
                color = strip_quotes(orb_args[0])
                items = orb_args[2].strip()
                if items.startswith("["):
                    for match in re.finditer(
                        r"new\s+DreamOrbLoot\(\s*\{\s*type:\s*ItemType\.item\s*,\s*id:\s*'((?:\\'|[^'])*)'",
                        items,
                    ):
                        name = match.group(1).replace("\\'", "'")
                        if name in pokemon_names:
                            dream_orbs.setdefault(name, [])
                            if color not in dream_orbs[name]:
                                dream_orbs[name].append(color)

            search_pos = orb_close + 1

        return dream_orbs

    def extract_battle_cafe_pokemon(battle_cafe_ts_path, pokemon_names):
        text = read_source(battle_cafe_ts_path)
        battle_cafe = {}
        spin_details = {
            "dayClockwiseBelow5": (1, "clockwise", "day"),
            "dayCounterclockwiseBelow5": (1, "counterclockwise", "day"),
            "nightClockwiseBelow5": (1, "clockwise", "night"),
            "nightCounterclockwiseAbove5": (5, "counterclockwise", "night"),
            "nightClockwiseAbove5": (5, "clockwise", "night"),
            "nightCounterclockwiseBelow5": (1, "counterclockwise", "night"),
            "dayClockwiseAbove5": (5, "clockwise", "day"),
            "dayCounterclockwiseAbove5": (5, "counterclockwise", "day"),
            "at5Above10": (11, "counterclockwise", "dusk"),
        }

        evolutions_marker = re.search(r"public static evolutions\s*:[^=]*=\s*\{", text)
        if evolutions_marker:
            evolutions_open = text.find("{", evolutions_marker.start())
            evolutions_text, _ = extract_matching(text, evolutions_open, "{", "}")
            sweet_marker = re.compile(
                r"\[GameConstants\.AlcremieSweet\[['\"]((?:\\'|[^'])*)['\"]\]\]\s*:\s*\{"
            )
            for sweet_match in sweet_marker.finditer(evolutions_text):
                sweet_open = evolutions_text.find("{", sweet_match.start())
                sweet_text, _ = extract_matching(evolutions_text, sweet_open, "{", "}")
                for spin_match in re.finditer(
                    r"\[GameConstants\.AlcremieSpins\.(\w+)\]\s*:\s*new\s+PokemonItem\(\s*'((?:\\'|[^'])*)'",
                    sweet_text,
                ):
                    details = spin_details.get(spin_match.group(1))
                    pokemon_name = spin_match.group(2).replace("\\'", "'")
                    if details and pokemon_name in pokemon_names:
                        battle_cafe.setdefault(pokemon_name, [])
                        result = details
                        if result not in battle_cafe[pokemon_name]:
                            battle_cafe[pokemon_name].append(result)

        cheesy_match = re.search(
            r"new\s+PokemonItem\(\s*'((?:\\'|[^'])*)'\s*,\s*0\s*\)",
            text,
        )
        if cheesy_match:
            pokemon_name = cheesy_match.group(1).replace("\\'", "'")
            if pokemon_name in pokemon_names:
                battle_cafe[pokemon_name] = [(3600, "any", "any")]

        return battle_cafe

    def extract_matching(text, open_pos, open_char, close_char):
        """
        Given text and the position of an opening bracket/paren/brace,
        return (content, close_pos) for the matching closing character.
        Handles nesting and quoted strings.
        """
        depth = 0
        in_string = False
        escaped = False

        for i in range(open_pos, len(text)):
            char = text[i]

            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "'":
                    in_string = False
                continue

            if char == "'":
                in_string = True
                continue

            if char == open_char:
                depth += 1
            elif char == close_char:
                depth -= 1
                if depth == 0:
                    return text[open_pos + 1:i], i

        return "", -1

    def split_top_level(text):
        """
        Split text on commas that sit outside of any bracket/paren/brace
        nesting and outside of quoted strings.
        """
        parts = []
        current = []
        depth = 0
        in_string = False
        escaped = False

        for char in text:
            if in_string:
                current.append(char)
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "'":
                    in_string = False
                continue

            if char == "'":
                in_string = True
                current.append(char)
                continue

            if char in "([{":
                depth += 1
            elif char in ")]}":
                depth -= 1

            if char == "," and depth == 0:
                parts.append("".join(current))
                current = []
            else:
                current.append(char)

        if current:
            parts.append("".join(current))

        return [part.strip() for part in parts if part.strip()]

    def extract_requirement_calls(text):
        calls = []
        marker = re.compile(r"new\s+(\w+Requirement)\(")
        search_pos = 0

        while True:
            match = marker.search(text, search_pos)
            if not match:
                break

            open_paren = text.find("(", match.start())
            args, close_paren = extract_matching(text, open_paren, "(", ")")
            if close_paren == -1:
                break

            calls.append({
                "type": match.group(1),
                "args": [arg.strip() for arg in split_top_level(args)],
            })
            search_pos = close_paren + 1

        return calls

    def format_requirement_arg(arg):
        arg = arg.strip()

        if arg.startswith("[") and arg.endswith("]"):
            return [format_requirement_arg(value) for value in split_top_level(arg[1:-1])]

        if arg.startswith("'") and arg.endswith("'"):
            return strip_quotes(arg)

        return arg

    def badge_name(value):
        badge = value.rsplit(".", 1)[-1].replace("_", " ")
        badge = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", badge)
        badge = " ".join(word.capitalize() for word in badge.split()) + " Badge"
        elite_champion = re.fullmatch(r"Elite (.+) Champion Badge", badge)
        if elite_champion:
            return f"{elite_champion.group(1)} Elite Champion Badge"
        return badge

    def strip_quotes(text):
        text = text.strip()

        if text.startswith("'") and text.endswith("'"):
            return text[1:-1].replace("\\'", "'")

        return text

    def humanize_underscore(text):
        return text.strip().replace("_", " ").title()

    def humanize_enum(arg):
        """'StoneType.Moon_stone' / 'MegaStoneType.Charizardite_X' -> 'Moon Stone' / 'Charizardite X'."""
        return humanize_underscore(arg.strip().split(".")[-1])

    def humanize_item_literal(arg):
        """'Black_Glasses' (quoted string arg) -> 'Black Glasses'."""
        return humanize_underscore(strip_quotes(arg))

    def extract_enum_list(arg):
        """'[WeatherType.Rain, WeatherType.Fog]' -> ['Rain', 'Fog']."""
        arg = arg.strip()

        if arg.startswith("[") and arg.endswith("]"):
            arg = arg[1:-1]

        return [humanize_enum(part) for part in split_top_level(arg)]

    # Each handler maps a Pokemon evolution function call to the indexes of
    # its "prev"/"evolved" name arguments, plus any extra fields to record
    # (level, item, time of day, region, etc.) on the evolved Pokemon.
    EVOLUTION_HANDLERS = {
        "DummyEvolution": (0, 1, lambda a: {}),
        "LevelEvolution": (0, 1, lambda a: {"level": a[2].strip()}),
        "StoneEvolution": (0, 1, lambda a: {"item": humanize_enum(a[2])}),
        "DayTimedStoneEvolution": (0, 1, lambda a: {"item": humanize_enum(a[2]), "time": "day"}),
        "NightTimedStoneEvolution": (0, 1, lambda a: {"item": humanize_enum(a[2]), "time": "night"}),
        "NightTimedLevelEvolution": (0, 1, lambda a: {"level": a[2].strip(), "time": "night"}),
        "DayTimedLevelEvolution": (0, 1, lambda a: {"level": a[2].strip(), "time": "day"}),
        "MegaEvolution": (1, 2, lambda a: {"item": humanize_enum(a[0])}),
        "DayTimedMegaEvolution": (1, 2, lambda a: {"item": humanize_enum(a[0]), "time": "day"}),
        "NightTimedMegaEvolution": (1, 2, lambda a: {"item": humanize_enum(a[0]), "time": "night"}),
        "HeldItemLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "item": humanize_item_literal(a[0])}),
        "RegionStoneEvolution": (1, 2, lambda a: {"item": humanize_enum(a[3]), "region": a[0].strip()}),
        "RegionLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "region": a[0].strip()}),
        "RegionNightTimedLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "region": a[0].strip(), "time": "night"}),
        "EnvironmentRestrictedLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "environment": strip_quotes(a[0])}),
        "WeatherRestrictedLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "weather": extract_enum_list(a[0])}),
        "DayCyclePartRestrictedLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "dayCyclePart": extract_enum_list(a[0])}),
        "QuestlineLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "questline": strip_quotes(a[0])}),
        "QuestlineStoneEvolution": (1, 2, lambda a: {"item": humanize_enum(a[3]), "questline": strip_quotes(a[0])}),
        "DungeonRestrictedLevelEvolution": (1, 2, lambda a: {"level": a[3].strip(), "dungeon_evolution": strip_quotes(a[0])}),
        "AttackEvolution": (2, 3, lambda a: {"attack": a[0].strip(), "attackIsPercent": a[1].strip()}),
    }

    def extract_pokemon_evolutions(pokemon_ts_path):
        """
        Read pokemon.ts and, for every evolution call found in a Pokemon's
        'evolutions' list, record on the evolved Pokemon who it evolves
        from ("prev") plus whatever else is needed (level, item, time of
        day, region, questline, etc.) via EVOLUTION_HANDLERS.
        """
        text = read_source(pokemon_ts_path)

        evolutions = {}
        dummy_evolutions = {}
        stone_evolutions = set()
        stone_evolution_types = {
            "StoneEvolution", "DayTimedStoneEvolution", "NightTimedStoneEvolution",
            "DayCyclePartRestrictedStoneEvolution", "MoonCyclePhaseStoneEvolution",
            "RegionStoneEvolution", "QuestlineStoneEvolution", "MegaEvolution",
            "DayTimedMegaEvolution", "NightTimedMegaEvolution",
        }
        array_marker = "export const pokemonList = createPokemonArray("
        array_start = text.find(array_marker)
        array_open = text.find("(", array_start)
        array_content, _ = extract_matching(text, array_open, "(", ")")
        search_pos = 0

        while True:
            obj_start = array_content.find("{", search_pos)
            if obj_start == -1:
                break

            obj_content, obj_end = extract_matching(array_content, obj_start, "{", "}")
            evo_match = re.search(r"'evolutions':\s*\[", obj_content)

            if evo_match:
                evo_open = obj_content.find("[", evo_match.start())
                evo_content, _ = extract_matching(obj_content, evo_open, "[", "]")

                for call in split_top_level(evo_content):
                    func_match = re.match(r"(\w+)\(", call)
                    if not func_match:
                        continue

                    handler = EVOLUTION_HANDLERS.get(func_match.group(1))
                    if not handler:
                        continue

                    prev_idx, evolved_idx, extra_fn = handler
                    call_open = call.find("(")
                    args_content, _ = extract_matching(call, call_open, "(", ")")
                    args = split_top_level(args_content)

                    if len(args) <= max(prev_idx, evolved_idx):
                        continue

                    evolved = strip_quotes(args[evolved_idx])
                    evolution = {"prev": strip_quotes(args[prev_idx]), **extra_fn(args)}
                    if func_match.group(1) == "DummyEvolution":
                        dummy_evolutions.setdefault(evolved, []).append(evolution)
                    else:
                        evolutions.setdefault(evolved, []).append(evolution)
                        if func_match.group(1) in stone_evolution_types:
                            stone_evolutions.add(evolved)

            search_pos = obj_end + 1

        return evolutions, dummy_evolutions, stone_evolutions

    def extract_baby_pokemon(pokemon_ts_path):
        """Read the names of Pokemon entries marked as baby Pokemon."""
        text = read_source(pokemon_ts_path)

        babies = []
        array_marker = "export const pokemonList = createPokemonArray("
        array_start = text.find(array_marker)
        array_open = text.find("(", array_start)
        array_content, _ = extract_matching(text, array_open, "(", ")")
        search_pos = 0

        while True:
            obj_start = array_content.find("{", search_pos)
            if obj_start == -1:
                break

            obj_content, obj_end = extract_matching(array_content, obj_start, "{", "}")
            name_match = re.search(r"'name':\s*'((?:\\'|[^'])*)'", obj_content)
            if name_match and re.search(r"'baby':\s*true", obj_content):
                babies.append(name_match.group(1).replace("\\'", "'"))

            search_pos = obj_end + 1

        return babies

    def extract_dungeon_encounters(dungeons_ts_path, pokemon_names):
        text = read_source(dungeons_ts_path)

        def has_not_yet_requirement(expression):
            return re.search(r"\bGameConstants\.AchievementOption\.less\b", expression) is not None

        def dungeon_requirement_alternatives(expression):
            marker = re.search(r"new\s+(\w+Requirement)\s*\(", expression)
            if not marker:
                return [expression]

            requirement_type = marker.group(1)
            open_paren = expression.find("(", marker.start())
            args_text, close_pos = extract_matching(expression, open_paren, "(", ")")
            if close_pos == -1:
                return [expression]

            requirement = expression[marker.start():close_pos + 1]
            if requirement_type not in ("OneFromManyRequirement", "MultiRequirement"):
                return [requirement]

            children = []
            for arg in split_top_level(args_text):
                arg = arg.strip()
                if arg.startswith("[") and arg.endswith("]"):
                    children.extend(split_top_level(arg[1:-1]))
                elif arg:
                    children.append(arg)

            if requirement_type == "OneFromManyRequirement":
                return [
                    alternative
                    for child in children
                    for alternative in dungeon_requirement_alternatives(child)
                ] or [requirement]

            child_alternatives = [
                dungeon_requirement_alternatives(child)
                for child in children
            ]
            if all(len(alternatives) == 1 for alternatives in child_alternatives):
                return [requirement]

            combinations = [[]]
            for alternatives in child_alternatives:
                combinations = [
                    combination + [alternative]
                    for combination in combinations
                    for alternative in alternatives
                ]
            return [
                "new MultiRequirement([" + ", ".join(combination) + "])"
                for combination in combinations
            ]

        def dungeon_requirement_terms(expression):
            marker = re.search(r"new\s+(\w+Requirement)\s*\(", expression)
            if not marker:
                return [], []

            requirement_type = marker.group(1)
            open_paren = expression.find("(", marker.start())
            args_text, close_pos = extract_matching(expression, open_paren, "(", ")")
            if close_pos == -1:
                return [], [{"type": requirement_type, "args": []}]

            args = split_top_level(args_text)
            if requirement_type == "MultiRequirement":
                terms = []
                unsupported = []
                for arg in args:
                    arg = arg.strip()
                    if arg.startswith("[") and arg.endswith("]"):
                        arg = arg[1:-1]
                    for child in split_top_level(arg):
                        child_terms, child_unsupported = dungeon_requirement_terms(child)
                        terms.extend(child_terms)
                        unsupported.extend(child_unsupported)
                return terms, unsupported

            if requirement_type == "DayOfWeekRequirement":
                return [], []

            if requirement_type == "WeatherRequirement":
                return ['make_rule(has_script, "Simple Weather Changer Script")'], []

            if requirement_type == "ObtainedPokemonRequirement" and args:
                pokemon_name = strip_quotes(args[0])
                quoted_name = "'" + pokemon_name.replace("'", "\\'") + "'"
                return [f"Has({quoted_name})"], []

            if requirement_type == "GymBadgeRequirement" and args:
                quoted_badge = "'" + badge_name(args[0]).replace("'", "\\'") + "'"
                return [f"Has({quoted_badge})"], []

            if (
                requirement_type == "QuestLineStepCompletedRequirement"
                and len(args) > 1
                and re.fullmatch(r"\d+", args[1].strip())
            ):
                quest_name = strip_quotes(args[0])
                quest_function = re.sub(
                    r"[^a-z0-9]+",
                    "_",
                    quest_name.lower().replace("'", ""),
                ).strip("_")
                return [f"make_rule({quest_function}{args[1].strip()})"], []

            if requirement_type == "QuestLineCompletedRequirement" and args:
                quest_name = strip_quotes(args[0])
                quest_function = re.sub(
                    r"[^a-z0-9]+",
                    "_",
                    quest_name.lower().replace("'", ""),
                ).strip("_")
                return [f"make_rule(completed_{quest_function})"], []

            if requirement_type == "SpecialEventRequirement" and args:
                return ['make_rule(has_script, "Infinite Seasonal Events Script")'], []

            if requirement_type == "TemporaryBattleRequirement" and args:
                battle_name = re.sub(r"_(?=\d)", "", functionify(strip_quotes(args[0])))
                return [f"make_rule({battle_name})"], []

            if requirement_type == "ClearDungeonRequirement" and len(args) > 1:
                dungeon_match = re.search(
                    r"getDungeonIndex\(\s*'((?:\\'|[^'])*)'\s*\)",
                    args[1],
                )
                if dungeon_match:
                    dungeon_name = dungeon_match.group(1).replace("\\'", "'")
                    return [f"make_rule({functionify(dungeon_name)}, True)"], []

            return [], [{
                "type": requirement_type,
                "args": [format_requirement_arg(arg) for arg in args],
            }]

        def event_is_required(requirement_expression):
            marker = re.search(r"new\s+(\w+Requirement)\s*\(", requirement_expression)
            if not marker:
                return False

            requirement_type = marker.group(1)
            args_text, close_pos = extract_matching(
                requirement_expression,
                requirement_expression.find("(", marker.start()),
                "(",
                ")",
            )
            if close_pos == -1:
                return False
            if requirement_type in ("SpecialEventRequirement", "SpecialEventRandomRequirement"):
                return True

            children = []
            for argument in split_top_level(args_text):
                argument = argument.strip()
                if argument.startswith("[") and argument.endswith("]"):
                    children.extend(split_top_level(argument[1:-1]))
                else:
                    children.append(argument)

            child_results = [event_is_required(child) for child in children]
            if requirement_type == "OneFromManyRequirement":
                return bool(child_results) and all(child_results)
            return any(child_results)

        unown_lists = {
            match.group(1): match.group(2)
            for match in re.finditer(
                r"const\s+(\w+UnownList)\s*=\s*'([^']*)'\.split\(''\)",
                text,
            )
        }
        encounters = {}
        search_pos = 0

        while True:
            dungeon_start = text.find("new Dungeon(", search_pos)
            if dungeon_start == -1:
                break

            open_paren = text.find("(", dungeon_start)
            dungeon_args, close_paren = extract_matching(text, open_paren, "(", ")")
            if close_paren == -1:
                break

            args = split_top_level(dungeon_args)
            if len(args) < 5:
                search_pos = close_paren + 1
                continue

            dungeon_name = strip_quotes(args[0])
            dungeon_data = encounters.setdefault(dungeon_name, {
                "normal": [],
                "conditional_encounters": [],
                "unresolved_requirements": [],
                "bosses": [],
                "conditional_bosses": [],
                "vivillon_quest_rules": [],
                "conditional_loot": [],
                "gmax_specials": [],
                "loot": [],
                "shadow_pokemon": [],
            })

            normal_arg = args[1]
            normal_content = normal_arg[1:-1] if normal_arg.startswith("[") else normal_arg
            for enemy in split_top_level(normal_content):
                enemy = enemy.strip()
                pokemon_match = re.match(
                    r"\{\s*pokemon\s*:\s*'((?:\\'|[^'])*)'",
                    enemy,
                )
                if pokemon_match:
                    name = pokemon_match.group(1).replace("\\'", "'")
                    options_match = re.search(r"\boptions\s*:\s*\{", enemy)
                    requirement_expression = ""
                    if options_match:
                        options_open = enemy.find("{", options_match.start())
                        options_text, _ = extract_matching(enemy, options_open, "{", "}")
                        requirement_match = re.search(r"\brequirement\s*:\s*", options_text)
                        if requirement_match:
                            requirement_expression = options_text[requirement_match.end():]

                    if requirement_expression:
                        for alternative in dungeon_requirement_alternatives(requirement_expression):
                            if has_not_yet_requirement(alternative):
                                continue

                            terms, unsupported = dungeon_requirement_terms(alternative)
                            terms.insert(0, f"make_rule({functionify(dungeon_name)}, False)")
                            dungeon_data["unresolved_requirements"].extend(unsupported)
                            if terms and name in pokemon_names:
                                dungeon_data["conditional_encounters"].append((name, terms, unsupported))
                        continue
                elif enemy.startswith("'") and enemy.endswith("'"):
                    name = strip_quotes(enemy)
                else:
                    continue

                if name in pokemon_names and name not in dungeon_data["normal"]:
                    dungeon_data["normal"].append(name)

            loot_arg = args[2]
            loot_search_pos = 0
            while True:
                match = re.search(r"\{\s*loot\s*:\s*'((?:\\'|[^'])*)'", loot_arg[loot_search_pos:])
                if not match:
                    break
                name = match.group(1).replace("\\'", "'")
                loot_open = loot_arg.find("{", loot_search_pos + match.start())
                loot_options, loot_close = extract_matching(loot_arg, loot_open, "{", "}")
                if loot_close == -1:
                    break

                requirement_match = re.search(r"\brequirement\s*:\s*", loot_options)
                if requirement_match:
                    requirement_expression = loot_options[requirement_match.end():]
                    for alternative in dungeon_requirement_alternatives(requirement_expression):
                        if has_not_yet_requirement(alternative):
                            continue

                        terms, unsupported = dungeon_requirement_terms(alternative)
                        terms.insert(0, f"make_rule({functionify(dungeon_name)}, False)")
                        if name in pokemon_names:
                            conditional_loot = (name, terms, unsupported)
                            if conditional_loot not in dungeon_data["conditional_loot"]:
                                dungeon_data["conditional_loot"].append(conditional_loot)
                elif name in pokemon_names and name not in dungeon_data["loot"]:
                    dungeon_data["loot"].append(name)

                loot_search_pos = loot_close + 1

            boss_search_pos = 0
            while True:
                boss_start = args[4].find("new DungeonBossPokemon(", boss_search_pos)
                if boss_start == -1:
                    break

                boss_open = args[4].find("(", boss_start)
                boss_args_text, boss_close = extract_matching(args[4], boss_open, "(", ")")
                if boss_close == -1:
                    break

                boss_args = split_top_level(boss_args_text)
                if len(boss_args) >= 2:
                    name = strip_quotes(boss_args[0])
                    attack = boss_args[1].strip()
                    requirement_expression = ""
                    if len(boss_args) > 3:
                        requirement_match = re.search(r"\brequirement\s*:\s*", boss_args[3])
                        if requirement_match:
                            requirement_expression = boss_args[3][requirement_match.end():]

                    if name.startswith("Vivillon ("):
                        for quest_match in re.finditer(
                            r"new\s+QuestLineStepCompletedRequirement\(\s*'The Great Vivillon Hunt!'\s*,\s*(\d+)([^)]*)\)",
                            requirement_expression,
                        ):
                            if "GameConstants.AchievementOption.less" in quest_match.group(2):
                                continue

                            quest_rule = (
                                name,
                                f"make_rule(the_great_vivillon_hunt{quest_match.group(1)})",
                                functionify(dungeon_name),
                                attack,
                            )
                            if quest_rule not in dungeon_data["vivillon_quest_rules"]:
                                dungeon_data["vivillon_quest_rules"].append(quest_rule)

                    requirement_alternatives = dungeon_requirement_alternatives(requirement_expression)
                    if len(requirement_alternatives) > 1:
                        for alternative in requirement_alternatives:
                            if has_not_yet_requirement(alternative):
                                continue

                            event_required = event_is_required(alternative)
                            requirement_terms, unsupported_requirements = dungeon_requirement_terms(
                                alternative
                            )
                            has_supported_requirement = (
                                bool(requirement_terms) and not unsupported_requirements
                            )
                            if name in pokemon_names and (
                                has_supported_requirement or event_required or unsupported_requirements
                            ):
                                conditional_boss = (
                                    name,
                                    dungeon_name,
                                    attack,
                                    event_required,
                                    requirement_terms,
                                    unsupported_requirements,
                                )
                                if conditional_boss not in dungeon_data["conditional_bosses"]:
                                    dungeon_data["conditional_bosses"].append(conditional_boss)
                        boss_search_pos = boss_close + 1
                        continue

                    if has_not_yet_requirement(requirement_expression):
                        boss_search_pos = boss_close + 1
                        continue

                    event_required = event_is_required(requirement_expression)
                    requirement_terms, unsupported_requirements = dungeon_requirement_terms(
                        requirement_expression
                    )

                    if dungeon_name == "Max Lair" and name.startswith("Gigantamax "):
                        unowned_requirement = re.search(
                            rf"new\s+ObtainedPokemonRequirement\(\s*'{re.escape(name)}'\s*,\s*true\s*\)",
                            requirement_expression,
                        )
                        if unowned_requirement:
                            quest_step = None
                            random_step = re.search(
                                r"QuestLineStepCompletedRequirement\(\s*'The Lair of Giants'\s*,\s*\(\)\s*=>\s*maxLairQuestStepRandomIndex\((\d+)\)",
                                requirement_expression,
                            )
                            fixed_step = re.search(
                                r"QuestLineStepCompletedRequirement\(\s*'The Lair of Giants'\s*,\s*(\d+)",
                                requirement_expression,
                            )
                            if random_step:
                                quest_step = 3 + int(random_step.group(1))
                            elif fixed_step:
                                quest_step = int(fixed_step.group(1))

                            dungeon_data["gmax_specials"].append({
                                "unowned": name,
                                "quest_step": quest_step,
                            })
                            boss_search_pos = boss_close + 1
                            continue

                        if re.search(
                            rf"new\s+ObtainedPokemonRequirement\(\s*'{re.escape(name)}'\s*\)",
                            requirement_expression,
                        ):
                            dungeon_data["gmax_specials"].append({"owned": name})
                            boss_search_pos = boss_close + 1
                            continue

                    has_supported_requirement = bool(requirement_terms) and not unsupported_requirements
                    if name in pokemon_names and (
                        has_supported_requirement or event_required or unsupported_requirements
                    ):
                        conditional_boss = (
                            name,
                            dungeon_name,
                            attack,
                            event_required,
                            requirement_terms,
                            unsupported_requirements,
                        )
                        if conditional_boss not in dungeon_data["conditional_bosses"]:
                            dungeon_data["conditional_bosses"].append(conditional_boss)
                    elif name in pokemon_names and (name, attack) not in dungeon_data["bosses"]:
                        dungeon_data["bosses"].append((name, attack))

                boss_search_pos = boss_close + 1

            for match in re.finditer(
                r"\.\.\.(\w+UnownList)\.map\(\(char,\s*index\)\s*=>\s*\{.*?"
                r"new\s+DungeonBossPokemon\(`Unown \(\$\{char\}\)`\s+as\s+PokemonNameType,\s*([^,]+)",
                args[4],
                re.DOTALL,
            ):
                attack = match.group(2).strip()
                for char in unown_lists.get(match.group(1), ""):
                    name = f"Unown ({char})"
                    if name in pokemon_names and (name, attack) not in dungeon_data["bosses"]:
                        dungeon_data["bosses"].append((name, attack))

            gym_search_pos = 0
            while True:
                gym_start = dungeon_args.find("new GymPokemon(", gym_search_pos)
                if gym_start == -1:
                    break

                gym_open = dungeon_args.find("(", gym_start)
                gym_args, gym_close = extract_matching(dungeon_args, gym_open, "(", ")")
                if gym_close == -1:
                    break

                gym_values = split_top_level(gym_args)
                if gym_values and any(
                    "GameConstants.ShadowStatus.Shadow" in value
                    for value in gym_values[1:]
                ):
                    name = strip_quotes(gym_values[0])
                    if name in pokemon_names and name not in dungeon_data["shadow_pokemon"]:
                        dungeon_data["shadow_pokemon"].append(name)

                gym_search_pos = gym_close + 1

            search_pos = close_paren + 1

        return encounters

    def extract_battle_frontier_pokemon(milestones_ts_path, pokemon_names):
        text = read_source(milestones_ts_path)
        rewards = {}
        marker = "new BattleFrontierMilestonePokemon("
        search_pos = 0

        while True:
            start = text.find(marker, search_pos)
            if start == -1:
                break

            open_paren = start + len(marker) - 1
            args_text, close_paren = extract_matching(text, open_paren, "(", ")")
            if close_paren == -1:
                break

            args = split_top_level(args_text)
            if len(args) >= 2:
                stage = int(args[0].strip())
                pokemon_name = strip_quotes(args[1])
                if pokemon_name in pokemon_names:
                    reward = rewards.setdefault(pokemon_name, {
                        "stages": [],
                        "requirements": [],
                    })
                    if stage not in reward["stages"]:
                        reward["stages"].append(stage)

                    if len(args) > 2:
                        for call in extract_requirement_calls(args[2]):
                            requirement = {
                                "type": call["type"],
                                "args": [format_requirement_arg(arg) for arg in call["args"]],
                            }
                            if requirement not in reward["requirements"]:
                                reward["requirements"].append(requirement)

            search_pos = close_paren + 1

        return rewards

    def extract_roamers(roaming_ts_path):
        text = read_source(roaming_ts_path)

        group_names = {}
        group_block = re.search(r"public static roamerGroups[^=]*=\s*\[(.*?)\];", text, re.DOTALL)
        if group_block:
            group_content = group_block.group(1)
            for region_index, region_block in enumerate(split_top_level(group_content)):
                group_names[region_index] = re.findall(
                    r"new RoamingGroup\('((?:\\'|[^'])*)'", region_block
                )

        roamers = []
        marker = "RoamingPokemonList.add("
        search_pos = 0
        while True:
            start = text.find(marker, search_pos)
            if start == -1:
                break

            open_paren = start + len(marker) - 1
            args_text, close_paren = extract_matching(text, open_paren, "(", ")")
            if close_paren == -1:
                break

            args = split_top_level(args_text)
            roamer_match = re.match(
                r"new\s+RoamingPokemon\(\s*'((?:\\'|[^'])*)'",
                args[2] if len(args) > 2 else "",
            )
            region_match = re.search(r"Region\.(\w+)", args[0] if args else "")
            group_match = re.match(r"(\d+)", args[1] if len(args) > 1 else "")
            if roamer_match and region_match and group_match:
                region_index = {
                    "kanto": 0, "johto": 1, "hoenn": 2, "sinnoh": 3,
                    "unova": 4, "kalos": 5, "alola": 6, "galar": 7,
                    "hisui": 8, "paldea": 9,
                }.get(region_match.group(1).lower())
                group_index = int(group_match.group(1))
                if region_index is not None:
                    requirements = extract_requirement_calls(args[2])
                    roamers.append({
                        "name": roamer_match.group(1).replace("\\'", "'"),
                        "group": group_names.get(region_index, [])[group_index],
                        "requirements": requirements,
                    })

            search_pos = close_paren + 1

        christmas_requirement = {
            "type": "SpecialEventRequirement",
            "args": ["Merry Christmas!"],
        }
        for group in dict.fromkeys(roamer["group"] for roamer in roamers):
            roamers.append({
                "name": "Santa Snorlax",
                "group": group,
                "requirements": [christmas_requirement],
            })

        return roamers

    def extract_berry_trades(berry_deal_ts_path, pokemon_names):
        text = read_source(berry_deal_ts_path)

        trades = {}
        location_methods = {
            "generateGoldenrodDeals": "Goldenrod City",
            "generateMauvilleDeals": "Mauville City",
            "generatePinkanDeals": "Pinkan Pokémon Reserve",
            "generateHearthomeDeals": "Hearthome City",
            "generateSecretBerryShopDeals": "Secret Berry Shop",
            "generateDriftveilDeals": "Driftveil City",
        }

        for method, location in location_methods.items():
            method_start = text.find(f"private static {method}()")
            if method_start == -1:
                continue

            body_start = text.find("{", method_start)
            body, _ = extract_matching(text, body_start, "{", "}")

            search_pos = 0
            while True:
                deal_start = body.find("new BerryDeal(", search_pos)
                if deal_start == -1:
                    break

                open_paren = body.find("(", deal_start)
                args_text, close_paren = extract_matching(body, open_paren, "(", ")")
                if close_paren == -1:
                    break

                args = split_top_level(args_text)
                if len(args) >= 3:
                    berry_match = re.search(r"BerryType\.(\w+)", args[0])
                    item_match = re.match(
                        r"ItemList\[['\"]((?:\\'|[^'\"])+)['\"]\]|ItemList\.(\w+)",
                        args[2].strip(),
                    )
                    if berry_match and item_match:
                        berry_name = humanize_underscore(berry_match.group(1)) + " Berry"
                        item_name = (item_match.group(1) or item_match.group(2)).replace("\\'", "'")
                        if item_name in pokemon_names:
                            trades.setdefault(item_name, []).append((functionify(location), [berry_name]))

                search_pos = close_paren + 1

        return trades

    def extract_generic_trades(generic_deal_ts_path, town_list_ts_path, pokemon_names):
        deal_text = read_source(generic_deal_ts_path)
        town_text = read_source(town_list_ts_path)

        trader_locations = {}
        for match in re.finditer(
            r"new\s+GenericTraderShop\(\s*['\"](\w+)['\"]",
            town_text,
        ):
            trader_id = match.group(1)
            town_start = town_text.rfind("TownList[", 0, match.start())
            town_match = re.search(
                r"TownList\[['\"]((?:\\'|[^'\"])+)['\"]\]\s*=",
                town_text[town_start:match.start()],
            )
            if town_match:
                trader_locations[trader_id] = functionify(town_match.group(1).replace("\\'", "'"))

        trades = {}
        list_marker = re.compile(r"GenericDeal\.list\.(\w+)\s*=\s*ko\.observableArray\(")
        for list_match in list_marker.finditer(deal_text):
            trader_id = list_match.group(1)
            location = trader_locations.get(trader_id)
            if not location:
                continue

            array_start = list_match.end() - 1
            array_body, _ = extract_matching(deal_text, array_start, "(", ")")
            search_pos = 0
            while True:
                deal_start = array_body.find("new GenericDeal(", search_pos)
                if deal_start == -1:
                    break

                deal_open = array_body.find("(", deal_start)
                deal_args, deal_end = extract_matching(array_body, deal_open, "(", ")")
                if deal_end == -1:
                    break

                costs_match = re.search(r"costs\s*:\s*\[", deal_args)
                profits_match = re.search(r"profits\s*:\s*\[", deal_args)
                if costs_match and profits_match:
                    costs_content, _ = extract_matching(
                        deal_args, deal_args.find("[", costs_match.start()), "[", "]"
                    )
                    profits_content, _ = extract_matching(
                        deal_args, deal_args.find("[", profits_match.start()), "[", "]"
                    )

                    cost_items = []
                    currency_costs = []
                    for cost in split_top_level(costs_content):
                        item_match = re.search(
                            r"item\s*:\s*ItemList(?:\[['\"]((?:\\'|[^'\"])+)['\"]\]|\.(\w+))",
                            cost,
                        )
                        if item_match:
                            cost_items.append((item_match.group(1) or item_match.group(2)).replace("\\'", "'"))
                            continue

                        amount_match = re.search(
                            r"currency\s*:\s*new\s+Amount\(\s*\d+\s*,\s*Currency\.(\w+)",
                            cost,
                        )
                        if amount_match:
                            currency_costs.append(amount_match.group(1))
                    cost_items = [humanize_underscore(item) for item in cost_items] + currency_costs

                    for profit in split_top_level(profits_content):
                        item_match = re.search(
                            r"item\s*:\s*ItemList(?:\[['\"]((?:\\'|[^'\"])+)['\"]\]|\.(\w+))",
                            profit,
                        )
                        if not item_match:
                            continue

                        item_name = (item_match.group(1) or item_match.group(2)).replace("\\'", "'")
                        if item_name not in pokemon_names:
                            continue

                        if cost_items:
                            trade = (location, cost_items)
                            if trade not in trades.setdefault(item_name, []):
                                trades[item_name].append(trade)

                search_pos = deal_end + 1

        return trades

    def extract_shard_trades(shard_deal_ts_path, item_list_ts_path, pokemon_names):
        text = read_source(shard_deal_ts_path)
        item_text = read_source(item_list_ts_path)

        item_pokemon = {}
        for match in re.finditer(
            r"ItemList(?:\[['\"]((?:\\'|[^'\"])+)['\"]\]|\.(\w+))\s*=\s*new\s+PokemonItem\(\s*['\"]((?:\\'|[^'\"])+)['\"]",
            item_text,
        ):
            item_key = (match.group(1) or match.group(2)).replace("\\'", "'")
            item_pokemon[item_key] = match.group(3).replace("\\'", "'")

        trades = {}
        location_marker = re.compile(
            r"ShardDeal\.list\[ShardTraderLocations(?:\[['\"]((?:\\'|[^'\"])+)['\"]\]|\.(\w+))\]\s*=\s*ko\.observableArray\("
        )
        for loc_match in location_marker.finditer(text):
            town_name = (loc_match.group(1) or loc_match.group(2)).replace("\\'", "'")
            array_body, array_close = extract_matching(text, loc_match.end() - 1, "(", ")")
            if array_close == -1:
                continue

            search_pos = 0
            while True:
                deal_start = array_body.find("new ShardDeal(", search_pos)
                if deal_start == -1:
                    break

                deal_open = array_body.find("(", deal_start)
                deal_args_text, deal_close = extract_matching(array_body, deal_open, "(", ")")
                if deal_close == -1:
                    break

                deal_args = split_top_level(deal_args_text)
                if len(deal_args) >= 2:
                    item_match = re.match(
                        r"ItemList\[['\"]((?:\\'|[^'\"])+)['\"]\]|ItemList\.(\w+)",
                        deal_args[1].strip(),
                    )
                    if item_match:
                        item_key = (item_match.group(1) or item_match.group(2)).replace("\\'", "'")
                        pokemon_name = item_pokemon.get(item_key)
                        if pokemon_name and pokemon_name in pokemon_names:
                            shard_parts = [
                                shard_match.group(1).replace(chr(92) + chr(39), chr(39))
                                for shard_match in re.finditer(
                                    r"shardTypeString:\s*'((?:\\'|[^'])*)'\s*,\s*amount:\s*(\d+)",
                                    deal_args[0],
                                )
                            ]
                            trade = (functionify(town_name), shard_parts)
                            if trade not in trades.setdefault(pokemon_name, []):
                                trades[pokemon_name].append(trade)

                search_pos = deal_close + 1

        return trades

    def extract_farm_wanderers(berry_ts_path, farming_ts_path, pokemon_names):
        berry_text = read_source(berry_ts_path)
        farming_text = read_source(farming_ts_path)

        wanderers = {}

        def add_wanderers(berry_name, names):
            for name in names:
                if name in pokemon_names:
                    wanderers.setdefault(name, []).append(berry_name + " Berry")

        base_match = re.search(
            r"public static baseWander[^=]*=\s*\[(.*?)\];",
            berry_text,
            re.DOTALL,
        )
        base_wanderers = extract_pokemon_names(base_match.group(1)) if base_match else []

        color_wanderers = {}
        color_block = re.search(
            r"public static colorWander[^=]*=\s*\{(.*?)\};",
            berry_text,
            re.DOTALL,
        )
        if color_block:
            for match in re.finditer(
                r"\[BerryColor\.(\w+)\]\s*:\s*\[(.*?)\]",
                color_block.group(1),
                re.DOTALL,
            ):
                color_wanderers[match.group(1)] = extract_pokemon_names(match.group(2))

        search_pos = 0
        while True:
            berry_start = farming_text.find("new Berry(", search_pos)
            if berry_start == -1:
                break

            open_paren = farming_text.find("(", berry_start)
            args_text, close_paren = extract_matching(farming_text, open_paren, "(", ")")
            if close_paren == -1:
                break

            args = split_top_level(args_text)
            if len(args) >= 10:
                berry_match = re.match(r"BerryType\.(\w+)", args[0].strip())
                color_match = re.match(r"BerryColor\.(\w+)", args[8].strip())
                if berry_match:
                    berry_name = humanize_underscore(berry_match.group(1))
                    add_wanderers(berry_name, base_wanderers)
                    if color_match:
                        add_wanderers(berry_name, color_wanderers.get(color_match.group(1), []))

                    if len(args) >= 14:
                        optional_wanderers = args[13].strip()
                        if optional_wanderers.startswith("[") and optional_wanderers.endswith("]"):
                            add_wanderers(berry_name, extract_pokemon_names(optional_wanderers))

            search_pos = close_paren + 1

        return wanderers

    def extract_shop_pokemon(town_list_ts_path, item_list_ts_path, pokemon_names):
        town_text = read_source(town_list_ts_path)
        item_text = read_source(item_list_ts_path)

        item_data = {}
        item_marker = re.compile(r"ItemList(?:\[['\"]((?:\\'|[^'\"])+)['\"]\]|\.(\w+))\s*=\s*new\s+PokemonItem\(")
        for match in item_marker.finditer(item_text):
            item_key = (match.group(1) or match.group(2)).replace("\\'", "'")
            args_text, close_paren = extract_matching(item_text, match.end() - 1, "(", ")")
            if close_paren == -1:
                continue

            args = split_top_level(args_text)
            if not args:
                continue

            pokemon_match = re.match(r"['\"]((?:\\'|[^'\"])+)['\"]", args[0].strip())
            if not pokemon_match:
                continue

            currency = "questPoint"
            if len(args) > 2:
                currency_match = re.match(r"Currency\.(\w+)", args[2].strip())
                if currency_match:
                    currency = currency_match.group(1)

            item_data[item_key] = {
                "pokemon": pokemon_match.group(1).replace("\\'", "'"),
                "currency": currency,
            }

        shop_items = {}
        shop_marker = re.compile(r"(?:const|let)\s+(\w+)\s*=\s*new\s+Shop\(")
        for match in shop_marker.finditer(town_text):
            args_text, close_paren = extract_matching(town_text, match.end() - 1, "(", ")")
            if close_paren == -1:
                continue

            shop_items[match.group(1)] = re.findall(
                r"ItemList(?:\[['\"]((?:\\'|[^'\"])+)['\"]\]|\.(\w+))",
                args_text,
            )

        shops_by_town = {}
        town_marker = re.compile(r"TownList\[['\"]((?:\\'|[^'\"])+)['\"]\]\s*=\s*new\s+(Dungeon)?Town\(")
        for match in town_marker.finditer(town_text):
            args_text, close_paren = extract_matching(town_text, match.end() - 1, "(", ")")
            if close_paren == -1:
                continue

            town_name = match.group(1).replace("\\'", "'")
            args = split_top_level(args_text)
            content_index = 4 if match.group(2) else 3
            if len(args) <= content_index:
                continue

            for shop_name, items in shop_items.items():
                if re.search(rf"\b{re.escape(shop_name)}\b", args[content_index]):
                    shops_by_town.setdefault(town_name, []).extend(items)

        shops = {}
        for town_name, item_refs in shops_by_town.items():
            for bracket_name, property_name in item_refs:
                item_key = (bracket_name or property_name).replace("\\'", "'")
                data = item_data.get(item_key)
                if data and data["pokemon"] in pokemon_names:
                    shops.setdefault(data["pokemon"], []).append((functionify(town_name), data["currency"]))

        return shops

    def extract_gem_shop_pokemon(gem_deal_ts_path, town_list_ts_path, item_list_ts_path, pokemon_names):
        gem_deal_text = read_source(gem_deal_ts_path)
        town_text = read_source(town_list_ts_path)
        item_text = read_source(item_list_ts_path)

        item_pokemon = {}
        for match in re.finditer(
            r"ItemList(?:\[['\"]((?:\\'|[^'\"])+)['\"]\]|\.(\w+))\s*=\s*new\s+PokemonItem\(\s*['\"]((?:\\'|[^'\"])+)['\"]",
            item_text,
        ):
            item_key = (match.group(1) or match.group(2)).replace("\\'", "'")
            item_pokemon[item_key] = match.group(3).replace("\\'", "'")

        deals_by_shop = {}
        shop_marker = re.compile(r"const\s+(\w+)\s*=\s*\[")
        for match in shop_marker.finditer(gem_deal_text):
            shop_name = match.group(1)
            body, _ = extract_matching(gem_deal_text, gem_deal_text.find("[", match.start()), "[", "]")
            deals = []
            for deal in re.finditer(r"new\s+GemDeal\(\s*\[(.*?)\]\s*,\s*ItemList(?:\.([\w]+)|\[['\"]((?:\\'|[^'\"])+)['\"]\])", body, re.DOTALL):
                costs = re.findall(r"gemType:\s*PokemonType\.(\w+)", deal.group(1))
                item_key = (deal.group(3) or deal.group(2)).replace("\\'", "'")
                item_name = item_pokemon.get(item_key)
                if costs and item_name in pokemon_names:
                    deals.append((item_name, humanize_underscore(costs[0]) + " Gems"))
            deals_by_shop[shop_name] = deals

        deals_by_gem_shop = {
            match.group(1): deals_by_shop.get(match.group(2), [])
            for match in re.finditer(
                r"\[GemShops\.(\w+)\]\s*:\s*ko\.observableArray\((\w+)\)",
                gem_deal_text,
            )
        }

        gem_shop_variables = {
            match.group(1): match.group(2)
            for match in re.finditer(
                r"const\s+(\w+)\s*=\s*new\s+GemMasterShop\(\s*GameConstants\.GemShops\.(\w+)",
                town_text,
            )
        }

        shops = {}
        town_marker = re.compile(r"TownList\[['\"]((?:\\'|[^'\"])+)['\"]\]\s*=\s*new\s+(?:Dungeon)?Town\(")
        for match in town_marker.finditer(town_text):
            town_name = match.group(1).replace("\\'", "'")
            town_block, _ = extract_matching(town_text, match.end() - 1, "(", ")")

            shop_names = [gem_shop_variables[name] for name in gem_shop_variables if re.search(rf"\b{re.escape(name)}\b", town_block)]
            shop_names.extend(re.findall(r"new\s+GemMasterShop\(\s*GameConstants\.GemShops\.(\w+)", town_block))
            for shop_name in shop_names:
                deals = deals_by_gem_shop.get(shop_name, [])
                for pokemon_name, currency in deals:
                    shops.setdefault(pokemon_name, []).append((functionify(town_name), currency))

        return shops

    def extract_safari_pokemon(safari_item_ts_path, pokemon_names):
        text = read_source(safari_item_ts_path)

        item_text = read_source(ITEM_LIST_PATH)
        pokemon_item_names = set(pokemon_names)
        for item_match in re.finditer(
            r"new\s+PokemonItem\(\s*['\"]((?:\\'|[^'\"])+)['\"]",
            item_text,
        ):
            pokemon_item_names.add(item_match.group(1).replace("\\'", "'"))

        safari = {}
        region_pattern = re.compile(
            r"\[GameConstants\.Region\.(\w+)\]\s*:\s*\["
        )
        for match in region_pattern.finditer(text):
            open_bracket = text.rfind("[", match.start(), match.end())
            region_content, _ = extract_matching(text, open_bracket, "[", "]")
            region_name = humanize_underscore(match.group(1))

            for item_match in re.finditer(r"item\s*:\s*\{([^{}]*)\}", region_content):
                item_data = item_match.group(1)
                id_match = re.search(r"id\s*:\s*['\"]((?:\\'|[^'\"])+)['\"]", item_data)
                if not id_match or not re.search(r"type\s*:\s*ItemType\.item\b", item_data):
                    continue

                pokemon_name = id_match.group(1).replace("\\'", "'")
                if pokemon_name in pokemon_item_names:
                    item_start = region_content.rfind("{", 0, item_match.start())
                    item_entry, _ = extract_matching(region_content, item_start, "{", "}")
                    required_match = re.search(
                        r"new\s+ObtainedPokemonRequirement\(\s*['\"]((?:\\'|[^'\"])+)['\"]",
                        item_entry,
                    )
                    required_pokemon = required_match.group(1).replace("\\'", "'") if required_match else True
                    region = (region_name, required_pokemon)
                    safari.setdefault(pokemon_name, [])
                    if region not in safari[pokemon_name]:
                        safari[pokemon_name].append(region)

        return safari

    def extract_safari_encounters(safari_pokemon_ts_path, pokemon_names):
        text = read_source(safari_pokemon_ts_path)

        encounters = {}
        method_regions = {
            "generateKantoSafariList": "Kanto",
            "generateJohtoSafariList": "Johto",
            "generateSinnohSafariList": "Sinnoh",
            "generateKalosSafariList": "Kalos",
            "generateAlolaSafariList": "Alola",
        }

        for method, region_name in method_regions.items():
            method_match = re.search(
                rf"(?:private|public)\s+static\s+{method}\(\)",
                text,
            )
            if not method_match:
                continue

            method_start = method_match.start()
            body_start = text.find("{", method_start)
            body, _ = extract_matching(text, body_start, "{", "}")
            for match in re.finditer(r"new\s+SafariEncounter\s*\(", body):
                encounter_args_text, encounter_close = extract_matching(body, match.end() - 1, "(", ")")
                if encounter_close == -1:
                    continue

                encounter_args = split_top_level(encounter_args_text)
                if not encounter_args:
                    continue

                pokemon_name = strip_quotes(encounter_args[0])
                if pokemon_name in pokemon_names:
                    requirement_expression = encounter_args[3].strip() if len(encounter_args) > 3 else ""
                    requires_pokemon = requirement_expression == "true"
                    requirements = []
                    if requirement_expression and not requires_pokemon and requirement_expression != "undefined":
                        requirements = [
                            {
                                "type": call["type"],
                                "args": [format_requirement_arg(arg) for arg in call["args"]],
                            }
                            for call in extract_requirement_calls(requirement_expression)
                            if call["type"] not in ("MultiRequirement", "OneFromManyRequirement")
                        ]
                    encounters.setdefault(pokemon_name, [])
                    encounter = (region_name, requires_pokemon, requirements)
                    if encounter not in encounters[pokemon_name]:
                        encounters[pokemon_name].append(encounter)

        return encounters

    def extract_egg_types(breeding_ts_path, pokemon_names):
        text = read_source(breeding_ts_path)

        hatch_list_match = re.search(r"hatchList[^=]*=\s*\{", text)
        if not hatch_list_match:
            return {}

        object_open = text.find("{", hatch_list_match.start())
        hatch_list_text, _ = extract_matching(text, object_open, "{", "}")
        egg_types = {}

        for match in re.finditer(r"\[GameConstants\.EggItemType\.(\w+)\]\s*:\s*\[", hatch_list_text):
            array_open = hatch_list_text.rfind("[", match.start(), match.end())
            array_text, _ = extract_matching(hatch_list_text, array_open, "[", "]")
            egg_name = humanize_underscore(match.group(1))
            for pokemon_name in extract_pokemon_names(array_text):
                if pokemon_name in pokemon_names:
                    egg_types.setdefault(pokemon_name, [])
                    if egg_name not in egg_types[pokemon_name]:
                        egg_types[pokemon_name].append(egg_name)

        return egg_types

    def extract_pokemon_gifts(town_list_ts_path):
        text = read_source(town_list_ts_path)
        gifts = {}
        gift_marker = re.compile(r"const\s+(\w+)\s*=\s*new\s+PokemonGiftNPC\(")

        for match in gift_marker.finditer(text):
            args_text, close_paren = extract_matching(text, match.end() - 1, "(", ")")
            if close_paren == -1:
                continue

            args = split_top_level(args_text)
            if len(args) < 3:
                continue

            gift_pokemon = strip_quotes(args[2])
            gift_requirements = []

            def add_gift_requirements(expression):
                for call in extract_requirement_calls(expression):
                    if call["type"] == "MultiRequirement":
                        for arg in call["args"]:
                            add_gift_requirements(arg)
                        continue

                    gift_requirements.append({
                        "type": call["type"],
                        "args": [format_requirement_arg(arg) for arg in call["args"]],
                    })

            if len(args) > 4:
                requirement_match = re.search(
                    r"\brequirement\s*:\s*new\s+(\w+Requirement)\s*\(",
                    args[4],
                )
                if requirement_match:
                    requirement_expression = args[4][requirement_match.start():]
                    add_gift_requirements(requirement_expression)

            gifts[match.group(1)] = {
                "pokemon": gift_pokemon,
                "requirements": gift_requirements,
            }

        specials = {}
        town_marker = re.compile(
            r"TownList(?:\[['\"]((?:\\'|[^'])*)['\"]\]|\.(\w+))"
            r"\s*=\s*new\s+(?:Dungeon)?Town\("
        )
        for match in town_marker.finditer(text):
            args_text, close_paren = extract_matching(text, match.end() - 1, "(", ")")
            if close_paren == -1:
                continue

            town_args = split_top_level(args_text)
            town_name = strip_quotes(town_args[0]) if town_args else (match.group(1) or match.group(2))
            npc_match = re.search(r"\bnpcs\s*:\s*\[", args_text)
            if not npc_match:
                continue

            npc_open = args_text.find("[", npc_match.start())
            npc_text, _ = extract_matching(args_text, npc_open, "[", "]")
            for npc in split_top_level(npc_text):
                gift = gifts.get(npc.strip())
                if not gift:
                    continue

                specials.setdefault(gift["pokemon"], []).append({
                    "route": functionify(town_name).strip("_"),
                    "requirements": gift["requirements"],
                    "gift": True,
                })

        return specials

    def temporary_battle_function(battle_name):
        return re.sub(r"_(?=\d)", "", functionify(battle_name))

    def extract_temporary_battle_rewards(temporary_battle_ts_path, pokemon_names):
        text = read_source(temporary_battle_ts_path)
        rewards = {}
        marker = "new TemporaryBattle("
        search_pos = 0

        while True:
            battle_start = text.find(marker, search_pos)
            if battle_start == -1:
                break

            battle_open = battle_start + len(marker) - 1
            args_text, battle_close = extract_matching(text, battle_open, "(", ")")
            if battle_close == -1:
                break

            args = split_top_level(args_text)
            if len(args) > 5:
                battle_name = strip_quotes(args[0])
                battle_function = temporary_battle_function(battle_name)
                for match in re.finditer(
                    r"gainPokemonByName\(\s*'((?:\\'|[^'])*)'",
                    args[5],
                ):
                    pokemon_name = match.group(1).replace("\\'", "'")
                    if pokemon_name in pokemon_names:
                        rewards.setdefault(pokemon_name, [])
                        if battle_function not in rewards[pokemon_name]:
                            rewards[pokemon_name].append(battle_function)

            search_pos = battle_close + 1

        return rewards

    def extract_temporary_battle_pokemon(temporary_battle_ts_path, pokemon_names):
        text = read_source(temporary_battle_ts_path)
        pokemon_battles = {}
        marker = "new TemporaryBattle("
        quest_step_pattern = re.compile(
            r"new\s+QuestLineStepCompletedRequirement\(\s*'((?:\\'|[^'])*)'\s*,\s*(\d+)"
        )
        search_pos = 0

        while True:
            battle_start = text.find(marker, search_pos)
            if battle_start == -1:
                break

            battle_open = battle_start + len(marker) - 1
            args_text, battle_close = extract_matching(text, battle_open, "(", ")")
            if battle_close == -1:
                break

            args = split_top_level(args_text)
            if len(args) > 5 and re.search(r"\bisTrainerBattle\s*:\s*false\b", args[5]):
                battle_function = temporary_battle_function(strip_quotes(args[0]))
                battle_requirements = args[3] if len(args) > 3 else ""
                complete_requirements = args[4] if len(args) > 4 else ""
                required_quest_steps = {
                    (match.group(1).replace("\\'", "'"), int(match.group(2)))
                    for match in quest_step_pattern.finditer(battle_requirements)
                }
                completed_quest_steps = {
                    (match.group(1).replace("\\'", "'"), int(match.group(2)))
                    for match in quest_step_pattern.finditer(complete_requirements)
                }
                caught_pokemon = {
                    match.group(1).replace("\\'", "'")
                    for match in re.finditer(
                        r"new\s+StatisticRequirement\(\s*\[\s*['\"]pokemonCaptured['\"]\s*,\s*PokemonHelper\.getPokemonByName\(\s*['\"]((?:\\'|[^'\"])+)['\"]\s*\)\.id\s*\]\s*,\s*(\d+)",
                        complete_requirements,
                    )
                    if int(match.group(2)) > 0
                }
                for match in re.finditer(
                    r"new\s+GymPokemon\(\s*'((?:\\'|[^'])*)'",
                    args[1],
                ):
                    name = match.group(1).replace("\\'", "'")
                    if name not in pokemon_names:
                        continue

                    catches_pokemon = any(
                        obtained.group(1).replace("\\'", "'") == name
                        for obtained in re.finditer(
                            r"new\s+ObtainedPokemonRequirement\(\s*'((?:\\'|[^'])*)'",
                            complete_requirements,
                        )
                    ) or name in caught_pokemon
                    completes_next_quest_step = any(
                        required_quest == completed_quest and completed_step == required_step + 1
                        for required_quest, required_step in required_quest_steps
                        for completed_quest, completed_step in completed_quest_steps
                    )
                    if catches_pokemon or completes_next_quest_step:
                        pokemon_battles.setdefault(name, [])
                        if battle_function not in pokemon_battles[name]:
                            pokemon_battles[name].append(battle_function)

            search_pos = battle_close + 1

        return pokemon_battles

    def extract_reward_pokemon(source_path, pokemon_names):
        text = read_source(source_path)
        return {
            match.group(1).replace("\\'", "'")
            for match in re.finditer(
                r"gainPokemonByName\(\s*'((?:\\'|[^'])*)'",
                text,
            )
            if match.group(1).replace("\\'", "'") in pokemon_names
        }

    def extract_questline_pokemon_rewards(questline_helper_path, pokemon_names):
        text = read_source(questline_helper_path)
        reward_functions = {}
        reward_marker = re.compile(r"(?:const|let)\s+(\w+)\s*=\s*\(\s*\)\s*=>\s*\{")

        for match in reward_marker.finditer(text):
            reward_body, reward_end = extract_matching(text, match.end() - 1, "{", "}")
            if reward_end == -1:
                continue

            pokemon_names_in_reward = [
                reward_match.group(1).replace("\\'", "'")
                for reward_match in re.finditer(
                    r"gainPokemonByName\(\s*'((?:\\'|[^'])*)'",
                    reward_body,
                )
                if reward_match.group(1).replace("\\'", "'") in pokemon_names
            ]
            if pokemon_names_in_reward:
                reward_functions[match.group(1)] = pokemon_names_in_reward

        quest_rewards = {}
        questline_marker = re.compile(
            r"const\s+(\w+)\s*=\s*new\s+QuestLine\(\s*'((?:\\'|[^'])*)'"
        )
        for match in questline_marker.finditer(text):
            questline_variable = match.group(1)
            questline_name = match.group(2).replace("\\'", "'")
            questline_function = re.sub(
                r"[^a-z0-9]+",
                "_",
                questline_name.lower().replace("'", ""),
            ).strip("_")

            method_start = text.rfind("public static ", 0, match.start())
            method_open = text.find("{", method_start)
            method_body, method_end = extract_matching(text, method_open, "{", "}")
            if method_end == -1:
                continue

            add_marker = re.compile(rf"\b{re.escape(questline_variable)}\.addQuest\s*\(")
            quest_calls = []
            for add_match in add_marker.finditer(method_body):
                quest_args, quest_close = extract_matching(method_body, add_match.end() - 1, "(", ")")
                if quest_close != -1:
                    quest_calls.append(quest_args)

            for step, quest_args in enumerate(quest_calls):
                reward_refs = re.findall(r"\.withCustomReward\(\s*(\w+)\s*\)", quest_args)
                quest_variable_match = re.fullmatch(r"\s*(\w+)\s*", quest_args)
                if quest_variable_match:
                    quest_variable = re.escape(quest_variable_match.group(1))
                    reward_declaration = re.search(
                        rf"\bconst\s+{quest_variable}\s*=\s*[^;]*?\.withCustomReward\(\s*(\w+)\s*\)[^;]*;",
                        method_body,
                        re.DOTALL,
                    )
                    if reward_declaration:
                        reward_refs.append(reward_declaration.group(1))

                for reward_ref in reward_refs:
                    for pokemon_name in reward_functions.get(reward_ref, []):
                        function_name = (
                            f"completed_{questline_function}"
                            if step == len(quest_calls) - 1
                            else f"{questline_function}{step}"
                        )
                        quest_rewards.setdefault(pokemon_name, [])
                        if function_name not in quest_rewards[pokemon_name]:
                            quest_rewards[pokemon_name].append(function_name)

        return quest_rewards

    # Read the pokemon list order and evolution info directly from PokemonList.ts
    POKEMON_ORDER = extract_pokemon_order(POKEMON_PATH)
    POKEMON_IDS = extract_pokemon_id_map(POKEMON_PATH)
    POKEMON_NATIVE_REGIONS, MAX_AVAILABLE_REGION, POKEMON_REGION_NAMES = extract_pokemon_regions(
        POKEMON_PATH, GAME_CONSTANTS_PATH
    )
    POKEMON_STARTERS = extract_regional_starters(GAME_CONSTANTS_PATH)
    POKEMON_EVOLUTIONS, POKEMON_DUMMY_EVOLUTIONS, STONE_EVOLUTIONS = extract_pokemon_evolutions(POKEMON_PATH)
    BABY_POKEMON = extract_baby_pokemon(POKEMON_PATH)
    DUNGEON_ENCOUNTERS = extract_dungeon_encounters(DUNGEONS_PATH, set(POKEMON_ORDER))
    BATTLE_FRONTIER_POKEMON = extract_battle_frontier_pokemon(BATTLE_FRONTIER_MILESTONES_PATH, set(POKEMON_ORDER))
    ROAMERS = extract_roamers(ROAMING_PATH)
    FARM_WANDERERS = extract_farm_wanderers(BERRY_PATH, FARMING_PATH, set(POKEMON_ORDER))
    BERRY_TRADES = extract_berry_trades(BERRY_DEAL_PATH, set(POKEMON_ORDER))
    SHOPS = extract_shop_pokemon(TOWN_LIST_PATH, ITEM_LIST_PATH, set(POKEMON_ORDER))
    GEM_SHOPS = extract_gem_shop_pokemon(GEM_DEAL_PATH, TOWN_LIST_PATH, ITEM_LIST_PATH, set(POKEMON_ORDER))
    GENERIC_TRADES = extract_generic_trades(GENERIC_DEAL_PATH, TOWN_LIST_PATH, set(POKEMON_ORDER))
    SHARD_TRADES = extract_shard_trades(SHARD_DEAL_PATH, ITEM_LIST_PATH, set(POKEMON_ORDER))
    SAFARI = extract_safari_pokemon(SAFARI_ITEM_PATH, set(POKEMON_ORDER))
    safari_encounters = extract_safari_encounters(SAFARI_POKEMON_PATH, set(POKEMON_ORDER))
    DISCORD_POKEMON = extract_discord_pokemon(DISCORD_PATH, POKEMON_PATH, GAME_CONSTANTS_PATH)
    DREAM_ORB_POKEMON = extract_dream_orb_pokemon(DREAM_ORB_PATH, set(POKEMON_ORDER))
    BATTLE_CAFE_POKEMON = extract_battle_cafe_pokemon(BATTLE_CAFE_PATH, set(POKEMON_ORDER))
    POKEMON_GIFTS = extract_pokemon_gifts(TOWN_LIST_PATH)
    TEMPORARY_BATTLE_REWARDS = extract_temporary_battle_rewards(TEMPORARY_BATTLE_PATH, set(POKEMON_ORDER))
    TEMPORARY_BATTLE_POKEMON = extract_temporary_battle_pokemon(TEMPORARY_BATTLE_PATH, set(POKEMON_ORDER))
    QUESTLINE_POKEMON_REWARDS = extract_questline_pokemon_rewards(QUEST_LINE_HELPER_PATH, set(POKEMON_ORDER))
    GYM_REWARD_POKEMON = extract_reward_pokemon(GYM_LIST_PATH, set(POKEMON_ORDER))
    DUNGEON_REWARD_POKEMON = extract_reward_pokemon(DUNGEONS_PATH, set(POKEMON_ORDER))
    for name, regions in safari_encounters.items():
        for region_name, requires_pokemon, requirements in regions:
            if requirements:
                pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
                safari_special = {
                    "region_safari": region_name,
                    "requirements": requirements,
                }
                if safari_special not in pokemon[name].setdefault("special", []):
                    pokemon[name]["special"].append(safari_special)
                continue

            SAFARI.setdefault(name, [])
            region = (region_name, requires_pokemon)
            if region not in SAFARI[name]:
                SAFARI[name].append(region)
    POKEMON_ORDER.extend(name for name in SAFARI if name not in POKEMON_ORDER)
    EGG_TYPES = extract_egg_types(BREEDING_PATH, set(POKEMON_ORDER))

    text = read_source(ROUTES_PATH)

    # Find every RegionRoute
    route_blocks = extract_region_routes(text)
    routes = {}

    for block in route_blocks:

        # Route name, e.g. new RegionRoute('Alola Route 3', Region.alola, 3,
        route_match = re.search(r"new RegionRoute\(\s*'((?:\\'|[^'])*)'", block)
        if not route_match:
            continue

        route = route_match.group(1).replace("\\'", "'")
        region_match = re.search(r"\bRegion\.(\w+)", block)
        routes[route] = {
            "land": [],
            "water": [],
            "headbutt": [],
            "special": [],
            "weather_land": False,
            "region": region_match.group(1).lower() if region_match else None,
        }

        # Normal land / water / headbutt encounters
        for method in ("land", "water", "headbutt"):
            method_match = re.search(rf"\b{method}\s*:\s*\[", block)
            if not method_match:
                continue

            open_bracket = block.find("[", method_match.start())
            content = extract_bracket_content(block, open_bracket)
            routes[route][method].extend(extract_pokemon_names(content))

        # Day-of-week specials count as land encounters; weather specials remain conditional.
        special_marker = "new SpecialRoutePokemon("
        search_pos = 0

        while True:
            special_start = block.find(special_marker, search_pos)
            if special_start == -1:
                break

            open_paren = block.find("(", special_start)

            # Find the matching closing ')'
            depth = 0
            in_string = False
            escaped = False
            close_paren = None

            for i in range(open_paren, len(block)):
                char = block[i]

                if in_string:
                    if escaped:
                        escaped = False
                    elif char == "\\":
                        escaped = True
                    elif char == "'":
                        in_string = False
                    continue

                if char == "'":
                    in_string = True
                    continue

                if char == "(":
                    depth += 1
                elif char == ")":
                    depth -= 1
                    if depth == 0:
                        close_paren = i
                        break

            if close_paren is None:
                break

            special_block = block[special_start:close_paren + 1]
            pokemon_list_match = re.search(r"new SpecialRoutePokemon\(\s*\[", special_block)

            if pokemon_list_match:
                open_bracket = special_block.find("[", pokemon_list_match.start())
                content = extract_bracket_content(special_block, open_bracket)
                special_pokemon = extract_pokemon_names(content)
                requirement_calls = extract_requirement_calls(special_block)
                requirements = [
                    {
                        "type": call["type"],
                        "args": (
                            [] if call["type"] == "WeatherRequirement"
                            else [format_requirement_arg(arg) for arg in call["args"]]
                        ),
                    }
                    for call in requirement_calls
                    if call["type"] != "DayOfWeekRequirement"
                ]
                is_weather = re.search(r"\bnew\s+WeatherRequirement\s*\(", special_block) is not None
                is_day = any(call["type"] == "DayOfWeekRequirement" for call in requirement_calls)
                routes[route]["weather_land"] |= any(
                    call["type"] == "WeatherRequirement" for call in requirement_calls
                )

                for name in special_pokemon:
                    if is_day and not is_weather and name not in routes[route]["land"]:
                        routes[route]["land"].append(name)

                    if requirements:
                        special = {
                            "name": name,
                            "requirements": requirements,
                        }
                        if not is_weather or special not in routes[route]["special"]:
                            routes[route]["special"].append(special)

            search_pos = close_paren + 1

    # Convert routes into the Pokemon dictionary
    holiday_specials = {
        "kanto": [
            ("Spooky Bulbasaur", "SpecialEventRequirement", "Halloween!"),
            ("Gastly", "SpecialEventRequirement", "Halloween!"),
            (
                "Santa Jynx",
                "SpecialEventRequirement",
                "Merry Christmas!",
                "TemporaryBattleRequirement",
                "Santa Jynx 1",
            ),
        ],
        "johto": [
            ("Spooky Togepi", "SpecialEventRequirement", "Halloween!"),
            ("Misdreavus", "SpecialEventRequirement", "Halloween!"),
        ],
        "hoenn": [
            ("Pikachu (Gengar)", "SpecialEventRequirement", "Halloween!"),
            ("Shuppet", "SpecialEventRequirement", "Halloween!"),
            ("Duskull", "SpecialEventRequirement", "Halloween!"),
        ],
    }

    for route, encounters in routes.items():
        region = route.split(" ", 1)[0].lower()
        for holiday in holiday_specials.get(region, []):
            name, requirement_type, event_name = holiday[:3]
            requirements = [{
                "type": requirement_type,
                "args": [event_name],
            }]
            if len(holiday) > 4:
                requirements.append({
                    "type": holiday[3],
                    "args": [holiday[4]],
                })
            elif len(holiday) > 3:
                requirements.append({
                    "type": "CustomRequirement",
                    "args": [holiday[3]],
                })

            encounters["special"].append({
                "name": name,
                "requirements": requirements,
            })

    for route, encounters in routes.items():
        land = encounters["land"]
        water = encounters["water"]
        headbutt = encounters["headbutt"]
        special = encounters["special"]

        for name in land:
            add_pokemon(name, functionify(route), "land")

        # If the route has land, water stays water; if not, water becomes land.
        if land or encounters["weather_land"]:
            for name in water:
                add_pokemon(name, functionify(route), "water")
        else:
            for name in water:
                add_pokemon(name, functionify(route), "land")

        for name in headbutt:
            add_pokemon(name, functionify(route), "headbutt")

        for encounter in special:
            name = encounter["name"]
            if name not in pokemon:
                pokemon[name] = {"land": [], "water": [], "headbutt": []}

            pokemon[name].setdefault("special", []).append({
                "route": functionify(route),
                "region": encounters["region"],
                "requirements": encounter["requirements"],
            })

    # Merge in evolution info ("prev" + level/item/etc.) so it gets written
    # out even for Pokemon with no route encounters.
    for name, evolutions in POKEMON_EVOLUTIONS.items():
        if name not in pokemon:
            pokemon[name] = {"land": [], "water": [], "headbutt": []}

        pokemon[name]["evolution"] = evolutions

    for baby in BABY_POKEMON:
        breeding = []
        breeding_evolutions = {**POKEMON_EVOLUTIONS, **POKEMON_DUMMY_EVOLUTIONS}
        pending = [
            evolved for evolved, evolutions in breeding_evolutions.items()
            if any(evolution["prev"] == baby for evolution in evolutions)
        ]
        while pending:
            evolved = pending.pop(0)
            if evolved in breeding:
                continue
            breeding.append(evolved)
            pending.extend(
                next_evolved
                for next_evolved, evolutions in breeding_evolutions.items()
                if next_evolved not in breeding
                and next_evolved not in pending
                and any(evolution["prev"] == evolved for evolution in evolutions)
            )

        if breeding:
            pokemon.setdefault(baby, {"land": [], "water": [], "headbutt": []})
            pokemon[baby]["breeding"] = breeding

    for dungeon_name, dungeon_data in DUNGEON_ENCOUNTERS.items():
        for name in dungeon_data["normal"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            if "dungeon" not in pokemon[name]:
                pokemon[name]["dungeon"] = [dungeon_name]
            elif isinstance(pokemon[name]["dungeon"], list) and dungeon_name not in pokemon[name]["dungeon"]:
                pokemon[name]["dungeon"].append(dungeon_name)

        for name, terms, unsupported in dungeon_data["conditional_encounters"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            condition_special = {
                "dungeon_encounter_terms": terms,
                "dungeon_name": dungeon_name,
                "unprocessed_requirements": unsupported,
            }
            if condition_special not in pokemon[name].setdefault("special", []):
                pokemon[name]["special"].append(condition_special)

        for name, attack in dungeon_data["bosses"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            pokemon[name].setdefault("dungeon_boss", []).append((dungeon_name, attack))

        for name, boss_dungeon, attack, event_required, requirement_terms, unsupported in dungeon_data["conditional_bosses"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            boss_special = {
                "dungeon_boss_rule": (boss_dungeon, attack),
                "seasonal_event_requirement": event_required,
                "requirement_terms": requirement_terms,
                "unprocessed_requirements": unsupported,
            }
            if boss_special not in pokemon[name].setdefault("special", []):
                pokemon[name]["special"].append(boss_special)

        for name, quest_rule, dungeon, attack in dungeon_data["vivillon_quest_rules"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            vivillon_special = {
                "vivillon_unowned_quest_rule": (quest_rule, dungeon, attack),
            }
            if vivillon_special not in pokemon[name].setdefault("special", []):
                pokemon[name]["special"].append(vivillon_special)

        for name, terms, unsupported in dungeon_data["conditional_loot"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            loot_special = {
                "dungeon_loot_terms": terms,
                "dungeon_name": dungeon_name,
                "unprocessed_requirements": unsupported,
            }
            if loot_special not in pokemon[name].setdefault("special", []):
                pokemon[name]["special"].append(loot_special)

        for special in dungeon_data["gmax_specials"]:
            name = special.get("unowned", special.get("owned"))
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            if special not in pokemon[name].setdefault("special", []):
                pokemon[name]["special"].append(special)

        for name in dungeon_data["shadow_pokemon"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            pokemon[name].setdefault("shadow_pokemon", []).append(dungeon_name)

        for name in dungeon_data["loot"]:
            pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
            pokemon[name].setdefault("dungeon_chest", []).append(dungeon_name)

    for name, reward in BATTLE_FRONTIER_POKEMON.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        if reward["requirements"]:
            pokemon[name].setdefault("special", []).extend({
                "battle_frontier_stage": stage,
                "requirements": reward["requirements"],
            } for stage in reward["stages"])
        else:
            pokemon[name]["battle_frontier_key"] = reward["stages"]

    for roamer in ROAMERS:
        name = roamer["name"]
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        if roamer["requirements"]:
            pokemon[name].setdefault("special", []).append({
                "roamer": roamer["group"],
                "requirements": [
                    {
                        "type": call["type"],
                        "args": [format_requirement_arg(arg) for arg in call["args"]],
                    }
                    for call in roamer["requirements"]
                ],
            })
        else:
            pokemon[name].setdefault("roamer", []).append(roamer["group"])

    for name, trades in BERRY_TRADES.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name].setdefault("trades", []).extend(trades)

    for name, trades in GENERIC_TRADES.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name].setdefault("trades", []).extend(trades)

    for name, trades in SHARD_TRADES.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name].setdefault("trades", []).extend(trades)

    for name, berries in FARM_WANDERERS.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["farm_wandering"] = berries

    for pokemon_id, regions in POKEMON_STARTERS.items():
        name = POKEMON_IDS.get(pokemon_id)
        if not name:
            continue
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["starter"] = regions

    for name, shops in SHOPS.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["shop"] = shops

    for name, shops in GEM_SHOPS.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name].setdefault("shop", [])
        for shop in shops:
            if shop not in pokemon[name]["shop"]:
                pokemon[name]["shop"].append(shop)

    for name, regions in SAFARI.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        for region in regions:
            if isinstance(region, tuple):
                region_name, requires_pokemon = region
            else:
                region_name, requires_pokemon = region, True
            if requires_pokemon:
                pokemon[name].setdefault("special", []).append({
                    "region_safari": region_name,
                    "requires_pokemon": requires_pokemon,
                })
            else:
                pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
                pokemon[name].setdefault("safari", []).append(region_name)

    for name, egg_types in EGG_TYPES.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["egg"] = egg_types[0] if len(egg_types) == 1 else egg_types

    for name, regions in DISCORD_POKEMON.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["discord"] = regions

    for name, colors in DREAM_ORB_POKEMON.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["dream_orbs"] = colors

    for name, combinations in BATTLE_CAFE_POKEMON.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["battle_cafe"] = combinations

    for name, specials in POKEMON_GIFTS.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name].setdefault("special", []).extend(specials)

    for name, battles in TEMPORARY_BATTLE_REWARDS.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["temporary_battle"] = battles

    for name, battles in TEMPORARY_BATTLE_POKEMON.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name].setdefault("temporary_battle", [])
        for battle in battles:
            if battle not in pokemon[name]["temporary_battle"]:
                pokemon[name]["temporary_battle"].append(battle)

    for name, quest_functions in QUESTLINE_POKEMON_REWARDS.items():
        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name]["quest"] = quest_functions

    obtainable_friend_safari_pokemon = (
        set(POKEMON_EVOLUTIONS)
        | set(BABY_POKEMON)
        | set(EGG_TYPES)
        | set(BATTLE_FRONTIER_POKEMON)
        | set(DISCORD_POKEMON)
        | set(POKEMON_GIFTS)
        | set(TEMPORARY_BATTLE_REWARDS)
        | set(TEMPORARY_BATTLE_POKEMON)
        | GYM_REWARD_POKEMON
        | DUNGEON_REWARD_POKEMON
        | set(QUESTLINE_POKEMON_REWARDS)
    )

    friend_safari_evolvable_fields = (
        "land", "water", "headbutt", "dungeon", "dungeon_boss", "dungeon_chest",
        "shadow_pokemon", "roamer", "routes", "safari", "shop", "trades",
        "farm_wandering", "dream_orbs", "battle_cafe",
    )
    fixed_kalos_safari_pokemon = {
        name
        for name, encounters in safari_encounters.items()
        if any(
            (region[0] if isinstance(region, tuple) else region) == "Kalos"
            for region in encounters
        )
    }

    for name in POKEMON_ORDER:
        if name not in obtainable_friend_safari_pokemon:
            continue
        if POKEMON_NATIVE_REGIONS.get(name, -1) > MAX_AVAILABLE_REGION:
            continue
        if name in fixed_kalos_safari_pokemon or name in STONE_EVOLUTIONS:
            continue

        data = pokemon.get(name, {})
        if any(data.get(field) for field in friend_safari_evolvable_fields):
            continue

        specials = data.get("special", [])
        if any(
            "region_safari" in special
            or "roamer" in special
            or "dungeon_boss_rule" in special
            or ("route" in special and not special.get("gift"))
            for special in specials
        ):
            continue

        pokemon.setdefault(name, {"land": [], "water": [], "headbutt": []})
        pokemon[name].setdefault("special", []).append({
            "region_safari": "Kalos",
            "requires_pokemon": True,
        })

    empty_pokemon = [
        name for name in POKEMON_ORDER
        if not pokemon.get(name) or not any(pokemon[name].values())
    ]
    print(f"Empty Pokemon ({len(empty_pokemon)}):")
    for name in empty_pokemon:
        print(f"- {name}")

    # Order in which metadata fields are printed, if present.
    EVOLUTION_FIELDS = (
        "dungeon", "dungeon_boss", "dungeon_chest", "evolution", "egg",
        "starter", "safari", "farm_wandering", "trades", "shadow_pokemon", "friend_safari",
        "shop", "dream_orbs", "quest", "discord", "battle_cafe", "temporary_battle",
        "battle_frontier_key", "breeding", "roamer",
    )
    EVOLUTION_METADATA_FIELDS = (
        "prev", "level", "item", "time", "region", "environment", "weather",
        "dayCyclePart", "questline", "dungeon_evolution", "attack", "attackIsPercent",
    )

    # Write output as a dictionary literal, keyed by Pokemon name in POKEMON_ORDER
    def quoted(value):
        return "'" + str(value).replace("'", "\\'") + "'"

    def write_evolution_dictionary(evolutions, output):
        if not evolutions:
            return

        print("        evolution: [", file=output)
        for evolution in evolutions:
            print("            {", file=output)
            for field in EVOLUTION_METADATA_FIELDS:
                if field not in evolution:
                    continue

                value = evolution[field]
                if field == "dungeon_evolution":
                    value = quoted(functionify(value))
                elif field == "level":
                    value = str(int(value))
                elif isinstance(value, list):
                    value = "[" + ", ".join(quoted(item) for item in value) + "]"
                else:
                    value = quoted(value)
                print(f"                {field}: {value},", file=output)
            print("            },", file=output)
        print("        ],", file=output)

    def write_requirement_dictionary(output, requirements, route=None, dungeon=None, rule=None):
        def format_argument(value):
            if isinstance(value, list):
                return "[" + ", ".join(format_argument(item) for item in value) + "]"
            if isinstance(value, str):
                return quoted(value)
            return str(value)

        print("            {", file=output)
        if route is not None:
            print(f"                route: {quoted(route)},", file=output)
        if dungeon is not None:
            print(f"                dungeon: {quoted(dungeon)},", file=output)
        if rule is not None:
            print(f"                rule: {rule},", file=output)
        print("                requirements: [", file=output)
        for requirement in requirements:
            print("                    {", file=output)
            print(f"                        type: {quoted(requirement['type'])},", file=output)
            print("                        args: [", file=output)
            for arg in requirement["args"]:
                print(f"                            {format_argument(arg)},", file=output)
            print("                        ],", file=output)
            print("                    },", file=output)
        print("                ],", file=output)
        print("            },", file=output)

    def order_special_terms(terms):
        def priority(term):
            if term.startswith("Has(") or term.startswith("not Has("):
                return 0
            if term.startswith("make_rule(has_script,"):
                return 1
            return 2

        return sorted(terms, key=priority)

    def roamer_requirement_term(requirement):
        requirement_type = requirement["type"]
        args = requirement["args"]

        if requirement_type == "SpecialEventRequirement":
            return 'make_rule(has_script, "Infinite Seasonal Events Script")'

        if requirement_type == "WeatherRequirement":
            return 'make_rule(has_script, "Simple Weather Changer Script")'

        if requirement_type == "ClearDungeonRequirement" and len(args) > 1:
            dungeon_match = re.search(
                r"getDungeonIndex\(\s*'((?:\\'|[^'])*)'\s*\)",
                str(args[1]),
            )
            if dungeon_match:
                return f"make_rule({functionify(dungeon_match.group(1).replace(chr(92) + chr(39), chr(39)))}, True)"

        if requirement_type == "MultiRequirement":
            terms = []
            for arg in args:
                if not isinstance(arg, list):
                    continue

                for nested in arg:
                    event_match = re.search(
                        r"new\s+SpecialEventRequirement\(\s*'((?:\\'|[^'])*)'",
                        nested,
                    )
                    dungeon_match = re.search(
                        r"new\s+ClearDungeonRequirement\(\s*\d+\s*,\s*getDungeonIndex\(\s*'((?:\\'|[^'])*)'\s*\)",
                        nested,
                    )
                    if event_match:
                        terms.append('make_rule(has_script, "Infinite Seasonal Events Script")')
                    elif dungeon_match:
                        dungeon_name = dungeon_match.group(1).replace(chr(92) + chr(39), chr(39))
                        terms.append(f"make_rule({functionify(dungeon_name)}, True)")

            if terms:
                return " & ".join(terms)

        return None

    def roamer_requirement_terms(requirements):
        terms = []

        for requirement in requirements:
            requirement_type = requirement["type"]
            args = requirement["args"]

            if requirement_type == "MultiRequirement":
                for arg in args:
                    if not isinstance(arg, list):
                        continue

                    for nested in arg:
                        nested_calls = extract_requirement_calls(nested)
                        if not nested_calls:
                            continue

                        nested_call = nested_calls[0]
                        terms.extend(roamer_requirement_terms([{
                            "type": nested_call["type"],
                            "args": [
                                format_requirement_arg(value)
                                for value in nested_call["args"]
                            ],
                        }]))
                continue

            term = roamer_requirement_term(requirement)

            if term:
                terms.append(term)
            elif requirement_type == "ObtainedPokemonRequirement" and args:
                terms.append(f"Has({quoted(args[0])})")
            elif requirement_type == "GymBadgeRequirement" and args:
                terms.append(f"Has({quoted(badge_name(args[0]))})")
            elif requirement_type == "QuestLineStepCompletedRequirement" and len(args) > 1:
                terms.append(f"make_rule({quest_rule_name(args[0], args[1])})")
            elif requirement_type == "QuestLineCompletedRequirement" and args:
                terms.append(f"make_rule({completed_quest_rule_name(args[0])})")
            elif requirement_type == "TemporaryBattleRequirement" and args:
                battle_name = re.sub(r"_(?=\d)", "", functionify(args[0]))
                terms.append(f"make_rule({battle_name})")
            elif requirement_type == "CaughtUniquePokemonByFilterRequirement" and len(args) > 2:
                pokemon_match = re.search(r"pokemonMap\.([A-Za-z0-9_]+)\.id", str(args[0]))
                amount = str(args[2]).strip()
                if pokemon_match and re.fullmatch(r"\d+", amount):
                    terms.append(f"HasGroupUnique({quoted(pokemon_match.group(1))}, {amount})")

        return terms

    def quest_rule_name(quest, step):
        quest_name = re.sub(r"[^a-z0-9]+", "_", quest.lower().replace("'", "")).strip("_")
        return f"{quest_name}{step}"

    def completed_quest_rule_name(quest):
        return f"completed_{quest_rule_name(quest, '')}"

    def omitted_level_pokemon(special):
        for requirement in special["requirements"]:
            if requirement["type"] != "CustomRequirement":
                continue

            for arg in requirement["args"]:
                if not isinstance(arg, str):
                    continue

                if "below level" not in arg.lower() and "level below" not in arg.lower():
                    continue

                pokemon_match = re.search(
                    r"(?:Have|Hatch)\s+([A-Za-z0-9()' -]+?)\s+(?:newly|at level|and at level)",
                    arg,
                )
                if pokemon_match:
                    return pokemon_match.group(1)

        return None

    def special_has_terms(special):
        terms = []
        quest_terms = []

        for requirement in special["requirements"]:
            if requirement["type"] == "ObtainedPokemonRequirement":
                terms.append(f"Has({quoted(requirement['args'][0])})")
            elif requirement["type"] == "GymBadgeRequirement":
                terms.append(f"Has({quoted(badge_name(requirement['args'][0]))})")
            elif requirement["type"] == "QuestLineStepCompletedRequirement":
                quest, step = requirement["args"][:2]
                quest_terms.extend([
                    f"make_rule({special['route']})",
                    f"make_rule({quest_rule_name(quest, step)})",
                ])
            elif requirement["type"] == "QuestLineCompletedRequirement" and requirement["args"]:
                terms.append(f"make_rule({completed_quest_rule_name(requirement['args'][0])})")
            elif requirement["type"] == "TemporaryBattleRequirement" and requirement["args"]:
                battle_name = re.sub(r"_(?=\d)", "", functionify(requirement["args"][0]))
                terms.append(f"make_rule({battle_name})")
            elif requirement["type"] in (
                "SpecialEventRequirement",
                "SpecialEventRandomRequirement",
            ):
                terms.append('make_rule(has_script, "Infinite Seasonal Events Script")')
            elif requirement["type"] == "WeatherRequirement":
                weather_term = 'make_rule(has_script, "Simple Weather Changer Script")'
                if weather_term not in terms:
                    terms.append(weather_term)
            elif requirement["type"] == "CustomRequirement":
                pokemon_name = omitted_level_pokemon(special)
                if pokemon_name:
                    # Level restrictions are intentionally omitted for these rules.
                    terms.append(f"Has({quoted(pokemon_name)})")
            elif requirement["type"] == "MultiRequirement":
                for arg in requirement["args"]:
                    if not isinstance(arg, list):
                        continue

                    for nested in arg:
                        obtained = re.search(
                            r"ObtainedPokemonRequirement\(\s*'((?:\\'|[^'])*)'",
                            nested
                        )
                        badge = re.search(r"GymBadgeRequirement\(\s*([^\)]+)", nested)
                        event = re.search(
                            r"SpecialEvent(?:Random)?Requirement\(\s*'((?:\\'|[^'])*)'",
                            nested,
                        )

                        if obtained:
                            terms.append(f"Has({quoted(obtained.group(1).replace(chr(92) + chr(39), chr(39)))})")
                        elif badge:
                            terms.append(f"Has({quoted(badge_name(badge.group(1).strip()))})")
                        elif event:
                            terms.append('make_rule(has_script, "Infinite Seasonal Events Script")')

                        if re.search(r"\bnew\s+WeatherRequirement\s*\(", nested):
                            weather_term = 'make_rule(has_script, "Simple Weather Changer Script")'
                            if weather_term not in terms:
                                terms.append(weather_term)

        return quest_terms + terms, bool(quest_terms)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        print("from .rules import *", file=f)
        print("from rule_builder.rules import Has, HasGroupUnique", file=f)

        print("""
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
""", file=f)
        
        print("POKEMON_RULES = {", file=f)

        for name in POKEMON_ORDER:

            if pokemon.get(name):
                print(f"    {quoted(name)}: {{", file=f)
                native_region = POKEMON_REGION_NAMES.get(POKEMON_NATIVE_REGIONS.get(name))
                if native_region:
                    print(f"        native_region: '{native_region}',", file=f)

                if pokemon[name]["land"] or pokemon[name]["water"] or pokemon[name]["headbutt"]:
                    print("        routes: {", file=f)
                    if pokemon[name]["land"]:
                        print("            land: [", file=f)
                        for route in pokemon[name]["land"]:
                            print(f"                {quoted(route)},", file=f)
                        print("            ],", file=f)

                    if pokemon[name]["water"]:
                        print("            water: [", file=f)
                        for route in pokemon[name]["water"]:
                            print(f"                {quoted(route)},", file=f)
                        print("            ],", file=f)

                    if pokemon[name]["headbutt"]:
                        print("            headbutt: [", file=f)
                        for route in pokemon[name]["headbutt"]:
                            print(f"                {quoted(route)},", file=f)
                        print("            ],", file=f)
                    print("        },", file=f)

                for field in EVOLUTION_FIELDS:
                    if field == "evolution":
                        if field in pokemon[name]:
                            write_evolution_dictionary(pokemon[name][field], f)
                        continue

                    if field in pokemon[name]:
                        value = pokemon[name][field]
                        output_field = "dungeons" if field == "dungeon" else field

                        if field == "dungeon_chest":
                            dungeon_locations = pokemon[name].get("dungeon", [])
                            if not isinstance(dungeon_locations, list):
                                dungeon_locations = [dungeon_locations]
                            value = [
                                dungeon for dungeon in value
                                if dungeon not in dungeon_locations
                            ]
                            if not value:
                                continue

                        if field in ("dungeon", "dungeon_boss", "dungeon_chest", "shadow_pokemon") and isinstance(value, list):
                            print(f"        {output_field}: [", file=f)
                            if field == "dungeon_boss":
                                values = [
                                    "(" + quoted(functionify(dungeon)) + ", " + attack + ")"
                                    for dungeon, attack in value
                                ]
                            else:
                                values = [quoted(functionify(dungeon)) for dungeon in value]

                            for item in values:
                                print(f"            {item},", file=f)
                            print("        ],", file=f)
                            continue

                        if field == "battle_frontier_key" and isinstance(value, list):
                            print(f"        {field}: [", file=f)
                            for stage in value:
                                print(f"            {stage},", file=f)
                            print("        ],", file=f)
                            continue

                        if field == "roamer" and isinstance(value, list):
                            print(f"        {field}: [", file=f)
                            for group in value:
                                print(f"            {quoted(group)},", file=f)
                            print("        ],", file=f)
                            continue

                        if field == "temporary_battle" and isinstance(value, list):
                            print(f"        {field}: [", file=f)
                            for battle in value:
                                print(f"            {quoted(battle)},", file=f)
                            print("        ],", file=f)
                            continue

                        if field == "quest" and isinstance(value, list):
                            print(f"        quest_rewards: [", file=f)
                            for quest in value:
                                print(f"            {quoted(quest)},", file=f)
                            print("        ],", file=f)
                            continue

                        if field == "battle_cafe" and isinstance(value, list):
                            print(f"        {field}: [", file=f)
                            for spin_time, direction, time_of_day in value:
                                print(
                                    f"            ({spin_time}, {quoted(direction)}, {quoted(time_of_day)}),",
                                    file=f,
                                )
                            print("        ],", file=f)
                            continue

                        if field == "trades":
                            print(f"        {field}: [", file=f)
                            for location, item_names in value:
                                if isinstance(item_names, str):
                                    item_names = [item_names]
                                items = "[" + ", ".join(quoted(item) for item in item_names) + "]"
                                print(f"            ({quoted(functionify(location))}, {items}),", file=f)
                            print("        ],", file=f)
                            continue

                        if field == "shop":
                            print("        shops: [", file=f)
                            for town_name, currency in value:
                                currency_value = quoted(currency)# if currency.endswith(" Gems") else currency
                                print(f"            ({quoted(town_name)}, {currency_value}),", file=f)
                            print("        ],", file=f)
                            continue

                        if isinstance(value, list):
                            if field == "dungeon_boss":
                                value = "[" + ", ".join(
                                    "(" + functionify(dungeon) + ", " + attack + ")"
                                    for dungeon, attack in value
                                ) + "]"
                            elif field in ("dungeon", "dungeon_chest"):
                                value = "[" + ", ".join(
                                    functionify(dungeon) for dungeon in value
                                ) + "]"
                            else:
                                value = "[" + ", ".join(quoted(v) for v in value) + "]"
                        elif field in ("dungeon", "dungeon_evolution"):
                            value = functionify(value)
                        elif field == "level":
                            value = str(int(value))
                        else:
                            value = quoted(value)

                        print(f"        {output_field}: {value},", file=f)

                if pokemon[name].get("special"):
                    print("        special: [", file=f)
                    prepared_specials = []
                    grouped_counts = {}

                    for special in pokemon[name]["special"]:
                        if "vivillon_unowned_quest_rule" in special:
                            prepared_specials.append({
                                "special": special,
                                "vivillon_unowned_quest_rule": True,
                            })
                            continue

                        if "dungeon_loot_terms" in special:
                            prepared_specials.append({
                                "special": special,
                                "dungeon_loot_rule": True,
                            })
                            continue

                        if "dungeon_encounter_terms" in special:
                            if special["unprocessed_requirements"]:
                                prepared_specials.append({
                                    "special": special,
                                    "dungeon_encounter_unprocessed": True,
                                })
                            else:
                                prepared_specials.append({
                                    "special": special,
                                    "dungeon_encounter_rule": True,
                                })
                            continue

                        if "unowned" in special:
                            prepared_specials.append({
                                "special": special,
                                "gmax_unowned_rule": True,
                            })
                            continue

                        if "owned" in special:
                            prepared_specials.append({
                                "special": special,
                                "gmax_owned_rule": True,
                            })
                            continue

                        if "dungeon_boss_rule" in special:
                            prepared_specials.append({
                                "special": special,
                                "dungeon_boss_rule": True,
                            })
                            continue

                        if "battle_frontier_stage" in special:
                            prepared_specials.append({
                                "special": special,
                                "battle_frontier_requirement": True,
                            })
                            continue

                        if "region_safari" in special:
                            prepared_specials.append({
                                "special": special,
                                "region_safari": True,
                            })
                            continue

                        requirements = special["requirements"]
                        if "roamer" in special:
                            prepared_specials.append({
                                "special": special,
                                "roamer": True,
                            })
                            continue

                        has_terms, route_included = special_has_terms(special)
                        omitted_level_name = omitted_level_pokemon(special)

                        if special.get("gift") and not requirements:
                            has_terms = [f"make_rule({special['route']})"]
                            route_included = True

                        if not has_terms:
                            if omitted_level_name:
                                has_terms = [f"Has({quoted(omitted_level_name)})"]

                        if has_terms:
                            route_term = f"make_rule({special['route']})"
                            base_terms = [term for term in has_terms if term != route_term]
                            group_key = (special.get("region"), tuple(base_terms))
                            if special.get("region") in (
                                "kanto", "johto", "hoenn", "alola"
                            ):
                                grouped_counts[group_key] = grouped_counts.get(group_key, 0) + 1

                            prepared_specials.append({
                                "special": special,
                                "terms": has_terms,
                                "route_included": route_included,
                                "route_term": route_term,
                                "base_terms": base_terms,
                                "group_key": group_key,
                                "omitted_level_name": omitted_level_name,
                            })
                            continue

                        prepared_specials.append({
                            "special": special,
                            "requirements": requirements,
                        })

                    # Pair each unowned Vivillon rule with the owned boss rule for the same dungeon.
                    for prepared in prepared_specials:
                        if not prepared.get("vivillon_unowned_quest_rule"):
                            continue
                        _, viv_dungeon, viv_attack = prepared["special"]["vivillon_unowned_quest_rule"]
                        for candidate in prepared_specials:
                            boss_special = candidate["special"]
                            if (
                                candidate.get("dungeon_boss_rule")
                                and not candidate.get("merged")
                                and not boss_special["unprocessed_requirements"]
                                and boss_special["dungeon_boss_rule"][1] == viv_attack
                                and functionify(boss_special["dungeon_boss_rule"][0]) == functionify(viv_dungeon)
                                and any(term.startswith(f"Has({quoted(name)})") for term in boss_special["requirement_terms"])
                            ):
                                candidate["merged"] = True
                                prepared["merged_boss"] = boss_special
                                break

                    emitted_groups = set()
                    for prepared in prepared_specials:
                        if prepared.get("merged"):
                            continue

                        if prepared.get("vivillon_unowned_quest_rule"):
                            quest_rule, dungeon, attack = prepared["special"]["vivillon_unowned_quest_rule"]
                            boss_special = prepared.get("merged_boss")
                            if boss_special:
                                dungeon_clear_term = f"make_rule({functionify(dungeon)}, True)"
                                terms = [
                                    term
                                    for term in boss_special["requirement_terms"]
                                    if term != dungeon_clear_term and not term.startswith(f"Has({quoted(name)})")
                                ]
                                terms.append(f"make_rule({functionify(dungeon)}, True, {attack})")
                                seasonal_term = "make_rule(has_script, 'Infinite Seasonal Events Script')"
                                if boss_special["seasonal_event_requirement"] and seasonal_term not in terms:
                                    terms.append(seasonal_term)
                                print(
                                    f"            (Has({quoted(name)}) | {quest_rule}) & "
                                    f"{' & '.join(order_special_terms(terms))},",
                                    file=f,
                                )
                                continue
                            print(
                                f"            not Has({quoted(name)}) & {quest_rule} & "
                                f"make_rule({dungeon}, True, {attack}),",
                                file=f,
                            )
                            continue

                        if prepared.get("dungeon_loot_rule"):
                            special = prepared["special"]
                            if special["unprocessed_requirements"]:
                                write_requirement_dictionary(
                                    f,
                                    special["unprocessed_requirements"],
                                    dungeon=functionify(special["dungeon_name"]),
                                    rule=" & ".join(special["dungeon_loot_terms"]),
                                )
                            else:
                                print(
                                    f"            {' & '.join(special['dungeon_loot_terms'])},",
                                    file=f,
                                )
                            continue

                        if prepared.get("dungeon_encounter_unprocessed"):
                            special = prepared["special"]
                            write_requirement_dictionary(
                                f,
                                special["unprocessed_requirements"],
                                dungeon=functionify(special["dungeon_name"]),
                                rule=" & ".join(special["dungeon_encounter_terms"]),
                            )
                            continue

                        if prepared.get("dungeon_encounter_rule"):
                            terms = prepared["special"]["dungeon_encounter_terms"]
                            print(f"            {' & '.join(order_special_terms(terms))},", file=f)
                            continue

                        if prepared.get("gmax_unowned_rule"):
                            special = prepared["special"]
                            if special["quest_step"] is not None:
                                print(
                                    f"            (Has({quoted(special['unowned'])}) | make_rule(lair_of_giants{special['quest_step']})) & make_rule(max_lair),",
                                    file=f,
                                )
                                continue
                            print("            make_rule(max_lair),", file=f)
                            continue

                        if prepared.get("gmax_owned_rule"):
                            special = prepared["special"]
                            if any(
                                other.get("unowned") == special["owned"]
                                for other in pokemon[name]["special"]
                            ):
                                continue
                            terms = [
                                f"Has({quoted(special['owned'])})",
                                "make_rule(max_lair)",
                            ]
                            print(
                                f"            ({' & '.join(order_special_terms(terms))}),",
                                file=f,
                            )
                            continue

                        if prepared.get("dungeon_boss_rule"):
                            special = prepared["special"]
                            dungeon, attack = special["dungeon_boss_rule"]
                            dungeon_clear_term = f"make_rule({functionify(dungeon)}, True)"
                            terms = [
                                term
                                for term in special["requirement_terms"]
                                if term != dungeon_clear_term
                            ]
                            terms.append(f"make_rule({functionify(dungeon)}, True, {attack})")
                            seasonal_term = 'make_rule(has_script, "Infinite Seasonal Events Script")'
                            if special["seasonal_event_requirement"] and seasonal_term not in terms:
                                terms.append(seasonal_term)
                            if special["unprocessed_requirements"]:
                                write_requirement_dictionary(
                                    f,
                                    special["unprocessed_requirements"],
                                    dungeon=functionify(dungeon),
                                    rule=" & ".join(order_special_terms(terms)),
                                )
                            else:
                                print(f"            {' & '.join(order_special_terms(terms))},", file=f)
                            continue

                        if prepared.get("battle_frontier_requirement"):
                            special = prepared["special"]
                            terms = [f"make_rule(battle_frontier, {special['battle_frontier_stage']})"]
                            terms.extend(roamer_requirement_terms(special["requirements"]))
                            print(f"            {' & '.join(order_special_terms(terms))},", file=f)
                            continue

                        if prepared.get("region_safari"):
                            special = prepared["special"]
                            region = special["region_safari"]
                            terms = [f"make_rule(region_safari, {quoted(region)})"]
                            if special.get("requires_pokemon"):
                                required_pokemon = special["requires_pokemon"]
                                terms.append(f"Has({quoted(required_pokemon if isinstance(required_pokemon, str) else name)})")
                            terms.extend(roamer_requirement_terms(special.get("requirements", [])))
                            print(f"            {' & '.join(order_special_terms(terms))},", file=f)
                            continue

                        if prepared.get("roamer"):
                            special = prepared["special"]
                            region = special["roamer"].replace('"', '\\"')
                            terms = [f"make_rule(roamer, '{region}')"]
                            terms.extend(roamer_requirement_terms(special["requirements"]))
                            print(f"            {' & '.join(order_special_terms(terms))},", file=f)
                            continue

                        if "requirements" in prepared:
                            special = prepared["special"]
                            requirements = prepared["requirements"]
                            write_requirement_dictionary(
                                f,
                                requirements,
                                route=special["route"],
                            )
                            continue

                        special = prepared["special"]
                        terms = list(prepared["terms"])
                        route_helper = f"any_{special.get('region', 'none')}_route"
                        can_group = (
                            "make_rule(has_script, 'Infinite Seasonal Events Script')" in prepared["base_terms"]
                            or (
                                special.get("region") == "alola"
                                and "make_rule(lets_go_meltan9)" in prepared["base_terms"]
                            )
                        )
                        is_grouped = can_group and grouped_counts.get(prepared["group_key"], 0) > 1

                        if is_grouped:
                            if prepared["group_key"] in emitted_groups:
                                continue
                            emitted_groups.add(prepared["group_key"])

                        if is_grouped:
                            if prepared["route_included"]:
                                terms = [
                                    f"make_rule({route_helper})" if term == prepared["route_term"] else term
                                    for term in terms
                                ]
                            else:
                                terms.append(f"make_rule({route_helper})")
                        elif not prepared["route_included"]:
                            if special.get("gift"):
                                terms.insert(0, prepared["route_term"])
                            else:
                                terms.append(prepared["route_term"])

                        if prepared["omitted_level_name"]:
                                print("            # below level omited. Fix client code!", file=f)
                        print(f"            {' & '.join(order_special_terms(terms))},", file=f)

                    print("        ],", file=f)

                print("    },", file=f)

        print("}", file=f)

    generated_output = OUTPUT_PATH.read_text(encoding="utf-8")
    generated_output = re.sub(
        r"(\bmake_rule\(\s*)([A-Za-z_][A-Za-z0-9_]*)\b",
        lambda match: f"{match.group(1)}{quoted(match.group(2))}",
        generated_output,
    )
    OUTPUT_PATH.write_text(generated_output, encoding="utf-8")

if __name__ == "__main__":
    compile_pokemon_dictionary()