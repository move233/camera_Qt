# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 430)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.camera_setting_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.camera_setting_button.setGeometry(QtCore.QRect(0, 10, 93, 28))
        self.camera_setting_button.setObjectName("camera_setting_button")
        self.connect_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(100, 10, 93, 28))
        self.connect_button.setObjectName("connect_button")
        self.capture_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.capture_button.setGeometry(QtCore.QRect(200, 10, 93, 28))
        self.capture_button.setObjectName("capture_button")
        self.recording_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.recording_button.setGeometry(QtCore.QRect(300, 10, 93, 28))
        self.recording_button.setObjectName("recording_button")
        self.stop_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(500, 10, 93, 28))
        self.stop_button.setObjectName("stop_button")

        self.stop_rec_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop_rec_button.setGeometry(QtCore.QRect(400, 10, 93, 28))
        self.stop_rec_button.setObjectName("stop_rec_button")


        self.l1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(0, 50, 200, 150))
        self.l1.setObjectName("l1")
        self.l4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(0, 210, 200, 150))
        self.l4.setObjectName("l4")
        self.l6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.l6.setGeometry(QtCore.QRect(420, 210, 200, 150))
        self.l6.setObjectName("l6")
        self.l2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(210, 50, 200, 150))
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(420, 50, 200, 150))
        self.l3.setObjectName("l3")
        self.l5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(210, 210, 200, 150))
        self.l5.setObjectName("l5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.camera_setting_button.setText(_translate("MainWindow", "相机设置"))
        self.connect_button.setText(_translate("MainWindow", "连接相机"))
        self.capture_button.setText(_translate("MainWindow", "图像采集"))
        self.recording_button.setText(_translate("MainWindow", "开始录制"))
        self.stop_button.setText(_translate("MainWindow", "停止"))
        self.stop_rec_button.setText(_translate("MainWindow", "停止录像"))
        self.l1.setText(_translate("MainWindow", "video1"))
        self.l4.setText(_translate("MainWindow", "video4"))
        self.l6.setText(_translate("MainWindow", "video6"))
        self.l2.setText(_translate("MainWindow", "video2"))
        self.l3.setText(_translate("MainWindow", "video3"))
        self.l5.setText(_translate("MainWindow", "video5"))