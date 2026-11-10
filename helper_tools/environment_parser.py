"""Generate Archipelago environment location identifiers from Pokéclicker source."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from pokemon_parser import GAME_CONSTANTS_PATH, PROJECT_DIR, functionify, quoted, read_source


ROUTES_PATH = PROJECT_DIR / "src" / "modules" / "routes" / "RouteData.ts"
TOWN_LIST_PATH = PROJECT_DIR / "src" / "scripts" / "towns" / "TownList.ts"
MAP_HELPER_PATH = PROJECT_DIR / "src" / "scripts" / "worldmap" / "MapHelper.ts"
OUTPUT_PATH = Path(__file__).resolve().parent / "environments.txt"

ENVIRONMENT_NAMES = (
    "PlantCloak",
    "SandyCloak",
    "TrashCloak",
    "MagneticField",
    "MossRock",
    "IceRock",
)


def extract_block(text: str, marker: str, open_char: str = "{", close_char: str = "}") -> str:
    """Return the balanced block beginning after marker, respecting quoted strings."""
    marker_position = text.find(marker)
    if marker_position < 0:
        raise ValueError(f"Could not find {marker!r}")

    start = text.find(open_char, marker_position + len(marker))
    if start < 0:
        raise ValueError(f"Could not find {open_char!r} after {marker!r}")

    depth = 0
    in_string = False
    escaped = False
    for position in range(start, len(text)):
        char = text[position]
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
        elif char == open_char:
            depth += 1
        elif char == close_char:
            depth -= 1
            if depth == 0:
                return text[start + 1:position]

    raise ValueError(f"Unclosed block after {marker!r}")


def unescape_ts_string(value: str) -> str:
    return value.replace("\\'", "'").replace("\\\\", "\\")


def region_ids(constants_text: str) -> dict[str, int]:
    match = re.search(r"export enum Region\s*\{([\s\S]*?)\}", constants_text)
    if not match:
        raise ValueError("Could not parse the Region enum")
    return {name: int(value) for name, value in re.findall(r"(\w+)\s*=\s*(-?\d+)", match.group(1))}


def parse_routes() -> dict[tuple[str, int], str]:
    text = read_source(ROUTES_PATH)
    pattern = re.compile(
        r"new RegionRoute\(\s*'((?:\\.|[^'])*)'\s*,\s*Region\.(\w+)\s*,\s*(\d+)"
    )
    return {
        (region, int(number)): unescape_ts_string(name)
        for name, region, number in pattern.findall(text)
    }


def parse_towns() -> list[tuple[str, str]]:
    text = read_source(TOWN_LIST_PATH)
    pattern = re.compile(
        r"TownList\['((?:\\.|[^'])*)'\]\s*=\s*new Town\(\s*"
        r"'((?:\\.|[^'])*)'\s*,\s*GameConstants\.Region\.(\w+)"
    )
    return [
        (region, unescape_ts_string(name))
        for _key, name, region in pattern.findall(text)
    ]


def parse_dungeons(constants_text: str) -> list[tuple[str, str]]:
    region_match = re.search(r"export const RegionDungeons\s*=\s*(\[[\s\S]*?\]);", constants_text)
    if not region_match:
        raise ValueError("Could not parse RegionDungeons")

    region_arrays = re.findall(r"\b(\w+Dungeons)\b", region_match.group(1))
    region_names = [
        name for name, _ in sorted(region_ids(constants_text).items(), key=lambda item: item[1])
        if name not in ("none", "final")
    ]

    result = []
    for region, array_name in zip(region_names, region_arrays):
        array_match = re.search(
            rf"export const {re.escape(array_name)}\s*=\s*(\[[\s\S]*?\]);",
            constants_text,
        )
        if not array_match:
            raise ValueError(f"Could not parse {array_name}")
        for raw_name in re.findall(r"'((?:\\.|[^'])*)'", array_match.group(1)):
            result.append((region, unescape_ts_string(raw_name)))
    return result


def parse_explicit_environments(constants_text: str, regions: dict[str, int]) -> dict[str, dict[str, set[str | int]]]:
    source = extract_block(constants_text, "export const Environments:")
    environments: dict[str, dict[str, set[str | int]]] = {}
    entry_pattern = re.compile(r"(\w+)\s*:\s*\{([\s\S]*?)\n\s*\},?", re.MULTILINE)
    region_pattern = re.compile(r"\[Region\.(\w+)\]\s*:\s*new Set\(\[([\s\S]*?)\]\)")
    value_pattern = re.compile(r"'((?:\\.|[^'])*)'|\b(\d+)\b")

    for environment, body in entry_pattern.findall(source):
        entries: dict[str, set[str | int]] = defaultdict(set)
        for region, values in region_pattern.findall(body):
            if region not in regions:
                continue
            for string_value, numeric_value in value_pattern.findall(values):
                entries[region].add(unescape_ts_string(string_value) if string_value else int(numeric_value))
        environments[environment] = dict(entries)

    return environments


def parse_hisui_land_environment(constants_text: str) -> dict[str, set[str | int]]:
    source = extract_block(constants_text, "export const Environments:")
    result: dict[str, set[str | int]] = {}
    for environment in (
        "JubilifeVillage", "ObsidianFieldlands", "CrimsonMirelands",
        "CobaltCoastlands", "CoronetHighlands", "AlabasterIcelands",
    ):
        match = re.search(rf"{environment}\s*:\s*\{{([\s\S]*?)\n\s*\}},?", source)
        if not match:
            continue
        region_values = re.search(r"\[Region\.hisui\]\s*:\s*new Set\(\[([\s\S]*?)\]\)", match.group(1))
        if region_values:
            result[environment] = {
                unescape_ts_string(string_value) if string_value else int(numeric_value)
                for string_value, numeric_value in re.findall(r"'((?:\\.|[^'])*)'|\b(\d+)\b", region_values.group(1))
            }
    return result


def add_location(locations: dict[str, dict[str, set[str]]], region: str, name: str, environment: str) -> None:
    locations[environment][region].add(name)


def build_environments() -> dict[str, dict[str, set[str]]]:
    constants_text = read_source(GAME_CONSTANTS_PATH)
    map_helper_text = read_source(MAP_HELPER_PATH)
    regions = region_ids(constants_text)
    explicit = parse_explicit_environments(constants_text, regions)
    routes = parse_routes()
    towns = parse_towns()
    dungeons = parse_dungeons(constants_text)

    # All map locations which can be the current area in MapHelper.getEnvironments().
    candidates: dict[str, set[str | int]] = defaultdict(set)
    for region, route_number in routes:
        candidates[region].add(route_number)
    for region, name in towns + dungeons:
        candidates[region].add(name)

    output: dict[str, dict[str, set[str]]] = {
        name: defaultdict(set) for name in ENVIRONMENT_NAMES
    }

    # Add explicit source assignments, resolving numeric route IDs to display names.
    for environment, region_values in explicit.items():
        if environment not in output:
            continue
        for region, values in region_values.items():
            for value in values:
                if isinstance(value, int):
                    route_name = routes.get((region, value))
                    if route_name is None:
                        raise ValueError(f"No route found for Region.{region} route {value} ({environment})")
                    name = route_name
                else:
                    name = value
                    candidates[region].add(name)
                add_location(output, region, name, environment)

    # Apply MapHelper's automatic Burmy cloak rules for caves, city-like towns, and Hisui.
    cave_locations = explicit.get("Cave", {})
    hisui_lands = parse_hisui_land_environment(constants_text)
    for region, areas in candidates.items():
        for area in areas:
            area_name = routes.get((region, area), "") if isinstance(area, int) else area
            matching = {
                environment
                for environment, region_values in explicit.items()
                if area in region_values.get(region, set())
            }

            if region == "hisui":
                area_envs = {
                    land for land, values in hisui_lands.items() if area in values
                }
                if "ObsidianFieldlands" in area_envs or "JubilifeVillage" in area_envs:
                    matching.add("PlantCloak")
                if "CoronetHighlands" in area_envs:
                    matching.add("MagneticField")
                if area_envs.intersection({"CoronetHighlands", "CrimsonMirelands"}):
                    matching.add("SandyCloak")
                if area_envs.intersection({"AlabasterIcelands", "CobaltCoastlands"}):
                    matching.add("TrashCloak")
            elif area in cave_locations.get(region, set()):
                matching.add("SandyCloak")
            elif isinstance(area, str) and any(word in area for word in ("City", "League", "Tower")):
                matching.add("TrashCloak")

            cloak_environments = {"PlantCloak", "SandyCloak", "TrashCloak"}
            if not matching.intersection(cloak_environments):
                matching.add("PlantCloak")

            for environment in matching.intersection(output):
                add_location(output, region, area_name, environment)

    # Fail early if the MapHelper's cloak inference has materially changed.
    expected_cloak_logic = (
        "burmyCloaks", "Cave", "City", "League", "Tower", "ObsidianFieldlands",
        "CrimsonMirelands", "CobaltCoastlands", "CoronetHighlands", "AlabasterIcelands",
    )
    if not all(token in map_helper_text for token in expected_cloak_logic):
        raise ValueError("MapHelper cloak rules changed; review environment extraction logic")

    return output


def write_environments(path: Path = OUTPUT_PATH) -> None:
    environments = build_environments()
    with path.open("w", encoding="utf-8", newline="\n") as output:
        output.write("ENVIRONMENTS = {\n")
        for environment in ENVIRONMENT_NAMES:
            output.write(f"    {quoted(environment)}: [\n")
            values = sorted(
                {
                    functionify(location)
                    for region_locations in environments[environment].values()
                    for location in region_locations
                }
            )
            for value in values:
                output.write(f"        {quoted(value)},\n")
            output.write("    ],\n")
        output.write("}\n")


if __name__ == "__main__":
    write_environments()
    print(f"Wrote environment lists to {OUTPUT_PATH}")
