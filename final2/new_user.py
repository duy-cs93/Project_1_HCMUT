import sys
from PyQt5 import QtWidgets
from PyQt5.Qt import QDialog
import json
import main2
from read_json import *

# def read_json():
#     data_file = open("user.json",encoding = 'UTF-8')
#     data = json.load(data_file)
#     data_file.close()
#     return data

class new_user(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Đăng ký new user')
        self.init_ui()
        
    def init_ui(self):
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText('Tên đăng nhập')
        self.label_1.move(40, 40)

        self.user_text = QtWidgets.QLineEdit(self)
        self.user_text.move(120, 35)
        self.user_text.resize(190, 25)
        self.user_text.setStyleSheet('background-color:#64ff64; color:#000000;padding-top:0px;'\
                                     'font-size:10px;padding-left:10px;font: bold 12px')


        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText('Mật khẩu')
        self.label_2.move(65, 75)
        self.password_text = QtWidgets.QLineEdit(self)
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.move(120, 70)
        self.password_text.resize(190, 25)
        self.password_text.setStyleSheet('background-color:#64ff64; color:#000000;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')
        
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText('Xác nhận mật khẩu')
        self.label_3.move(20,110)
        self.cfm_password = QtWidgets.QLineEdit(self)
        self.cfm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cfm_password.move(120, 105)
        self.cfm_password.resize(190, 25)
        self.cfm_password.setStyleSheet('background-color:#64ff64; color:#000000;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')
        
        self.add_btn = QtWidgets.QPushButton('Thêm', self)
        self.add_btn.move(90, 180)
        self.add_btn.resize(80, 30)
        self.add_btn.clicked.connect(self.add)
        
        self.cancel_btn = QtWidgets.QPushButton('Hủy', self)
        self.cancel_btn.move(180, 180)
        self.cancel_btn.resize(80, 30)
        self.cancel_btn.clicked.connect(self.close)     
        
        self.show()
        
    def add(self):
        if not self.user_text.text():
            self.error = error_form("Hãy nhập vào username")
            self.error.show()
        else:
            data = read_json()
            if self.password_text.text() == self.cfm_password.text():
                data.update({self.user_text.text():[[self.user_text.text(),self.password_text.text()]]})
                with open('user.json',mode='w',encoding='utf-8') as f:
                    json.dump(data,f)
                self.success = QtWidgets.QErrorMessage()
                self.success.showMessage('Đăng ký thành công !')
                self.close()
                self.login = main2.Login()
                self.login.show()
            else:
                self.error = error_form('Mật khẩu chưa trùng khớp')
                self.error.show()
            
class error_form(QDialog):
    def __init__(self,text):
        super().__init__()
        self.text = text
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Lỗi')
        self.resize(200,100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(50,30)
        self.l1.setText(self.text)
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(65,60)
        self.button.clicked.connect(self.close)            
        
#         
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ex = new_user()
#     sys.exit(app.exec_())
    
