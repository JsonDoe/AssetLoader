from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetModel import CategorySelectorWidgetModel
from .infoWidgetView import InfoWidgetView
from .Widgets.publishWidget import PublishWidget


class PublishSelectorWidgetView(QtWidgets.QFrame):

    def __init__(self, model:CategorySelectorWidgetModel, view):
        super(PublishSelectorWidgetView, self).__init__()

        self.handler = model
        self.infoView = view
        self.setWindowTitle("this is the task selector")
        self.initUI()
        self.setStyleSheet('''
            QWidget {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            };
            ''')


    def initUI(self):
        """creates and organizes the UI
        """
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        
        self.listLayout = QtWidgets.QVBoxLayout()
        self.listLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.menuLayout         = QtWidgets.QHBoxLayout()
        self.menuLayout.setAlignment(QtCore.Qt.AlignLeft)

        self.titleWidget        = QtWidgets.QLabel("Publishes:")
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
        if self.handler.selectedTask is not None:
            publishes = self.handler.publishedFiles
            for pub in publishes:
                parent.addWidget(PublishWidget(pub))

    def refreshStyle(self):
        for i in range(self.listLayout.count()):
            if self.listLayout.itemAt(i).widget().selected == False:
                self.listLayout.itemAt(i).widget().setStyleSheet('''
	                        QLabel {
                                font-family: 'Verdana';
                                font-size: 12px;
                            }
                            ''')


    def unSelectAll(self):
        """unselect all the objects
        """
        for i in range(self.listLayout.count()):
            self.listLayout.itemAt(i).widget().selected = False
        self.handler.selectedPublish = None


    def refresh(self):
        print(self.handler.selectedTask)
        #print(self.handler.assets)
        for obj in reversed(range(self.listLayout.count())):
            # Get the widget of the layout item.
            widget = self.listLayout.itemAt(obj).widget()
            #delete the widget (by removing parent) 
            widget.setParent(None)
        
        self.createEntityWidgets(self.listLayout)

        self.infoView.refresh()

        print("refreshed")

    def _onClickButton(self):
        self.refresh()
