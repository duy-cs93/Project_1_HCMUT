'''
Created on Nov 15, 2018

@author: USER
'''
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
import os
import csv


class Login(QtWidgets.QDialog):
 
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
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.move(self.left, self.top)
        self.setFixedSize(self.width, self.height)
        
        #create label 1
        l1 = QtWidgets.QLabel(self)       
        l1.setText('Tên đăng nhập')
        l1.move(30, 50)
        # Create ID text box 1
        user_text = QtWidgets.QLineEdit(self)
        user_text.move(30, 80)
        user_text.resize(220, 25)
        
        #create label 2
        l2 = QtWidgets.QLabel(self)
        l2.setText('Mật khẩu')
        l2.move(30, 120)
        # Create password text box 2
        password_text = QtWidgets.QLineEdit(self)
        password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        password_text.move(30, 150)
        password_text.resize(220, 25)
        
        # Create button in the window
        self.button = QtWidgets.QPushButton('Quản lý', self)
        self.button.move(200, 300)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        self.show()
        
    def on_click(self):  
        self.close()
        self.main = MainWindow()
        self.main.show()
                

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super().__init__(parent)
        self.setup_ui(self)

    def setup_ui(self, MainWindow):
        MainWindow.setWindowTitle('Cửa hàng chính')
        # MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)

        #create menu_bar
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        # self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menu_bar.move(0, 0)
        self.menu_bar.setFixedSize(800, 21)
        self.quan_ly = QtWidgets.QMenu('Quản lý cửa hàng', self.menu_bar) 
        exit_app = QtWidgets.QAction('&Exit',self)
        exit_app.setShortcut('Ctrl+Q')
        exit_app.setStatusTip('ExitApplication')
        exit_app.triggered.connect(self.close)
        self.quan_ly.addAction(exit_app)


        self.hang_hoa = QtWidgets.QMenu('Hàng hóa', self.menu_bar)
        self.giao_dich = QtWidgets.QMenu('Giao dịch', self.menu_bar)
        self.doi_tac = QtWidgets.QMenu('Đối tác', self.menu_bar)
        self.so_quy = QtWidgets.QMenu('$ Sổ quỹ', self.menu_bar)
        self.bao_cao = QtWidgets.QMenu(' Báo cáo', self.menu_bar)

        self.danh_muc = QtWidgets.QAction('Danh mục', self)
        self.danh_muc.triggered.connect(self.show_win1)

        self.thiet_lap_gia = QtWidgets.QAction('Thiết lập giá', self)
        self.thiet_lap_gia.triggered.connect(self.show_win2)

        self.kiem_kho = QtWidgets.QAction('Kiểm kho', self)
        #self.kiem_kho.triggered.connect(self.show_win3)

        self.hoa_don = QtWidgets.QAction('Hóa đơn', self)
        #self.hoa_don.triggered.connect(self.show_win4)

        self.tra_hang = QtWidgets.QAction('Trả hàng', self)
        #self.tra_hang.triggered.connect(self.show_win5)

        self.nhap_hang = QtWidgets.QAction('Nhập hàng', self)
        #self.nhap_hang.triggered.connect(self.show_win6)

        self.tra_hang_nhap = QtWidgets.QAction('Trả hàng nhập', self)
        #self.tra_hang_nhap.triggered.connect(self.show_win7)

        self.xuat_huy = QtWidgets.QAction('Xuất hủy', self)
        #self.xuat_huy.triggered.connect(self.show_win8)

        self.khach_hang = QtWidgets.QAction('Khách hàng', self)
        self.khach_hang.triggered.connect(self.show_win9)

        self.nha_cung_cap = QtWidgets.QAction('Nhà cung cấp', self)
        #self.nha_cung_cap.triggered.connect(self.show_win10)
        
        self.hang_hoa.addAction(self.danh_muc)
        self.hang_hoa.addAction(self.thiet_lap_gia)
        self.hang_hoa.addAction(self.kiem_kho)
        self.giao_dich.addAction(self.hoa_don)
        self.giao_dich.addAction(self.tra_hang)
        self.giao_dich.addAction(self.nhap_hang)
        self.giao_dich.addAction(self.tra_hang_nhap)
        self.giao_dich.addAction(self.xuat_huy)
        self.doi_tac.addAction(self.khach_hang)
        self.doi_tac.addAction(self.nha_cung_cap)
        self.menu_bar.addAction(self.quan_ly.menuAction())
        self.menu_bar.addAction(self.hang_hoa.menuAction())
        self.menu_bar.addAction(self.giao_dich.menuAction())
        self.menu_bar.addAction(self.doi_tac.menuAction())
        self.menu_bar.addAction(self.so_quy.menuAction())
        self.menu_bar.addAction(self.bao_cao.menuAction())
     
     
    def show_win1(self):
        self.win1 = Window_1()
        self.win1.show()
            
    def show_win9(self):
        self.win9 = Window_9()
        self.win9.show()

class Window_1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):

        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Tên sản phẩm')
        self.l1.move(110,110)
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(200,100,200,30)

        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Danh mục')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Nhãn hiệu')
        self.l3.move(110, 210)
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(200, 200, 200, 30)
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Giá')
        self.l4.move(110,260)
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(200, 250,200, 30)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Chi tiết')
        self.l5.move(110,310)
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(200, 300, 200, 30)
        
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Hình')
        self.l5.move(110, 360)
        
        self.upload = QtWidgets.QPushButton('Upload hình',self)
        self.upload.move(300, 350)
        self.upload.clicked.connect(self.upload_hinh)
        
        self.button = QtWidgets.QPushButton('Insert',self)
        self.button.setGeometry(200, 400, 100, 30)
        
    def upload_hinh(self):
        self.image = QFileDialog.getOpenFileName(None,'OpenFile','',"Image file(*.jpg *gif *.png)")


class Window_2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
    
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(QtCore.QRect(10,10,600,350))
        self.table.setRowCount(10)
        self.table.setColumnCount(5)
        col_headers = ['Mã hàng hóa','Tên hàng','Giá bán','Giá vốn','Tồn kho']
        self.table.setHorizontalHeaderLabels(col_headers)
        
        self.btn_load = QtWidgets.QPushButton('Xuất file',self)
        self.btn_load.move(200,400)
        self.btn_load.clicked.connect(self.export_csv)
        
    def export_csv(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'),'CSV(*.csv')
        if path[0] != '':
            with open(path[0],newline ='') as csv_file:
                writer = csv.writer(csv_file,dialect ='excel')
                for row in range(self.rowCount()):
                    row_data  = []
                    for column in range(self.colorCount()):
                        item = self.item(row , column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)

class Window_9(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Tên khách hàng')
        self.l1.move(110, 110)
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(200, 100, 200, 30)
        
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Địa chỉ')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Số điện thoại')
        self.l3.move(110, 210)
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(200, 200, 200, 30)
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Giói tính')
        self.l3.move(110, 260)
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(200, 250, 200, 30)
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Giới tính')
        self.l4.move(110, 310)
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(200, 300, 200, 30)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Ngày tham gia')
        self.l5.move(110, 360)
        self.line_edit6 = QtWidgets.QLineEdit(self)
        self.line_edit6.setGeometry(200, 350, 200, 30)
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        self.button.setGeometry(200, 400, 100, 30)

   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())