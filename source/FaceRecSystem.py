# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceRecSystem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from pick_class import Info  # for pickle get a instance
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets,QtCore,QtGui
import cv2
import face_recognition
import time
import pickle

class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    managerRec = pyqtSignal()
    staffRec=pyqtSignal()
    unknownRec=pyqtSignal()
    noneRec=pyqtSignal()

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.cap = cv2.VideoCapture(0)
        self.fn = 'data.pkl'
        with open(self.fn, 'rb') as f:
            self.infos=pickle.load(f, fix_imports=False)
        self.encodings=[]
        for info in self.infos:
            self.encodings.append(info.encoding)
    def run(self):
        # cap.set(6, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));
        while True:
            ret, frame = self.cap.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            face_locations = face_recognition.face_locations(small_frame)
            if face_locations.__len__() == 0:               #no face was detected
                self.noneRec.emit()
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            face_names = []
            # compare face
            for face_encoding in face_encodings:                    #scan every face in videl
                match = face_recognition.compare_faces(self.encodings, face_encoding)  #compare every face in data
                for i in range(0,self.encodings.__len__()):
                    if match[i]:
                        name = self.infos[i].name
                        if(self.infos[i].admin==1):
                           self.managerRec.emit()
                        else:
                            self.staffRec.emit()
                    else:
                        name = "unknown"
                        self.unknownRec.emit()
                    face_names.append(name)

            # draw rectangle
            for (top, right, bottom, left), name in zip(face_locations, face_names):
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
            time.sleep(0.1)

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
        self.pmsignButton = QtWidgets.QPushButton(self.centralwidget)
        self.pmsignButton.setEnabled(False)
        self.pmsignButton.setFlat(False)
        self.pmsignButton.setGeometry(QtCore.QRect(330, 60, 61, 41))
        self.pmsignButton.setObjectName("pmsignButton")
        self.manageButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageButton.setEnabled(False)
        self.manageButton.setFlat(False)
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
        self.infoButton.clicked.connect(self.today_information_slot)
        self.manButton.clicked.connect(self.new_staff_slot)
        self.staffButton.clicked.connect(self.new_staff_slot)
        self.setUiHome()
        self.manageButton.clicked.connect(self.setUiManager)
        self.returnButton.clicked.connect(self.setUiHome)

        self.th = Thread(self)
        self.th.changePixmap.connect(self.video_label.setPixmap)              #signal connect video label
        self.th.managerRec.connect(self.managerFace)
        self.th.staffRec.connect(self.staffFace)
        self.th.unknownRec.connect(self.unknownFace)
        self.th.noneRec.connect(self.noneFace)
        self.th.start()

        self.staffDialog=Ui_StaffInput(self)
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
    def today_information_slot(self):pass
    def new_staff_slot(self):
        if (self.th.face_encodings.__len__() != 1):  # not one face in Camera
            return
        else:
            self.staffDialog.setupUi(self)
            self.staffDialog.show()

    #actions for different roles
    def staffFace(self):        #set Ui when face is detected and the face belong one of System's members
        self.amsignButton.setEnabled(True)
        self.pmsignButton.setEnabled(True)
        self.staffButton.setEnabled(False)
        self.manButton.setEnabled(False)
        self.manageButton.setEnabled(False)
    def unknownFace(self):       #set Ui when face is not the System's member
        self.staffButton.setEnabled(True)
        self.manButton.setEnabled(True)
    def managerFace(self):    #set Ui by whether face is detected and the face belong one of System's members
        self.manageButton.setEnabled(True)
        self.amsignButton.setEnabled(True)
        self.pmsignButton.setEnabled(True)
        self.staffButton.setEnabled(False)
        self.manButton.setEnabled(False)
    def noneFace(self):               #no man in camera,all buttons are supposed to disable
        self.manageButton.setEnabled(False)
        self.amsignButton.setEnabled(False)
        self.pmsignButton.setEnabled(False)
        self.staffButton.setEnabled(False)
        self.manButton.setEnabled(False)

    def newStaff(self,name):
        new_info=Info()
        new_info.name=self.staffDialog.textEdit
        new_info.encoding=self.th.face_encodings[0]
        new_info.admin=0
        self.th.infos.append(new_info)
        with open(self.th.fn, 'wb') as f:  # open file with write-mode
            pickle.dump(self.th.infos, f, fix_imports=False)  # serialize and save object

class Ui_StaffInput(QtWidgets.QDialog):
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
        self.label.setGeometry(QtCore.QRect(10, 20, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(StaffInputDialog)
        self.buttonBox.accepted.connect(StaffInputDialog.accept)
        self.buttonBox.rejected.connect(StaffInputDialog.reject)
        self.buttonBox.accepted.connect(Ui_MainWindow.newStaff)
        QtCore.QMetaObject.connectSlotsByName(StaffInputDialog)

    def retranslateUi(self, StaffInputDialog):
        _translate = QtCore.QCoreApplication.translate
        StaffInputDialog.setWindowTitle(_translate("StaffInputDialog", "Dialog"))
        self.label.setText(_translate("StaffInputDialog", "Name:"))