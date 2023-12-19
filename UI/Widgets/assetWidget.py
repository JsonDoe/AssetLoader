from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui
import PySide6.QtGui
from pipelineCore.shotgrid.asset import Asset


class AssetWidget(QtWidgets.QFrame):
    """Student Widget
    """
    def __init__(self, asset:Asset) -> None:
        super(AssetWidget, self).__init__()

        self._asset = asset

        self.selected = False

        self.initUI()

    def initUI(self):
        """creates and organizes the UI.
        """
        self.mainLayout = QtWidgets.QGridLayout()

        self.nameWidget = QtWidgets.QLabel(self._asset.name)
        # self.nameWidget.setObjectName("studentLabel")

        self.mainLayout.addWidget(self.nameWidget)

        self.setLayout(self.mainLayout)
    

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:

        print("selected %s" % self._asset)

        self.parent().parent().parent().parent().unSelectAll() # TODO adapt 

        if (event.button() == QtCore.Qt.LeftButton):
            self.widgetSelected.emit(self)
            self.selected = True
        
        self.parent().parent().parent().parent().handler.selectedAsset = self._asset

        # print(self.parent().parent().parent().parent().handler.assets)


AssetWidget.widgetSelected = QtCore.Signal(AssetWidget)
