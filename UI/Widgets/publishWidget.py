from typing import Optional
from PySide2 import QtWidgets, QtCore, QtGui
import PySide2.QtGui
from pipelineCore.shotgrid.publishedFile import PublishedFile


class PublishWidget(QtWidgets.QFrame):
    """class to handle a category widget

    :param QtWidgets: PySde2 Widget
    :type QtWidgets: object
    """
    def __init__(self, publish:PublishedFile) -> None:
        super(PublishWidget, self).__init__()

        self._publish = publish

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

        self.nameWidget = QtWidgets.QLabel(self._publish.name)

        self.mainLayout.addWidget(self.nameWidget)

        self.setLayout(self.mainLayout)

        self.setAcceptDrops(True)
    

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Define the widget reaction to click event

        :param event: click event
        :type event: QtGui.QMouseEvent
        """

        self.parent().parent().parent().parent().parent().unSelectAll()

        if (event.button() == QtCore.Qt.LeftButton or QtCore.Qt.RightButton):
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
        
        self.parent().parent().parent().parent().parent().handler.selectedPublish = self._publish

        self.parent().parent().parent().parent().parent().refreshStyle()

        self.parent().parent().parent().parent().parent().infoView.refresh()

    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.RightButton:
                drag = QtGui.QDrag(self)
                mime = QtCore.QMimeData()
                drag.setMimeData(mime)
                drag.exec_(QtCore.Qt.MoveAction)
                print("dragged")
                self.parent().parent().parent().parent().parent(
                ).parent().parent().parent()._loadBase()

PublishWidget.widgetSelected = QtCore.Signal(PublishWidget)
