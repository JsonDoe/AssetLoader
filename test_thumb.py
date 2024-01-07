import sys
import requests
from PySide2.QtGui     import QPixmap, QScreen
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2 import QtCore


URL = 'http://openweathermap.org/img/wn/01d@2x.png'

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('getAndSetImageFromURL()')
        self.label  = QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = QPixmap()
        self.getAndSetImageFromURL(URL)
        self.resize(self.pixmap.width(),self.pixmap.height())
        screenSize = QScreen.availableGeometry(QApplication.primaryScreen())
        frmX = (screenSize.width () - self.width ())/2
        frmY = (screenSize.height() - self.height())/2
        self.move(frmX, frmY)
        self.show() 
    
    def getAndSetImageFromURL(self,imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        self.smaller_pixmap = self.pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.label.setPixmap(self.smaller_pixmap)
        self.label.setScaledContents(True)
        #QApplication.processEvents() # uncoment if executed on loop
    
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec_())