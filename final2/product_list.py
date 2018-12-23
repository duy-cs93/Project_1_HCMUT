import product_db
import product_edit
import csv
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

class product_list(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Danh sách sản phẩm')
        self.resize(800, 400)
        self.setStyleSheet('background-color:#1effff')
        self.init_ui()
        
    def init_ui(self):   
        # self.button = QtWidgets.QPushButton('Refresh',self)
        # self.button.move(600, 1)
        # self.button.clicked.connect(self.refresh)

        self.button = QtWidgets.QPushButton('Export CSV',self)
        self.button.move(700, 1)
        self.button.clicked.connect(self.export)

        list_1,count_row = product_db.select_all()   
        self.p_list = QtWidgets.QTableWidget(self)
        self.p_list.move(1, 25)
        self.p_list.resize(800, 400)
        self.p_list.setStyleSheet('background-color:white')
        self.p_list.setRowCount(count_row)
        self.p_list.setColumnCount(9)    
        self.p_list.setHorizontalHeaderLabels(["Code", "Name", "Category", "Image", "Brand", "Price", "Detail","",""])
        ############
        item0 = QtWidgets.QTableWidgetItem("Code")
        item0.setBackground(QtGui.QColor(0,255,0))
        self.p_list.setHorizontalHeaderItem(0,item0)
        item1 = QtWidgets.QTableWidgetItem("Name")
        item1.setBackground(QtGui.QColor(0,255,0))
        self.p_list.setHorizontalHeaderItem(1,item1)
        item2 = QtWidgets.QTableWidgetItem("Category")
        item2.setBackground(QtGui.QColor(0,255,0))
        self.p_list.setHorizontalHeaderItem(2,item2)
        item3 = QtWidgets.QTableWidgetItem("Image")
        item3.setBackground(QtGui.QColor(0,255,0))
        self.p_list.setHorizontalHeaderItem(3,item3)
        item4 = QtWidgets.QTableWidgetItem("Brand")
        item4.setBackground(QtGui.QColor(0,255,0))
        self.p_list.setHorizontalHeaderItem(4,item4)
        item5 = QtWidgets.QTableWidgetItem("Price")
        item5.setBackground(QtGui.QColor(0,255,0))
        self.p_list.setHorizontalHeaderItem(5,item5)
        item6 = QtWidgets.QTableWidgetItem("Detail")
        item6.setBackground(QtGui.QColor(0,255,0))
        self.p_list.setHorizontalHeaderItem(6,item6)
        ############
        self.p_list.verticalHeader().hide()
        self.p_list.setColumnWidth(0, 50)
        self.p_list.setColumnWidth(1, 120)
        self.p_list.setColumnWidth(2, 200)  
        self.p_list.setColumnWidth(3, 100)
        self.p_list.setColumnWidth(4, 50)  
        self.p_list.setColumnWidth(5, 80)
        self.p_list.setColumnWidth(6, 80)  
        self.p_list.setColumnWidth(7, 50) 
        self.p_list.setColumnWidth(8, 50)
        self.p_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.p_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for i in range(0, count_row):
            self.p_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["product_code"])))
            self.p_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["product_name"])))
            self.p_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(list_1[i]["product_category"])))
            self.p_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(list_1[i]["product_image"])))
            self.p_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(list_1[i]["product_brand"])))
            self.p_list.setItem(i, 5, QtWidgets.QTableWidgetItem(str(list_1[i]["product_price"])))
            self.p_list.setItem(i, 6, QtWidgets.QTableWidgetItem(str(list_1[i]["product_detail"])))
            self.p_list.setItem(i, 7, QtWidgets.QTableWidgetItem("Edit"))
            self.p_list.setItem(i, 8, QtWidgets.QTableWidgetItem("Delete"))
        self.p_list.cellClicked.connect(self.modify)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

    def modify(self, row, column):
        if self.p_list.item(row, column).text() == 'Delete':
            self.confirm_f = confirm_form()
            self.confirm_f.show()
            if self.confirm_f.exec_():
                product_db.delete(self.p_list.item(row, 0).text())
                self.p_list.removeRow(row)
                self.success_f = success_form()
                self.success_f.show()   
            
        elif self.p_list.item(row, column).text() == 'Edit':
            self.code = self.p_list.item(row, 0).text()
            self.name = self.p_list.item(row, 1).text()
            self.category = self.p_list.item(row, 2).text()
            self.image = self.p_list.item(row, 3).text()
            self.brand = self.p_list.item(row, 4).text()
            self.price = self.p_list.item(row, 5).text()
            self.detail = self.p_list.item(row, 6).text()
            self.edit = product_edit.product_edit(self.code,self.name,self.category,self.image,self.brand,self.price,self.detail)
            self.edit.show()

    def refresh(self):   
        list_1,count_row = product_db.select_all()
        self.p_list.setRowCount(count_row)
        for i in range(0, count_row):
            self.p_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["product_code"])))
            self.p_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["product_name"])))
            self.p_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(list_1[i]["product_category"])))
            self.p_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(list_1[i]["product_image"])))
            self.p_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(list_1[i]["product_brand"])))
            self.p_list.setItem(i, 5, QtWidgets.QTableWidgetItem(str(list_1[i]["product_price"])))
            self.p_list.setItem(i, 6, QtWidgets.QTableWidgetItem(str(list_1[i]["product_detail"])))
            self.p_list.setItem(i, 7, QtWidgets.QTableWidgetItem("Edit"))
            self.p_list.setItem(i, 8, QtWidgets.QTableWidgetItem("Delete"))    

    def export(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV',os.getenv('HOME'),'CSV(*.csv)')
        if path[0] != '':
            header = ["Code", "Name", "Category", "Image", "Brand", "Price", "Detail"]
            with open(path[0],'w',newline ='') as csv_file:
                writer = csv.writer(csv_file,dialect ='excel')
                writer.writerow(i for i in header)
                for row in range(self.p_list.rowCount()):
                    row_data = []
                    for column in range(self.p_list.columnCount()-2):
                        item = self.p_list.item(row, column)
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
        self.setWindowTitle('Xác nhận')
        self.resize(250, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Bạn muốn xóa thông tin sản phẩm này?')
        self.button_1 = QtWidgets.QPushButton('OK',self)
        self.button_1.move(50, 60)
        self.button_1.clicked.connect(self.accept)
        self.button_2 = QtWidgets.QPushButton('Cancel',self)
        self.button_2.move(130, 60)
        self.button_2.clicked.connect(self.reject)


class success_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()   

    def init_ui(self): 
        self.setWindowTitle('Thông báo')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Đã xóa thông tin sản phẩm')
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(20, 60)
        self.button.clicked.connect(self.close)