import bill_db, bill_detail_db
import csv
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap


class Bill(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Bill, self).__init__(parent)
        self.title = "Hóa đơn"
        self.width = 800
        self.height = 600
        self.b_list = None
        self.init_ui()

    def init_ui(self):
        self.button = QtWidgets.QPushButton('Export to CSV',self)
        self.button.move(700, 1)
        self.button.clicked.connect(self.export)

        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        list_1, count_row = bill_db.select_all()
        self.b_list = QtWidgets.QTableWidget(self)
        self.b_list.move(1, 30)
        self.b_list.resize(800, 600)
        self.b_list.setRowCount(count_row)
        self.b_list.setColumnCount(9)
        self.b_list.setHorizontalHeaderLabels(["Bill code",
                                               "Employee code",
                                               "Date",
                                               "Time",
                                               "Customer code",
                                               "Total cost",
                                               "Discount",
                                               "Bill cost",
                                               "Bill note"])
        self.b_list.verticalHeader().hide()
        self.b_list.setColumnWidth(0, 50)
        self.b_list.setColumnWidth(1, 120)
        self.b_list.setColumnWidth(2, 200)
        self.b_list.setColumnWidth(3, 100)
        self.b_list.setColumnWidth(4, 50)
        self.b_list.setColumnWidth(5, 80)
        self.b_list.setColumnWidth(6, 80)
        self.b_list.setColumnWidth(7, 50)
        self.b_list.setColumnWidth(8, 50)
        self.b_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.b_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for i in range(0, count_row):
            self.b_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(list_1[i]["bill_code"])))
            self.b_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(list_1[i]["employee_code"])))
            self.b_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(list_1[i]["bill_date"])))
            self.b_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(list_1[i]["bill_time"])))
            self.b_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(list_1[i]["customer_code"])))
            self.b_list.setItem(i, 5, QtWidgets.QTableWidgetItem(str(list_1[i]["total_cost"])))
            self.b_list.setItem(i, 6, QtWidgets.QTableWidgetItem(str(list_1[i]["discount"])))
            self.b_list.setItem(i, 7, QtWidgets.QTableWidgetItem(str(list_1[i]["bill_cost"])))
            self.b_list.setItem(i, 8, QtWidgets.QTableWidgetItem(str(list_1[i]["bill_note"])))


    def export(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV',os.getenv('HOME'),'CSV(*.csv)')
        if path[0] != '':
            header = ["Code", "Employee","Date", "Time","Customer", "Total","Discount", "Cost","Note"]
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
