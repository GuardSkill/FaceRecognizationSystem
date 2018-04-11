# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DelDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleDialog(object):
    def __init__(self):
        super(Ui_DeleDialog, self).__init__()
        self.x = 0
        self.checkBoxs = []

    def setupUi(self, DeleDialog, names):
        DeleDialog.setObjectName("DeleDialog")
        DeleDialog.resize(313, 148)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 120, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox.setGeometry(QtCore.QRect(60, 10, 70, 15))
        self.checkBox.setObjectName("checkBox")
        self.checkBoxs.append(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 40, 70, 15))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBoxs.append(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 70, 70, 15))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBoxs.append(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_4.setGeometry(QtCore.QRect(180, 10, 70, 15))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBoxs.append(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_5.setGeometry(QtCore.QRect(180, 40, 70, 15))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBoxs.append(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(DeleDialog)
        self.checkBox_6.setGeometry(QtCore.QRect(180, 70, 70, 15))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBoxs.append(self.checkBox_6)
        self.pushButton = QtWidgets.QPushButton(DeleDialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        if names.__len__() <= 6:
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)
        self.redisplay(names)
        self.retranslateUi(DeleDialog)
        self.pushButton.clicked.connect(lambda: self.redisplay(names))
        self.buttonBox.accepted.connect(DeleDialog.accept)
        self.buttonBox.rejected.connect(DeleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleDialog)

    def redisplay(self, names):
        if self.x >= names.__len__():  # reset to zero when index>len(a loop to display all data)
            self.x = 0
        for i in range(0, 6):            #set every CheckBoxs's information
            if self.x < names.__len__():
                self.checkBoxs[i].setVisible(True)
                self.checkBoxs[i].setText(names[self.x])
                self.x += 1
            else:
                self.checkBoxs[i].setVisible(False)
                self.x += 1

    def retranslateUi(self, DeleDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleDialog.setWindowTitle(_translate("DeleDialog", "删除成员数据"))
        # for i in range(0,5):
        #  self.checkBoxs[i].setText(_translate("DeleDialog", "CheckBox"))
        # self.checkBox.setText(_translate("DeleDialog", "CheckBox"))
        # self.checkBox_2.setText(_translate("DeleDialog", "CheckBox"))
        # self.checkBox_3.setText(_translate("DeleDialog", "CheckBox"))
        # self.checkBox_4.setText(_translate("DeleDialog", "CheckBox"))
        # self.checkBox_5.setText(_translate("DeleDialog", "CheckBox"))
        # self.checkBox_6.setText(_translate("DeleDialog", "CheckBox"))
        self.pushButton.setText(_translate("DeleDialog", "next Page"))


