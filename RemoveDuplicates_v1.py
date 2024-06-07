#!/usr/bin/python3

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QMessageBox
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QDesktopServices
import pyperclip

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove Duplicates")

        self.input_label = QLabel("Enter a new line separated list:", self)
        self.input_label.setGeometry(10, 10, 250, 20)

        self.input_text_widget = QTextEdit(self)
        self.input_text_widget.setGeometry(10, 30, 250, 100)

        self.remove_button = QPushButton("Remove Duplicates", self)
        self.remove_button.setGeometry(10, 140, 120, 30)
        self.remove_button.clicked.connect(self.remove_duplicates)

        self.clear_button = QPushButton("Clear Input", self)
        self.clear_button.setGeometry(140, 140, 120, 30)
        self.clear_button.clicked.connect(self.clear_input)

        self.result_text_widget = QTextEdit(self)
        self.result_text_widget.setGeometry(10, 180, 250, 100)

        self.copy_button = QPushButton("Copy to Clipboard", self)
        self.copy_button.setGeometry(10, 290, 250, 30)
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        self.url_label = QLabel("<a href='https://github.com/mattsolution' style='color:#00ffff ' >https://github.com/mattsolution</a>", self)
        self.url_label.setGeometry(10, 330, 250, 30)
        self.url_label.setOpenExternalLinks(True)

    def remove_duplicates(self):
        input_text = self.input_text_widget.toPlainText()
        input_list = input_text.split('\n')

        unique_items = set()
        result_list = []

        for item in input_list:
            stripped_item = item.strip()
            if stripped_item and stripped_item not in unique_items:
                unique_items.add(stripped_item)
                result_list.append(stripped_item)

        self.result_text_widget.setPlainText('\n'.join(result_list))

    def clear_input(self):
        self.input_text_widget.clear()

    def copy_to_clipboard(self):
        result_text = self.result_text_widget.toPlainText()
        pyperclip.copy(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 270, 370)
    window.show()
    sys.exit(app.exec_())
