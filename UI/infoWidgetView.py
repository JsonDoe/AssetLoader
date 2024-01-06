from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetModel import CategorySelectorWidgetModel
from .Widgets.categoryWidget import CategoryWidget


class InfoWidgetView(QtWidgets.QFrame):

    def __init__(
            self, model:CategorySelectorWidgetModel):
        super(InfoWidgetView, self).__init__()

        self.init = 0
        self.handler = model
        self.setWindowTitle("this is the beginning")
        self.initUI()

    def initUI(self):
        """creates and organizes the UI
        """
        self.setMinimumWidth(400)

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

    def setupInfoLayout(self, parent:QtWidgets.QVBoxLayout) -> None:
        """create the different entity widgets to the parent layout

        :parent: (QtWidgets.QVBoxLayout): parent of the widget
        """
        if self.handler.selectedPublish is not None:
            print(self.handler.selectedPublish.publishedFileType)
            self.info0 = QtWidgets.QLabel(
                "File name: %s" % self.handler.selectedPublish.name)
            parent.addWidget(self.info0)

            self.info1 = QtWidgets.QLabel(
                "File type: %s" % self.handler.selectedPublish.publishType)
            parent.addWidget(self.info1)

            self.info2 = QtWidgets.QLabel(
                "version number: %s" % str(self.handler.selectedPublish.versionNumber))
            parent.addWidget(self.info2)

            self.info3 = QtWidgets.QLabel(
                "task: %s(%s)" % (
                    self.handler.selectedTask.name,
                    self.handler.selectedTask.status))
            parent.addWidget(self.info3)

            self.info4 = QtWidgets.QLabel(
                "path: %s" % self.handler.selectedPublish.path)
            parent.addWidget(self.info4)


    def refresh(self):
        for obj in reversed(range(self.listLayout.count())):
            # Get the widget of the layout item.
            widget = self.listLayout.itemAt(obj).widget()
            #delete the widget (by removing parent) 
            widget.setParent(None)
        self.setupInfoLayout(self.listLayout)