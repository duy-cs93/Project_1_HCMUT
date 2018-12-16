import warehouse_db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

class warehouse_edit(QDialog):
    def __init__(self,code,number):
       	super().__init__()
        self.setWindowTitle('Cập nhật thông tin khách hàng')
        self.code = code
        self.number = number
        self.init_ui()
        
    def init_ui(self):       
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Mã sản phẩm')
        self.l1.move(110, 110)
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(200, 100, 200, 30)
        self.line_edit1.setText(self.code)
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Số lượng')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        self.line_edit2.setText(self.number)
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        self.button.setGeometry(200, 450, 100, 30)
        self.button.clicked.connect(self.insert)
    
    def insert(self):
        warehouse_list, warehouse_count = warehouse_db.select(self.line_edit1.text())
        if self.line_edit1.text() != self.code:
            self.error = error_form('Sai mã sản phẩm')
            self.error.show()
        elif self.line_edit1.text() == '':
            self.error = error_form('Vui lòng nhập mã sản phẩm')
            self.error.show()
        elif self.line_edit2.text() == '':
            self.error = error_form('Vui lòng nhập số lượng sản phẩm')
            self.error.show()
        else: 
            warehouse_db.update(self.line_edit1.text(),self.line_edit2.text(),self.code)
            self.error = success_form()
            self.error.show()
            self.close()
        

class error_form(QDialog):
    def __init__(self,text):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Lỗi')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(50, 30)
        self.l1.setText(self.text)
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)


class success_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Thông báo')
        self.resize(250, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Đã cập nhật thông tin kho hàng')
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)