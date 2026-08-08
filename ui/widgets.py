from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel
)


class StatCard(QFrame):

    def __init__(self, title):
        super().__init__()

        self.setObjectName(
            "statCard"
        )

        self.setMinimumHeight(
            100
        )

        self.setMaximumHeight(
            110
        )

        layout = QVBoxLayout(
            self
        )

        layout.setContentsMargins(
            16,
            12,
            16,
            12
        )

        layout.setSpacing(
            2
        )

        self.value = QLabel(
            "0"
        )

        self.value.setObjectName(
            "statValue"
        )

        self.title = QLabel(
            title
        )

        self.title.setObjectName(
            "statTitle"
        )

        layout.addWidget(
            self.value
        )

        layout.addWidget(
            self.title
        )

    def setValue(self, value):

        self.value.setText(
            str(value)
        )