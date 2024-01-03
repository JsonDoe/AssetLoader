import sys
from PySide2 import QtWidgets
from UI.mainWindow import MainWindow

def __main__():
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle("fusion")

    #V load and apply the application style

    wid = MainWindow()
    
    wid.show()

    app.exec_()

__main__()