from pathlib import Path
import winreg
import re

def get_libraries(steam_path: Path) -> list[Path]:
    """Возвращает все библиотеки Steam."""

    libraries = [steam_path]

    vdf = steam_path / "steamapps" / "libraryfolders.vdf"

    if not vdf.exists():
        return libraries

    text = vdf.read_text(encoding="utf8", errors="ignore")

    pattern = r'"path"\s*"([^"]+)"'

    for path in re.findall(pattern, text):

        p = Path(path.replace("\\\\", "\\"))

        if p.exists():
            libraries.append(p)

    return libraries

def get_steam_path() -> Path | None:
    """Возвращает путь к Steam."""

    keys = [
        (winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam"),
    ]

    for hive, key in keys:
        try:
            with winreg.OpenKey(hive, key) as reg:
                value, _ = winreg.QueryValueEx(reg, "SteamPath")
                return Path(value)
        except FileNotFoundError:
            pass

    return None

def find_workshop() -> Path | None:

    steam = get_steam_path()

    if steam is None:
        return None

    for lib in get_libraries(steam):

        workshop = lib / "steamapps" / "workshop" / "content" / "108600"

        if workshop.exists():
            return workshop

    return None