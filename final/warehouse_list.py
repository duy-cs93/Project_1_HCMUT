import warehouse_db
import warehouse_edit
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

class warehouse_list(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Danh sách kho hàng')
        self.resize(800, 600)
        self.init_ui()
        
    def init_ui(self):   
        self.button = QtWidgets.QPushButton('Refresh',self)
        self.button.move(700, 1)
        self.button.clicked.connect(self.refresh)

        list_1,count_row = warehouse_db.select_all()   
        self.w_list = QtWidgets.QTableWidget(self)
        self.w_list.move(1, 25)
        self.w_list.resize(800, 600)
        self.w_list.setRowCount(count_row)
        self.w_list.setColumnCount(9)    
        self.w_list.setHorizontalHeaderLabels(["Code", "Quantity","",""])
        self.w_list.verticalHeader().hide()
        self.w_list.setColumnWidth(0, 200)
        self.w_list.setColumnWidth(1, 200)
        self.w_list.setColumnWidth(2, 200)  
        self.w_list.setColumnWidth(3, 200)

        self.w_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.w_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for i in range(0, count_row):
            self.w_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["product_code"])))
            self.w_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["inventory_number"])))
            self.w_list.setItem(i, 2, QtWidgets.QTableWidgetItem("Edit"))
            self.w_list.setItem(i, 3, QtWidgets.QTableWidgetItem("Delete"))
        self.w_list.cellClicked.connect(self.modify)

    def modify(self, row, column):
        if self.w_list.item(row, column).text() == 'Delete':
            warehouse_db.delete(self.w_list.item(row, 0).text())
            self.w_list.removeRow(row)
            self.confirm = confirm_form()
            self.confirm.show()
            
        elif self.w_list.item(row, column).text() == 'Edit':
            self.code = self.w_list.item(row, 0).text()
            self.number = self.w_list.item(row, 1).text()
            self.edit = warehouse_edit.warehouse_edit(self.code,self.number)
            self.edit.show()

    def refresh(self):   
        list_1,count_row = warehouse_db.select_all()
        self.w_list.setRowCount(count_row)
        for i in range(0, count_row):
            self.w_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["product_code"])))
            self.w_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["inventory_number"])))
            self.w_list.setItem(i, 3, QtWidgets.QTableWidgetItem("Edit"))
            self.w_list.setItem(i, 4, QtWidgets.QTableWidgetItem("Delete"))


class confirm_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Thông báo')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Đã xóa thông tin kho hàng này')
        self.button = QtWidgets.QPushButton('OK',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)