from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetView import CategorySelectorWidgetView
from .categorySelectorWidgetModel import CategorySelectorWidgetModel
from .assetSelectorWidgetView import AssetSelectorWidgetView
from .taskSelectorWidgetView import TaskSelectorWidgetView
from .publishSelectorWidgetView import PublishSelectorWidgetView


class MainWidget(QtWidgets.QFrame):

    def __init__(self):
        super(MainWidget, self).__init__()

        self.handler = CategorySelectorWidgetModel()

        self.setWindowTitle("this is the main widget")
        self.initUI()

    def initUI(self):
        """creates and organizes the UI
        """
        self.mainLayout = QtWidgets.QHBoxLayout()

        catSelectorWidget = CategorySelectorWidgetView(self.handler)

        astSelectorWidget = AssetSelectorWidgetView(self.handler)

        taskSelectorWidget = TaskSelectorWidgetView(self.handler)

        pubSelectorWidget = PublishSelectorWidgetView(self.handler)

        self.mainLayout.addWidget(catSelectorWidget)
        self.mainLayout.addWidget(astSelectorWidget)
        self.mainLayout.addWidget(taskSelectorWidget)
        self.mainLayout.addWidget(pubSelectorWidget)

        self.setLayout(self.mainLayout)