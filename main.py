import sys
from PySide2 import QtWidgets
from UI.mainWidget import MainWidget

def __main__():
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle("fusion")

    #V load and apply the application style

    wid = MainWidget()
    
    wid.show()

    app.exec_()

__main__()