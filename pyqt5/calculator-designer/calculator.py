from email.mime import application
from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec_())


window()