# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from ORM import  CheckInfo

class Ui_Form(object):
    def setupUi(self, Form,infos):
        Form.setObjectName("Form")
        Form.resize(420, 400)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 400, 350))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(infos.__len__())
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        i=0
        #
        for info in infos:
            self.tableWidget.setItem(i,0,QTableWidgetItem(info.name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(info.up_time.hour)+':'+str(info.up_time.minute)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(info.off_time.hour) + ':' + str(info.off_time.minute)))
            delta=info.off_time-info.up_time
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(int(delta.total_seconds()/60))))
            i+=1

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "今日考勤信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "上班时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "下班时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "工作时长"))
        self.label.setText(_translate("Form", "今日考勤信息"))


