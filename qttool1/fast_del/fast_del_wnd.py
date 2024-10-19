import os
import string
import subprocess
import sys

from PySide6.QtGui import QAction, QIcon, QPixmap, QKeySequence
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtCore import QFile, Slot

import format_text.tools_format_text
from format_text.tools_format_text import formatText
from ui_fast_del_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_do.clicked.connect(self.on_btn_clicked)

    @Slot()
    def on_btn_clicked(self):
        # file:///D:/liu/Downloads/
        # self.ui.edt_path
        text = self.ui.edt_path.toPlainText()
        lines = text.splitlines(keepends=False)
        for i in range(len(lines)):
            delFolder(lines[i])

        pass

def delFolder(txt:string):
    if txt.startswith("file:///"):
        txt = txt.replace("file:///", "")

    txt = txt.replace("/", "\\")
    cmd = "rmdir /s /q \"" + txt + "\""

    # 执行命令
    print("pending exec:", cmd)
    result, val = subprocess.getstatusoutput(cmd)
    if result == 0:
        print("succ, cmd=", cmd)
    else:
        print("failed, result=", result, val)

    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
