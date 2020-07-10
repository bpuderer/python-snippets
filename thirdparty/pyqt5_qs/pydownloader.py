# Example code from Bo Milanovich's "Python Desktop Application Development"
# course on Pluralsight
# Completed 5/6/20
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import urllib.request

# https://doc.qt.io/qt-5/qtwidgets-module.html

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("PyDownloader")

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse =  QPushButton("Browse")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)


    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As",
                                                directory=".", filter="All Files (*.*)")
        self.save_location.setText(QDir.toNativeSeparators(save_file[0]))


    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return

        QMessageBox.information(self, "Information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")


    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percentage = readsofar * 100 / totalsize
            self.progress.setValue(int(percentage))




app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()
