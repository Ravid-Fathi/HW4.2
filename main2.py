import importlib
from pathlib import Path

import csv

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT,
)
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class SalesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ice Cream Sales")
        self.setMinimumSize(820, 600)
        self.resize(1060, 720)

        self.temperatures = []
        self.profits = []

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.setContentsMargins(32, 28, 32, 28)
        central_layout.setSpacing(22)

        header_layout = QHBoxLayout()
        heading_layout = QVBoxLayout()
        title = QLabel("Ice Cream Sales")
        title.setObjectName("pageTitle")
        subtitle = QLabel("Explore how temperature affects sales profit.")
        subtitle.setObjectName("subtitle")
        heading_layout.addWidget(title)
        heading_layout.addWidget(subtitle)
        header_layout.addLayout(heading_layout)
        header_layout.addStretch()

        self.load_button = QPushButton("Load File")
        self.load_button.setObjectName("primaryButton")
        self.load_button.clicked.connect(self.open_file_dialog)
        self.about_button = QPushButton("About")
        self.about_button.setObjectName("secondaryButton")
        self.about_button.clicked.connect(self.open_about)
        header_layout.addWidget(self.load_button)
        header_layout.addWidget(self.about_button)
        central_layout.addLayout(header_layout)

        chart_card = QFrame()
        chart_card.setObjectName("chartCard")
        chart_layout = QVBoxLayout(chart_card)
        chart_layout.setContentsMargins(18, 14, 18, 18)
        chart_layout.setSpacing(8)

        chart_heading = QLabel("Profit vs. temperature")
        chart_heading.setObjectName("chartTitle")
        chart_layout.addWidget(chart_heading)

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        chart_layout.addWidget(self.toolbar)
        chart_layout.addWidget(self.canvas, stretch=1)
        central_layout.addWidget(chart_card, stretch=1)

        self.setCentralWidget(central_widget)
        self.plot_data()

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Load sales data",
            "",
            "CSV files (*.csv);;All files (*)",
        )
        if file_path:
            self.load_file(file_path)

    def load_file(self, file_path):
        if file_path:
            self.temperatures.clear()
            self.profits.clear()

            with open(file_path, mode='r', encoding='utf-8-sig', newline='') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if row:
                        self.temperatures.append(float(row[0]))
                        self.profits.append(float(row[1]))

            self.plot_data()


    def plot_data(self):
        self.ax.clear()
        self.ax.plot(
            [15, 20, 25, 30, 35],
            [120, 180, 260, 340, 430],
            marker="o",
            color="#2f7f78",
            linewidth=2.5,
            markersize=7,
        )
        self.ax.set_xlabel("Temperature (°C)")
        self.ax.set_ylabel("Profit")
        self.ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.35)
        self.figure.tight_layout()
        self.canvas.draw()

    def open_about(self):
        about_module = importlib.import_module("About2")
        self.about_window = about_module.AboutWindow()
        self.about_window.show()


def main():
    app = QApplication([])
    stylesheet_path = Path(__file__).with_name("style2.qss")
    app.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    window = SalesWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()