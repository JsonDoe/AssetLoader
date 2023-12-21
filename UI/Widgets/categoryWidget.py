from typing import Optional
from PySide2 import QtWidgets, QtCore, QtGui
import PySide2.QtGui
from pipelineCore.shotgrid.entity import Entity


class CategoryWidget(QtWidgets.QFrame):
    """Student Widget
    """
    def __init__(self, entity:Entity) -> None:
        super(CategoryWidget, self).__init__()

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

        print("selected %s" % self._entity)

        self.parent().parent().parent().parent().unSelectAll() # TODO adapt 

        if (event.button() == QtCore.Qt.LeftButton):
            self.widgetSelected.emit(self)
            self.selected = True
        
        self.parent().parent().parent().parent().handler.selectedCategory=self._entity

        print(self.parent().parent().parent().parent().handler.assets)



CategoryWidget.widgetSelected = QtCore.Signal(CategoryWidget)
