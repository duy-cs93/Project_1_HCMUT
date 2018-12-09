import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap
from email.charset import QP
import datetime

from read_json import *
from MyTable import *
from Add import *

import bill_db, bill_detail_db, product_db, warehouse_db
import bill_list, bill_detail_list
import customer_add, customer_list
import product_add, product_list
import warehouse_add, warehouse_list

class Login(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Log in'
        self.left = 380
        self.top = 220
        self.width = 540
        self.height = 380
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.move(self.left, self.top)
        self.setFixedSize(self.width, self.height)

        # create label 1
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Tên đăng nhập')
        self.l1.move(30, 50)
        # Create ID text box 1
        self.user_text = QtWidgets.QLineEdit(self)
        self.user_text.move(30, 80)
        self.user_text.resize(220, 25)

        # create label 2
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Mật khẩu')
        self.l2.move(30, 120)
        # Create password text box 2
        self.password_text = QtWidgets.QLineEdit(self)
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.move(30, 150)
        self.password_text.resize(220, 25)

        # Create button in the window
        self.button = QtWidgets.QPushButton('Quản lý', self)
        self.button.move(200, 300)

        # connect button to function on_click
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


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title = "Quản lý bán hàng"
        self.width = 1050
        self.height = 600
        self.amount_of_products = 0  # this variable is used for counting the number of purchased item
        self.discount_percentage = 0
        self.total_cost = None
        self.discount_cost = None
        self.already_added_row = []
        self.bill = None
        self.bill_detail = None
        self.bill_info = None
        self.bill_detail_info = None
        self.product_list_db, self.product_amount_entry = product_db.select_all()  # get the product list from database
        self.warehouse_list_db, self.warehouse_amount_entry = warehouse_db.select_all()

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
        self.search_box = None
        # Table
        self.purchased_list = None
        self.product_list = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.statusBar().showMessage("Hello Customers! Our best wishes to you!")

        #create menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))    
        
        self.thoat = QtWidgets.QMenu("Thoát", self.menubar)
        exitApp = QAction("&Exit",self)
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
        self.search_btn = QtWidgets.QPushButton(self)
        self.search_btn.setIcon(QtGui.QIcon("magnifying glass.png"))
        self.search_btn.move(310, 30)
        self.search_btn.resize(25, 25)

        self.add_product_btn = QtWidgets.QPushButton("Thêm vào", self)
        self.add_product_btn.move(800, 100)
        self.add_product_btn.resize(70, 30)

        self.add_tab_btn = QtWidgets.QPushButton("Thêm tab", self)
        self.add_tab_btn.move(800, 150)
        self.add_tab_btn.resize(70, 30)

        self.charge_btn = QtWidgets.QPushButton("Thanh toán", self)
        self.charge_btn.move(800, 200)
        self.charge_btn.resize(70, 30)

        # ADD LABEL ---------------------------------------------------------------------------------------------------
        self.total_price = QtWidgets.QLabel("Tổng giá: ", self)
        self.total_price.move(800, 250)
        self.total_price_value = QtWidgets.QLabel(self)
        self.total_price_value.move(900, 250)

        self.discount = QtWidgets.QLabel("Giảm giá: ", self)
        self.discount.move(800, 300)

        self.discount_value = QtWidgets.QComboBox(self)
        self.discount_value.move(800, 300)
        self.discount_value.addItems(["0%", "15%", "30%", "50%"])

        self.actual_money = QtWidgets.QLabel("Tiền phải trả: ", self)
        self.actual_money.move(800, 350)
        self.actual_money_value = QtWidgets.QLabel(self)
        self.actual_money_value.move(900, 350)

        self.payed_money = QtWidgets.QLabel("Khách thanh toán: ", self)
        self.payed_money.move(800, 400)
        self.payed_money_value = QtWidgets.QLabel(self)
        self.payed_money_value.move(900, 400)

        self.change_money = QtWidgets.QLabel("Tiền thối lại:", self)
        self.change_money.move(800, 450)
        self.change_money_value = QtWidgets.QLabel(self)
        self.change_money_value.move(900, 450)

        # ADD EDIT BOX ------------------------------------------------------------------------------------------------
        self.search_box = QtWidgets.QLineEdit(self)
        self.search_box.move(30, 30)
        self.search_box.resize(280, 25)

        # ADD TABLE ---------------------------------------------------------------------------------------------------
        self.purchased_list = QtWidgets.QTableWidget(self)
        self.purchased_list.setRowCount(0)
        self.purchased_list.setColumnCount(10)
        self.purchased_list.move(30, 100)
        self.purchased_list.resize(750, 250)
        self.purchased_list.setHorizontalHeaderLabels(
            ["No", "Code", "Name", "Category", "Brand", "Amount", "", "", "Price", ""])
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
        self.product_list.setRowCount(self.product_amount_entry)
        self.product_list.setColumnCount(5)
        self.product_list.move(30, 360)
        self.product_list.resize(520, 200)
        self.product_list.setHorizontalHeaderLabels(["Code", "Name", "Category", "Brand", "Price"])
        self.product_list.verticalHeader().hide()
        self.product_list.horizontalHeaderItem(0).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(1).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(2).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(3).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(4).setTextAlignment(0)
        self.product_list.setColumnWidth(0, 50)
        self.product_list.setColumnWidth(1, 150)
        self.product_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # disable editing feature
        self.product_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.load_product_from_db()

        # TRIGGERED EVENTS --------------------------------------------------------------------------------------------
        self.purchased_list.cellClicked.connect(self.del_incr_decr_operation)
        self.add_tab_btn.clicked.connect(self.add_tab)
        self.discount_value.currentTextChanged.connect(self.add_price_discount)
        self.product_list.cellClicked.connect(self.select_product_from_db)
        self.charge_btn.clicked.connect(self.charge)

    # DEFINE TRIGGERED EVENTS -----------------------------------------------------------------------------------------
    def search_trigger(self):
        print("search thu gi do o day")

    def insert_item_to_table(self, table, code="102020", name="Random", category="laptop", brand="dell",
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

    def add_tab(self):
        pass

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

    def select_product_from_db(self, row, column):
        print(self.already_added_row)
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

    def charge(self):  # a trigger button to save the bill into the database
        now = datetime.datetime.now()
        bill_date = now.strftime("%Y-%m-%d")
        bill_time = now.strftime("%H:%M")
        bill_code = (now.strftime("%Y%m%d") + now.strftime("%H%M"))[2:]  # get the bill code from date & time
        print(bill_code)
        employee_code = "007"
        # total_cost = self.total_cost
        # discount = self.discount_percentage
        # bill_cost = self.discount_cost
        customer_code = "1234"
        bill_note = "nah nah nah"

        bill_db.insert(bill_code,
                       employee_code,
                       bill_date, bill_time,
                       customer_code,
                       self.total_cost,
                       self.discount_percentage,
                       self.discount_cost,
                       bill_note)

        for i in range(0, self.purchased_list.rowCount()):
            bill_detail_db.insert(bill_code,
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
                                               
   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
