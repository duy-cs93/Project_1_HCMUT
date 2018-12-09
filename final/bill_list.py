import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import bill_db, bill_detail_db


class Bill(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Bill, self).__init__(parent)
        self.title = "Hóa đơn"
        self.width = 800
        self.height = 600
        self.b_list = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        list_1, count_row = bill_db.select_all()
        self.b_list = QtWidgets.QTableWidget(self)
        self.b_list.move(1, 1)
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


    def add_tab(self):
        tab = QtWidgets.QTabWidget()
        tab_inner = QtWidgets.QWidget()
        tab.addTab(tab_inner, "tab")

