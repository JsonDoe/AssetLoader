from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetView import CategorySelectorWidgetView
from .categorySelectorWidgetModel import CategorySelectorWidgetModel
from .assetSelectorWidgetView import AssetSelectorWidgetView
from .taskSelectorWidgetView import TaskSelectorWidgetView
from .publishSelectorWidgetView import PublishSelectorWidgetView
from .infoWidgetView import InfoWidgetView
from pipelineCore.maya import Loader

class MainWidget(QtWidgets.QFrame):

    def __init__(self):
        super(MainWidget, self).__init__()

        self.handler = CategorySelectorWidgetModel()
        self.loader = Loader()

        self.setWindowTitle("this is the main widget")
        self.initUI()

    def initUI(self):
        """creates and organizes the UI
        """
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.slcLayout = QtWidgets.QHBoxLayout()

        self.infoWidget = InfoWidgetView(self.handler)
        self.pubSelectorWidget = PublishSelectorWidgetView(
            self.handler, self.infoWidget)
        self.taskSelectorWidget = TaskSelectorWidgetView(
            self.handler, self.pubSelectorWidget)
        self.astSelectorWidget = AssetSelectorWidgetView(
            self.handler, self.taskSelectorWidget)
        self.catSelectorWidget = CategorySelectorWidgetView(
            self.handler, self.astSelectorWidget)

        self.createButtons()


        self.slcLayout.addWidget(self.catSelectorWidget)
        self.slcLayout.addWidget(self.astSelectorWidget)
        self.slcLayout.addWidget(self.taskSelectorWidget)
        self.slcLayout.addWidget(self.pubSelectorWidget)
        self.slcLayout.addWidget(self.infoWidget)

        self.mainLayout.addLayout(self.slcLayout)
        self.mainLayout.addLayout(self.btnLayout)

        self.setLayout(self.mainLayout)

    def createButtons(self):

        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnLayout.setAlignment(QtCore.Qt.AlignRight)

        self.btnLoad = QtWidgets.QPushButton("Load")
        self.btnLoad.clicked.connect(self.loadButton)

        self.btnLayout.addWidget(self.btnLoad)

    def loadButton(self):
        if self.handler.selectedPublish:
            self.loader.loadScene(path=self.handler.selectedPublish.path)
        else: print("Please select a Publish")