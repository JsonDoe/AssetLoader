from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .selectorWidgetModel import SelectorWidgetModel
from .Widgets.thumbnail import Thumbnail


class InfoWidgetView(QtWidgets.QWidget):
    """Class to handle the info UI
    """
    def __init__(
            self, model:SelectorWidgetModel):
        super(InfoWidgetView, self).__init__()

        self.init = 0
        self.pixmap = None
        self.handler = model
        self.setWindowTitle("this is the beginning")
        self.initUI()
        self.setStyleSheet('''
            QWidget {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            };
            ''')
        self.setMinimumWidth(250)

    def initUI(self):
        """creates and organizes the UI
        """

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        
        self.listLayout = QtWidgets.QVBoxLayout()
        self.listLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.menuLayout = QtWidgets.QHBoxLayout()
        self.menuLayout.setAlignment(QtCore.Qt.AlignLeft)

        self.titleWidget = QtWidgets.QLabel("Infos:")
        self.menuLayout.addWidget(self.titleWidget)

        self.setupInfoLayout(self.listLayout)

        self.container = QtWidgets.QWidget()
        self.container.setLayout(self.listLayout)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.container)

        self.mainLayout.addLayout(self.menuLayout)
        self.mainLayout.addWidget(self.scrollArea)

        self.setLayout(self.mainLayout)

    """
    def getAndSetImageFromURL(self,imageURL):

        thumbWidget = QtWidgets.QWidget()

        label  = QtWidgets.QLabel(thumbWidget)
        self.pixmap = QtGui.QPixmap()
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        self.smaller_pixmap = self.pixmap.scaled(
            150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        label.setPixmap(self.smaller_pixmap)
        label.setScaledContents(True)

        thumbWidget.resize(self.pixmap.width(),self.pixmap.height())
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        thumbWidget.setLayout(layout)

        return thumbWidget
    """

    def setupInfoLayout(self, parent:QtWidgets.QVBoxLayout) -> None:
        """create the different entity widgets to the parent layout

        :parent: (QtWidgets.QVBoxLayout): parent of the widget
        """
        if self.handler.selectedPublish is not None:

            self.info0 = QtWidgets.QLabel(
                "File name: %s" % self.handler.selectedPublish.name)
            parent.addWidget(self.info0)

            self.info5 = QtWidgets.QLabel(
                "Created at: %s" % self.handler.selectedPublish.createdAt)
            parent.addWidget(self.info5)

            self.info1 = QtWidgets.QLabel(
                "File type: %s" % self.handler.selectedPublish.publishType)
            parent.addWidget(self.info1)

            self.info2 = QtWidgets.QLabel(
                "version number: %s" % str(
                    self.handler.selectedPublish.versionNumber))
            parent.addWidget(self.info2)

            self.info3 = QtWidgets.QLabel(
                "Task: %s(%s)" % (
                    self.handler.selectedTask.name,
                    self.handler.selectedTask.status))
            parent.addWidget(self.info3)

            self.info4 = QtWidgets.QLabel(
                "Path: %s" % self.handler.selectedPublish.path)
            parent.addWidget(self.info4)

    def refresh(self):
        """refresh the diverses widgets from the list
        """
        for obj in reversed(range(self.listLayout.count())):
            # Get the widget of the layout item.
            widget = self.listLayout.itemAt(obj).widget()
            #delete the widget (by removing parent) 
            widget.setParent(None)
        self.setupInfoLayout(self.listLayout)
