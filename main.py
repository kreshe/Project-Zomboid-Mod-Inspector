from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.style import STYLE


app = QApplication(sys.argv)


window = MainWindow()
window.setStyleSheet(
    STYLE
)

window.show()


sys.exit(
    app.exec()
)
from core.config import load_config
from core.scanner import scan_workshop
from core.parser import parse_mod
from core.indexer import index_mod
from engines.conflict_engine import check_lua_conflicts
from engines.conflict_engine import check_item_conflicts
from analyzers.dependency import (
    check_missing_dependencies,
    check_load_order
)
from reports.full_report import generate_report
from reports.json_report import save_json_report
from analyzers.server import analyze_server
config = load_config()

workshop = Path(config["workshop_path"])

print("Сканирование Workshop...")

mods = []

for folder in scan_workshop(workshop):
    mod = parse_mod(folder)
    mod = index_mod(mod)
    mods.append(mod)



server_report = analyze_server(
    "C:/Users/re-kr/Zomboid/Server/servertest.ini",
    mods
)

missing = check_missing_dependencies(mods)
order = check_load_order(mods)

lua_conflicts = check_lua_conflicts(mods)
item_conflicts = check_item_conflicts(mods)

generate_report(
    mods,
    lua_conflicts,
    item_conflicts,
    missing,
    order
)

save_json_report(
    "pz_report.json",
    mods,
    lua_conflicts,
    item_conflicts,
    missing,
    order
)
print("Найдено модов:", len(mods))