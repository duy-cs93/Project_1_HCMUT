'''
Created on Dec 3, 2018

@author: USER
'''
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMainWindow
import os
import csv

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from store_application.lib import PlotCanvas
from store_application.lib import read_json
from store_application.lib import MyTable


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
        self.l1 = QtWidgets.QLabel(self)       
        self.l1.setText('Tên đăng nhập')
        self.l1.move(30, 50)
        # Create ID text box 1
        self.user_text = QtWidgets.QLineEdit(self)
        self.user_text.move(30, 80)
        self.user_text.resize(220, 25)
        
        #create label 2
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

        self.nhan_vien = QtWidgets.QAction('Nhân viên', self)
        self.nhan_vien.triggered.connect(self.show_win10)
        
        self.tuan = QtWidgets.QAction('Tuần rồi',self)
        self.tuan.triggered.connect(self.show_win11)
        
        '''self.thang = QtWidgets.QAction('Trong tháng',self)
        self.thang.triggered.connect(self.show_win12)'''
        
        self.hang_hoa.addAction(self.danh_muc)
        self.hang_hoa.addAction(self.thiet_lap_gia)
        self.hang_hoa.addAction(self.kiem_kho)
        self.giao_dich.addAction(self.hoa_don)
        self.giao_dich.addAction(self.tra_hang)
        self.giao_dich.addAction(self.nhap_hang)
        self.giao_dich.addAction(self.tra_hang_nhap)
        self.giao_dich.addAction(self.xuat_huy)
        self.doi_tac.addAction(self.khach_hang)
        self.doi_tac.addAction(self.nhan_vien)
        
        self.bao_cao.addAction(self.tuan)
        #self.bao_cao.addAction(self.thang) 
        
        self.menu_bar.addAction(self.quan_ly.menuAction())
        self.menu_bar.addAction(self.hang_hoa.menuAction())
        self.menu_bar.addAction(self.giao_dich.menuAction())
        self.menu_bar.addAction(self.doi_tac.menuAction())
        self.menu_bar.addAction(self.so_quy.menuAction())
        self.menu_bar.addAction(self.bao_cao.menuAction())
   
    def show_win1(self):
        self.win1 = Window_1()
        self.win1.show()
            
    def show_win2(self):
        self.win1 = Window_2()
        self.win1.show()
        
    def show_win9(self):
        self.win9 = Window_9()
        self.win9.show()
        
    def show_win10(self):
        self.win10 = Window_10()
        self.win10.show()
        
    def show_win11(self):
        self.win11 = Window_11()
        self.win11.show()


class Window_1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  
        
        self.setFixedSize(700,400)
        self.form_widget = MyTable(10, 5)
        self.setCentralWidget(self.form_widget)
        self.form_widget.setHorizontalHeaderLabels(["Mã hàng", "Tên hàng", "Giá bán", "Giá vốn", "Tồn kho"])
     
     
        self.load = QtWidgets.QPushButton('Nhập file',self)
        self.load.move(600,50)
        self.load.resize(60,35)
        self.load.clicked.connect(self.form_widget.open_sheet)
     
        self.export = QtWidgets.QPushButton('Xuất file',self)
        self.export.move(600,100)
        self.export.resize(60,35)
        self.export.clicked.connect(self.form_widget.save_sheet)
        
        self.btn_add = QtWidgets.QPushButton('Thêm mới',self)
        self.btn_add.move(600,150)
        self.btn_add.resize(60,35)
        self.btn_add.clicked.connect(self.add)
        
    def add(self):
        self.adding = Add()
        self.adding.show()
        

