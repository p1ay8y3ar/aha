# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pks_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pks_login(object):
    def setupUi(self, pks_login):
        pks_login.setObjectName("pks_login")
        pks_login.resize(294, 192)
        self.bt_login = QtWidgets.QPushButton(pks_login)
        self.bt_login.setGeometry(QtCore.QRect(30, 130, 81, 31))
        self.bt_login.setObjectName("bt_login")
        self.la_username = QtWidgets.QLabel(pks_login)
        self.la_username.setGeometry(QtCore.QRect(20, 20, 81, 51))
        self.la_username.setObjectName("la_username")
        self.bt_signup = QtWidgets.QPushButton(pks_login)
        self.bt_signup.setGeometry(QtCore.QRect(170, 130, 81, 31))
        self.bt_signup.setObjectName("bt_signup")
        self.la_password = QtWidgets.QLabel(pks_login)
        self.la_password.setGeometry(QtCore.QRect(20, 60, 81, 51))
        self.la_password.setObjectName("la_password")
        self.le_username = QtWidgets.QLineEdit(pks_login)
        self.le_username.setGeometry(QtCore.QRect(110, 40, 151, 21))
        self.le_username.setObjectName("le_username")
        self.le_password = QtWidgets.QLineEdit(pks_login)
        self.le_password.setGeometry(QtCore.QRect(110, 80, 151, 21))
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")

        self.retranslateUi(pks_login)
        QtCore.QMetaObject.connectSlotsByName(pks_login)

    def retranslateUi(self, pks_login):
        _translate = QtCore.QCoreApplication.translate
        pks_login.setWindowTitle(_translate("pks_login", "PublicKeySystem"))
        self.bt_login.setText(_translate("pks_login", "login"))
        self.la_username.setText(_translate("pks_login", "username"))
        self.bt_signup.setText(_translate("pks_login", "signup"))
        self.la_password.setText(_translate("pks_login", "password"))
