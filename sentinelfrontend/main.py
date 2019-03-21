# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basescreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json, urllib.request
import requests
import VTscan
import pygal
import pycountry

class Ui_BaseScreen(object):
    def setupUi(self, BaseScreen):
        BaseScreen.setObjectName("BaseScreen")
        self.URL = "localhost"
        self.output = requests.post('http://'+self.URL+':5000/getProcesses').json()
        self.data=requests.post("http://localhost:5000/getConnectedCountries").json()
        self.filters = {
            "connectionType": ["tcp","udp"],
            "location": [],
            "users": []
        }


#####################################################################

        self.systemHealth=3
        self.redLower=2
        self.yellowLower=1
        
        # print(requests.post('http://localhost:5000/getSystemUsage'))
        self.systemUsage = requests.post('http://localhost:5000/getSystemUsage').json()
        BaseScreen.resize(1290, 775)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BaseScreen.sizePolicy().hasHeightForWidth())
        BaseScreen.setSizePolicy(sizePolicy)
        BaseScreen.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.centralWidget = QtWidgets.QWidget(BaseScreen)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 311, 711))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(134, 139, 142);")
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 311, 3))
        self.frame_2.setStyleSheet("border: 0.5px solid white;\n"
                                   "background-color: rgb(238, 238, 236);\n"
                                   "border-style: inset;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 311, 3))
        self.frame_4.setStyleSheet("border: 0.5px solid white;\n"
                                   "background-color: rgb(238, 238, 236);\n"
                                   "border-style: inset;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("usernew.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 0, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(238, 238, 236);\n"
                                   "font-weight: 700;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 30, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(238, 238, 236);\n"
                                   "font-weight: 700;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 241, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(238, 238, 236);\n"
                                   "font-weight: 700;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(238, 238, 236);\n"
                                   "font-weight: 700;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 150, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(238, 238, 236);\n"
                                   "font-weight: 700;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(238, 238, 236);\n"
                                   "font-weight: 700;")
        self.label_9.setObjectName("label_9")
        self.processStartTime = QtWidgets.QLabel(self.frame)
        self.processStartTime.setGeometry(QtCore.QRect(120, 180, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.processStartTime.setFont(font)
        self.processStartTime.setStyleSheet("color: rgb(238, 238, 236);\n"
                                            "font-weight: 700;")
        self.processStartTime.setObjectName("processStartTime")
        self.processType = QtWidgets.QLabel(self.frame)
        self.processType.setGeometry(QtCore.QRect(120, 150, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.processType.setFont(font)
        self.processType.setStyleSheet("color: rgb(238, 238, 236);\n"
                                       "font-weight: 700;")
        self.processType.setObjectName("processType")
        self.processName = QtWidgets.QLabel(self.frame)
        self.processName.setGeometry(QtCore.QRect(120, 120, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.processName.setFont(font)
        self.processName.setStyleSheet("color: rgb(238, 238, 236);\n"
                                       "font-weight: 700;")
        self.processName.setObjectName("processName")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(10, 220, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(10, 260, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(10, 290, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(10, 320, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(10, 560, 241, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_17.setObjectName("label_17")
        self.processCPU = QtWidgets.QLabel(self.frame)
        self.processCPU.setGeometry(QtCore.QRect(130, 660, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.processCPU.setFont(font)
        self.processCPU.setStyleSheet("color: rgb(238, 238, 236);\n"
                                      "font-weight: 700;")
        self.processCPU.setObjectName("processCPU")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(30, 600, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_19.setObjectName("label_19")
        self.processDisk = QtWidgets.QLabel(self.frame)
        self.processDisk.setGeometry(QtCore.QRect(130, 600, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.processDisk.setFont(font)
        self.processDisk.setStyleSheet("color: rgb(238, 238, 236);\n"
                                       "font-weight: 700;")
        self.processDisk.setObjectName("processDisk")

        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(30, 660, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(30, 630, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_23.setObjectName("label_23")
        self.processNetwork = QtWidgets.QLabel(self.frame)
        self.processNetwork.setGeometry(QtCore.QRect(130, 630, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.processNetwork.setFont(font)
        self.processNetwork.setStyleSheet("color: rgb(238, 238, 236);\n"
                                          "font-weight: 700;")
        self.processNetwork.setObjectName("processNetwork")
        self.processCPUVal = "8"
        self.processDiskVal = "5"
        self.processNetworkVal = "2MBps"
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 420, 271, 41))
        self.pushButton.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                                      "color: rgb(89, 89, 89);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 470, 271, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                                        "color: rgb(89, 89, 89);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 520, 271, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                                        "color: rgb(89, 89, 89);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 370, 271, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                                        "color: rgb(89, 89, 89);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(450, 90, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_22.setObjectName("label_22")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(450, 30, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(350, 30, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(350, 90, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(450, 60, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(350, 60, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(238, 238, 236);\n"
                                    "font-weight: 700;")
        self.label_29.setObjectName("label_29")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1029, 0, 261, 711))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(253, 253, 253);")
        self.groupBox_2.setObjectName("groupBox_2")
        # self.pushButton_BarGraph = QtWidgets.QPushButton(self.groupBox_2)
        # self.pushButton_BarGraph.setGeometry(QtCore.QRect(0, 570, 261, 41))
        # self.pushButton_BarGraph.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        #                                 "background-color: rgb(243, 243, 243);")
        # self.pushButton_BarGraph.setObjectName("pushButton_BarGraph")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 630, 261, 41))
        self.pushButton_9.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                        "background-color: rgb(243, 243, 243);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 221, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setObjectName("label_39")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_39)
        # self.tcpCheck = QtWidgets.QCheckBox(self.formLayoutWidget)
        # self.tcpCheck.setObjectName("tcpCheck")
        # self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.tcpCheck)
        # self.udpCheck = QtWidgets.QCheckBox(self.formLayoutWidget)
        # self.udpCheck.setObjectName("udpCheck")
        # self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.udpCheck)
        self.label_40 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("")
        self.label_40.setObjectName("label_40")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_40)
        # self.checkBox_3 = QtWidgets.QCheckBox(self.formLayoutWidget)
        # self.checkBox_3.setObjectName("checkBox_3")
        # self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        # self.checkBox_4 = QtWidgets.QCheckBox(self.formLayoutWidget)
        # self.checkBox_4.setObjectName("checkBox_4")
        # self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_4)
        self.label_43 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("")
        self.label_43.setObjectName("label_43")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.listWidgetUser = QtWidgets.QListWidget(self.formLayoutWidget)
        self.listWidgetUser.setObjectName("listWidgetUser")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.listWidgetUser)
        self.listWidgetCountry = QtWidgets.QListWidget(self.formLayoutWidget)
        self.listWidgetCountry.setObjectName("listWidget")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.listWidgetCountry)
        # self.checkBox_15 = QtWidgets.QCheckBox(self.formLayoutWidget)
        # self.checkBox_15.setObjectName("checkBox_15")
        # self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.checkBox_15)
        # self.checkBox_14 = QtWidgets.QCheckBox(self.formLayoutWidget)
        # self.checkBox_14.setObjectName("checkBox_14")
        # self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.checkBox_14)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 370, 221, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.plainTextEdit)
        self.filterButton = QtWidgets.QPushButton(self.groupBox_2)
        self.filterButton.setGeometry(QtCore.QRect(20, 430, 221, 41))
        self.filterButton.setStyleSheet("background-color: rgb(136, 138, 133);\n"
                                        "background-color: rgb(211, 215, 207);\n"
                                        "")
        self.filterButton.setObjectName("filterButton")
        self.filterButton.clicked.connect(self.updateFilter)

        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.filterButton)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(310, 0, 721, 101))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.verticalLayoutWidget_3.setFont(font)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color: rgb(237, 237, 237);")
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 61))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sentinel.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 591, 41))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 130, 721, 371))
        self.tableWidget.setMaximumSize(QtCore.QSize(721, 16777215))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tableWidget.clicked.connect(self.on_click)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        self.getfilters()
        self.filterCurrent = {
            "connectionType": ["tcp","udp"],
            "location": [],
            "users": []
        }
        self.getfilterCurrent()
        # self.filterCurrent=self.filters.copy()
        self.retranslateTable(BaseScreen)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)


        self.frame_41 = QtWidgets.QFrame(self.centralWidget)
        self.frame_41.setGeometry(QtCore.QRect(310, 500, 721, 211))
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.label_30 = QtWidgets.QLabel(self.frame_41)
        self.label_30.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(239, 41, 41);\n"
                                    "font-weight:700;")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_41)
        self.label_31.setGeometry(QtCore.QRect(10, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(68, 68, 68);")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_41)
        self.label_32.setGeometry(QtCore.QRect(10, 70, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(68, 68, 68);")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_41)
        self.label_33.setGeometry(QtCore.QRect(10, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(68, 68, 68);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_41)
        self.label_34.setGeometry(QtCore.QRect(10, 130, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(68, 68, 68);")
        self.label_34.setObjectName("label_34")
        self.totalProcesses = QtWidgets.QLabel(self.frame_41)
        self.totalProcesses.setGeometry(QtCore.QRect(220, 40, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalProcesses.setFont(font)
        self.totalProcesses.setStyleSheet("color: rgb(68, 68, 68);")
        self.totalProcesses.setObjectName("totalProcesses")
        self.totalDiskUsage = QtWidgets.QLabel(self.frame_41)
        self.totalDiskUsage.setGeometry(QtCore.QRect(220, 70, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalDiskUsage.setFont(font)
        self.totalDiskUsage.setStyleSheet("color: rgb(68, 68, 68);")
        self.totalDiskUsage.setObjectName("totalDiskUsage")
        self.totalCpuUsage = QtWidgets.QLabel(self.frame_41)
        self.totalCpuUsage.setGeometry(QtCore.QRect(220, 100, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalCpuUsage.setFont(font)
        self.totalCpuUsage.setStyleSheet("color: rgb(68, 68, 68);")
        self.totalCpuUsage.setObjectName("totalRemoteConnections")
        self.totalNetworkUsage = QtWidgets.QLabel(self.frame_41)
        self.totalNetworkUsage.setGeometry(QtCore.QRect(220, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalNetworkUsage.setFont(font)
        self.totalNetworkUsage.setStyleSheet("color: rgb(68, 68, 68);")
        self.totalNetworkUsage.setObjectName("totalNetworkUsage")
        self.line = QtWidgets.QFrame(self.frame_41)
        self.line.setGeometry(QtCore.QRect(370, 10, 20, 191))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_41)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 160, 271, 41))
        self.pushButton_8.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                        "color: rgb(238, 238, 236);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.chkRootKit = QtWidgets.QPushButton(self.frame_41)
        self.chkRootKit.setGeometry(QtCore.QRect(420, 10, 271, 41))
        self.chkRootKit.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                          "color: rgb(238, 238, 236);")
        self.chkRootKit.setObjectName("chkRootKitButton")
        self.chkRootKit.clicked.connect(self.runChk)
        self.advancedScanButton = QtWidgets.QPushButton(self.frame_41)
        self.advancedScanButton.setGeometry(QtCore.QRect(420, 110, 271, 41))
        self.advancedScanButton.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                              "color: rgb(238, 238, 236);")
        self.advancedScanButton.setObjectName("advancedScanButton")
        self.advancedScanButton.clicked.connect(self.getAdvancedScanReports)
        self.blockedIPButton = QtWidgets.QPushButton(self.frame_41)
        self.blockedIPButton.setGeometry(QtCore.QRect(420, 60, 271, 41))
        self.blockedIPButton.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                           "color: rgb(238, 238, 236);")
        self.blockedIPButton.setObjectName("blockedIPButton")
        self.blockedIPButton.clicked.connect(self.blockedIPList)
        BaseScreen.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(BaseScreen)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1290, 22))
        self.menuBar.setObjectName("menuBar")
        BaseScreen.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(BaseScreen)
        self.mainToolBar.setObjectName("mainToolBar")
        BaseScreen.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(BaseScreen)
        self.statusBar.setObjectName("statusBar")
        BaseScreen.setStatusBar(self.statusBar)
        self.selectedRow = 0
        self.processUsage ={}
        self.runningAsUser = "-"
        self.retranslateUi(BaseScreen)
        QtCore.QMetaObject.connectSlotsByName(BaseScreen)

    def retranslateUi(self, BaseScreen):
        _translate = QtCore.QCoreApplication.translate
        BaseScreen.setWindowTitle(_translate("BaseScreen", "BaseScreen"))
        self.label_4.setText(_translate("BaseScreen", "Devdas"))
        self.label_5.setText(_translate("BaseScreen", "SYS3981 India Interlink "))
        self.label_6.setText(_translate("BaseScreen", "Selected Process Details"))
        self.label_7.setText(_translate("BaseScreen", "Name:"))
        self.label_8.setText(_translate("BaseScreen", "Type:"))
        self.label_9.setText(_translate("BaseScreen", "Start Time:"))
        self.processStartTime.setText(_translate("BaseScreen", "Wed 9:30 AM"))
        self.processType.setText(_translate("BaseScreen", "linux executable"))
        self.processName.setText(_translate("BaseScreen", "Kakarot.py"))
        self.label_13.setText(_translate("BaseScreen", "Flags"))
        self.label_14.setText(_translate("BaseScreen", "Idle/Waiting"))
        self.label_15.setText(_translate("BaseScreen", "Type of Process"))
        self.label_16.setText(_translate("BaseScreen", "running as : "+ self.runningAsUser))
        self.label_17.setText(_translate("BaseScreen", "Usage"))
        self.processCPU.setText(_translate("BaseScreen", self.processCPUVal))
        self.label_19.setText(_translate("BaseScreen", "Disk:"))
        self.processDisk.setText(_translate("BaseScreen", self.processDiskVal))
        self.label_21.setText(_translate("BaseScreen", "CPU:"))
        self.label_23.setText(_translate("BaseScreen", "Network:"))
        self.processNetwork.setText(_translate("BaseScreen", self.processNetworkVal))
        self.pushButton.setText(_translate("BaseScreen", "IP Scan"))
        self.pushButton_2.setText(_translate("BaseScreen", "Kill Process"))
        self.pushButton_2.clicked.connect(self.killProcess)
        self.pushButton_3.setText(_translate("BaseScreen", "Blacklist IP"))
        self.pushButton_3.clicked.connect(self.blockIP)
        self.pushButton_4.setText(_translate("BaseScreen", "Quick Scan With Virustotal"))
        self.pushButton_4.clicked.connect(self.quickScanClick)
        self.label_22.setText(_translate("BaseScreen", "Wed 9:30 AM"))
        self.label_25.setText(_translate("BaseScreen", "Kakarot.py"))
        self.label_26.setText(_translate("BaseScreen", "Name:"))
        self.label_27.setText(_translate("BaseScreen", "Start Time:"))
        self.label_28.setText(_translate("BaseScreen", "linux executable"))
        self.label_29.setText(_translate("BaseScreen", "Type:"))
        self.groupBox_2.setTitle(_translate("BaseScreen", "Filter Connections"))
        # self.pushButton_BarGraph.setText(_translate("BaseScreen", "Pictorial Representation"))
        # self.pushButton_BarGraph.clicked.connect(self.connectionBar)
        self.pushButton_9.setText(_translate("BaseScreen", "Global Map"))
        self.pushButton_9.clicked.connect(self.connectionGraph)
        self.label00 = QtWidgets.QLabel(self.frame_3)
        self.label00.setGeometry(QtCore.QRect(10, 10, 91, 61))
        self.label0 = QtWidgets.QLabel(self.groupBox_2)
        self.label0.setGeometry(QtCore.QRect(28,65,71,71))
        
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setItalic(True)
        self.label00.setFont(font)
        self.label00.setText("")
        self.label00.setPixmap(QtGui.QPixmap("sentinel.png"))
        self.label00.setScaledContents(True)
        self.label00.setObjectName("label00")
        self.label0.setFont(font)
        self.label0.setText("")
        self.label0.setPixmap(QtGui.QPixmap("index.jpeg"))
        self.label0.setScaledContents(True)
        self.label0.setObjectName("label0")


        # self.label_39.setText(_translate("BaseScreen", ("Parameter\n"+(self.systemHealth)))
        self.label_39.setText ("            Score\n             0.8")
        # self.tcpCheck.setText(_translate("BaseScreen", "TCP"))
        # self.udpCheck.setText(_translate("BaseScreen", "UDP"))
        self.label_40.setText(_translate("BaseScreen", "User"))
        # self.checkBox_3.setText(_translate("BaseScreen", "Admin"))
        # self.checkBox_4.setText(_translate("BaseScreen", "Devansh"))
        self.label_43.setText(_translate("BaseScreen", "Country"))
        # self.checkBox_15.setText(_translate("BaseScreen", "India"))
        # self.checkBox_14.setText(_translate("BaseScreen", "Newzealand"))
        self.plainTextEdit.setPlainText(_translate("BaseScreen", "Search For Text"))
        self.filterButton.setText(_translate("BaseScreen", "Filter Remote Connections"))
        self.label_2.setText(_translate("BaseScreen", "SENTINEL - ADVANCED PROCESS LOOKUP AND ROOTKIT DETECTION"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BaseScreen", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BaseScreen", "USER"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BaseScreen", "Process Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BaseScreen", "Safe Score"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("BaseScreen", "Local Port"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BaseScreen", "Remote Address"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("BaseScreen", "Remote Port"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("BaseScreen", "Remote Location"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("BaseScreen", "Company"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


        self.label_30.setText(_translate("BaseScreen", "Overview"))
        self.label_31.setText(_translate("BaseScreen", "Number of Processes:"))
        self.label_32.setText(_translate("BaseScreen", "Total CPU Usage:"))
        self.label_33.setText(_translate("BaseScreen", "Total Disk Usage:"))
        self.label_34.setText(_translate("BaseScreen", "Number of Remote Connections:"))
        #self.label_34.setText(_translate("BaseScreen", "Total Network Usage:"))
        self.totalProcesses.setText(_translate("BaseScreen", self.systemUsage['num_process']))
        self.totalCpuUsage.setText(_translate("BaseScreen", self.systemUsage['cpu_usage']))
        self.totalDiskUsage.setText(_translate("BaseScreen", self.systemUsage['memory_usage']))
        self.totalNetworkUsage.setText(_translate("BaseScreen", "12 MiB/s"))
        self.pushButton_8.setText(_translate("BaseScreen", "Refresh"))
        self.pushButton_8.clicked.connect(self.reset)
        self.chkRootKit.setText(_translate("BaseScreen", "Run Chkrootkit"))
        self.advancedScanButton.setText(_translate("BaseScreen", "Get Advance Scan Reports"))
        self.blockedIPButton.setText(_translate("BaseScreen", "Manage Blocked IPs"))

    def getfilterCurrent(self):
        _translate = QtCore.QCoreApplication.translate
        outputCountry = set()
        for x in self.output['processes']:
            outputCountry.add(x["country"])

        outputCountry = sorted(outputCountry, key=str.lower)
        
        outputUser = set()
        for x in self.output['processes']:
            outputUser.add(x["User"])
        outputUser = sorted(outputUser, key=str.lower)
        
        # outputConnectionType = set()
        # for x in self.output['processes']:
        #     outputConnectionType.add(x["cType"])
        # outputConnectionType = sorted(outputConnectionType, key=str.lower)
        # for x in outputConnectionType:
        #     item = QtWidgets.QListWidgetItem()
        #     item.setText(_translate("BaseScreen", str(x)))
        #     item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        #     item.setCheckState(QtCore.Qt.Checked)
        #     self.listWidgetConnection.addItem(item)
        
        for i in outputUser:
            self.filterCurrent["users"].append(i)
        for i in outputCountry:
            self.filterCurrent["location"].append(i)
        # self.filters["connectionType"].append(con for con in outputConnectionType)

    def connectionBar(self):
        pass

    def connectionGraph(self):
        print(self.data)
        self.worldmap_chart = pygal.maps.world.World()
        self.worldmap_chart.title = 'Countries connected'
        for key in self.data["results"]:
            country = key
            occurence = self.data["results"][str(key)]
            if pycountry.countries.get(name=country) == None:
                continue
            self.worldmap_chart.add('{} {}'.format(country, occurence), [ str(pycountry.countries.get(name=country).alpha_2.lower()) ])
        self.worldmap_chart.render_in_browser()


    def getfilters(self):
        _translate = QtCore.QCoreApplication.translate
        outputCountry = set()
        for x in self.output['processes']:
            outputCountry.add(x["country"])

        outputCountry = sorted(outputCountry, key=str.lower)
        for x in outputCountry:
            item = QtWidgets.QListWidgetItem()
            item.setText(_translate("BaseScreen", str(x)))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            # item.stateChanged.connect(self.updateFilter(item))
            self.listWidgetCountry.addItem(item)

        outputUser = set()
        for x in self.output['processes']:
            outputUser.add(x["User"])
        outputUser = sorted(outputUser, key=str.lower)
        for x in outputUser:
            item = QtWidgets.QListWidgetItem()
            item.setText(_translate("BaseScreen", str(x)))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.listWidgetUser.addItem(item)
        
        # outputConnectionType = set()
        # for x in self.output['processes']:
        #     outputConnectionType.add(x["cType"])
        # outputConnectionType = sorted(outputConnectionType, key=str.lower)
        # for x in outputConnectionType:
        #     item = QtWidgets.QListWidgetItem()
        #     item.setText(_translate("BaseScreen", str(x)))
        #     item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        #     item.setCheckState(QtCore.Qt.Checked)
        #     self.listWidgetConnection.addItem(item)
        
        for i in outputUser:
            self.filters["users"].append(i)
        for i in outputCountry:
            self.filters["location"].append(i)
        # self.filters["connectionType"].append(con for con in outputConnectionType)



    def updateFilter(self):

            print("***************************************")
            outputLocation=set()
            # print(outputLocation)
            # print(k)
            for k in range(len(self.filters["location"])):
                print(self.filters["location"])
                # print(k)
                if self.listWidgetCountry.item(k).checkState()==2 :
                    # print(self.filters["location"][k])
                    outputLocation.add(self.filters["location"][k])
            # print(outputLocation)
            outputLocation = sorted(outputLocation, key=str.lower)

            outputUser=set()
            # outputUser.clear()
            for k in range(self.listWidgetUser.count()):
                if self.listWidgetUser.item(k).checkState()==2 :
                    outputUser.add(self.filters["users"][k])
            outputUser = sorted(outputUser, key=str.lower)

            
            self.filterCurrent["users"].clear()
            self.filterCurrent["location"].clear()
            for i in outputUser:
                self.filterCurrent["users"].append(i)
            for i in outputLocation:
                self.filterCurrent["location"].append(i)

            print(self.filterCurrent)
        

            self.filterResult(BaseScreen)
            self.retranslateTable(BaseScreen)

    
    def scanIP(self):
        dIP = str(self.output["processes"][self.selectedRow]["remoteAddr"][0])
        out = requests.post('http://' + self.URL + ':5000/scanIP', {'IP': dIP}).json()['results']
        avP = int(out['average_percent'])
        n = int(out['negatives'])
        p = int(out['positives'])
        self.str = ""
        if n>0:
            print("Safe Ip")
            self.str = "Safe Ip"
        elif p>0:
            print("Unsafe Ip")
            self.str = "Unsafe Ip"
        else:
            print("Safe Ip")
            self.str = "Safe Ip"

        self.infoMessage(str)


    def retranslateTable(self, BaseScreen):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setRowCount(len(self.output['processes']))
        

        # outputCountry = set()
        # for x in self.output['processes']:
        #     outputCountry.add(x["country"])
        # outputCountry = sorted(outputCountry, key=str.lower)
        # for x in outputCountry:
        #     item = QtWidgets.QListWidgetItem()
        #     item.setText(_translate("BaseScreen", str(x)))
        #     item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        #     item.setCheckState(QtCore.Qt.Checked)
        #     self.listWidgetCountry.addItem(item)

        # outputUser = set()
        # for x in self.output['processes']:
        #     outputUser.add(x["User"])
        # outputUser = sorted(outputUser, key=str.lower)
        # for x in outputUser:
        #     item = QtWidgets.QListWidgetItem()
        #     item.setText(_translate("BaseScreen", str(x)))
        #     item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        #     item.setCheckState(QtCore.Qt.Checked)
        #     self.listWidgetUser.addItem(item)

        for i in range(min(len(self.output['processes']), 22)):
            brush = QtGui.QBrush(QtGui.QColor(0,0,0))
            # if(self.output['processes'][i]["health"]>5){
            #     brush = QtGui.QBrush(QtGui.QColor(232, 0, 0))
            # }elif (self.output['processes'][i]["health"]>3){
            #     brush = QtGui.QBrush(QtGui.QColor(135,206,250))
            # }
            item = QtWidgets.QTableWidgetItem()
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            item.setForeground(brush)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 3, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 4, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 5, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 6, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 7, item)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush)
            item.setForeground(brush)
            self.tableWidget.setItem(i, 8, item)

            item = self.tableWidget.item(i, 0)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["PID"]) if len(
                self.output["processes"][i]["PID"]) else "Not Found"))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["User"]) if len(
                self.output["processes"][i]["User"]) else "Not Found"))
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["Pname"]) if len(
                self.output["processes"][i]["Pname"]) else "Not Found"))
            item = self.tableWidget.item(i, 3)
            item.setText(_translate("BaseScreen", str(0)))
            item = self.tableWidget.item(i, 4)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["localAddr"][1]) if len(
                self.output["processes"][i]["localAddr"]) else "Not Found"))
            item = self.tableWidget.item(i, 5)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["remoteAddr"][0]) if len(
                self.output["processes"][i]["remoteAddr"]) else "Not Found"))
            item = self.tableWidget.item(i, 6)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["remoteAddr"][1]) if len(
                self.output["processes"][i]["remoteAddr"]) else "Not Found"))
            item = self.tableWidget.item(i, 7)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["country"]) if len(
                self.output["processes"][i]["country"]) else "Not Found"))
            item = self.tableWidget.item(i, 8)
            item.setText(_translate("BaseScreen", str(self.output["processes"][i]["company"]) if len(
                self.output["processes"][i]["company"]) else "Not Found"))


    def filterResult(self,BaseScreen):
        print("---------------------------------------")
        filteredlocation=filter(self.fun,self.output["processes"])
         
        lst=list(filteredlocation)
        dic={'processes':[]}
        for i in range(len(lst)):
            dic["processes"].append(lst[i])
            
        print("-------------------------------------")
        print(dic)
                    
        self.output=dic
        self.retranslateTable(BaseScreen)



    def fun(self,variable):
        if variable["country"] in self.filterCurrent["location"] :
            if variable["cType"] in self.filterCurrent["connectionType"]:
                if variable["User"] in self.filterCurrent["users"]:
                    return True 
        else :
            return False


    def on_click(self):
        print("\n")

        self.selectedRow = self.tableWidget.selectedItems()[0].row()
        pid = str(self.output['processes'][self.selectedRow]["PID"])
        # self.processUsage = requests.post("http://"+self.URL+":5000/getProcessUsage",{'PID':(int)(pid)}).json()
        self.processCPUVal = "8"
        self.processDiskVal = "5"
        self.runningAsUser = ""
        self.label_16.setText("running as : " + self.runningAsUser)
        if self.runningAsUser == "root":
            self.label_15.setText("System Process")
        else:
            self.label_15.setText("User Level Process")

    def quickScanClick(self):
        self.clickedProcess = str(self.output['processes'][self.selectedRow]["PID"])
        import os
        print('python ' + 'VTscan.py' + ' ' + (self.clickedProcess) + ' & disown')
        os.system('python ' + 'VTscan.py' + ' ' + (self.clickedProcess) + ' & disown')

    def blockIP(self):
        dIP = str(self.output["processes"][self.selectedRow]["remoteAddr"][0])
        dPort = str(self.output["processes"][self.selectedRow]["remoteAddr"][1])
        response = requests.post('http://' + self.URL + ':5000/blockIP', {'IP': dIP, 'port': dPort})
        print(response)
        self.reset()
        # message = QMessageBox.question(self, "Your Concern", "Do you want to Block Ip "+dIP+" ?",
        #                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # if message == QMessageBox.Yes:
        #     response = requests.post('http://' + self.URL + ':5000/blockIP', {'IP': dIP, 'port': dPort})
        #     QMessageBox.about(self, "Confirmed", "IP BLocked")
        #     print(response)
        # else:
        #     print("No no")


        # self.output = requests.post('http://' + URL + '/lookupProcess', {'PID': self.data}).json()

    def QuestionMessage(self, msg):

        def do():
            message = QMessageBox.question(self, "Your Concern", msg + "?",
                                           QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            if message == QMessageBox.Yes:
                print("Blocked/Delete")
            else:
                print("No no")

        return do

    def infoMessage(self, msg):

        def do():
            QMessageBox.about(self, "Confirmed", msg)
        return do

    def killProcess(self):
        pid = str(self.output['processes'][self.selectedRow]["PID"])
        # message = QMessageBox.question(self, "Your Concern", "Do you want to kill Process with process Id = "+pid + " ?",
        #                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        #
        # if message == QMessageBox.Yes:
        print(pid)
        print("Blocked/Delete")
        requests.post('http://' + self.URL + ':5000/killProcess', {'PID': pid})
        self.reset()
            # QMessageBox.about(self, "Confirmed", "Process Kiled")

        # else:
        #     print("No no")

    def getAdvancedScanReports(self):
        import os
        os.system('python ' + 'reports.py' + ' & disown')

    # def getProcessUsage(self):
    #     pid = str(self.output['processes'][self.selectedRow - 1]["PID"])

    def reset(self):
        self.output = requests.post('http://' + self.URL + ':5000/getProcesses').json()
        self.retranslateTable(BaseScreen)

    def blockedIPList(self):
        import os
        os.system('python ' + 'blockIPlist.py' + ' & disown')

    # def scanIP(self):
    #     dIP = str(self.output["processes"][self.selectedRow]["remoteAddr"][0])
    #     requests.post('http://' + self.URL + ':5000/killProcess', {'IP': dIP}).jsonify()


    def runChk(self):
        str = requests.post("http://"+self.URL+":5000/chkrScan")
        import os
        os.system('python ' + 'chkScan.py' + ' & disown')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaseScreen = QtWidgets.QMainWindow()
    ui = Ui_BaseScreen()
    ui.setupUi(BaseScreen)
    BaseScreen.show()
    sys.exit(app.exec_())