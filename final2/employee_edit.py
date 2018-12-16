import employee_db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

class employee_edit(QDialog):
    def __init__(self,code,name,sex,add,phone,DOB,FWD,salary):
       	super().__init__()
        self.setWindowTitle('Cập nhật thông tin nhân viên')
        self.code = code
        self.name = name
        self.sex = sex
        self.add = add
        self.phone = phone
        self.DOB = DOB
        self.FWD = FWD 
        self.salary = salary
        self.setStyleSheet('background-color:qlineargradient(spread:pad, x1:0.45,y1:0.3695,x2:0.426\
        ,y2:0,stop:0 rgba(0,170,255,255),stop:1 rgba(255,255,255,255))')
        self.init_ui()
        
    def init_ui(self):       
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Mã nhân viên')
        self.l1.move(110, 110)
        self.l1.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(210, 105, 200, 30)
        self.line_edit1.setText(self.code)
        self.line_edit1.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')

        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Tên nhân viên')
        self.l2.move(110, 160)
        self.l2.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(210, 155, 200, 30)
        self.line_edit2.setText(self.name)
        self.line_edit2.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Giới tính')
        self.l3.move(110, 210)
        self.l3.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(210, 205, 200, 30)
        self.line_edit3.setText(self.sex)
        self.line_edit3.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Địa chỉ')
        self.l4.move(110, 260)
        self.l4.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(210, 255, 200, 30)
        self.line_edit4.setText(self.add)
        self.line_edit4.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Số điện thoại')
        self.l5.move(110, 310)
        self.l5.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(210, 305, 200, 30)
        self.line_edit5.setText(self.phone)
        self.line_edit5.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText('Ngày sinh')
        self.l6.move(110, 360)
        self.l6.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit6 = QtWidgets.QLineEdit(self)
        self.line_edit6.setGeometry(210, 355, 200, 30)
        self.line_edit6.setText(self.DOB)
        self.line_edit6.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')

        self.l7 = QtWidgets.QLabel(self)
        self.l7.setText('Ngày vào làm')
        self.l7.move(110, 410)
        self.l7.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit7 = QtWidgets.QLineEdit(self)
        self.line_edit7.setGeometry(210, 405, 200, 30)
        self.line_edit7.setText(self.FWD)
        self.line_edit7.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l8 = QtWidgets.QLabel(self)
        self.l8.setText('Lương')
        self.l8.move(110, 460)
        self.l8.setStyleSheet('background-color:#f7f7f7;color:black;font-size:14px;bold 14px')
        self.line_edit8 = QtWidgets.QLineEdit(self)
        self.line_edit8.setGeometry(210, 455, 200, 30)
        self.line_edit8.setText(self.salary)
        self.line_edit8.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        self.button.setGeometry(200, 505, 100, 30)
        self.button.clicked.connect(self.insert)
        self.button.setStyleSheet('color:#fafafa;font-size =15px;font: bold 14px;background-color:qlineargradient(spread:pad, x1:0.45,y1:0.3695,x2:0.426\
        ,y2:0,stop:0 rgba(255,170,0,228),stop:1 rgba(255,255,255,255));border-radius:10px;border:none')
    
    def insert(self):
        employee_list, employee_count = employee_db.select(self.line_edit1.text())
        if self.line_edit1.text() != self.code:
            self.error = error_form('Sai mã nhân viên')
            self.error.show()
        elif self.line_edit1.text() == '':
            self.error = error_form('Vui lòng nhập mã nhân viên')
            self.error.show()
        elif self.line_edit2.text() == '':
            self.error = error_form('Vui lòng nhập tên nhân viên')
            self.error.show()
        else: 
            employee_db.update(self.line_edit1.text(),self.line_edit2.text(),self.line_edit3.text(),self.line_edit4.text(),self.line_edit5.text(),self.line_edit6.text(),self.line_edit7.text(),self.line_edit8.text(),self.code)
            self.error = success_form()
            self.error.show()
            self.close()
        

class error_form(QDialog):
    def __init__(self,text):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Lá»—i')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(50, 30)
        self.l1.setText(self.text)
        self.button = QtWidgets.QPushButton('Ä�Ã³ng',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)


class success_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('ThÃ´ng bÃ¡o')
        self.resize(250, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Ä�Ã£ cáº­p nháº­t thÃ´ng tin khÃ¡ch hÃ ng')
        self.button = QtWidgets.QPushButton('Ä�Ã³ng',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)