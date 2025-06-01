import sys
from PySide6 import QtWidgets,QtCore

class Doc(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("here")


        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.button)

        

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    Ui = Doc()
    Ui.resize(500,200)
    Ui.show()
    sys.exit(app.exec())