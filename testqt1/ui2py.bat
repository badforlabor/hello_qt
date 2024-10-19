
::layout
pyside6-uic mainwindow.ui -o ui_mainwindow.py
pyside6-uic format_text_window.ui -o ui_format_text_window.py

::rcc
pyside6-rcc icons.qrc -o rc_icons.py