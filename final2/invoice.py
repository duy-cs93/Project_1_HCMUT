# import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import bill_db
import bill_detail_db
import warehouse_db
import employee_db
import customer_db


class Invoice(QtWidgets.QDialog):
    # my_signal = QtCore.pyqtSignal()

    def __init__(self,
                 purchased_list,
                 employee_name,
                 customer_name,
                 bill_code,
                 employee_code,
                 bill_date,
                 bill_time,
                 customer_code,
                 total_price,
                 discount,
                 actual_price):
        super().__init__()
        self.width = 100
        self.height = 100
        self.setFixedSize(300, 500)
        self.setWindowTitle("Hóa đơn")
        self.bill_code = bill_code
        self.employee_code = employee_code
        self.bill_date = bill_date
        self.bill_time = bill_time
        self.customer_code = customer_code
        self.purchased_list = purchased_list
        self.total_price = total_price
        self.discount = discount
        self.actual_price = actual_price
        self.employee_name = employee_name
        self.customer_name = customer_name

        # self.bill, self.bill_count = bill_        db.select_all()
        # self.product, self.product_type = bill_detail_db.select_all()
        # self.is_product, self.is_product_type = product_db.select_all()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout2 = QtWidgets.QHBoxLayout(self)
        self.invoice = QtWidgets.QPlainTextEdit(self)
        self.iv_charge_btn = QtWidgets.QPushButton("Hoàn tất", self)
        self.iv_cancel_btn = QtWidgets.QPushButton("Hủy", self)

        self.init_ui()

    def init_ui(self):
        # font = QtGui.QFont("Fake Receipt", 8)
        font = QtGui.QFont("Merchant Copy", 18)
        self.invoice.setReadOnly(True)      # Read only applied
        self.invoice.setFont(font)
        self.layout.addWidget(self.invoice)
        self.layout2.addWidget(self.iv_charge_btn)
        self.layout2.addWidget(self.iv_cancel_btn)
        self.layout.addLayout(self.layout2)
        self.setLayout(self.layout)
        self.print_invoice()

        self.iv_charge_btn.clicked.connect(self.accept)

        self.iv_cancel_btn.clicked.connect(self.reject)
        self.show()

    def print_invoice(self):
        self.invoice.insertPlainText("      Hoa don ban le\n")
        self.invoice.insertPlainText("Nhan vien: %s\n" % self.employee_name)
        self.invoice.insertPlainText("Khach hang: %s\n" % self.customer_name)
        self.invoice.insertPlainText("--------------------------\n")
        self.invoice.insertPlainText("   Ma hoa don " + self.bill_code)
        for i in range(0, self.purchased_list.rowCount()):
            self.invoice.insertPlainText("\n\n\n%s  %s  x%s\n" % (self.purchased_list.item(i, 1).text(),
                                                                  self.purchased_list.item(i, 2).text(),
                                                                  self.purchased_list.item(i, 5).text()))
            self.invoice.insertPlainText("\n                %s\n" % self.purchased_list.item(i, 8).text())

        self.invoice.insertPlainText("--------------------------\n")
        self.invoice.insertPlainText("Tong gia:       %d" % self.total_price)
        self.invoice.insertPlainText("\nGiam gia:       %d %%" % self.discount)
        self.invoice.insertPlainText("\nKhach phai tra: %d" % self.actual_price)
        pass

    # def charge(self):
    #     # employee_code
    #     # total_cost = self.total_cost
    #     # discount = self.discount_percentage
    #     # bill_cost = self.discount_cost
    #     # customer_code = "1234"
    #     bill_note = "nah nah nah"
    #
    #     bill_db.insert(self.bill_code,
    #                    self.employee_code,
    #                    self.bill_date,
    #                    self.bill_time,
    #                    self.customer_code,
    #                    self.total_price,
    #                    self.discount,
    #                    self.actual_price,
    #                    bill_note)
    #
    #     for i in range(0, self.purchased_list.rowCount()):
    #         bill_detail_db.insert(self.bill_code,
    #                               str(self.purchased_list.item(i, 1).text()),
    #                               int(self.purchased_list.item(i, 5).text()),
    #                               float(self.purchased_list.item(i, 8).text()))


# class ExecuteThread(QtCore.QThread):
#     my_signal = QtCore.pyqtSignal()
#     def run(self):
#         self.my_signal.emit(
#
#         )


# app = QtWidgets.QApplication(sys.argv)
# ex = Invoice()
# sys.exit(app.exec_())