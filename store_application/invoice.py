import sys
from PyQt5 import QtWidgets, QtCore, QtGui, Qt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.amount_of_products = 0  # this variable is used for counting the number of purchased item
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        # self.resize(800, 600)
        self.setFixedSize(1000, 600)
        self.statusBar().showMessage("Hello Customers! Our best wishes to you!")
        # selected_color = QtGui.QColor(0, 255, 255)
        # self.setStyleSheet("QWidget {background-color: %s}" % selected_color.name())

        # ADD SEARCH BOX
        search_box = QtWidgets.QLineEdit(self)
        search_box.move(30, 30)
        search_box.resize(280, 25)

        # ADD BUTTON
        search_btn = QtWidgets.QPushButton(self)
        search_btn.setIcon(QtGui.QIcon("magnifying glass.png"))
        search_btn.move(310, 30)
        search_btn.resize(25, 25)

        add_product_btn = QtWidgets.QPushButton("Thêm vào", self)
        add_product_btn.move(800, 100)
        add_product_btn.resize(70, 30)

        # ADD TABLE
        self.purchased_list = QtWidgets.QTableWidget(self)
        self.purchased_list.setRowCount(0)
        self.purchased_list.setColumnCount(8)
        self.purchased_list.setHorizontalHeaderLabels(["No", "Code", "Name", "Amount", "", "", "Price", ""])
        # self.purchased_list.horizontalHeaderItem(0).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(1).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(2).setTextAlignment(0)
        self.purchased_list.horizontalHeaderItem(3).setTextAlignment(0)
        self.purchased_list.verticalHeader().hide()
        # header = self.purchased_list.horizontalHeader()
        # header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.purchased_list.setColumnWidth(0, 25)
        self.purchased_list.setColumnWidth(3, 55)
        self.purchased_list.setColumnWidth(4, 25)
        self.purchased_list.setColumnWidth(5, 25)
        # self.purchased_list.setColumnWidth(6, 25)
        self.purchased_list.setColumnWidth(7, 25)

        self.purchased_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)   # disable editing feature
        self.purchased_list.move(30, 100)
        self.purchased_list.resize(700, 300)

        # TRIGGERED EVENTS
        add_product_btn.clicked.connect(lambda: self.insert_item_to_table(self.purchased_list))
        # need to fix this
        self.purchased_list.cellClicked.connect(self.del_incr_decr_operation)

    # DEFINE TRIGGERED EVENTS
    def search_trigger(self):
        print("search thu gi do o day")

    def insert_item_to_table(self, table, item_code="102020", item_name="Random", amount="1", price="11000"):
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


# MAIN CODE HERE
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

