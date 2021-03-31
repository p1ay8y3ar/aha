# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pks_signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResigerUI(object):
    def setupUi(self, ResigerUI):
        ResigerUI.setObjectName("ResigerUI")
        ResigerUI.resize(375, 185)
        self.label = QtWidgets.QLabel(ResigerUI)
        self.label.setGeometry(QtCore.QRect(40, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ResigerUI)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ResigerUI)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.le_username = QtWidgets.QLineEdit(ResigerUI)
        self.le_username.setGeometry(QtCore.QRect(130, 30, 191, 21))
        self.le_username.setObjectName("le_username")
        self.le_pwd = QtWidgets.QLineEdit(ResigerUI)
        self.le_pwd.setGeometry(QtCore.QRect(130, 70, 191, 21))
        self.le_pwd.setObjectName("le_pwd")
        self.le_pwd_again = QtWidgets.QLineEdit(ResigerUI)
        self.le_pwd_again.setGeometry(QtCore.QRect(130, 110, 191, 21))
        self.le_pwd_again.setObjectName("le_pwd_again")
        self.bt_register = QtWidgets.QPushButton(ResigerUI)
        self.bt_register.setGeometry(QtCore.QRect(220, 140, 113, 32))
        self.bt_register.setObjectName("bt_register")

        self.retranslateUi(ResigerUI)
        QtCore.QMetaObject.connectSlotsByName(ResigerUI)

    def retranslateUi(self, ResigerUI):
        _translate = QtCore.QCoreApplication.translate
        ResigerUI.setWindowTitle(_translate("ResigerUI", "Register"))
        self.label.setText(_translate("ResigerUI", "username"))
        self.label_2.setText(_translate("ResigerUI", "password"))
        self.label_3.setText(_translate("ResigerUI", "password"))
        self.bt_register.setText(_translate("ResigerUI", "register"))
