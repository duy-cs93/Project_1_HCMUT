import sys
from PyQt5 import QtWidgets, QtGui
import bill_detail_db
import bill_db


class BillDetail(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600
        self.title = "Bill details"
        self.tab_list = []
        self.list, self.row_count = bill_detail_db.select_all()
        self.bill, self.bill_count = bill_db.select_all()

        # initially declare variables
        self.tab_widget = None
        self.layout = None
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(self.width, self.height)

        self.setWindowTitle(self.title)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.bill_tab = QtWidgets.QTabWidget(self)
        self.bill_tab.layout = QtWidgets.QVBoxLayout(self)
        for i in range(0, self.bill_count):
            self.tab_list.append(None)
            self.tab_list[i] = Tab()
            self.bill_tab.layout.addWidget(self.tab_list[i])

        self.layout.addWidget(self.bill_tab)
        self.show()


class Tab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.a = QtWidgets.QLabel("hello")
        self.a.move(200, 200)
        self.init_ui()

    def init_ui(self):
        # self.show()
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = BillDetail()
    sys.exit(app.exec_())


