import os
import string
import subprocess
import sys

from PySide6.QtGui import QAction, QIcon, QPixmap, QKeySequence
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtCore import QFile, Slot

# import fast_del
# import format_text
from format_text import *
from fast_del import *

from ui_main_window import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.format_text_wnd = None
        self.fast_del_wnd = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_format_text.triggered.connect(self.on_btn_action_format_text)
        self.ui.action_fast_del.triggered.connect(self.on_btn_action_fast_del)

    @Slot()
    def on_btn_action_format_text(self):
        if self.format_text_wnd == None:
            self.format_text_wnd = tools_format_text.MainWindow()
        self.format_text_wnd.hide()
        self.format_text_wnd.show()
        pass

    @Slot()
    def on_btn_action_fast_del(self):
        if self.fast_del_wnd == None:
            self.fast_del_wnd = fast_del_wnd.MainWindow()
        self.fast_del_wnd.hide()
        self.fast_del_wnd.show()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
