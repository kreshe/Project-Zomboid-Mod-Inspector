from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QProgressBar
)
from PySide6.QtGui import QColor
import os
from PySide6.QtWidgets import (
    QLineEdit,
    QHeaderView
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTextEdit
from ui.widgets import StatCard
from core.scanner import scan_workshop
from core.config import (
    load_config,
    save_config
)
from core.indexer import index_mod
from core.engine import ModChecker

from pathlib import Path

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Project Zomboid Mod Inspector"
        )

        config = load_config()

        self.indexed_mods = []

        self.workshop_path = None

        self.statusBar().showMessage(
            "Готов"
        )

        if "workshop_path" in config:

            path = Path(
                config["workshop_path"]
            )


            if path.exists():

                self.workshop_path = path

        self.resize(
            1100,
            700
        )

        self.setup_ui()
        self.setStyleSheet("""
            QMainWindow {
                background:#202020;
            }


            QWidget {
                color:#dddddd;
                font-size:14px;
            }


            QLineEdit {
                background:#2b2b2b;
                border:1px solid #555;
                padding:6px;
                border-radius:5px;
            }


            QPushButton {
                background:#333;
                border:1px solid #666;
                padding:8px 15px;
                border-radius:6px;
            }


            QPushButton:hover {
                background:#444;
            }


            QTabWidget::pane {
                border:1px solid #444;
            }


            QTableWidget {
                background:#252525;
                alternate-background-color:#303030;
                gridline-color:#444;
            }


            QHeaderView::section {
                background:#333;
                padding:6px;
                border:1px solid #555;
            }


            QProgressBar {
                border:1px solid #555;
                height:18px;
            }


            QProgressBar::chunk {
                background:#3daee9;
            }


            QTreeWidget {
                background:#252525;
            }

            """)
        if self.workshop_path:

            self.path_label.setText(
                str(self.workshop_path)
            )


    def setup_ui(self):

        root = QWidget()
        root.setObjectName("root")

        layout = QVBoxLayout(root)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(10)

        # =========================================================
        # TOP BAR
        # =========================================================

        top = QHBoxLayout()
        top.setSpacing(8)

        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍  Поиск модов...")
        self.search.setMinimumHeight(38)

        btn = QPushButton("📂  Workshop")
        btn.setMinimumHeight(38)
        btn.setMinimumWidth(140)

        self.scan_btn = QPushButton("▶  Сканировать")
        self.scan_btn.setMinimumHeight(38)
        self.scan_btn.setMinimumWidth(150)

        self.search.textChanged.connect(
            self.filter_mods
        )

        btn.clicked.connect(
            self.select_folder
        )

        self.scan_btn.clicked.connect(
            self.start_scan
        )

        top.addWidget(
            self.search,
            1
        )

        top.addWidget(
            btn
        )

        top.addWidget(
            self.scan_btn
        )

        layout.addLayout(top)

        # =========================================================
        # WORKSHOP PATH
        # =========================================================

        self.path_label = QLabel(
            "Workshop не выбран"
        )

        self.path_label.setObjectName(
            "pathLabel"
        )

        self.path_label.setMinimumHeight(28)

        layout.addWidget(
            self.path_label
        )

        # =========================================================
        # TABS
        # =========================================================

        self.tabs = QTabWidget()

        self.tabs.setDocumentMode(True)

        # =========================================================
        # DASHBOARD
        # =========================================================

        self.dashboard = QWidget()

        dash_layout = QVBoxLayout(
            self.dashboard
        )

        dash_layout.setContentsMargins(
            4,
            12,
            4,
            4
        )

        dash_layout.setSpacing(12)

        # ---------------------------------------------------------
        # STAT CARDS
        # ---------------------------------------------------------

        cards = QHBoxLayout()
        cards.setSpacing(10)

        self.mods_card = StatCard(
            "Mods"
        )

        self.lua_card = StatCard(
            "Lua conflicts"
        )

        self.item_card = StatCard(
            "Item conflicts"
        )

        self.dep_card = StatCard(
            "Missing dependencies"
        )

        cards.addWidget(
            self.mods_card
        )

        cards.addWidget(
            self.lua_card
        )

        cards.addWidget(
            self.item_card
        )

        cards.addWidget(
            self.dep_card
        )

        dash_layout.addLayout(
            cards
        )

        # ---------------------------------------------------------
        # PROGRESS
        # ---------------------------------------------------------

        self.progress = QProgressBar()

        self.progress.setValue(0)

        self.progress.setMinimumHeight(22)

        dash_layout.addWidget(
            self.progress
        )

        # ---------------------------------------------------------
        # LOG
        # ---------------------------------------------------------

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.log.setPlaceholderText(
            "Результаты сканирования..."
        )

        dash_layout.addWidget(
            self.log,
            1
        )

        # =========================================================
        # MODS TABLE
        # =========================================================

        self.mods = QTableWidget()

        self.mods.setColumnCount(5)

        self.mods.setHorizontalHeaderLabels(
            [
                "Название",
                "ID",
                "Workshop",
                "Risk",
                "Ошибки"
            ]
        )

        self.mods.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.mods.setSelectionMode(
            QTableWidget.SingleSelection
        )

        self.mods.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.mods.setAlternatingRowColors(
            True
        )

        self.mods.verticalHeader().setVisible(
            False
        )

        self.mods.setSortingEnabled(
            True
        )

        self.mods.setShowGrid(
            False
        )

        header = self.mods.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            4,
            QHeaderView.ResizeToContents
        )

        # =========================================================
        # CONFLICTS
        # =========================================================

        self.conflicts = QTreeWidget()

        self.conflicts.setHeaderLabels(
            [
                "Тип",
                "Объект",
                "Риск"
            ]
        )

        self.conflicts.setAlternatingRowColors(
            True
        )

        self.conflicts.setRootIsDecorated(
            True
        )

        self.conflicts.setColumnWidth(
            0,
            100
        )

        self.conflicts.setColumnWidth(
            2,
            100
        )

        # =========================================================
        # TABS
        # =========================================================

        self.tabs.addTab(
            self.dashboard,
            "📊  Dashboard"
        )

        self.tabs.addTab(
            self.mods,
            "🧩  Mods"
        )

        self.tabs.addTab(
            self.conflicts,
            "⚠  Conflicts"
        )

        layout.addWidget(
            self.tabs,
            1
        )

        # =========================================================
        # CENTRAL WIDGET
        # =========================================================

        self.setCentralWidget(
            root
        )

        # =========================================================
        # DOUBLE CLICK
        # =========================================================

        self.mods.cellDoubleClicked.connect(
            self.open_mod_folder
        )

    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Steam Workshop"
        )


        if folder:


            self.workshop_path = Path(
                folder
            )


            self.path_label.setText(
                str(folder)
            )


            config = load_config()


            config["workshop_path"] = str(
                self.workshop_path
            )


            save_config(
                config
            )
    def start_scan(self):

        if not self.workshop_path:

            self.path_label.setText(
                "Выберите Workshop"
            )


            return


        self.progress.setValue(10)

        #
        # Сканирование
        #

        mods = scan_workshop(
            self.workshop_path
        )


        self.progress.setValue(30)


        #
        # Индексация
        #

        indexed = []

        for mod in mods:
            indexed.append(
                index_mod(mod)
            )


        self.indexed_mods = indexed.copy()


        self.progress.setValue(60)



        #
        # Анализ
        #

        checker = ModChecker(
            indexed
        )


        report = checker.run()

        self.statusBar().showMessage(
            f"Проверено модов: {len(indexed)} | "
            f"Ошибок: {len(report['lua']) + len(report['items'])}"
        )

        self.progress.setValue(100)

        self.log.clear()

        self.log.append(
            "PROJECT ZOMBOID MOD INSPECTOR"
        )

        self.log.append(
            "==========================="
        )

        self.log.append(
            f"Mods: {len(indexed)}"
        )

        self.log.append(
            f"Lua conflicts: {len(report['lua'])}"
        )

        self.log.append(
            f"Item conflicts: {len(report['items'])}"
        )

        self.log.append(
            f"Missing dependencies: {len(report['missing'])}"
        )

        self.log.append(
            f"Load order: {len(report['order'])}"
        )

        #
        # Карточки
        #

        self.mods_card.setValue(
            len(indexed)
        )


        self.lua_card.setValue(
            len(report["lua"])
        )


        self.item_card.setValue(
            len(report["items"])
        )


        self.dep_card.setValue(
            len(report["missing"])
        )



        #
        # Таблица модов
        #

        self.mods.setRowCount(
            len(indexed)
        )


        for row, mod in enumerate(indexed):

            errors = 0
            risk = 0


            for conflict in report["items"]:

                if mod.name in conflict["mods"]:

                    errors += 1

                    risk = max(
                        risk,
                        conflict["risk"]
                    )


            for conflict in report["lua"]:

                if mod.name in conflict["mods"]:

                    errors += 1

                    risk = max(
                        risk,
                        conflict["risk"]
                    )


            name_item = QTableWidgetItem(
                mod.name
            )

            name_item.setData(
                Qt.UserRole,
                mod
            )

            self.mods.setItem(
                row,
                0,
                name_item
            )


            self.mods.setItem(
                row,
                1,
                QTableWidgetItem(
                    mod.mod_id
                )
            )


            self.mods.setItem(
                row,
                2,
                QTableWidgetItem(
                    mod.workshop_id
                )
            )


            risk_item = QTableWidgetItem()

            if risk >= 90:
                risk_item.setText(f"🔴 {risk}")
            elif risk >= 60:
                risk_item.setText(f"🟠 {risk}")
            elif risk >= 30:
                risk_item.setText(f"🟡 {risk}")
            else:
                risk_item.setText(f"🟢 {risk}")

            # Числовое значение для сортировки
            risk_item.setData(
                Qt.UserRole,
                risk
            )

            # Центрируем Risk
            risk_item.setTextAlignment(
                Qt.AlignCenter
            )

            self.mods.setItem(
                row,
                3,
                risk_item
            )


            self.mods.setItem(
                row,
                4,
                QTableWidgetItem(
                    str(errors)
                )
            )

            self.mods.setSortingEnabled(True)
        #
        # Конфликты
        #

        self.conflicts.clear()


        for item in report["items"][:100]:


            node = QTreeWidgetItem(
                [
                    "ITEM",
                    item["item"],
                    str(item["risk"])
                ]
            )


            for mod in item["mods"]:


                child = QTreeWidgetItem(
                    [
                        "",
                        mod,
                        ""
                    ]
                )


                node.addChild(
                    child
                )


            self.conflicts.addTopLevelItem(
                node
            )
    def open_mod_folder(self, row, column):

        item = self.mods.item(
            row,
            0
        )

        if not item:
            return

        mod = item.data(
            Qt.UserRole
        )

        if mod and mod.path:

            os.startfile(
                str(mod.path)
            )
    def filter_mods(self,text):

        text = text.lower()


        for row in range(
            self.mods.rowCount()
        ):

            name = self.mods.item(
                row,
                0
            ).text().lower()


            self.mods.setRowHidden(
                row,
                text not in name
            )