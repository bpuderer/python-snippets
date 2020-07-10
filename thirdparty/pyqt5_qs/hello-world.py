# Example code from Bo Milanovich's "Python Desktop Application Development"
# course on Pluralsight
# Completed 5/6/20
# Qt pronounced "cute"
from PyQt5.QtWidgets import *
import sys

# https://doc.qt.io/qt-5/qtwidgets-module.html

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # super(HelloWorld, self).__init__()

        # QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
        layout = QGridLayout()

        self.label = QLabel("<b>Hello World!</b>")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(self.label, 0, 0)  # row, column
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        # events/signals <---> handlers/slots
        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.change_text_label)


    def change_text_label(self, text):
        self.label.setText("Hello " + text + "!")


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
sys.exit(app.exec_())
