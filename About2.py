import os

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About the Developer")
        self.resize(360, 420)
        
        self.setStyleSheet("""QWidget {background-color: #f8f9fa;font-family: Arial, sans-serif;}""")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(15)

        title_label = QLabel("About")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #2c3e50;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images.webp")
        pixmap = QPixmap(image_path)
        
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap.scaled(110, 110, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.setStyleSheet("border-radius: 55px; border: 2px solid #bdc3c7; background: white;")
        else:
            self.image_label.setText("👤")
            self.image_label.setStyleSheet("""font-size: 45px; color: #7f8c8d; background: #ecf0f1; border-radius: 55px; border: 2px solid #bdc3c7;""")
            self.image_label.setFixedSize(110, 110)
        
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        name_label = QLabel("Ravid Fathi")
        name_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #34495e;")
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)

        email_label = QLabel("Email: Ravid.Fathi@s.afeka.ac.il")
        email_label.setStyleSheet("font-size: 14px; color: #7f8c8d;")
        email_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(email_label)

        linkedin_label = QLabel('<a href="http://www.linkedin.com/in/ravid-fathi-5ab909298" style="color: #0077b5; text-decoration: none; font-weight: bold; font-size: 15px;">🔗 View my LinkedIn profile</a>')
        linkedin_label.setOpenExternalLinks(True)
        linkedin_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(linkedin_label)

        Git_label = QLabel('<a href="https://github.com/Ravid-Fathi/HW4.2" style="color: #0077b5; text-decoration: none; font-weight: bold; font-size: 15px;">View my GitHub code</a>')
        Git_label.setOpenExternalLinks(True)
        Git_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(Git_label)
        layout.addSpacing(10)

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""QPushButton {background-color: #e74c3c;color: white;border-radius: 6px;padding: 8px 20px;font-weight: bold;font-size: 14px;}QPushButton:hover {background-color: #c0392b;}""")
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn, alignment=Qt.AlignCenter)