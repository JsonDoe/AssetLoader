import os
from.mainWidget import MainWidget
from PySide2 import QtWidgets, QtGui, QtCore
from UI.utils.folderPath import UTILSPATH


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Asset Loader 1.0")
        self.setWindowIcon(QtGui.QIcon(
              UTILSPATH + os.path.sep + 'loading'))
        self.setMinimumSize(700, 300)
        self.initUI()
        self._createMenus()
        self.setStyleSheet('''             
            QToolBar {
                   font-family: 'Verdana';
                    font-size: 12px;
                    background-color : rgb(40, 40, 40);
                    color :rgb(255, 255, 255)        
            };
            ''')

    def initUI(self):
        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)


    def _createMenus(self):
        """Create the diverses menus, status menus and adding actions to it.
        """
        #create the menu bar
        self.toolbar = QtWidgets.QToolBar("My main toolbar")
        self.toolbar.setIconSize(QtCore.QSize(32,32))
        self.addToolBar(self.toolbar)

        self.buttonClose = QtWidgets.QAction(QtGui.QIcon(QtGui.QIcon(
              UTILSPATH + os.path.sep + 'switch1')), "Close", self)
        self.buttonClose.setStatusTip("Click here to close")
        self.buttonClose.triggered.connect(self._onClickClose)

        self.buttonHome = QtWidgets.QAction(QtGui.QIcon(QtGui.QIcon(
              UTILSPATH + os.path.sep + 'home')), "Home", self)
        self.buttonHome.setStatusTip("Click here to close")
        self.buttonHome.triggered.connect(self._onClickHome)

        self.toolbar.addAction(self.buttonClose)
        self.toolbar.addAction(self.buttonHome)
        self.toolbar.setMovable(False)
    
    def _onClickClose(self):
        self.close()

    def _onClickHome(self):
        self.mainWidget.catSelectorWidget.unSelectAll()
        self.mainWidget.catSelectorWidget.refresh()
        self.mainWidget.catSelectorWidget.searchbar.setText("")