class Window_2(QtWidgets.QMainWindow):
    def __init__(self):
        
        super().__init__()
        
        self.setFixedSize(600,400)
        self.form_widget_2 = MyTable(10,4)
        self.setCentralWidget(self.form_widget_2)
        col_headers = ['Mã hàng hóa','Tên hàng','Giá cũ','Giá mới']
        self.form_widget_2.setHorizontalHeaderLabels(col_headers)
                      
        self.btn_save = QtWidgets.QPushButton('Lưu',self)
        # !!!!!!!!!!!!!!! important
        '''self.btn_save.clicked.connect(self.insert_data())'''
        self.btn_save.move(100,340)
        self.btn_save.resize(60,35)
        #self.btn_save.clicked.connect(self.save)
        
        self.btn_load = QtWidgets.QPushButton('Xuất file',self)
        self.btn_load.move(200,340)
        self.btn_load.resize(60,35)
        self.btn_load.clicked.connect(self.form_widget_2.save_sheet)

    '''                
    def insert_data(self):
        gia_moi = [self.table.item(row, 2).text() for row in range(self.table.rowCount())]
        
        con = mdb.connect('localhost', 'root', '', 'pyqt5')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO data(gia_moi)"
                        "VALUES('%s')" %(''.join(gia_moi)))'''
                    
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
        #self.line_edit1.textChanged.connect(self.newText)
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Địa chỉ')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        #self.line_edit2.textChanged.connect(self.newText)
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Số điện thoại')
        self.l3.move(110, 210)
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(200, 200, 200, 30)
        #self.line_edit3.textChanged.connect(self.newText)
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Giói tính')
        self.l4.move(110, 260)
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(200, 250, 200, 30)
        #self.line_edit4.textChanged.connect(self.newText)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Giới tính')
        self.l5.move(110, 310)
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(200, 300, 200, 30)
        #self.line_edit5.textChanged.connect(self.newText)
        
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText('Ngày tham gia')
        self.l6.move(110, 360)
        self.line_edit6 = QtWidgets.QLineEdit(self)
        self.line_edit6.setGeometry(200, 350, 200, 30)
        #self.line_edit6.textChanged.connect(self.newText)
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        #self.button.clicked.connect(self.insert_data())
        self.button.setGeometry(200, 400, 100, 30)
    '''  
    def insert_data(self):
        con = mdb.connect(host="localhost",user="user", passwd="password",db="testdb")
        
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO pyqt5data(name, email, phone)
                           VALUES (%s, %s, %s)", 
                           ( self.line_edit1.text(),
                             self.line_edit2.text(),
                             self.line_edit3.text(),
                             self.line_edit4.text(),
                             self.line_edit5.text(),
                             self.line_edit6.text() )
                       )            
            cur.close()
        self.line_edit1.setText('')
        self.line_edit2.setText('')
        self.line_edit3.setText('')
        self.line_edit4.text()
        self.line_edit5.text()
        self.line_edit6.text()
        self.init_ui() 
        
    def newText(self):
        if self.line_edit1.text() and self.line_edit2.text() and self.line_edit3.text() and\
        self.line_edit4.text() and self.line_edit5.text() and self.line_edit6.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)  
     '''
                      
class Window_10(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Tên nhân viên')
        self.l1.move(110, 110)
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(200, 100, 200, 30)
        
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Giới tính')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Địa chỉ')
        self.l3.move(110, 210)
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(200, 200, 200, 30)
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Số điện thoại')
        self.l4.move(110, 260)
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(200, 250, 200, 30)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('DOB')
        self.l5.move(110, 310)
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(200, 300, 200, 30)
        
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText('FWD')
        self.l6.move(110, 360)
        self.line_edit6 = QtWidgets.QLineEdit(self)
        self.line_edit6.setGeometry(200, 350, 200, 30)
        
        self.l7 = QtWidgets.QLabel(self)
        self.l7.setText('Lương')
        self.l7.move(110, 410)
        self.line_edit7 = QtWidgets.QLineEdit(self)
        self.line_edit7.setGeometry(200, 400, 200, 30)
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        self.button.setGeometry(200, 450, 100, 30)
        #self.button.clicked.connect(self.insert_data())
    '''  
    def insert_data(self):
        con = mdb.connect(host="localhost",user="user", passwd="password",db="testdb")
        
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO pyqt5data(name, email, phone)
                           VALUES (%s, %s, %s)", 
                           ( self.line_edit1.text(),
                             self.line_edit2.text(),
                             self.line_edit3.text(),
                             self.line_edit4.text(),
                             self.line_edit5.text(),
                             self.line_edit6.text(),
                             self.line_edit7.text() )
                       )            
            cur.close()
        self.line_edit1.setText('')
        self.line_edit2.setText('')
        self.line_edit3.setText('')
        self.line_edit4.text()
        self.line_edit5.text()
        self.line_edit6.text()
        self.line_edit7.text()
        self.init_ui() 
        
    def newText(self):
        if self.line_edit1.text() and self.line_edit2.text() and self.line_edit3.text() and\
        self.line_edit4.text() and self.line_edit5.text() and self.line_edit6.text()\
        and self.line_edit7.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)  
     '''

class Window_11(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 400
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        m = PlotCanvas(self,width=5,height=4)
        
        button = QtWidgets.QPushButton('Test',self)
        button.move(500,0)
        button.resize(100,100)
        
        self.show() 
        
class Add(QtWidgets.QDialog):
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
        
                
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())