'''
Created on Nov 15, 2018

@author: USER
'''
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap

class Login(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Log in'
        self.left = 380
        self.top = 220
        self.width = 540
        self.height = 380
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #create label 1
        l1 = QLabel(self)       
        l1.setText('Tên đăng nhập')
        l1.move(30,50)
        # Create ID text box 1
        user_text = QLineEdit(self)
        user_text.move(30, 80)
        user_text.resize(220,25)
        
        #create label 2
        l2 = QLabel(self)
        l2.setText('Mật khẩu')
        l2.move(30,120)
        # Create password text box 2
        password_text = QLineEdit(self)
        password_text.setEchoMode(QLineEdit.Password)
        password_text.move(30, 150)
        password_text.resize(220,25)
        
        # Create button in the window
        self.button = QPushButton('Quản lý', self)
        self.button.move(200,300)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        self.show()
        
    @pyqtSlot() 
    def on_click(self):  
        self.close()
        self.main = MainWindow()
        self.main.show()
                

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        
        
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Cửa hàng chính')
        MainWindow.resize(800, 600)
        
        #create menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))    
        
        self.quan_ly = QtWidgets.QMenu('Quản lý cửa hàng', self.menubar) 
        exitApp = QAction('&Exit',self)
        exitApp.setShortcut('Ctrl+Q')
        exitApp.setStatusTip('ExitApplication')
        exitApp.triggered.connect(self.close)
        self.quan_ly.addAction(exitApp)
        

        self.hang_hoa = QtWidgets.QMenu('Hàng hóa', self.menubar)
        self.giao_dich = QtWidgets.QMenu('Giao dịch', self.menubar)
        self.doi_tac = QtWidgets.QMenu('Đối tác', self.menubar)
        self.so_quy = QtWidgets.QMenu('$ Sổ quỹ', self.menubar)
        self.bao_cao = QtWidgets.QMenu(' Báo cáo', self.menubar)
        
        self.danh_muc = QtWidgets.QAction('Danh mục', self)
        self.danh_muc.triggered.connect(self.show_win1)
        
        self.thiet_lap_gia = QtWidgets.QAction('Thiết lập giá', self)
        #self.thiet_lap_gia.triggered.connect(self.show_win2)
        
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
        self.menubar.addAction(self.quan_ly.menuAction())
        self.menubar.addAction(self.hang_hoa.menuAction())
        self.menubar.addAction(self.giao_dich.menuAction())
        self.menubar.addAction(self.doi_tac.menuAction())
        self.menubar.addAction(self.so_quy.menuAction())
        self.menubar.addAction(self.bao_cao.menuAction())
     
     
    def show_win1(self):
        self.win1 = Window_1()
        self.win1.show()
            
    def show_win9(self):
        self.win9 = Window_9()
        self.win9.show()

class Window_1(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):

        self.l1 = QLabel(self)
        self.l1.setText('Tên sản phẩm')
        self.l1.move(110,110)
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setGeometry(200,100,200,30)
        
        
        self.l2 = QLabel(self)
        self.l2.setText('Danh mục')
        self.l2.move(110,160)
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setGeometry(200,150,200,30)
        
        self.l3 = QLabel(self)
        self.l3.setText('Nhãn hiệu')
        self.l3.move(110,210)
        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setGeometry(200,200,200,30)
        
        
        self.l4 = QLabel(self)
        self.l4.setText('Giá')
        self.l4.move(110,260)
        self.lineedit4 = QLineEdit(self)
        self.lineedit4.setGeometry(200,250,200,30)
        
        
        self.l5 = QLabel(self)
        self.l5.setText('Chi tiết')
        self.l5.move(110,310)
        self.lineedit5 = QLineEdit(self)
        self.lineedit5.setGeometry(200,300,200,30)
        
        
        self.l5 = QLabel(self)
        self.l5.setText('Hình')
        self.l5.move(110,360)
        
        self.upload = QPushButton('Upload hình',self)
        self.upload.move(300,350)
        self.upload.clicked.connect(self.upload_hinh)
        
        self.button = QPushButton('Insert',self)
        self.button.setGeometry(200,400,100,30)
        
    def upload_hinh(self):
        self.image = QFileDialog.getOpenFileName(None,'OpenFile','',"Image file(*.jpg *gif *.png)")

class Window_9(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.l1 = QLabel(self)
        self.l1.setText('Tên khách hàng')
        self.l1.move(110,110)
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setGeometry(200,100,200,30)
        
        
        self.l2 = QLabel(self)
        self.l2.setText('Địa chỉ')
        self.l2.move(110,160)
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setGeometry(200,150,200,30)
        
        
        self.l3 = QLabel(self)
        self.l3.setText('Số điện thoại')
        self.l3.move(110,210)
        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setGeometry(200,200,200,30)
        
        self.l3 = QLabel(self)
        self.l3.setText('Giói tính')
        self.l3.move(110,260)
        self.lineedit4 = QLineEdit(self)
        self.lineedit4.setGeometry(200,250,200,30)
        
        self.l4 = QLabel(self)
        self.l4.setText('Giới tính')
        self.l4.move(110,310)
        self.lineedit5 = QLineEdit(self)
        self.lineedit5.setGeometry(200,300,200,30)
        
        self.l5 = QLabel(self)
        self.l5.setText('Ngày tham gia')
        self.l5.move(110,360)
        self.lineedit6 = QLineEdit(self)
        self.lineedit6.setGeometry(200,350,200,30)
        
        self.button = QPushButton('Lưu',self)
        self.button.setGeometry(200,400,100,30)

   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())