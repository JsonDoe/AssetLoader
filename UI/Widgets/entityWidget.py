from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui
import PySide6.QtGui
from pipelineCore.shotgrid.entity import Entity


class EntityWidget(QtWidgets.QFrame):
    """Student Widget
    """
    def __init__(self, entity:Entity) -> None:
        super(EntityWidget
        , self).__init__()

        self._entity = entity

        self.selected = False

        self.initUI()

    def initUI(self):
        """creates and organizes the UI.
        """
        self.mainLayout = QtWidgets.QGridLayout()

        self.nameWidget = QtWidgets.QLabel(self._entity)
        # self.nameWidget.setObjectName("studentLabel")

        self.mainLayout.addWidget(self.nameWidget)

        self.setLayout(self.mainLayout)
    

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:

        print("selected")
        """
        self.parent().parent().parent().parent().unSelectAll() # TODO adapt 

        if (event.button() == QtCore.Qt.LeftButton):
            self.widgetSelected.emit(self)
            self.selected = True
        """


# EntityWidget.widgetSelected = QtCore.Signal(EntityWidget)
