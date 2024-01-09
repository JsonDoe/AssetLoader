from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetModel import CategorySelectorWidgetModel
from .assetSelectorWidgetView import AssetSelectorWidgetView
from .Widgets.categoryWidget import CategoryWidget


class CategorySelectorWidgetView(QtWidgets.QFrame):
    """Class to handle the category selection UI
    """
    def __init__(
            self, model:CategorySelectorWidgetModel,
            assetView:AssetSelectorWidgetView):
        super(CategorySelectorWidgetView, self).__init__()

        self.handler = model
        self.assetView = assetView
        self.setWindowTitle("this is the beginning ")
        self.initUI()
        self.setStyleSheet('''
            QWidget {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            };
            ''')
        self.setMinimumWidth(160)

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

        self.searchbar = QtWidgets.QLineEdit()
        self.searchbar.textChanged.connect(self.update_display)
        self.searchbar.setPlaceholderText("Search Category")
        self.searchbar.setMaximumHeight(35)
        self.searchbar.setMinimumHeight(35)

        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.addWidget(self.scrollArea)
        self.splitter.addWidget(self.searchbar)
        self.splitter.setSizes([1, 0])

        self.mainLayout.addLayout(self.menuLayout)
        self.mainLayout.addWidget(self.splitter)

        self.setLayout(self.mainLayout)


    def createEntityWidgets(self, parent:QtWidgets.QVBoxLayout) -> None:
        """create the different entity widgets to the parent layout

        :parent: (QtWidgets.QVBoxLayout): parent of the widget
        """
        for category in self.handler.categories:
            parent.addWidget(CategoryWidget(category))
        parent.addWidget(CategoryWidget("Sequence"))

    def refreshStyle(self):
        """refresh the style sheet of the widgets from the list layout
        """
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
        self.handler.selectedCategory   = None
        self.handler.selectedAsset      = None
        self.handler.selectedTask       = None
        self.handler.selectedPublish    = None

    def refresh(self):
        """refresh the diverses widgets from the list
        """
        for obj in reversed(range(self.listLayout.count())):
            # Get the widget of the layout item.
            widget = self.listLayout.itemAt(obj).widget()
            #delete the widget (by removing parent) 
            widget.setParent(None)
        self.assetView.refresh()

        self.createEntityWidgets(self.listLayout)
    
    def update_display(self, text):
        """update the display depending of the entered 

        :param text: text currently entered in the QLineEdit
        :type text: str
        """
        for obj in reversed(range(self.listLayout.count())):
            widget = self.listLayout.itemAt(obj).widget()
            if text.lower() in widget.nameWidget.text().lower():
                widget.show()
            else:
                widget.hide()