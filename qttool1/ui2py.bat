
::layout
pyside6-uic main_window.ui -o ui_main_window.py
pyside6-uic format_text/format_text_window.ui -o format_text/ui_format_text_window.py
pyside6-uic fast_del/fast_del_window.ui -o fast_del/ui_fast_del_window.py

::rcc
pyside6-rcc icons.qrc -o rc_icons.py