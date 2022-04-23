import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setGeometry(200,200,300,500)
        self.setToolTip('First app')
        self.setWindowTitle('First app')
        self.setWindowIcon(QIcon('feather.png'))
        self.initUI()

    def submit(self):
        print('Butona tiklandi , name : ' + self.txt_name.text() + ' surname : ' + self.txt_surname.text())
        self.label_result.setText(self.label_result.text() + ' name : ' + self.txt_name.text() + ' , surname : ' + self.txt_surname.text())

    def initUI(self):
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setText('Adiniz')
        self.label_name.move(50,50)

        self.label_surname = QtWidgets.QLabel(self)
        self.label_surname.setText('Soyadiniz')
        self.label_surname.move(50,100)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,50)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,100)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Kaydet')
        self.btn_save.move(150,150)
        self.btn_save.clicked.connect(self.submit)

        self.label_result = QtWidgets.QLabel(self)
        self.label_result.move(50,200)
        self.label_result.resize(200,32)
        self.label_result.setText('Sonuc : ')
    

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()