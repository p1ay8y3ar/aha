'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-03-31 21:38:57
LastEditor: p1ay8y3ar
LastEditTime: 2021-03-31 23:03:17
Email: p1ay8y3ar@gmail.com
'''

from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox
from UI import pks_login
from UI import pks_text_editor
from UI import pks_user
from UI import pks_signup
from UI.db import User, convert_path

import hashlib


class LoginWindow(QWidget, pks_login.Ui_pks_login):
    """
    登陆界面
    """
    db_user = User  # sqllite3

    def __init__(self):
        QWidget.__init__(self)
        pks_login.Ui_pks_login.__init__(self)
        self.setupUi(self)

        # 设置槽函数
        self.bt_login.clicked.connect(self.login)
        self.bt_signup.clicked.connect(self.signup)
        self.rw = RegisterWin()
        
    def login(self):
        username = self.le_username.text()
        password = self.le_password.text()
        if len(username) == 0 or len(password) == 0:
            self.showmsg("account or password wrong")
            return
        if self.db_user.select().where(
                self.db_user.username == username).count() == 0:
            self.showmsg("account or password wrong")
            return
        password_md5 = hashlib.md5(password.encode("utf-8")).hexdigest()

        user_db = self.db_user.select().where(
            self.db_user.username == username).get()

        if user_db.password != password_md5:
            self.showmsg("account or password wrong")
            return

    def signup(self):
        
        
        self.rw.show()
        print("点击")

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)


class RegisterWin(QWidget, pks_signup.Ui_ResigerUI):
    def __init__(self):
        QWidget.__init__(self)
        pks_signup.Ui_ResigerUI.__init__(self)
        self.setupUi(self)


class UserInterface(QMainWindow, pks_user.Ui_UserInterface):
    """
    用户界面
    """
    def __init__(self):
        QMainWindow.__init__(self)
        pks_user.Ui_pks_login.__init__(self)
        self.setupUi(self)

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)


class TextEditor(QWidget, pks_text_editor.Ui_TextEditor):
    """
    编辑信息的界面
    """
    def __init__(self):
        QWidget.__init__(self)
        pks_text_editor.Ui_TextEditor.__init__(self)
        self.setupUi(self)

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)