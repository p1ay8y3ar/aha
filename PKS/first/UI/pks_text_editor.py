# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pks_text_editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextEditor(object):
    def setupUi(self, TextEditor):
        TextEditor.setObjectName("TextEditor")
        TextEditor.resize(400, 300)
        self.textEditor = QtWidgets.QTextEdit(TextEditor)
        self.textEditor.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.textEditor.setObjectName("textEditor")
        self.bt_ok = QtWidgets.QPushButton(TextEditor)
        self.bt_ok.setGeometry(QtCore.QRect(280, 260, 113, 32))
        self.bt_ok.setObjectName("bt_ok")

        self.retranslateUi(TextEditor)
        QtCore.QMetaObject.connectSlotsByName(TextEditor)

    def retranslateUi(self, TextEditor):
        _translate = QtCore.QCoreApplication.translate
        TextEditor.setWindowTitle(_translate("TextEditor", "Form"))
        self.bt_ok.setText(_translate("TextEditor", "Ok"))
