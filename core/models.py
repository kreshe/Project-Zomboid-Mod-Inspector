from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class LuaFunction:

    class_name: str = ""

    function_name: str = ""

    file: Path | None = None

    relative_file: str = ""


@dataclass
class ModInfo:

    workshop_id: str = ""

    mod_id: str = ""

    name: str = ""

    description: str = ""

    version: str = ""


    path: Path | None = None


    lua_files: list[Path] = field(
        default_factory=list
    )


    script_files: list[Path] = field(
        default_factory=list
    )


    map_files: list[Path] = field(
        default_factory=list
    )


    lua_functions: list[LuaFunction] = field(
        default_factory=list
    )


    item_ids: set[str] = field(
        default_factory=set
    )

    dependencies: list[str] = field(
        default_factory=list
    )

    workshop_items: list[str] = field(
        default_factory=list
    )