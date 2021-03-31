# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pks_user.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserInterface(object):
    def setupUi(self, UserInterface):
        UserInterface.setObjectName("UserInterface")
        UserInterface.resize(364, 273)
        self.la_showname = QtWidgets.QLabel(UserInterface)
        self.la_showname.setGeometry(QtCore.QRect(40, 20, 131, 41))
        self.la_showname.setObjectName("la_showname")
        self.bt_dl_rabin_pubkey = QtWidgets.QPushButton(UserInterface)
        self.bt_dl_rabin_pubkey.setGeometry(QtCore.QRect(180, 110, 141, 41))
        self.bt_dl_rabin_pubkey.setObjectName("bt_dl_rabin_pubkey")
        self.bt_generateRabinKey = QtWidgets.QPushButton(UserInterface)
        self.bt_generateRabinKey.setGeometry(QtCore.QRect(20, 110, 141, 41))
        self.bt_generateRabinKey.setObjectName("bt_generateRabinKey")
        self.bt_dl_raspubkey = QtWidgets.QPushButton(UserInterface)
        self.bt_dl_raspubkey.setGeometry(QtCore.QRect(20, 160, 141, 41))
        self.bt_dl_raspubkey.setObjectName("bt_dl_raspubkey")
        self.bt_encrypt_msg = QtWidgets.QPushButton(UserInterface)
        self.bt_encrypt_msg.setGeometry(QtCore.QRect(20, 200, 141, 41))
        self.bt_encrypt_msg.setObjectName("bt_encrypt_msg")
        self.bt_decrypt_msg = QtWidgets.QPushButton(UserInterface)
        self.bt_decrypt_msg.setGeometry(QtCore.QRect(180, 200, 141, 41))
        self.bt_decrypt_msg.setObjectName("bt_decrypt_msg")
        self.bt_verify_signature = QtWidgets.QPushButton(UserInterface)
        self.bt_verify_signature.setGeometry(QtCore.QRect(180, 160, 141, 41))
        self.bt_verify_signature.setObjectName("bt_verify_signature")
        self.la_status = QtWidgets.QLabel(UserInterface)
        self.la_status.setGeometry(QtCore.QRect(0, 250, 361, 21))
        self.la_status.setText("")
        self.la_status.setObjectName("la_status")
        self.bt_changepwd = QtWidgets.QPushButton(UserInterface)
        self.bt_changepwd.setGeometry(QtCore.QRect(180, 60, 141, 41))
        self.bt_changepwd.setObjectName("bt_changepwd")
        self.bt_change_sign = QtWidgets.QPushButton(UserInterface)
        self.bt_change_sign.setGeometry(QtCore.QRect(20, 60, 141, 41))
        self.bt_change_sign.setObjectName("bt_change_sign")

        self.retranslateUi(UserInterface)
        QtCore.QMetaObject.connectSlotsByName(UserInterface)

    def retranslateUi(self, UserInterface):
        _translate = QtCore.QCoreApplication.translate
        UserInterface.setWindowTitle(_translate("UserInterface", "Form"))
        self.la_showname.setText(_translate("UserInterface", "用户名称"))
        self.bt_dl_rabin_pubkey.setText(_translate("UserInterface", "dl_rabin_pubkey"))
        self.bt_generateRabinKey.setText(_translate("UserInterface", "generate_rabinkey"))
        self.bt_dl_raspubkey.setText(_translate("UserInterface", "dl_sign_pubkey"))
        self.bt_encrypt_msg.setText(_translate("UserInterface", "encrypt_msg"))
        self.bt_decrypt_msg.setText(_translate("UserInterface", "decrypt_msg"))
        self.bt_verify_signature.setText(_translate("UserInterface", "verify_signature"))
        self.bt_changepwd.setText(_translate("UserInterface", "changepassword"))
        self.bt_change_sign.setText(_translate("UserInterface", "changepassword"))
