from typing import Optional
from PySide6 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetView import CategorySelectorWidgetView
from .categorySelectorWidgetModel import CategorySelectorWidgetModel
from .assetSelectorWidgetView import AssetSelectorWidgetView
from .taskSelectorWidgetView import TaskSelectorWidgetView


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

        self.mainLayout.addWidget(catSelectorWidget)
        self.mainLayout.addWidget(astSelectorWidget)
        self.mainLayout.addWidget(taskSelectorWidget)

        self.setLayout(self.mainLayout)