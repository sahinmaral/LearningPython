import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import QPalette,QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100,100,500,500)

        # Vertical and horizontal layout

        # layout = QtWidgets.QHBoxLayout()
   
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('green'))

        # button = QtWidgets.QPushButton()
        # button.setText('Testing')
        # layout.addWidget(button)

        layout = QtWidgets.QGridLayout()
   
        layout.addWidget(Color('red'),0,0)
        layout.addWidget(Color('blue'),0,1)
        layout.addWidget(Color('green'),0,2)
        layout.addWidget(Color('yellow'),1,2)
        

        widget = QWidget()
        widget.setLayout(layout)

        # widget = Color('blue')
        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

app()