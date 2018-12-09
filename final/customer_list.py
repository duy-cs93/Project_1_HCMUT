import customer_db
import customer_edit
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

class customer_list(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Danh sách khách hàng')
        self.resize(800, 600)
        self.init_ui()
        
    def init_ui(self):   
        self.button = QtWidgets.QPushButton('Refresh',self)
        self.button.move(700, 1)
        self.button.clicked.connect(self.refresh)

        list_1,count_row = customer_db.select_all()   
        self.c_list = QtWidgets.QTableWidget(self)
        self.c_list.move(1, 25)
        self.c_list.resize(800, 600)
        self.c_list.setRowCount(count_row)
        self.c_list.setColumnCount(9)    
        self.c_list.setHorizontalHeaderLabels(["Code", "Name", "Address", "Phone", "Sex", "DOB", "DOP","",""])
        self.c_list.verticalHeader().hide()
        self.c_list.setColumnWidth(0, 50)
        self.c_list.setColumnWidth(1, 120)
        self.c_list.setColumnWidth(2, 200)  
        self.c_list.setColumnWidth(3, 100)
        self.c_list.setColumnWidth(4, 50)  
        self.c_list.setColumnWidth(5, 80)
        self.c_list.setColumnWidth(6, 80)  
        self.c_list.setColumnWidth(7, 50) 
        self.c_list.setColumnWidth(8, 50)
        self.c_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.c_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for i in range(0, count_row):
            self.c_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_code"])))
            self.c_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_name"])))
            self.c_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_address"])))
            self.c_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_phone"])))
            self.c_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_sex"])))
            self.c_list.setItem(i, 5, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_DOB"])))
            self.c_list.setItem(i, 6, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_DOP"])))
            self.c_list.setItem(i, 7, QtWidgets.QTableWidgetItem("Edit"))
            self.c_list.setItem(i, 8, QtWidgets.QTableWidgetItem("Delete"))
        self.c_list.cellClicked.connect(self.modify)

    def modify(self, row, column):
        if self.c_list.item(row, column).text() == 'Delete':
            customer_db.delete(self.c_list.item(row, 0).text())
            self.c_list.removeRow(row)
            self.confirm = confirm_form()
            self.confirm.show()
            
        elif self.c_list.item(row, column).text() == 'Edit':
            self.code = self.c_list.item(row, 0).text()
            self.name = self.c_list.item(row, 1).text()
            self.add = self.c_list.item(row, 2).text()
            self.phone = self.c_list.item(row, 3).text()
            self.sex = self.c_list.item(row, 4).text()
            self.DOB = self.c_list.item(row, 5).text()
            self.DOP = self.c_list.item(row, 6).text()
            self.edit = customer_edit.customer_edit(self.code,self.name,self.add,self.phone,self.sex,self.DOB,self.DOP)
            self.edit.show()

    def refresh(self):   
        list_1,count_row = customer_db.select_all()
        self.c_list.setRowCount(count_row)
        for i in range(0, count_row):
            self.c_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_code"])))
            self.c_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_name"])))
            self.c_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_address"])))
            self.c_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_phone"])))
            self.c_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_sex"])))
            self.c_list.setItem(i, 5, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_DOB"])))
            self.c_list.setItem(i, 6, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_DOP"])))
            self.c_list.setItem(i, 7, QtWidgets.QTableWidgetItem("Edit"))
            self.c_list.setItem(i, 8, QtWidgets.QTableWidgetItem("Delete"))    


class confirm_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Thông báo')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Đã xóa thông tin khách hàng này')
        self.button = QtWidgets.QPushButton('OK',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)