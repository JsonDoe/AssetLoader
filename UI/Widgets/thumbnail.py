import sys
from PySide2 import QtCore, QtGui, QtWidgets 


class Thumbnail(QtWidgets.QWidget):

    def __init__(self, URL):
        super().__init__()
        self.URL = URL
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('getAndSetImageFromURL()')
        self.label  = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = QtGui.QPixmap()
        self.getAndSetImageFromURL(self.URL)
        self.resize(self.pixmap.width(),self.pixmap.height())
        screenSize = QtGui.QScreen.availableGeometry(
            QtWidgets.QApplication.primaryScreen())
        frmX = (screenSize.width () - self.width ())/2
        frmY = (screenSize.height() - self.height())/2
        self.move(frmX, frmY)

    
    def getAndSetImageFromURL(self,imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        self.smaller_pixmap = self.pixmap.scaled(
            50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.label.setPixmap(self.smaller_pixmap)
        self.label.setScaledContents(True)
        #QApplication.processEvents() # uncoment if executed on loop
    