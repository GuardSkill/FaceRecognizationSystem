# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DelDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleDialog(object):
    def setupUi(self, DeleDialog):
        DeleDialog.setObjectName("DeleDialog")
        DeleDialog.resize(313, 148)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 120, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox.setGeometry(QtCore.QRect(60, 10, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 10, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 40, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_4.setGeometry(QtCore.QRect(180, 40, 71, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_5.setGeometry(QtCore.QRect(60, 70, 71, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_6.setGeometry(QtCore.QRect(180, 70, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.pushButton = QtWidgets.QPushButton(DeleDialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeleDialog)
        self.buttonBox.accepted.connect(DeleDialog.accept)
        self.buttonBox.rejected.connect(DeleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleDialog)

    def retranslateUi(self, DeleDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleDialog.setWindowTitle(_translate("DeleDialog", "删除成员数据"))
        self.checkBox.setText(_translate("DeleDialog", "CheckBox"))
        self.checkBox_2.setText(_translate("DeleDialog", "CheckBox"))
        self.checkBox_3.setText(_translate("DeleDialog", "CheckBox"))
        self.checkBox_4.setText(_translate("DeleDialog", "CheckBox"))
        self.checkBox_5.setText(_translate("DeleDialog", "CheckBox"))
        self.checkBox_6.setText(_translate("DeleDialog", "CheckBox"))
        self.pushButton.setText(_translate("DeleDialog", "next Page"))

