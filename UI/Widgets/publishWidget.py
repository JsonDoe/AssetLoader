from typing import Optional
from PySide2 import QtWidgets, QtCore, QtGui
import PySide2.QtGui
from pipelineCore.shotgrid.publishedFile import PublishedFile


class PublishWidget(QtWidgets.QFrame):
    """Student Widget
    """
    def __init__(self, publish:PublishedFile) -> None:
        super(PublishWidget, self).__init__()

        self._publish = publish

        self.selected = False

        self.initUI()

    def initUI(self):
        """creates and organizes the UI.
        """
        self.mainLayout = QtWidgets.QGridLayout()

        self.nameWidget = QtWidgets.QLabel(self._publish.name)

        self.mainLayout.addWidget(self.nameWidget)

        self.setLayout(self.mainLayout)
    

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:

        print("selected %s" % self._publish)

        # self.parent().parent().parent().parent().unSelectAll() # TODO adapt 

        if (event.button() == QtCore.Qt.LeftButton):
            self.widgetSelected.emit(self)
            self.selected = True
        
        self.parent().parent().parent().parent().handler.selectedPublish = self._publish

        self.parent().parent().parent().parent().infoView.refresh()

PublishWidget.widgetSelected = QtCore.Signal(PublishWidget)
