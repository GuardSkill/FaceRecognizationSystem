# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MsgDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MsgDialog(object):
    def setupUi(self, MsgDialog,message):
        MsgDialog.setObjectName("MsgDialog")
        MsgDialog.resize(163, 65)
        self.pushButton = QtWidgets.QPushButton(MsgDialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(MsgDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label.setObjectName("label")
        self.label.setText(message)

        self.retranslateUi(MsgDialog)
        self.pushButton.clicked.connect(MsgDialog.close)
        QtCore.QMetaObject.connectSlotsByName(MsgDialog)

    def retranslateUi(self, MsgDialog):
        _translate = QtCore.QCoreApplication.translate
        MsgDialog.setWindowTitle(_translate("MsgDialog", "友情提示："))
        self.pushButton.setText(_translate("MsgDialog", "好嘛"))
        self.label.setText(_translate("MsgDialog", "TextLabel"))

