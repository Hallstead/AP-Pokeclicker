
from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld
from .Data import meta_table
from .Helpers import convert_to_long_string

##############
# Meta Classes
##############
class ManualWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up manual game integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Fuzzy"]
    )]

######################################
# Convert meta.json data to properties
######################################
def set_world_description(base_doc: str) -> str:
    if meta_table.get("docs", {}).get("apworld_description"):
        return convert_to_long_string(meta_table["docs"]["apworld_description"])

    return base_doc


def set_world_webworld(web: WebWorld) -> WebWorld:
    from .Options import make_options_group
    if meta_table.get("docs", {}).get("web", {}):
        Web_Config = meta_table["docs"]["web"]

        web.theme = Web_Config.get("theme", web.theme)
        web.game_info_languages = Web_Config.get("game_info_languages", web.game_info_languages)
        web.options_presets = Web_Config.get("options_presets", web.options_presets)
        web.options_page = Web_Config.get("options_page", web.options_page)
        web.option_groups = make_options_group()
        if hasattr(web, 'bug_report_page'):
            web.bug_report_page = Web_Config.get("bug_report_page", web.bug_report_page)
        else:
            web.bug_report_page = Web_Config.get("bug_report_page", None)

        if Web_Config.get("tutorials", []):
            tutorials = []
            for tutorial in Web_Config.get("tutorials", []):
                # Converting json to Tutorials
                tutorials.append(Tutorial(
                    tutorial.get("name", "Multiworld Setup Guide"),
                    tutorial.get("description", "A guide to setting up manual game integration for Archipelago multiworld games."),
                    tutorial.get("language", "English"),
                    tutorial.get("file_name", "setup_en.md"),
                    tutorial.get("link", "setup/en"),
                    tutorial.get("authors", [meta_table.get("creator", meta_table.get("player", "Unknown"))])
                ))
            web.tutorials = tutorials
    return web

#################
# Meta Properties
#################
world_description: str = set_world_description("""
    Pokéclicker is an incremental idle game where players catch, hatch, and battle Pokémon to progress through regions, earn badges, and complete their Pokédex.
    """)
world_webworld: ManualWeb = set_world_webworld(ManualWeb())

enable_region_diagram = bool(meta_table.get("enable_region_diagram", False))
