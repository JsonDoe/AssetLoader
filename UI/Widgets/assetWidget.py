from typing import Optional
from PySide2 import QtWidgets, QtCore, QtGui
import PySide2.QtGui
from pipelineCore.shotgrid.asset import Asset


class AssetWidget(QtWidgets.QFrame):
    """Class to handle asset widgets 
    """
    def __init__(self, asset:Asset) -> None:
        super(AssetWidget, self).__init__()

        self._asset = asset

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

        self.nameWidget = QtWidgets.QLabel(self._asset.name)
        # self.nameWidget.setObjectName("studentLabel")

        self.mainLayout.addWidget(self.nameWidget)

        self.setLayout(self.mainLayout)
    

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Define the widget reaction to click event

        :param event: click event
        :type event: QtGui.QMouseEvent
        """

        self.parent().parent().parent().parent().parent().unSelectAll()

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
        
        self.parent().parent().parent().parent().parent().handler.selectedAsset = self._asset

        self.parent().parent().parent().parent().parent().refreshStyle()

        self.parent().parent().parent().parent().parent().taskView.refresh()


AssetWidget.widgetSelected = QtCore.Signal(AssetWidget)
