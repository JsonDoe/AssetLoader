import sys
from PySide6 import QtWidgets
from UI.fileSelectorWidgetView import FileSelectorWidgetView

def __main__():
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle("fusion")

    #V load and apply the application style

    wid = FileSelectorWidgetView()
    
    wid.show()

    app.exec()

__main__()