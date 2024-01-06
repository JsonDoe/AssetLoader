from PySide2 import QtWidgets, QtCore, QtGui
import PySide2.QtGui


class WarningDialog():
    def __init__(self, parent=None) -> None:
        self.parent = parent

    def BasicWarningDIag(self, title:str="Warning", text="Error"):
        dlg = QtWidgets.QMessageBox(self.parent)
        dlg.setWindowTitle(title)
        dlg.setText(text)
        dlg.setStandardButtons(
            QtWidgets.QMessageBox.Ok)
        dlg.setIcon(QtWidgets.QMessageBox.Warning)
        dlg.exec()
