'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-03-31 22:56:03
LastEditor: p1ay8y3ar
LastEditTime: 2021-04-01 13:44:17
Email: p1ay8y3ar@gmail.com
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pks_signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterUI(object):
    def setupUi(self, RegisterUI):
        RegisterUI.setObjectName("RegisterUI")
        RegisterUI.resize(375, 185)
        self.label = QtWidgets.QLabel(RegisterUI)
        self.label.setGeometry(QtCore.QRect(40, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(RegisterUI)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(RegisterUI)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.le_username = QtWidgets.QLineEdit(RegisterUI)
        self.le_username.setGeometry(QtCore.QRect(130, 30, 191, 21))
        self.le_username.setObjectName("le_username")
        self.le_pwd = QtWidgets.QLineEdit(RegisterUI)
        self.le_pwd.setGeometry(QtCore.QRect(130, 70, 191, 21))
        self.le_pwd.setObjectName("le_pwd")
        self.le_pwd_again = QtWidgets.QLineEdit(RegisterUI)
        self.le_pwd_again.setGeometry(QtCore.QRect(130, 110, 191, 21))
        self.le_pwd_again.setObjectName("le_pwd_again")
        self.bt_register = QtWidgets.QPushButton(RegisterUI)
        self.bt_register.setGeometry(QtCore.QRect(220, 140, 113, 32))
        self.bt_register.setObjectName("bt_register")

        self.retranslateUi(RegisterUI)
        QtCore.QMetaObject.connectSlotsByName(RegisterUI)

    def retranslateUi(self, RegisterUI):
        _translate = QtCore.QCoreApplication.translate
        RegisterUI.setWindowTitle(_translate("RegisterUI", "Register"))
        self.label.setText(_translate("RegisterUI", "username"))
        self.label_2.setText(_translate("RegisterUI", "password"))
        self.label_3.setText(_translate("RegisterUI", "password"))
        self.le_username.setPlaceholderText(_translate("RegisterUI", "length more than 8"))
        self.le_pwd.setPlaceholderText(_translate("RegisterUI", "length more than 8"))
        self.le_pwd_again.setPlaceholderText(_translate("RegisterUI", "please input agin"))
        self.bt_register.setText(_translate("RegisterUI", "OK"))
