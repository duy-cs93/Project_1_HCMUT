'''
Created on Dec 14, 2018

@author: USER
'''
import employee_db
import employee_edit
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

import os
import csv

class employee_list(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Danh sách nhân viên')
        self.resize(800, 400)
        self.setStyleSheet('background-color:qlineargradient(spread:pad, x1:0.45,y1:0.3695,x2:0.426\
        ,y2:0,stop:0 rgba(0,170,255,255),stop:1 rgba(255,255,255,255))')
        self.init_ui()
        
    def init_ui(self):       
        self.button = QtWidgets.QPushButton('Refresh',self)
        self.button.move(700, 1)
        self.button.clicked.connect(self.refresh)
        
        self.btn_exp = QtWidgets.QPushButton('Export',self)
        self.btn_exp.move(600,1)
        self.btn_exp.clicked.connect(self.save_sheet)
                    
        list_1,count_row = employee_db.select_all()   
        self.e_list = QtWidgets.QTableWidget(self)
        self.e_list.move(1, 25)
        self.e_list.resize(800, 600)
        self.e_list.setStyleSheet('background-color:white')
        self.e_list.setRowCount(count_row)
        self.e_list.setColumnCount(10)    
        self.e_list.setHorizontalHeaderLabels(["Code", "Name","Sex","Address", "Phone", "DOB", "FWD","salary","",""])
        #########
        item0 = QtWidgets.QTableWidgetItem("Code")
        item0.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(0,item0)
        item1 = QtWidgets.QTableWidgetItem("Name")
        item1.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(1,item1)
        item2 = QtWidgets.QTableWidgetItem("Sex")
        item2.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(2,item2)
        item3 = QtWidgets.QTableWidgetItem("Address")
        item3.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(3,item3)
        item4 = QtWidgets.QTableWidgetItem("Phone")
        item4.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(4,item4)
        item5 = QtWidgets.QTableWidgetItem("DOB")
        item5.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(5,item5)
        item6 = QtWidgets.QTableWidgetItem("FWD")
        item6.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(6,item6)
        item7 = QtWidgets.QTableWidgetItem("salary")
        item7.setBackground(QtGui.QColor(0,255,0))
        self.e_list.setHorizontalHeaderItem(7,item6)
        ###########
        self.e_list.verticalHeader().hide()
        self.e_list.setColumnWidth(0, 50)
        self.e_list.setColumnWidth(1, 120)
        self.e_list.setColumnWidth(2, 50)  
        self.e_list.setColumnWidth(3, 150)
        self.e_list.setColumnWidth(4, 60)  
        self.e_list.setColumnWidth(5, 80)
        self.e_list.setColumnWidth(6, 80)  
        self.e_list.setColumnWidth(7, 60) 
        self.e_list.setColumnWidth(8, 50)
        self.e_list.setColumnWidth(9, 50)
        self.e_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.e_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for i in range(0, count_row):
            self.e_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_code"])))
            self.e_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_name"])))
            self.e_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_sex"])))
            self.e_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_address"])))
            self.e_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_phone"])))
            self.e_list.setItem(i, 5, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_DOB"])))
            self.e_list.setItem(i, 6, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_FWD"])))
            self.e_list.setItem(i, 7, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_salary"])))  
            self.e_list.setItem(i, 8, QtWidgets.QTableWidgetItem("Edit"))
            #######
            item_del = QtWidgets.QTableWidgetItem("Delete")
            item_del.setBackground(QtGui.QColor(255,0,0))
            self.e_list.setItem(i, 9, item_del)
            #######
        self.e_list.cellClicked.connect(self.modify)
        
    def modify(self, row, column):
        if self.e_list.item(row, column).text() == 'Delete':
            employee_db.delete(self.e_list.item(row, 0).text())
            self.e_list.removeRow(row)
            self.confirm = confirm_form()
            self.confirm.show()
            
        elif self.e_list.item(row, column).text() == 'Edit':
            self.code = self.e_list.item(row, 0).text()
            self.name = self.e_list.item(row, 1).text()
            self.sex = self.e_list.item(row, 2).text()
            self.add = self.e_list.item(row, 3).text()
            self.phone = self.e_list.item(row, 4).text()
            self.DOB = self.e_list.item(row, 5).text()
            self.FWD = self.e_list.item(row, 6).text()
            self.salary = self.e_list.item(row, 7).text()    
            self.edit = employee_edit.employee_edit(self.code,self.name,self.sex,self.add,self.phone,self.DOB,self.FWD,self.salary)
            self.edit.show()

    def refresh(self):   
        list_1,count_row = employee_db.select_all()
        self.e_list.setRowCount(count_row)
        for i in range(0, count_row):
            self.e_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_code"])))
            self.e_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_name"])))
            self.e_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_sex"])))
            self.e_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_address"])))
            self.e_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_phone"])))
            self.e_list.setItem(i, 5, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_DOB"])))
            self.e_list.setItem(i, 6, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_FWD"])))
            self.e_list.setItem(i, 7, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_salary"])))
            self.e_list.setItem(i, 8, QtWidgets.QTableWidgetItem("Edit"))
            self.e_list.setItem(i, 9, QtWidgets.QTableWidgetItem("Delete"))    
            
    
    def save_sheet(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV',os.getenv('HOME'),'CSV(*.csv)')
        if path[0] != '':
            header = ["Code", "Name","Sex","Address", "Phone", "DOB", "FWD","salary","",""]
            with open(path[0],'w',newline ='') as csv_file:
                writer = csv.writer(csv_file,dialect ='excel')
                writer.writerow(i for i in header)
                for row in range(self.e_list.rowCount()):
                    row_data = []
                    for column in range(self.e_list.columnCount()):
                        item = self.e_list.item(row, column)
                        if item is not None:
                            row_data.append(str(item.text()))
                        else:
                            row_data.append('')
                    writer.writerow(row_data)                
        
class confirm_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Thông báo')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Đã xóa thông tin nhân viên này')
        self.button = QtWidgets.QPushButton('OK',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)