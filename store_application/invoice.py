import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import pandas


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.amount_of_products = 0  # this variable is used for counting the number of purchased item
        self.discount_percentage = 0
        self.already_added_row = []
        self.data_csv = pandas.read_csv("data.csv")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Bán hàng")
        # self.resize(600, 600)
        self.setFixedSize(1000, 600)
        self.statusBar().showMessage("Hello Customers! Our best wishes to you!")
        # selected_color = QtGui.QColor(0, 255, 255)
        # self.setStyleSheet("QWidget {background-color: %s}" % selected_color.name())

        # ADD BUTTON --------------------------------------------------------------------------------------------------
        search_btn = QtWidgets.QPushButton(self)
        search_btn.setIcon(QtGui.QIcon("magnifying glass.png"))
        search_btn.move(310, 30)
        search_btn.resize(25, 25)

        add_product_btn = QtWidgets.QPushButton("Thêm vào", self)
        add_product_btn.move(600, 100)
        add_product_btn.resize(70, 30)

        add_tab_btn = QtWidgets.QPushButton("Thêm tab", self)
        add_tab_btn.move(600, 150)
        add_tab_btn.resize(70, 30)

        charge_btn = QtWidgets.QPushButton("Thanh toán", self)
        charge_btn.move(600, 200)
        charge_btn.resize(70, 30)

        # ADD LABEL ---------------------------------------------------------------------------------------------------
        self.total_price = QtWidgets.QLabel("Tổng giá: ", self)
        self.total_price.move(600, 250)
        self.total_price_value = QtWidgets.QLabel(self)
        self.total_price_value.move(700, 250)

        self.discount = QtWidgets.QLabel("Giảm giá: ", self)
        self.discount.move(600, 300)
        self.discount_value = QtWidgets.QComboBox(self)
        self.discount_value.move(700, 300)
        self.discount_value.addItems(["0%", "15%", "30%", "50%"])
        self.discount_value.currentTextChanged.connect(self.add_price_discount)

        self.actual_money = QtWidgets.QLabel("Tiền phải trả: ", self)
        self.actual_money.move(600, 350)
        self.actual_money_value = QtWidgets.QLabel(self)
        self.actual_money_value.move(700, 350)

        self.payed_money = QtWidgets.QLabel("Khách thanh toán: ", self)
        self.payed_money.move(600, 400)
        self.payed_money_value = QtWidgets.QLabel(self)
        self.payed_money_value.move(700, 400)

        self.change_money = QtWidgets.QLabel("Tiền thối lại:", self)
        self.change_money.move(600, 450)
        self.change_money_value = QtWidgets.QLabel(self)
        self.change_money_value.move(700, 450)

        # ADD EDIT BOX ------------------------------------------------------------------------------------------------
        self.search_box = QtWidgets.QLineEdit(self)
        self.search_box.move(30, 30)
        self.search_box.resize(280, 25)

        # ADD TABLE ---------------------------------------------------------------------------------------------------
        self.purchased_list = QtWidgets.QTableWidget(self)
        self.purchased_list.setRowCount(0)
        self.purchased_list.setColumnCount(8)
        self.purchased_list.move(30, 100)
        self.purchased_list.resize(520, 250)
        self.purchased_list.setHorizontalHeaderLabels(["No", "Code", "Name", "Amount", "", "", "Price", ""])
        self.purchased_list.verticalHeader().hide()
        # self.purchased_list.horizontalHeaderItem(0).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(1).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(2).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(3).setTextAlignment(0)
        # header = self.purchased_list.horizontalHeader()
        # header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.purchased_list.setColumnWidth(0, 25)
        self.purchased_list.setColumnWidth(3, 55)
        self.purchased_list.setColumnWidth(4, 25)
        self.purchased_list.setColumnWidth(5, 25)
        # self.purchased_list.setColumnWidth(6, 25)
        self.purchased_list.setColumnWidth(7, 25)
        self.purchased_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)   # disable editing feature

        # CREATE TABLE OF PRODUCTS ------------------------------------------------------------------------------------
        row_count, column_count = self.data_csv.shape
        self.product_list = QtWidgets.QTableWidget(self)
        self.product_list.setRowCount(row_count)
        self.product_list.setColumnCount(3)
        self.product_list.move(30, 360)
        self.product_list.resize(520, 200)
        self.product_list.setHorizontalHeaderLabels(["Code", "Name", "Price"])
        self.product_list.horizontalHeaderItem(0).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(1).setTextAlignment(0)
        self.product_list.horizontalHeaderItem(2).setTextAlignment(0)
        self.product_list.verticalHeader().hide()
        # self.product_list.horizontalHeader().hide()
        self.product_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)    # disable editing feature
        # self.product_list.setItem(0, 0, QtWidgets.QTableWidgetItem(self.data_csv["name"][1]))
        self.load_product_list(row_count)
        # self.product_list.setSelectionBehavior(QtGui.QAbstractItemView.selectionRows)
        self.product_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

        ##################################################################################
        # this part I will fix later, trying to add image into the cell!
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("quat.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon2 = QtWidgets.Qtable
        # self.product_list.setItem(0, 0, icon)
        # self.product_list.setCellWidget(0, 0, QtGui.QPixmap())
        ##################################################################################

        # TRIGGERED EVENTS --------------------------------------------------------------------------------------------
        add_product_btn.clicked.connect(lambda: self.insert_item_to_table(self.purchased_list))
        # need to fix this
        self.purchased_list.cellClicked.connect(self.del_incr_decr_operation)
        add_tab_btn.clicked.connect(self.add_tab)
        # temporary disable below line
        # charge_btn.clicked.connect(self.add_price)
        # self.discount_value.activated[str].connect(self.add_price_discount)
        self.product_list.cellClicked.connect(self.select_product_list)

    # DEFINE TRIGGERED EVENTS -----------------------------------------------------------------------------------------
    def search_trigger(self):
        print("search thu gi do o day")

    def insert_item_to_table(self, table, item_code="102020", item_name="Random", price="11000"):
        amount = "1"
        row_position = table.rowCount()
        table.insertRow(row_position)
        # this part may need to be fixed for clearer code
        # table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(row_position)))
        # item = QtWidgets.QTableWidgetItem(str(row_position+1))
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(row_position + 1)))
        # table.setItem(row_position, 0, item)
        table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(item_code))
        table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(item_name))
        table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(amount))
        table.setItem(row_position, 4, QtWidgets.QTableWidgetItem("+"))
        table.setItem(row_position, 5, QtWidgets.QTableWidgetItem("-"))
        table.setItem(row_position, 6, QtWidgets.QTableWidgetItem(price))
        table.setItem(row_position, 7, QtWidgets.QTableWidgetItem("X"))

        # add up all the costs
        self.total_price_value.setText(str(round(self.add_price()[0])))

    def del_incr_decr_operation(self, row, column):
        if self.purchased_list.item(row, column).text() == 'X':
            print("delete row number %s" % row)
            self.purchased_list.removeRow(row)

            for index in range(0, self.purchased_list.rowCount()):
                # row_index = QtWidgets.QTableWidgetItem(str(index + 1))
                # row_index.setTextAlignment(QtCore.Qt.AlignCenter)
                # self.purchased_list.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row_index))
                self.purchased_list.setItem(index, 0, QtWidgets.QTableWidgetItem(str(index + 1)))

        elif self.purchased_list.item(row, column).text() == '+':
            print("increase")
            amount = int(self.purchased_list.item(row, column - 1).text()) + 1
            self.purchased_list.setItem(row, column - 1, QtWidgets.QTableWidgetItem(str(amount)))

            # price increase
            price = int(self.purchased_list.item(row, column + 2).text())
            print(price)
            price += price/(amount - 1)
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
                price -= price/(amount + 1)
                self.purchased_list.setItem(row, column + 1, QtWidgets.QTableWidgetItem(str(round(price))))
                # same reason as above

        else:
            # for other situations ignore and move on!
            pass

        # add up all the costs
        self.total_price_value.setText(str(round(self.add_price()[0])))

    def add_tab(self):
        pass

    def add_price(self):
        base_price = 0
        for row in range(0, self.purchased_list.rowCount()):
            base_price += int(self.purchased_list.item(row, 6).text())
        discounted_price = base_price - (self.discount_percentage / 100) * base_price
        print(base_price)
        self.actual_money_value.setText(str(round(discounted_price)))
        # return multiple value by using list
        return [base_price, discounted_price]

    def add_price_discount(self, text):
        text = text[:len(text)-1]
        print(text)
        self.discount_percentage = int(text)
        self.actual_money_value.setText(str(round(self.add_price()[1])))

    def load_product_list(self, row):
        print(row)
        for i in range(0, row):
            # self.product_list.setItem(0, 0, QtWidgets.QTableWidgetItem(self.data_csv["name"][1]))
            self.product_list.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.data_csv["code"][i])))
            self.product_list.setItem(i, 1, QtWidgets.QTableWidgetItem(self.data_csv["name"][i]))
            self.product_list.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.data_csv["price"][i])))

    def select_product_list(self, row, column):
        # this part of the code need to be optimized by using static variable like c++
        print(self.already_added_row)
        if row in self.already_added_row:
            index = self.already_added_row.index(row)
            amount = int(self.purchased_list.item(index, 3).text()) + 1
            self.purchased_list.setItem(index, 3, QtWidgets.QTableWidgetItem(str(amount)))
        else:
            self.already_added_row.append(row)
            code = str(self.data_csv["code"][row])
            name = str(self.data_csv["name"][row])
            price = str(self.data_csv["price"][row])
            self.insert_item_to_table(self.purchased_list, code, name, price)


# MAIN CODE HERE ------------------------------------------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

