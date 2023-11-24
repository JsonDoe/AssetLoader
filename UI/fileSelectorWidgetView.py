from typing import Optional
from PySide6 import QtWidgets, QtGui, QtCore
from .fileSelectorWidgetHandler import FileSelectorWidgetHandler
from .Widgets.entityWidget import EntityWidget


class FileSelectorWidgetView(QtWidgets.QFrame):

    def __init__(self, handler=FileSelectorWidgetHandler):
        super(FileSelectorWidgetView, self).__init__()

        self.handler = handler
        self.setWindowTitle("this is the beginning ")
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

        self.titleWidget        = QtWidgets.QLabel("Category:")
        self.menuLayout.addWidget(self.titleWidget)

        self.createEntityWidgets(self.listLayout)

        self.container = QtWidgets.QFrame()
        self.container.setLayout(self.listLayout)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.container)

        self.mainLayout.addLayout(self.menuLayout)
        self.mainLayout.addWidget(self.scrollArea)

        self.setLayout(self.mainLayout)

        

    def createEntityWidgets(self, parent:QtWidgets.QVBoxLayout) -> None:
        """create the different entity widgets to the parent layout

        :parent: (QtWidgets.QVBoxLayout): parent of the widget
        """
        for category in self.handler._categories:
            parent.addWidget(EntityWidget(category))


