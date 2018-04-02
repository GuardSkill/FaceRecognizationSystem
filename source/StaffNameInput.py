# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffNameInput.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StaffInputDialog(object):
    def setupUi(self, StaffInputDialog):
        StaffInputDialog.setObjectName("StaffInputDialog")
        StaffInputDialog.resize(235, 82)
        self.buttonBox = QtWidgets.QDialogButtonBox(StaffInputDialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 10, 61, 301))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(StaffInputDialog)
        self.textEdit.setGeometry(QtCore.QRect(70, 25, 80, 30))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(StaffInputDialog)
        self.label.setGeometry(QtCore.QRect(10, 25, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(StaffInputDialog)
        self.buttonBox.accepted.connect(StaffInputDialog.accept)
        self.buttonBox.rejected.connect(StaffInputDialog.reject)
        self.buttonBox.accepted.connect(StaffInputDialog.newstaff)
        QtCore.QMetaObject.connectSlotsByName(StaffInputDialog)

    def retranslateUi(self, StaffInputDialog):
        _translate = QtCore.QCoreApplication.translate
        StaffInputDialog.setWindowTitle(_translate("StaffInputDialog", "Dialog"))
        self.label.setText(_translate("StaffInputDialog", "Name:"))

