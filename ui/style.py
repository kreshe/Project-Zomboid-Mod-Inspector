STYLE = """

/* =========================================================
   MAIN WINDOW
   ========================================================= */

QMainWindow {
    background: #181818;
}

QWidget#root {
    background: #181818;
    color: #dddddd;
    font-size: 14px;
}


/* =========================================================
   SEARCH
   ========================================================= */

QLineEdit {
    background: #252526;
    color: #eeeeee;

    border: 1px solid #3f3f46;
    border-radius: 7px;

    padding: 8px 12px;
}

QLineEdit:hover {
    border: 1px solid #555;
}

QLineEdit:focus {
    border: 1px solid #2d7dff;
}


/* =========================================================
   BUTTONS
   ========================================================= */

QPushButton {
    background: #2d7dff;
    color: white;

    border: none;
    border-radius: 7px;

    padding: 8px 16px;
}

QPushButton:hover {
    background: #5595ff;
}

QPushButton:pressed {
    background: #1c5ed6;
}

QPushButton:disabled {
    background: #333333;
    color: #777777;
}


/* =========================================================
   WORKSHOP PATH
   ========================================================= */

QLabel#pathLabel {
    background: #202020;
    color: #999999;

    border: 1px solid #303030;
    border-radius: 6px;

    padding: 6px 10px;
}


/* =========================================================
   STAT CARDS
   ========================================================= */

QFrame#statCard {
    background: #252526;

    border: 1px solid #333333;
    border-radius: 10px;
}

QLabel#statValue {
    color: #ffffff;

    font-size: 30px;
    font-weight: bold;
}

QLabel#statTitle {
    color: #999999;

    font-size: 13px;
}


/* =========================================================
   TABS
   ========================================================= */

QTabWidget::pane {
    background: #181818;

    border: 1px solid #333333;
    border-radius: 7px;
}

QTabBar {
    background: #181818;
}

QTabBar::tab {
    background: #252526;
    color: #aaaaaa;

    padding: 9px 18px;

    margin-right: 2px;

    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
}

QTabBar::tab:hover {
    background: #303030;
    color: #ffffff;
}

QTabBar::tab:selected {
    background: #2d7dff;
    color: #ffffff;
}


/* =========================================================
   TABLE
   ========================================================= */

QTableWidget {
    background: #181818;
    color: #dddddd;

    alternate-background-color: #202020;

    border: 1px solid #333333;
    border-radius: 6px;

    gridline-color: #2d2d2d;

    selection-background-color: #2d7dff;
    selection-color: white;
}

QTableWidget::item {
    padding: 6px;
}

QTableWidget::item:hover {
    background: #292929;
}

QTableWidget::item:selected {
    background: #2d7dff;
    color: white;
}


/* =========================================================
   TABLE HEADER
   ========================================================= */

QHeaderView::section {
    background: #252526;
    color: #bbbbbb;

    padding: 8px;

    border: none;
    border-bottom: 1px solid #333333;
}


/* =========================================================
   TREE
   ========================================================= */

QTreeWidget {
    background: #181818;
    color: #dddddd;

    border: 1px solid #333333;
    border-radius: 6px;

    alternate-background-color: #202020;
}

QTreeWidget::item {
    padding: 5px;
}

QTreeWidget::item:selected {
    background: #2d7dff;
    color: white;
}


/* =========================================================
   PROGRESS BAR
   ========================================================= */

QProgressBar {
    background: #252526;

    border: 1px solid #333333;
    border-radius: 6px;

    text-align: center;

    color: #dddddd;

    min-height: 18px;
}

QProgressBar::chunk {
    background: #2d7dff;
    border-radius: 5px;
}


/* =========================================================
   LOG
   ========================================================= */

QTextEdit {
    background: #141414;
    color: #bbbbbb;

    border: 1px solid #333333;
    border-radius: 6px;

    padding: 8px;
}


/* =========================================================
   SCROLLBARS
   ========================================================= */

QScrollBar:vertical {
    background: #181818;

    width: 10px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: #3a3a3a;

    min-height: 30px;

    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #555555;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background: #181818;

    height: 10px;
}

QScrollBar::handle:horizontal {
    background: #3a3a3a;

    border-radius: 5px;
}
"""