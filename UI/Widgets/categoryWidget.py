from typing import Optional
from PySide2 import QtWidgets, QtCore, QtGui
import PySide2.QtGui
from pipelineCore.shotgrid.entity import Entity


class CategoryWidget(QtWidgets.QFrame):
    """class to handle a category widget

    :param QtWidgets: PySde2 Widget
    :type QtWidgets: object
    """
    def __init__(self, entity:Entity) -> None:
        super(CategoryWidget, self).__init__()

        self._entity = entity

        self.selected = False

        self.initUI()

        self.setStyleSheet('''
                * ::hover {
                border-radius: 10px;
                background-color: rgb(74, 74, 74);
                font-family: 'Verdana';
                font-size: 12px;
                }
                QLabel {
                           background-color: transparent;
                }
                ''')
    


    def initUI(self):
        """creates and organizes the UI.
        """
        self.mainLayout = QtWidgets.QGridLayout()

        self.nameWidget = QtWidgets.QLabel(self._entity)
        # self.nameWidget.setObjectName("studentLabel")

        self.mainLayout.addWidget(self.nameWidget)

        self.setLayout(self.mainLayout)
    

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Define the widget reaction to click event

        :param event: click event
        :type event: QtGui.QMouseEvent
        """

        self.parent().parent().parent().parent().parent().unSelectAll() # TODO adapt 

        if (event.button() == QtCore.Qt.LeftButton):
            self.widgetSelected.emit(self)
            self.selected = True
            self.setStyleSheet('''
                * {
                    font-family: 'Verdana';
                    font-size: 12px;
                    border-radius: 10px;
                    background-color: rgb(74, 74, 74);
                    color :rgb(255, 255, 255)
                    }
                ''')
        
        self.parent().parent().parent().parent().parent().handler.selectedCategory=self._entity

        self.parent().parent().parent().parent().parent().refreshStyle()

        self.parent().parent().parent().parent().parent().assetView.refresh() # TODO adapt 


CategoryWidget.widgetSelected = QtCore.Signal(CategoryWidget)
