'''
Created on Dec 8, 2018

@author: USER
'''

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Add(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):

        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Tên sản phẩm')
        self.l1.move(110,110)
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(200,100,200,30)

        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Danh mục')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Nhãn hiệu')
        self.l3.move(110, 210)
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(200, 200, 200, 30)
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Giá')
        self.l4.move(110,260)
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(200, 250,200, 30)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Chi tiết')
        self.l5.move(110,310)
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(200, 300, 200, 30)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Hình')
        self.l5.move(110, 360)
        
        self.upload = QtWidgets.QPushButton('Upload hình',self)
        self.upload.move(300, 350)
        self.upload.clicked.connect(self.upload_hinh)
        
        self.button = QtWidgets.QPushButton('Insert',self)
        self.button.setGeometry(200, 400, 100, 30)
        
    def upload_hinh(self):
        self.image = QFileDialog.getOpenFileName(None,'OpenFile','',"Image file(*.jpg *gif *.png)")