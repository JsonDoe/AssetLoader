import sys
from functools import cached_property

from PySide6.QtCore import Signal, QObject, Qt, QUrl
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class ImageDownloader(QObject):
    finished = Signal(QImage)

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
        image = QImage()
        image.loadFromData(reply.readAll())
        self.finished.emit(image)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineedit = QLineEdit()
        self.button = QPushButton("Start")
        self.label = QLabel(alignment=Qt.AlignCenter)

        lay = QGridLayout(self)
        lay.addWidget(self.lineedit, 0, 0)
        lay.addWidget(self.button, 0, 1)
        lay.addWidget(self.label, 1, 0, 1, 2)

        self.downloader = ImageDownloader()

        self.downloader.finished.connect(self.handle_finished)
        self.button.clicked.connect(self.handle_clicked)

        self.lineedit.setText("http://openweathermap.org/img/wn/01d@2x.png")

        self.resize(300, 300)

    def handle_finished(self, image):
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

    def handle_clicked(self):
        url = QUrl.fromUserInput(self.lineedit.text())
        self.downloader.start_download(url)


def main():
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()