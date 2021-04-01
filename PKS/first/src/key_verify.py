# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_verify.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Verify(object):
    def setupUi(self, Verify):
        Verify.setObjectName("Verify")
        Verify.resize(400, 182)
        self.bt_load_rabin = QtWidgets.QPushButton(Verify)
        self.bt_load_rabin.setGeometry(QtCore.QRect(210, 30, 141, 71))
        self.bt_load_rabin.setObjectName("bt_load_rabin")
        self.bt_load_rsa = QtWidgets.QPushButton(Verify)
        self.bt_load_rsa.setGeometry(QtCore.QRect(30, 30, 141, 71))
        self.bt_load_rsa.setObjectName("bt_load_rsa")
        self.bt_verify = QtWidgets.QPushButton(Verify)
        self.bt_verify.setGeometry(QtCore.QRect(140, 130, 131, 41))
        self.bt_verify.setObjectName("bt_verify")

        self.retranslateUi(Verify)
        QtCore.QMetaObject.connectSlotsByName(Verify)

    def retranslateUi(self, Verify):
        _translate = QtCore.QCoreApplication.translate
        Verify.setWindowTitle(_translate("Verify", "Verify"))
        self.bt_load_rabin.setText(_translate("Verify", "openRabinPub"))
        self.bt_load_rsa.setText(_translate("Verify", "openRsaPub"))
        self.bt_verify.setText(_translate("Verify", "verify"))
