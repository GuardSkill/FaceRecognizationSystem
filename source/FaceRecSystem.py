# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceRecSystem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from DelDialog import Ui_DeleDialog
from StaffNameInput import Ui_StaffInput
from pick_class import Info  # for pickle get a instance
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2
import face_recognition
import time
import pickle
from ORM import  CheckInfo,Service
from tableWidget import Ui_Form


class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    managerRec = pyqtSignal()
    staffRec = pyqtSignal()
    unknownRec = pyqtSignal()
    noneRec = pyqtSignal()

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.cap = cv2.VideoCapture(0)
        self.fn = 'data.pkl'
        self.loaddata()

    def run(self):
        # cap.set(6, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));
        while True:
            ret, frame = self.cap.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            face_locations = face_recognition.face_locations(small_frame)
            if face_locations.__len__() == 0:  # no face was detected
                self.noneRec.emit()
            self.face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            self.face_names = []
            # compare face
            for face_encoding in self.face_encodings:  # scan every face in video
                match = face_recognition.compare_faces(self.encodings, face_encoding)  # compare every face in data
                for i in range(0, self.encodings.__len__()):
                    if match[i]:
                        name = self.infos[i].name
                        if (self.infos[i].admin == 1):
                            self.managerRec.emit()
                        else:
                            self.staffRec.emit()
                        break
                    else:
                        name = "unknown"
                        self.unknownRec.emit()
                self.face_names.append(name)  # tag name for each face in camera

            # draw rectangle
            for (top, right, bottom, left), name in zip(face_locations, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            qimage = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
            qpixmap = QPixmap.fromImage(qimage).scaled(300, 250, Qt.KeepAspectRatio)

            self.changePixmap.emit(qpixmap)
            time.sleep(0.03)

    def loaddata(self):
        with open(self.fn, 'rb') as f:
            self.infos = pickle.load(f, fix_imports=False)
        self.encodings = []
        self.names = []
        for info in self.infos:
            self.encodings.append(info.encoding)
            self.names.append(info.name)

    def savedata(self):
        with open(self.fn, 'wb') as f:  # open file with write-mode
            pickle.dump(self.infos, f, fix_imports=False)  # serialize and save object

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.amsignButton = QtWidgets.QPushButton(self.centralwidget)
        self.amsignButton.setEnabled(False)
        self.amsignButton.setGeometry(QtCore.QRect(330, 10, 61, 41))
        self.amsignButton.setDefault(True)
        self.amsignButton.setFlat(False)
        self.amsignButton.setObjectName("amsignButton")
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(330, 110, 61, 41))
        self.infoButton.setObjectName("infoButton")
        self.infoButton.setDefault(True)
        self.pmsignButton = QtWidgets.QPushButton(self.centralwidget)
        self.pmsignButton.setEnabled(False)
        self.pmsignButton.setFlat(False)
        self.pmsignButton.setDefault(True)
        self.pmsignButton.setGeometry(QtCore.QRect(330, 60, 61, 41))
        self.pmsignButton.setObjectName("pmsignButton")
        self.manageButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageButton.setEnabled(False)
        self.manageButton.setFlat(False)
        self.manageButton.setDefault(True)
        self.manageButton.setGeometry(QtCore.QRect(330, 160, 61, 41))
        self.manageButton.setObjectName("manageButton")
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setGeometry(QtCore.QRect(0, 0, 300, 250))
        self.video_label.setObjectName("video_label")
        self.staffButton = QtWidgets.QPushButton(self.centralwidget)
        self.staffButton.setEnabled(True)
        self.staffButton.setGeometry(QtCore.QRect(330, 10, 61, 41))
        self.staffButton.setDefault(True)
        self.staffButton.setFlat(False)
        self.staffButton.setObjectName("staffButton")
        self.manButton = QtWidgets.QPushButton(self.centralwidget)
        self.manButton.setEnabled(True)
        self.manButton.setGeometry(QtCore.QRect(330, 60, 61, 41))
        self.manButton.setDefault(True)
        self.manButton.setFlat(False)
        self.manButton.setObjectName("manButton")
        self.delButtin = QtWidgets.QPushButton(self.centralwidget)
        self.delButtin.setGeometry(QtCore.QRect(330, 110, 61, 41))
        self.delButtin.setObjectName("delButtin")
        self.delButtin.setFlat(False)
        self.delButtin.setDefault(True)
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setEnabled(True)
        self.returnButton.setFlat(False)
        self.returnButton.setGeometry(QtCore.QRect(330, 160, 61, 41))
        self.returnButton.setObjectName("returnButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.amsignButton.clicked.connect(self.uptime_slot)
        self.pmsignButton.clicked.connect(self.offtime_slot)
        self.infoButton.clicked.connect(self.today_information_slot)
        self.manButton.clicked.connect(self.new_man_slot)
        self.staffButton.clicked.connect(self.new_staff_slot)
        self.delButtin.clicked.connect(self.del_staff_slot)
        self.setUiHome()

        self.manageButton.clicked.connect(self.setUiManager)  # transformit UI
        self.returnButton.clicked.connect(self.setUiHome)

        self.service=Service()
        self.th = Thread(self)
        self.th.changePixmap.connect(self.video_label.setPixmap)  # signal connect video label
        self.th.managerRec.connect(self.managerFace)  # bind some detection with it's own privilege
        self.th.staffRec.connect(self.staffFace)
        self.th.unknownRec.connect(self.unknownFace)
        self.th.noneRec.connect(self.noneFace)
        self.th.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FaceDetection"))
        self.amsignButton.setText(_translate("MainWindow", "上班打卡"))
        self.infoButton.setText(_translate("MainWindow", "今日信息"))
        self.pmsignButton.setText(_translate("MainWindow", "下班打卡"))
        self.manageButton.setText(_translate("MainWindow", "后台管理"))
        self.staffButton.setText(_translate("MainWindow", "员工录入"))
        self.manButton.setText(_translate("MainWindow", "管员录入"))
        self.delButtin.setText(_translate("MainWindow", "成员删除"))
        self.returnButton.setText(_translate("MainWindow", "主菜单"))

    def setUiManager(self):
        self.infoButton.setVisible(False);
        self.amsignButton.setVisible(False);
        self.pmsignButton.setVisible(False);
        self.manageButton.setVisible(False);
        self.delButtin.setVisible(True);
        self.manButton.setVisible(True);
        self.returnButton.setVisible(True);
        self.staffButton.setVisible(True);

    def setUiHome(self):
        self.infoButton.setVisible(True);
        self.amsignButton.setVisible(True);
        self.pmsignButton.setVisible(True);
        self.manageButton.setVisible(True);
        self.delButtin.setVisible(False);
        self.manButton.setVisible(False);
        self.returnButton.setVisible(False);
        self.staffButton.setVisible(False);

    def uptime_slot(self):
        for name in self.th.face_names:
            if name !='unknown':
                if self.service.newinfo(name):
                    msg=name+"上班打卡成功"
                else:
                    msg=name+"上班打卡失败"
                QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                                      "友情提示：",
                                                      msg)
    def offtime_slot(self):
        for name in self.th.face_names:
            if name !='unknown':
                if self.service.updateinfo(name):
                    msg=name+"下班打卡成功"
                else:
                    msg=name+"下班打卡失败"
                QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                                      "友情提示：",
                                                      msg)
    def today_information_slot(self):
        self.form=QtWidgets.QDialog()
        self.form.ui=Ui_Form()
        self.form.ui.setupUi(self.form,self.service.listinfo())
        self.form.exec_()


    def new_staff_slot(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_StaffInput()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.buttonBox.accepted.connect(self.newStaff)
        self.dialog.exec_()
        # self.dialog.show()

    def new_man_slot(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_StaffInput()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.buttonBox.accepted.connect(self.newMan)
        self.dialog.exec_()
        # self.dialog.show()

    def del_staff_slot(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_DeleDialog()
        self.dialog.ui.setupUi(self.dialog, self.th.names)
        self.dialog.ui.buttonBox.accepted.connect(self.delStaffs)
        self.dialog.exec_()

    def newStaff(self):
        if self.th.face_encodings.__len__() != 1:  # not one face in Camera
            QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                              "友情提示：",
                                              "没有人在摄像头前")
            return
        new_info = Info()
        new_info.name = self.dialog.ui.textEdit.toPlainText()  # remember use oPlainText()
        new_info.encoding = self.th.face_encodings[0]
        if new_info.name in self.th.names or not self.unknownflag:
            QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                              "友情提示：",
                                              "此人数据已存在系统")
            return
        new_info.admin = 0
        self.th.infos.append(new_info)
        self.th.savedata()
        self.th.loaddata()
        QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                          "友情提示：",
                                          "人脸数据存储成功！")

    def newMan(self):
        if self.th.face_encodings.__len__() != 1:  # not one face in Camera
            if self.th.face_encodings.__len__() != 1:  # not one face in Camera
                QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                                  "友情提示：",
                                                  "没有人在摄像头前")
                return
        new_info = Info()
        # new_info.name = self.staffDialog.textEdit
        new_info.name = self.dialog.ui.textEdit.toPlainText()
        new_info.encoding = self.th.face_encodings[0]
        if new_info.name in self.th.names or not self.unknownflag:
            QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                              "友情提示：",
                                              "此人数据已存在系统")
            return
        new_info.admin = 1
        self.th.infos.append(new_info)
        self.th.savedata()
        self.th.loaddata()
        QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                          "友情提示：",
                                          "人脸数据存储成功！")

    def delStaffs(self):
        for i in range(0, 6):
            if self.dialog.ui.checkBoxs[i].isChecked():
                del self.th.infos[i + self.dialog.ui.x - 6]
                self.th.savedata()
                self.th.loaddata()
                QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                                  "友情提示：",
                                                  "删除成功")
                return

    # actions for different roles
    def staffFace(self):  # set Ui when face is detected and the face belong one of System's members
        self.amsignButton.setEnabled(True)
        self.pmsignButton.setEnabled(True)
        self.staffButton.setEnabled(False)
        self.manButton.setEnabled(False)
        self.manageButton.setEnabled(False)
        self.infoButton.setEnabled(True)
        self.unknownflag = False

    def unknownFace(self):  # set Ui when face is not the System's member
        self.manageButton.setEnabled(False)
        self.amsignButton.setEnabled(False)
        self.pmsignButton.setEnabled(False)
        self.staffButton.setEnabled(False)
        self.manButton.setEnabled(False)
        self.infoButton.setEnabled(True)
        self.unknownflag = True

    def managerFace(self):  # set Ui by whether face is detected and the face belong one of System's members
        self.manageButton.setEnabled(True)
        self.amsignButton.setEnabled(True)
        self.pmsignButton.setEnabled(True)
        self.staffButton.setEnabled(True)
        self.manButton.setEnabled(True)
        self.infoButton.setEnabled(True)
        self.unknownflag = False

    def noneFace(self):  # no man in camera,all buttons are supposed to disable
        self.manageButton.setEnabled(False)
        self.amsignButton.setEnabled(False)
        self.pmsignButton.setEnabled(False)
        self.staffButton.setEnabled(False)
        self.manButton.setEnabled(False)
        self.infoButton.setEnabled(False)
        self.unknownflag = False



