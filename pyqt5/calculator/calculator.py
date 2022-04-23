import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from functools import partial

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setGeometry(200,200,300,500)
        self.setToolTip('Calculator')
        self.setWindowTitle('Calculator')
        self.initUI()

    def calculate(self,value):

        result = 0

        if(value == ' Toplama'):
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
            self.label_sonuc.setText('Sonuc : ' + str(result))
        elif(value == 'Cikarma'):
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
            self.label_sonuc.setText('Sonuc : ' + str(result))
        elif(value == 'Carpma'):
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
            self.label_sonuc.setText('Sonuc : ' + str(result))
        elif(value == 'Bolme'):
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
            self.label_sonuc.setText('Sonuc : ' + str(result))
        

    def initUI(self):
        self.label_sayi1 = QtWidgets.QLabel(self)
        self.label_sayi1.setText('Sayi 1 : ')
        self.label_sayi1.move(50,50)

        self.label_sayi2 = QtWidgets.QLabel(self)
        self.label_sayi2.setText('Sayi 2 : ')
        self.label_sayi2.move(50,100)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,50)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,100)

        self.button_toplama = QtWidgets.QPushButton(self)
        self.button_toplama.setText('Toplama')
        self.button_toplama.move(150,150)
        self.button_toplama.clicked.connect(partial(self.calculate, 'Toplama'))

        self.button_cikarma = QtWidgets.QPushButton(self)
        self.button_cikarma.setText('Cikarma')
        self.button_cikarma.move(150,200)
        self.button_cikarma.clicked.connect(partial(self.calculate, 'Cikarma'))

        self.button_carpma = QtWidgets.QPushButton(self)
        self.button_carpma.setText('Carpma')
        self.button_carpma.move(150,250)
        self.button_carpma.clicked.connect(partial(self.calculate, 'Carpma'))

        self.button_bolme = QtWidgets.QPushButton(self)
        self.button_bolme.setText('Bolme')
        self.button_bolme.move(150,300)
        self.button_bolme.clicked.connect(partial(self.calculate, 'Bolme'))

        self.label_sonuc = QtWidgets.QLabel(self)
        self.label_sonuc.setText('Sonuc : ')
        self.label_sonuc.move(150,350)
        self.label_sonuc.resize(200,32)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()