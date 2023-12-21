from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetModel import CategorySelectorWidgetModel
from .taskSelectorWidgetView import TaskSelectorWidgetView
from .Widgets.assetWidget import AssetWidget


class AssetSelectorWidgetView(QtWidgets.QFrame):

    def __init__(
            self, model:CategorySelectorWidgetModel,
            taskView:TaskSelectorWidgetView):
        super(AssetSelectorWidgetView, self).__init__()

        self.taskView = taskView
        self.handler = model
        self.setWindowTitle("this is the asset selector")
        self.initUI()

    

    def initUI(self):
        """creates and organizes the UI
        """
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        
        self.listLayout = QtWidgets.QVBoxLayout()
        self.listLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.menuLayout         = QtWidgets.QHBoxLayout()
        self.menuLayout.setAlignment(QtCore.Qt.AlignLeft)

        self.titleWidget        = QtWidgets.QLabel("Assets:")
        self.menuLayout.addWidget(self.titleWidget)

        self.createEntityWidgets(self.listLayout)

        self.container = QtWidgets.QFrame()
        self.container.setLayout(self.listLayout)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.container)

        self.button = QtWidgets.QPushButton("refresh")
        self.button.clicked.connect(self._onClickButton)

        self.mainLayout.addLayout(self.menuLayout)
        self.mainLayout.addWidget(self.scrollArea)
        self.mainLayout.addWidget(self.button)

        self.setLayout(self.mainLayout)


    def createEntityWidgets(self, parent:QtWidgets.QVBoxLayout) -> None:
        """create the different entity widgets to the parent layout

        :parent: (QtWidgets.QVBoxLayout): parent of the widget
        """
        if self.handler.selectedCategory is not None:
            assets = self.handler.assets
            for asset in assets:
                parent.addWidget(AssetWidget(asset))

    def unSelectAll(self):
        """unselect all the objects
        """
        for i in range(self.listLayout.count()):
            self.listLayout.itemAt(i).widget().selected = False
        self.handler.selectedAsset = None
        self.handler.selectedTask = None
        self.handler.selectedPublish = None

        self.refresh()

    def refresh(self):
        print(self.handler.selectedCategory)
        #print(self.handler.assets)
        for obj in reversed(range(self.listLayout.count())):
            # Get the widget of the layout item.
            widget = self.listLayout.itemAt(obj).widget()
            #delete the widget (by removing parent) 
            widget.setParent(None)

        self.taskView.refresh()

        self.createEntityWidgets(self.listLayout)

        print("refreshed")


    def _onClickButton(self):
        self.refresh()
