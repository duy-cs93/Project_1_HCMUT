import customer_db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

class customer_add(QDialog):
    def __init__(self):
       	super().__init__()
        self.setWindowTitle('Thông tin khách hàng mới')
        self.init_ui()
        
    def init_ui(self):       
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Mã khách hàng')
        self.l1.move(110, 110)
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(200, 100, 200, 30)
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Tên khách hàng')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Địa chỉ')
        self.l3.move(110, 210)
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(200, 200, 200, 30)
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Số điện thoại')
        self.l4.move(110, 260)
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(200, 250, 200, 30)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Giới tính')
        self.l5.move(110, 310)
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(200, 300, 200, 30)
        
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText('Ngày sinh')
        self.l6.move(110, 360)
        self.line_edit6 = QtWidgets.QLineEdit(self)
        self.line_edit6.setGeometry(200, 350, 200, 30)

        self.l7 = QtWidgets.QLabel(self)
        self.l7.setText('Ngày tham gia')
        self.l7.move(110, 410)
        self.line_edit7 = QtWidgets.QLineEdit(self)
        self.line_edit7.setGeometry(200, 400, 200, 30)
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        self.button.setGeometry(200, 450, 100, 30)
        self.button.clicked.connect(self.insert)
    
    def insert(self):
        customer_list, customer_count = customer_db.select(self.line_edit1.text())
        if customer_count != 0:
            self.error = error_form('Mã khách hàng đã tồn tại')
            self.error.show()
        elif self.line_edit1.text() == '':
            self.error = error_form('Vui lòng nhập mã khách hàng')
            self.error.show()
        elif self.line_edit2.text() == '':
            self.error = error_form('Vui lòng nhập tên khách hàng')
            self.error.show()
        else: 
            customer_db.insert(self.line_edit1.text(),self.line_edit2.text(),self.line_edit3.text(),self.line_edit4.text(),self.line_edit5.text(),self.line_edit6.text(),self.line_edit7.text())
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
        self.l1.setText('Đã thêm vào danh sách khách hàng')
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)