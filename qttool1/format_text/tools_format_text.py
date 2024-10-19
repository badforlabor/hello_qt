import os
import string
import sys
from os.path import dirname

from PySide6.QtGui import QAction, QIcon, QPixmap, QKeySequence
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtCore import QFile, Slot

from ui_format_text_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_doaction.clicked.connect(self.on_btn_clicked)

    @Slot()
    def on_btn_clicked(self):
        old = self.ui.txt_input.toPlainText()
        self.ui.txt_output.setText(formatText(old))
        pass

# 如果一行中的内容，都是数字，就删掉
def formatText(text: str):

    lines = text.splitlines(keepends=False);
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip(' ').isdigit():
            del lines[i]

    if len(lines) == 0:
        return ""

    return "\n".join(lines)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
