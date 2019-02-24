import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap
from email.charset import QP
import datetime
import copy
from colorama import Fore
from colorama import Style

from read_json import *
from MyTable import *
from Add import *

import bill_db, bill_detail_db, product_db, warehouse_db, customer_db, employee_db
import bill_list, bill_detail_list
import customer_add, customer_list
import product_add, product_list
import warehouse_add, warehouse_list
import employee_list, employee_add
import invoice
import new_user


class Login(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = "Log in"
        self.left = 380
        self.top = 220
        self.width = 250
        self.height = 220
        self.setStyleSheet('background-color:#1effff')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.move(self.left, self.top)
        self.setFixedSize(self.width, self.height)
        # font = QtGui.QFont("Arial", 11, QtGui.QFont.Bold)
        # self.setFont(font)

        # add logo
        bk_logo = QtWidgets.QLabel(self)
        bk_pic = QtGui.QPixmap("bachkhoa.png")
        bk_pic2 = bk_pic.scaled(64, 64)
        bk_logo.setPixmap(bk_pic2)
        bk_logo.move(180, 0)

        # color = QtGui.QColor(30, 255, 255)
        self.setAutoFillBackground(True)
        p = self.palette()
        # p.setColor(self.backgroundRole(), color)
        self.setPalette(p)

        # create label 1
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText('Tên đăng nhập')
        self.label_1.setStyleSheet('color:black;font-size:15px;bold 12px;font :15pt Comic Sans MS')
        self.label_1.move(30, 40)
        # Create ID text box 1
        self.user_text = QtWidgets.QLineEdit(self)
        self.user_text.move(30, 70)
        self.user_text.resize(190, 25)
        self.user_text.setStyleSheet('background-color:#64ff64; color:#000000;padding-top:0px;'
                                     'font-size:10px;padding-left:10px;font: bold 12px')

        # create label 2
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText('Mật khẩu')
        self.label_2.move(30, 110)
        self.label_2.setStyleSheet('color:black;font-size:15px;bold 12px;font :15pt Comic Sans MS')
        # Create password text box 2
        self.password_text = QtWidgets.QLineEdit(self)
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.move(30, 140)
        self.password_text.resize(190, 25)
        self.password_text.setStyleSheet('background-color:#64ff64; color:#000000;padding-top:0px;font-size:10px;padding-left:10px;font: bold 12px')

        # Create New user button in the window
        self.btn_new_user = QtWidgets.QPushButton('User mới', self)
        self.btn_new_user.move(20, 180)
        self.btn_new_user.resize(70, 30)
        self.btn_new_user.setStyleSheet('background-color:#4e4e4e; color:#fafafa ; font-size =15px; border = 1px solid #4e4e4e;border-radius:10px;font: bold 14px')

	self.btn_new_user.clicked.connect(self.show_new_user)

        # Create Log in button in the window
        self.button = QtWidgets.QPushButton('Đăng nhập', self)
        self.button.move(130, 180)
        self.button.resize(80, 30)
        self.button.setStyleSheet('background-color:#4e4e4e; color:#fafafa ; font-size =15px; border = 1px solid #4e4e4e;border-radius:10px;font: bold 14px')
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        self.close()
        list_json = read_json()
        flag = False
        for item in list_json:
            for i in list_json[item]:
                if i[0] == self.user_text.text() and i[1] == self.password_text.text():
                    flag = True
        if flag:
            self.main = MainWindow()
            self.main.show()
        else:
            self.error = QtWidgets.QErrorMessage()
            self.error.showMessage('Tên đăng nhập và mật khẩu chưa đúng !')
            self.error.setWindowTitle('Error')

    def show_new_user(self):
        self.close()
        self.new_user = new_user.new_user()
        self.new_user.show()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title = "Quản lý bán hàng"
        self.setStyleSheet('background-color:#1effff')
        self.width = 1050
        self.height = 600
        # self.amount_of_products = 0  # this variable is used for counting the number of purchased item
        self.discount_percentage = 0
        self.total_cost = None
        self.discount_cost = None
        self.already_added_row = []
        self.bill = None
        self.bill_detail = None
        self.bill_info = None
        self.bill_detail_info = None
        self.employee_code = None
        self.customer_code = None
        self.product_list_db, self.product_amount_entry = product_db.select_all()  # get the product list from database
        self.product_name_list = [self.product_list_db[member]["product_name"] for member in range(self.product_amount_entry)]
        self.warehouse_list_db, self.warehouse_amount_entry = warehouse_db.select_all()
        self.customer_list, self.customer_amount_entry = customer_db.select_all()
        self.employee_list, self.employee_amount_entry = employee_db.select_all()

        # Pre-initialize gui variables *
        # Buttons **
        self.search_btn = None
        self.add_product_btn = None
        self.add_tab_btn = None
        self.charge_btn = None
        # Labels & Combobox **
        self.total_price = None
        self.total_price_value = None
        self.discount = None
        self.discount_value = None
        self.actual_money = None
        self.actual_money_value = None
        self.payed_money = None
        self.payed_money_value = None
        self.change_money = None
        self.change_money_value = None

        # Edit box
        self.search_box = None  # search box
        self.model = QtCore.QStringListModel(self)
        self.model.setStringList([self.product_list_db[member]["product_name"]
                                  for member in range(self.product_amount_entry)])
        # print(self.model.stringList())
        self.completer = QtWidgets.QCompleter(self)
        self.completer.setModel(self.model)

        # Table
        self.purchased_list = None
        self.product_list = None

        self.init_ui()
        self.show()

    def init_ui(self):
        print('vao main')
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.statusBar().showMessage("Hello Customers! Our best wishes to you!")
        # self.setStyleSheet('background-color:qlineargradient(spread:pad, x1:0.45,y1:0.3695,x2:0.426\
        #         ,y2:0,stop:0 rgba(0,170,255,255),stop:1 rgba(255,255,255,255))')
        # self.setStyleSheet('background-color:white')

        #create menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightgray,stop:1 darkgray)')
        
        self.thoat = QtWidgets.QMenu("Thoát", self.menubar)
        exitApp = QAction("&Exit", self)
        exitApp.setShortcut("Ctrl+Q")
        exitApp.setStatusTip("ExitApplication")
        exitApp.triggered.connect(self.close)
        self.thoat.addAction(exitApp)
        self.menubar.addAction(self.thoat.menuAction())

        self.khach_hang = QtWidgets.QMenu('Khách hàng', self.menubar)
        self.add_khach_hang = QtWidgets.QAction('Thêm khách hàng', self)
        self.add_khach_hang.triggered.connect(self.show_add_c)
        self.list_khach_hang = QtWidgets.QAction('Danh sách khách hàng', self)
        self.list_khach_hang.triggered.connect(self.show_list_c)
        self.khach_hang.addAction(self.add_khach_hang)
        self.khach_hang.addAction(self.list_khach_hang)
        self.menubar.addAction(self.khach_hang.menuAction())

        # self.nhan_vien = QtWidgets.QMenu('Nhân viên', self.menubar)
        # self.add_nhan_vien = QtWidgets.QAction('Thêm nhân viên', self)
        # self.add_nhan_vien.triggered.connect(self.show_add_e)
        # self.list_nhan_vien = QtWidgets.QAction('List nhân viên', self)
        # self.list_nhan_vien.triggered.connect(self.show_list_e)
        # self.nhan_vien.addAction(self.add_nhan_vien)
        # self.nhan_vien.addAction(self.list_nhan_vien)
        # self.menubar.addAction(self.nhan_vien.menuAction())

        self.giao_dich = QtWidgets.QMenu("Giao dịch", self.menubar)
        self.bill_info = QtWidgets.QAction("Hóa đơn", self)
        self.bill_info.triggered.connect(self.show_bill_info)
        self.bill_detail_info = QtWidgets.QAction("Hóa đơn chi tiết", self)
        self.bill_detail_info.triggered.connect(self.show_bill_detail_info)
        self.giao_dich.addAction(self.bill_info)
        self.giao_dich.addAction(self.bill_detail_info)
        self.menubar.addAction(self.giao_dich.menuAction())

        self.san_pham = QtWidgets.QMenu('Sản phẩm', self.menubar)
        self.add_san_pham = QtWidgets.QAction('Thêm sản phẩm', self)
        self.add_san_pham.triggered.connect(self.show_add_p)
        self.list_san_pham = QtWidgets.QAction('Danh sách sản phẩm', self)
        self.list_san_pham.triggered.connect(self.show_list_p)
        self.san_pham.addAction(self.add_san_pham)
        self.san_pham.addAction(self.list_san_pham)
        self.menubar.addAction(self.san_pham.menuAction())

        self.kho_hang = QtWidgets.QMenu('Kho hàng', self.menubar)
        self.add_kho_hang = QtWidgets.QAction('Thêm số liệu kho hàng', self)
        self.add_kho_hang.triggered.connect(self.show_add_w)
        self.list_kho_hang = QtWidgets.QAction('Danh sách kho hàng', self)
        self.list_kho_hang.triggered.connect(self.show_list_w)
        self.kho_hang.addAction(self.add_kho_hang)
        self.kho_hang.addAction(self.list_kho_hang)
        self.menubar.addAction(self.kho_hang.menuAction())

        # ADD BUTTON --------------------------------------------------------------------------------------------------
        self.refresh_btn = QtWidgets.QPushButton("Refresh", self)
        self.refresh_btn.move(900, 30)
        self.refresh_btn.setStyleSheet('color:#fafafa;font-size =15px;font: bold 14px;background-color:qlineargradient(spread:pad, x1:0.45,y1:0.3695,x2:0.426\
        ,y2:0,stop:0 rgba(255,170,0,228),stop:1 rgba(255,255,255,255));border-radius:10px;border:none')
        self.refresh_btn.clicked.connect(self.refresh)

        self.charge_btn = QtWidgets.QPushButton("Thanh toán", self)
        self.charge_btn.setStyleSheet('color:#fafafa;font-size =15px;font: bold 14px;background-color:qlineargradient(spread:pad, x1:0.45,y1:0.3695,x2:0.426\
        ,y2:0,stop:0 rgba(255,170,0,228),stop:1 rgba(255,255,255,255));border-radius:10px;border:none')
        self.charge_btn.move(800, 530)
        self.charge_btn.resize(100, 30)

        # ADD LABEL ---------------------------------------------------------------------------------------------------
        self.total_price_lbl = QtWidgets.QLabel("Tổng giá: ", self)
        self.total_price_lbl.move(800, 380)
        self.total_price_lbl.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.total_price_value = QtWidgets.QLabel(self)
        self.total_price_value.move(900, 380)

        self.discount_lbl = QtWidgets.QLabel("Giảm giá: ", self)
        self.discount_lbl.move(800, 430)
        self.discount_lbl.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.discount_value = QtWidgets.QComboBox(self)
        self.discount_value.move(900, 430)
        self.discount_value.setStyleSheet('background-color:white')
        self.discount_value.addItems(["0%", "15%", "30%", "50%"])

        self.employee_lbl = QtWidgets.QLabel("Nhân viên: ", self)
        self.employee_lbl.move(800, 100)
        self.employee_lbl.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.chosen_employee = QtWidgets.QLineEdit(self)
        self.chosen_employee.move(870, 110)
        self.chosen_employee.setReadOnly(True)
        self.chosen_employee.setFixedSize(150, 20)
        self.employee_value = QtWidgets.QListWidget(self)
        self.employee_value.setStyleSheet('background-color:white')
        self.employee_value.move(870, 130)
        for row in range(-1, self.employee_amount_entry):
            if row == -1:
                self.employee_value.addItem("None")
                self.chosen_employee.setText("None")
            else:
                self.employee_value.addItem(self.employee_list[row]["employee_name"])
        self.employee_value.setFixedSize(150, 100)

        self.customer = QtWidgets.QLabel("Khách hàng: ", self)
        self.customer.move(800, 250)
        self.customer.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.chosen_customer = QtWidgets.QLineEdit(self)
        self.chosen_customer.move(870, 260)
        self.chosen_customer.setReadOnly(True)
        self.chosen_customer.setFixedSize(150, 20)
        self.customer_value = QtWidgets.QListWidget(self)
        self.customer_value.setStyleSheet('background-color:white')
        self.customer_value.move(870, 280)
        for row2 in range(-1, self.customer_amount_entry):
            if row2 == -1:
                self.customer_value.addItem("None")
                self.chosen_customer.setText("None")
            else:
                self.customer_value.addItem(self.customer_list[row2]["customer_name"])
        self.customer_value.setFixedSize(150, 100)

        self.actual_money = QtWidgets.QLabel("Tiền phải trả: ", self)
        self.actual_money.move(800, 480)
        self.actual_money.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.actual_money_value = QtWidgets.QLabel(self)
        self.actual_money_value.move(900, 480)

        # self.payed_money = QtWidgets.QLabel("Khách thanh toán: ", self)
        # self.payed_money.move(800, 400)
        # self.payed_money_value = QtWidgets.QLabel(self)
        # self.payed_money_value.move(900, 400)

        # self.change_money = QtWidgets.QLabel("Tiền thối lại:", self)
        # self.change_money.move(800, 450)
        # self.change_money_value = QtWidgets.QLabel(self)
        # self.change_money_value.move(900, 450)

        # ADD SEARCH BOX ----------------------------------------------------------------------------------------------
        self.last_search = -1
        self.search_box = QtWidgets.QLineEdit(self)
        self.search_box.move(30, 30)
        self.search_box.setStyleSheet('background-color:white')
        self.search_box.resize(280, 25)
        self.search_box.setCompleter(self.completer)    # give hints for user
        # self.search_box.textChanged.connect(self.search_box)    # call the function every time text changed
        self.search_box.textChanged.connect(self.clear_highlight)   # call the clear function to clear lingering color
        self.search_box.returnPressed.connect(lambda: self.search_trigger(self.search_box.text(), self.product_name_list))       
        self.search_box.setFocus()  # set the cursor in the edit box

        self.search_btn = QtWidgets.QPushButton(self)
        self.search_btn.setIcon(QtGui.QIcon("magnifying glass.png"))
        self.search_btn.move(310, 30)
        self.search_btn.resize(25, 25)
        self.search_btn.clicked.connect(lambda: self.search_trigger(self.search_box.text(), self.product_name_list))  
        # connect to the same function as the edit box

        # ADD TABLE ---------------------------------------------------------------------------------------------------
        self.purchased_list = QtWidgets.QTableWidget(self)
        self.purchased_list.setStyleSheet('background-color:white')
        self.purchased_list.setRowCount(0)
        self.purchased_list.setColumnCount(10)
        self.purchased_list.move(30, 100)
        self.purchased_list.resize(750, 250)
        self.purchased_list.setHorizontalHeaderLabels(
            ["No", "Code", "Name", "Category", "Brand", "Amount", "", "", "Price", ""])

        item0 = QtWidgets.QTableWidgetItem("No")
        item0.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(0, item0)
        item1 = QtWidgets.QTableWidgetItem("Code")
        item1.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(1, item1)
        item2 = QtWidgets.QTableWidgetItem("Name")
        item2.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(2, item2)
        item3 = QtWidgets.QTableWidgetItem("Category")
        item3.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(3, item3)
        item4 = QtWidgets.QTableWidgetItem("Brand")
        item4.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(4, item4)
        item5 = QtWidgets.QTableWidgetItem("Amount")
        item5.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(5, item5)
        item6 = QtWidgets.QTableWidgetItem("")
        item6.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(6, item6)
        item7 = QtWidgets.QTableWidgetItem("")
        item7.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(7, item7)
        item8 = QtWidgets.QTableWidgetItem("Price")
        item8.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(8, item8)
        item9 = QtWidgets.QTableWidgetItem("")
        item9.setBackground(QtGui.QColor(0, 255, 0))
        self.purchased_list.setHorizontalHeaderItem(9, item9)

        self.purchased_list.verticalHeader().hide()
        # self.purchased_list.horizontalHeaderItem(0).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(1).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(2).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(3).setTextAlignment(0)
        self.purchased_list.setColumnWidth(0, 25)
        self.purchased_list.setColumnWidth(3, 75)
        self.purchased_list.setColumnWidth(6, 25)
        self.purchased_list.setColumnWidth(7, 25)
        self.purchased_list.setColumnWidth(9, 25)
        self.purchased_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # disable editing feature

        # CREATE TABLE OF PRODUCTS ------------------------------------------------------------------------------------
        self.product_list = QtWidgets.QTableWidget(self)
        self.product_list.setStyleSheet('background-color:white')
        self.product_list.setRowCount(self.product_amount_entry)
        self.product_list.setColumnCount(6)
        self.product_list.move(30, 360)
        self.product_list.resize(520, 200)
        self.product_list.setHorizontalHeaderLabels(["Code", "Name", "Category", "Brand", "Price", ""])

        item0 = QtWidgets.QTableWidgetItem("Code")
        item0.setBackground(QtGui.QColor(0, 255, 0))
        self.product_list.setHorizontalHeaderItem(0, item0)
        item1 = QtWidgets.QTableWidgetItem("Name")
        item1.setBackground(QtGui.QColor(0, 255, 0))
        self.product_list.setHorizontalHeaderItem(1, item1)
        item2 = QtWidgets.QTableWidgetItem("Category")
        item2.setBackground(QtGui.QColor(0, 255, 0))
        self.product_list.setHorizontalHeaderItem(2, item2)
        item3 = QtWidgets.QTableWidgetItem("Brand")
        item3.setBackground(QtGui.QColor(0, 255, 0))
        self.product_list.setHorizontalHeaderItem(3, item3)
        item4 = QtWidgets.QTableWidgetItem("Price")
        item4.setBackground(QtGui.QColor(0, 255, 0))
        self.product_list.setHorizontalHeaderItem(4, item4)
        item5 = QtWidgets.QTableWidgetItem("")
        item5.setBackground(QtGui.QColor(0, 255, 0))
        self.product_list.setHorizontalHeaderItem(5, item5)

        self.product_list.verticalHeader().hide()
        self.product_list.horizontalHeaderItem(0).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(1).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(2).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(3).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(4).setTextAlignment(0)

        self.product_list.setColumnWidth(0, 50)
        self.product_list.setColumnWidth(1, 150)
        self.product_list.setColumnWidth(3, 75)
        self.product_list.setColumnWidth(4, 75)
        self.product_list.setColumnWidth(5, 30)
        self.product_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # disable editing feature
        self.product_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.load_product_from_db()

        # CREATE PICTURE LABEL
        self.pic = QtWidgets.QLabel(self)
        self.pic.resize(200, 200)
        self.pic.move(570, 360)

        # TRIGGERED EVENTS --------------------------------------------------------------------------------------------
        self.purchased_list.cellClicked.connect(self.del_incr_decr_operation)
        # self.add_tab_btn.clicked.connect(self.add_tab)
        self.discount_value.currentTextChanged.connect(self.add_price_discount)
        self.product_list.cellClicked.connect(self.select_product_from_db)
        # self.charge_btn.clicked.connect(self.charge)
        self.charge_btn.clicked.connect(lambda: self.show_invoice(self.purchased_list.rowCount()))
        self.employee_value.currentTextChanged.connect(self.choose_employee)
        self.customer_value.currentTextChanged.connect(self.choose_customer)

        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.refresh)
        # self.timer.start(1000)

    # DEFINE TRIGGERED EVENTS -----------------------------------------------------------------------------------------
    def search_trigger(self, name, name_list):
        print("vao ham")
        if name in name_list:
            print("tim thay")
            name_index = name_list.index(name)
            for i in range(6):
                self.product_list.item(name_index, i).setBackground(QtGui.QColor(150, 150, 150))
            if self.last_search >= 0:
                for i in range(6):
                    self.product_list.item(self.last_search, i).setBackground(QtGui.QColor(255, 255, 255))
            self.last_search = copy.deepcopy(name_index)
        else:
            print("khong tim thay")

    def clear_highlight(self):
        if self.search_box.text() == "":
            if self.last_search >= 0:    
                for i in range(6):
                    self.product_list.item(self.last_search, i).setBackground(QtGui.QColor(255, 255, 255))
            self.last_search = -1   # reset value of last-search index

    def insert_item_to_table(self,
                             table,
                             code="102020",
                             name="Random",
                             category="laptop",
                             brand="dell",
                             price="11000"):
        amount = "1"
        row_position = table.rowCount()
        table.insertRow(row_position)
        # this part may need to be fixed for clearer code
        table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(row_position + 1)))
        table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(code))
        table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(name))
        table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(category))
        table.setItem(row_position, 4, QtWidgets.QTableWidgetItem(brand))
        table.setItem(row_position, 5, QtWidgets.QTableWidgetItem(amount))
        table.setItem(row_position, 6, QtWidgets.QTableWidgetItem("+"))
        table.setItem(row_position, 7, QtWidgets.QTableWidgetItem("-"))
        table.setItem(row_position, 8, QtWidgets.QTableWidgetItem(price))
        table.setItem(row_position, 9, QtWidgets.QTableWidgetItem("X"))
        # add up all the costs
        self.add_price()

    def del_incr_decr_operation(self, row, column):
        if self.purchased_list.item(row, column).text() == 'X':
            print("delete row number %s" % row)
            self.purchased_list.removeRow(row)
            del self.already_added_row[row]
            for index in range(0, self.purchased_list.rowCount()):
                self.purchased_list.setItem(index, 0, QtWidgets.QTableWidgetItem(str(index + 1)))

        elif self.purchased_list.item(row, column).text() == '+':
            print("increase")
            amount = int(self.purchased_list.item(row, column - 1).text()) + 1
            therow = self.already_added_row[row]
            # print("this is %d %d" % (therow, amount))
            if self.out_of_stock_warning(therow, amount) is not True:
                # print("out")
                self.purchased_list.setItem(row, column - 1, QtWidgets.QTableWidgetItem(str(amount)))
                # price increase
                price = int(self.purchased_list.item(row, column + 2).text())
                print(price)
                price += price / (amount - 1)
                self.purchased_list.setItem(row, column + 2, QtWidgets.QTableWidgetItem(str(round(price))))
                # round function is used to round up the value, remove every single digit behind the calculated result
                # therefor prevent any latent error happen when conversion "string->int" is implemented
        elif self.purchased_list.item(row, column).text() == '-':
            print("decrease")
            amount = int(self.purchased_list.item(row, column - 2).text()) - 1
            if amount == 0:
                # if the amount has touched the allowed minimum value -> STOP!
                pass
            else:
                self.purchased_list.setItem(row, column - 2, QtWidgets.QTableWidgetItem(str(amount)))
                # price decrease
                price = int(self.purchased_list.item(row, column + 1).text())
                price -= price / (amount + 1)
                self.purchased_list.setItem(row, column + 1, QtWidgets.QTableWidgetItem(str(round(price))))
                # same reason as above
        else:
            # for other situations ignore and move on!
            pass
        # add up all the costs
        self.add_price()

    def add_price(self):
        base_price = 0
        for row in range(0, self.purchased_list.rowCount()):
            base_price += int(self.purchased_list.item(row, 8).text())
        discounted_price = base_price - (self.discount_percentage / 100) * base_price
        print(base_price)
        self.total_cost = base_price
        self.discount_cost = discounted_price
        self.actual_money_value.setText(str(round(discounted_price)))
        self.total_price_value.setText(str(round(base_price)))
        # return multiple value by using list
        return [base_price, discounted_price]

    def add_price_discount(self, text):
        text = text[:len(text) - 1]
        print(text)
        self.discount_percentage = int(text)
        self.actual_money_value.setText(str(round(self.add_price()[1])))

    def load_product_from_db(self):
        print(self.product_list)
        print(self.product_amount_entry)
        for i in range(0, self.product_amount_entry):
            self.product_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.product_list_db[i]["product_code"])))
            self.product_list.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.product_list_db[i]["product_name"])))
            self.product_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.product_list_db[i]["product_category"])))
            self.product_list.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.product_list_db[i]["product_brand"])))
            self.product_list.setItem(i, 4, QtWidgets.QTableWidgetItem(str(round(self.product_list_db[i]["product_price"]))))
            self.product_list.setItem(i, 5, QtWidgets.QTableWidgetItem("+"))

    def select_product_from_db(self, row, column):
        # print(self.already_added_row)
        if self.product_list.item(row, column).text() == '+':
            if row in self.already_added_row:
                index = self.already_added_row.index(row)
                amount = int(self.purchased_list.item(index, 5).text()) + 1
                if self.out_of_stock_warning(row, amount) is not True:
                    self.purchased_list.setItem(index, 5, QtWidgets.QTableWidgetItem(str(amount)))
                    price = int(self.purchased_list.item(index, 8).text())
                    # print(price)
                    price += price / (amount - 1)
                    self.purchased_list.setItem(index, 8, QtWidgets.QTableWidgetItem(str(round(price))))
                    self.add_price()
            else:
                if self.out_of_stock_warning(row, 1) is not True:
                    self.already_added_row.append(row)
                    code = str(self.product_list_db[row]["product_code"])
                    name = str(self.product_list_db[row]["product_name"])
                    category = str(self.product_list_db[row]["product_category"])
                    brand = str(self.product_list_db[row]["product_brand"])
                    price = str(round(self.product_list_db[row]["product_price"]))
                    print(price)
                    self.insert_item_to_table(self.purchased_list, code, name, category, brand, price)
        self.load_pixmap(row, column)
        # print(self.product_list_db[row]["product_image"])

    def load_pixmap(self, row, column):
        pixmap = QtGui.QPixmap("C:/Users/DELL/Documents/pycharm/image/" + self.product_list_db[row]["product_image"])
        pixmap_scaled = pixmap.scaled(QtCore.QSize(200, 200), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.pic.setPixmap(pixmap_scaled)

    def out_of_stock_warning(self, number, amount):
        remain = self.warehouse_list_db[number]["inventory_number"]
        print("the remain ", remain)
        if remain < amount:
            warning = QtWidgets.QErrorMessage(self)
            warning.setWindowTitle("Out of stock!!")
            if remain != 0:
                warning.showMessage("Remain in stock: %d" % remain)
            else:
                warning.showMessage("Out of stock")
            return True  # out of stock
        print("nothing still have some left")
        return False  # still have some
        pass

    def charge(self, bill_date, bill_time):
        # a trigger button to save the bill into the database
        # now = datetime.datetime.now()
        # bill_date = now.strftime("%Y-%m-%d")
        # bill_time = now.strftime("%H:%M")
        # self.bill_code = (now.strftime("%Y%m%d") + now.strftime("%H%M"))[2:]  # get the bill code from date & time
        # print(self.bill_code)

        # employee_code = "007"
        # total_cost = self.total_cost
        # discount = self.discount_percentage
        # bill_cost = self.discount_cost
        # customer_code = "1234"
        bill_note = "nah nah nah"

        bill_db.insert(self.bill_code,
                       self.employee_code,
                       bill_date,
                       bill_time,
                       self.customer_code,
                       self.total_cost,
                       self.discount_percentage,
                       self.discount_cost,
                       bill_note)

        for i in range(0, self.purchased_list.rowCount()):
            print("vao bill detail")
            bill_detail_db.insert(self.bill_code,
                                  str(self.purchased_list.item(i, 1).text()),
                                  int(self.purchased_list.item(i, 5).text()),
                                  float(self.purchased_list.item(i, 8).text()))

    def show_bill_info(self):
        self.bill = bill_list.Bill()
        self.bill.show()

    def show_bill_detail_info(self):
        self.bill_detail = bill_detail_list.BillDetail()
        self.bill_detail.show()
    # ******************************************************************************

    def choose_employee(self):
        self.onshift_emp = self.employee_value.currentItem().text()
        self.chosen_employee.setText(self.onshift_emp)
        for i in range(self.employee_amount_entry):
            if self.employee_list[i]["employee_name"] == self.onshift_emp:
                self.employee_code = self.employee_list[i]["employee_code"]
                break
            else:
                continue
        pass

    def choose_customer(self):
        self.current_cus = self.customer_value.currentItem().text()

        self.chosen_customer.setText(self.current_cus)
        for i in range(self.customer_amount_entry):
            if self.customer_list[i]["customer_name"] == self.current_cus:
                self.customer_code = self.customer_list[i]["customer_code"]
                break
            else:
                continue
        pass

    def show_invoice(self, row_amount):
        if row_amount < 1:
            print("no record")
            warning = QtWidgets.QErrorMessage(self)
            warning.setWindowTitle("No product added yet!!")
            warning.showMessage("Bạn chưa thêm vào bất cứ sản phẩm nào!!!")

        elif (self.customer_code is None) or (self.employee_code is None):
            warning2 = QtWidgets.QErrorMessage(self)
            warning2.setWindowTitle("Empty field!")
            warning2.showMessage("Bạn chưa chọn nhân viên hoặc khách hàng")
            
        else:
            now = datetime.datetime.now()
            bill_date = now.strftime("%Y-%m-%d")
            bill_time = now.strftime("%H:%M")
            self.bill_code = (now.strftime("%Y%m%d") + now.strftime("%H%M"))[2:]  # get the bill code from date & time
            print(self.bill_code)

            self.test = invoice.Invoice(self.purchased_list,
                                        self.onshift_emp,
                                        self.current_cus,
                                        self.bill_code,
                                        self.employee_code,
                                        bill_date,
                                        bill_time,
                                        self.customer_code,
                                        self.total_cost,
                                        self.discount_percentage,
                                        self.discount_cost)
            if self.test.exec_():
                print("ok")
                self.charge(bill_date, bill_time)
                self.erase_purchase_list(self.purchased_list.rowCount())
                self.test.close()
            else:
                print("close")
                self.test.close()

    def erase_purchase_list(self, row_count):
        self.reduce_product_in_db()
        for i in range(row_count, -1, -1):
            self.purchased_list.removeRow(i)
        del self.already_added_row[:]

    def reduce_product_in_db(self):
        print("Giam so luong")
        for i in range(self.purchased_list.rowCount()):
            product_code = self.purchased_list.item(i, 1).text()
            product_count = int(self.purchased_list.item(i, 5).text())
            var1, var2 = warehouse_db.select(product_code)
            var3 = int(var1[0]['inventory_number']) - product_count
            warehouse_db.update(product_code, var3, product_code)

    def refresh(self):
        """ Refresh method """
        # Refresh product table list
        while (self.product_list.rowCount() > 0):
            self.product_list.removeRow(0)

        self.product_list_db, self.product_amount_entry = product_db.select_all()
        for i in range(self.product_amount_entry):
            self.product_list.insertRow(i)
        self.load_product_from_db()
        
        # Refresh employee table list
        self.employee_list, self.employee_amount_entry = employee_db.select_all()
        self.employee_value.setCurrentItem(self.employee_value.item(0))
        for i in range(self.employee_amount_entry,0,-1):
            self.employee_value.takeItem(i)

        for j in range(self.employee_amount_entry):
            self.employee_value.addItem(self.employee_list[j]["employee_name"])
        

        # Refresh customer table list
        self.customer_list, self.customer_amount_entry = customer_db.select_all()
        self.customer_value.setCurrentItem(self.customer_value.item(0))
        for i in range(self.customer_amount_entry,0,-1):
            # self.customer_value.takeItem(self.customer_value.currentRow())
            self.customer_value.takeItem(i)

        # self.customer_value.clear()
        # self.customer_value.takeItem(self.customer_value.currentItem())
                
        for j in range(self.customer_amount_entry):
            self.customer_value.addItem(self.customer_list[j]["customer_name"])
        # self.customer_value.setFixedSize(150, 100)



    def refresh1(self):
        self.customer_list, self.customer_amount_entry = customer_db.select_all()
        self.customer_value.clear()
        for row2 in range(self.customer_amount_entry):
            self.customer_value.addItem(self.customer_list[row2]["customer_name"])

    def show_list_c(self):
        self.list_c = customer_list.customer_list()
        self.list_c.show()

    def show_add_c(self):
        self.add_c = customer_add.customer_add()
        self.add_c.show()

    def show_list_p(self):
        self.list_p = product_list.product_list()
        self.list_p.show()

    def show_add_p(self):
        self.add_p = product_add.product_add()
        self.add_p.show()

    def show_list_w(self):
        self.list_p = warehouse_list.warehouse_list()
        self.list_p.show()

    def show_add_w(self):
        self.add_w = warehouse_add.warehouse_add()
        self.add_w.show()

    def show_list_e(self):
        self.list_e = employee_list.employee_list()
        self.list_e.show()

    def show_add_e(self):
        self.add_e = employee_add.employee_add()
        self.add_e.show()


class CustomError(Exception):
    pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    ex = Login()
    sys.exit(app.exec_())