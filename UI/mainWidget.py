from typing import Optional
from PySide2 import QtWidgets, QtGui, QtCore
from .categorySelectorWidgetView import CategorySelectorWidgetView
from .selectorWidgetModel import SelectorWidgetModel
from .assetSelectorWidgetView import AssetSelectorWidgetView
from .taskSelectorWidgetView import TaskSelectorWidgetView
from .publishSelectorWidgetView import PublishSelectorWidgetView
from .infoWidgetView import InfoWidgetView
from pipelineCore.maya import Loader
from UI.Dialogs import WarningDialog

class MainWidget(QtWidgets.QFrame):

    def __init__(self):
        super(MainWidget, self).__init__()

        self.handler = SelectorWidgetModel()
        self.loader = Loader()
        self.warDiag = WarningDialog(self)

        self.setWindowTitle("this is the main widget")
        self.initUI()
        self.setStyleSheet('''
            QFrame {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            }
                           
            QPushButton {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            }
            
            QMenu {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            }

            QAction {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            }

            QMessageBox{
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            }
            ''')

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

        self.createMenu()
        self.createButtons()

        self.slcLayout.addWidget(self.catSelectorWidget)
        self.slcLayout.addWidget(self.astSelectorWidget)
        self.slcLayout.addWidget(self.taskSelectorWidget)
        self.slcLayout.addWidget(self.pubSelectorWidget)

        self.slcContainerWidget = QtWidgets.QWidget()
        self.slcContainerWidget.setLayout(self.slcLayout)

        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.slcContainerWidget)
        self.splitter.addWidget(self.infoWidget)
        self.splitter.setSizes([1, 0])

        self.mainLayout.addWidget(self.splitter)
        self.mainLayout.addLayout(self.btnLayout)

        self.setLayout(self.mainLayout)

    def createButtons(self):

        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnLayout.setAlignment(QtCore.Qt.AlignRight)

        self.btnLoad = QtWidgets.QPushButton("Load")
        self.btnLoad.setMenu(self.menu)

        self.btnLayout.addWidget(self.btnLoad)

    def createMenu(self):
        """create the menu
        """
        self.createActions()
        self.menu = QtWidgets.QMenu("action")
        self.menu.addAction(self.loadAct)
        self.menu.addAction(self.loadWithNamespaceAct)
        self.menu.addAction(self.loadAsRefAct)


    def createActions(self):
        """create QActions for the menu
        """
        self.loadAct = QtWidgets.QAction("Load without namespace", self)
        self.loadAct.triggered.connect(self._loadBase)

        self.loadWithNamespaceAct = QtWidgets.QAction("Load with namespace", self)
        self.loadWithNamespaceAct.triggered.connect(self._loadWithNamespace)

        self.loadAsRefAct = QtWidgets.QAction("Load as reference", self)
        self.loadAsRefAct.triggered.connect(self._loadAsReference)

    def _loadBase(self):
        if self.handler.selectedPublish:
            self.loader.loadAsset(
                path=self.handler.selectedPublish.path)
        else: self.warDiag.BasicWarningDIag(
            title='Error', text='Please select a publish')
    
    def _loadWithNamespace(self):
        if self.handler.selectedPublish:
            self.loader.loadAssetWithNamespace(
                path=self.handler.selectedPublish.path,
                assetName=self.handler.selectedPublish.name)
        else: self.warDiag.BasicWarningDIag(
            title='Error', text='Please select a publish')
        

    def _loadAsReference(self):
        if self.handler.selectedPublish:
            self.loader.loadAssetAsReference(
                path=self.handler.selectedPublish.path,
                assetName=self.handler.selectedPublish.name)
        else: self.warDiag.BasicWarningDIag(
            title='Error', text='Please select a publish')
