import sys
import requests
from PySide2.QtGui     import QPixmap, QScreen
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2 import QtCore


URL = 'https://sg-media-ireland.s3-accelerate.amazonaws.com/52a5da8d7d1471cb1b595ed4fb7ec9d0a8c7f8bb/bb30ee30140916601847770bb9165d072d5d63d9/da25c933ca63d451_RIG_bob.v001.jpg?response-content-disposition=filename%3D%22da25c933ca63d451_RIG_bob.v001.jpg%22&x-amz-meta-user-id=453&x-amz-meta-user-type=HumanUser&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJG6Z4JIV2PVJ4MO%2F20240104%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240104T132228Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIQD7PHxsV10Ds8dGMuVDhRdSzAs7X2KAXTpv2eCDmxPfzQIfY8TIZF5GL5Br4NWi5DpSNJdj7UIzirSsa3xhMrtAZiqYAgh2EAAaDDU2OTU1MDQzMDgwMSIMAOT2quUQUYJ%2BnhUqKvUBJ1KbrdtDm2GjNwnBQ8oZvR1QNLa1OKKXp7URFMxPMWtzBRPjwDFHe3rDwGdi2qbn2PTDA%2F4v%2B38vluAcmv3T0JVeuvjKzy5T8ByyAANrRC%2BSWdFOYnaI3uqgHXoNefjzIMOOrpj%2FjMJm4xnumrknj1pxHocVJqqe2cKZftvFvOuh%2BmFunA5RqwD7hvx%2FvNFYLUMxECIYiBIf0HgAQdq4%2FjUSZ8x3CTSyuOwmIudd4q5AcScPQulRzfk7F3EApsG7ut6fkZiXcwz009PJzof9HhQjY2vlhP5MAbIce2Zf2c0lwmJoDv8aIRTSHyJkmWnDWZ6RVWIwz83arAY6ngHshD%2BFV5cybAfalydNkTBo3SPcptd6xrHypgGhjUIODTMpOR0xyGSGdYNbnjcQXI4%2ByhMd7QxAs6hcAZU%2FIM3nqgcAFDC9NkmFfl6TR6hgqFnRWhKNUOGOTzABDBL3WeNXVewW0AGsfbMfwTNNq8b3kqgMTNPLL55twbPA6YPYkBr444flp5C1JVJjk7iOVc1uFSqGEnI%2FKDwkv6bRlg%3D%3D&X-Amz-Signature=dde2551270a30edc0fc05d31acd9a4e8b8cb2bea458c1dfeffc8566e70f29307'
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('getAndSetImageFromURL()')
        self.label  = QLabel(self)
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
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        #QApplication.processEvents() # uncoment if executed on loop
    
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec_())