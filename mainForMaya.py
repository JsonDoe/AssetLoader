from maya import OpenMayaUI
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
from UI.mainWindow import MainWindow


def maya_main_window():
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

gui = MainWindow(parent=maya_main_window())
gui.show()