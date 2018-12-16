import warehouse_db
import warehouse_edit
import csv
import os
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
        # self.button = QtWidgets.QPushButton('Refresh',self)
        # self.button.move(600, 1)
        # self.button.clicked.connect(self.refresh)

        self.button = QtWidgets.QPushButton('Export to CSV',self)
        self.button.move(700, 1)
        self.button.clicked.connect(self.export)

        list_1,count_row = warehouse_db.select_all()   
        self.w_list = QtWidgets.QTableWidget(self)
        self.w_list.move(1, 25)
        self.w_list.resize(800, 600)
        self.w_list.setRowCount(count_row)
        self.w_list.setColumnCount(4)    
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

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

    def modify(self, row, column):
        if self.w_list.item(row, column).text() == 'Delete': 
            self.confirm_f = confirm_form()
            self.confirm_f.show()
            if self.confirm_f.exec_():
                warehouse_db.delete(self.w_list.item(row, 0).text())
                self.w_list.removeRow(row)
                self.success_f = success_form()
                self.success_f.show()
            
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
            self.w_list.setItem(i, 2, QtWidgets.QTableWidgetItem("Edit"))
            self.w_list.setItem(i, 3, QtWidgets.QTableWidgetItem("Delete"))

    def export(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV',os.getenv('HOME'),'CSV(*.csv)')
        if path[0] != '':
            header = ["Code", "Quantity"]
            with open(path[0],'w',newline ='') as csv_file:
                writer = csv.writer(csv_file,dialect ='excel')
                writer.writerow(i for i in header)
                for row in range(self.w_list.rowCount()):
                    row_data = []
                    for column in range(self.w_list.columnCount()-2):
                        item = self.w_list.item(row, column)
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
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Bạn muốn xóa thông tin kho hàng này?')
        self.button_1 = QtWidgets.QPushButton('OK',self)
        self.button_1.move(20, 60)
        self.button_1.clicked.connect(self.accept)
        self.button_2 = QtWidgets.QPushButton('Cancel',self)
        self.button_2.move(100, 60)
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
        self.l1.setText('Đã xóa thông tin kho hàng')
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(20, 60)
        self.button.clicked.connect(self.close)