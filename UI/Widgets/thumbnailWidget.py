from functools import cached_property
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest


class ImageDownloader(QtCore.QObject):
    finished = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager.finished.connect(self.handle_finished)

    @cached_property
    def manager(self):
        return QNetworkAccessManager()

    def start_download(self, url):
        self.manager.get(QNetworkRequest(url))

    def handle_finished(self, reply):
        if reply.error() != QNetworkReply.NoError:
            print("error: ", reply.errorString())
            return
        image = QtGui.QImage()
        image.loadFromData(reply.readAll())
        self.finished.emit(image)


class ThumbnailWidget(QtWidgets.QWidget):
    def __init__(self, URL:str, parent=None):
        super().__init__(parent)
        self.url = URL
        self.label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignLeft)

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addWidget(self.label)

        self.downloader = ImageDownloader()
        self.downloader.finished.connect(self.handle_finished)
        self.handle_clicked()

        self.setLayout(self.mainLayout)
        self.resize(200, 200)

    def handle_finished(self, image):
        pixmap = QtGui.QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

    def handle_clicked(self):
        url = QtCore.QUrl.fromUserInput(self.url)
        self.downloader.start_download(url)
