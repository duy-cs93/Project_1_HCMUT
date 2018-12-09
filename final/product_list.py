import product_db
import product_edit
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
        self.resize(800, 600)
        self.init_ui()
        
    def init_ui(self):   
        self.button = QtWidgets.QPushButton('Refresh',self)
        self.button.move(700, 1)
        self.button.clicked.connect(self.refresh)

        list_1,count_row = product_db.select_all()   
        self.p_list = QtWidgets.QTableWidget(self)
        self.p_list.move(1, 25)
        self.p_list.resize(800, 600)
        self.p_list.setRowCount(count_row)
        self.p_list.setColumnCount(9)    
        self.p_list.setHorizontalHeaderLabels(["Code", "Name", "Category", "Image", "Brand", "Price", "Detail","",""])
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

    def modify(self, row, column):
        if self.p_list.item(row, column).text() == 'Delete':
            product_db.delete(self.p_list.item(row, 0).text())
            self.p_list.removeRow(row)
            self.confirm = confirm_form()
            self.confirm.show()
            
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


class confirm_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Thông báo')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Đã xóa thông tin sản phẩm này')
        self.button = QtWidgets.QPushButton('OK',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)