# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blockIPlist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from sentinelbackend.routes import *

URL = "localhost:5000"
class BlockIPListWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        # self.output = requests.post('http://%s/getRules' % URL).json()
        self.output = get_rules()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.creatingTables()

        self.unblockIPbutton = QtWidgets.QPushButton(self.centralwidget)
        self.unblockIPbutton.setGeometry(QtCore.QRect(90, 390, 201, 41))
        self.unblockIPbutton.setObjectName("unblockIPbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sentinel.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 291, 61))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.refreshbutton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbutton.setGeometry(QtCore.QRect(350, 390, 201, 41))
        self.refreshbutton.setObjectName("refreshbutton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def creatingTables(self):
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(5, 101, 631, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(len(self.output['rules']))
        self.tableWidget.setColumnCount(2)

        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setHorizontalHeaderLabels(["IP address", "Port blocked"])
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        count = 0
        for item in self.output['rules']:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(item["ip"]))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(item["port"] if item["port"] != "*" else "all"))
            count = count + 1

        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.unblockIPbutton.setText(_translate("MainWindow", "Unblock IP"))
        self.unblockIPbutton.clicked.connect(self.unblockIP)

        self.label_2.setText(_translate("MainWindow", "Blocked IP List"))
        self.refreshbutton.setText(_translate("MainWindow", "Refresh"))
        self.refreshbutton.clicked.connect(self.refresh)

    def unblockIP(self):
        row = self.tableWidget.currentRow()
        firstColumnInRow = self.tableWidget.item(row, 0)
        port = self.tableWidget.item(row,1).text()
        # requests.post('http://%s/unblockIP' % URL, data={"IP" : firstColumnInRow.text(), "port" : port})
        unblock_ip(firstColumnInRow.text(), port)
        self.refresh()

    def refresh(self):
        self.tableWidget.setRowCount(0)
        # self.output = requests.post('http://%s/getRules' % URL).json()
        self.output = get_rules()
        self.tableWidget.setRowCount(len(self.output['rules']))
        count = 0
        for item in self.output['rules']:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(item["ip"]))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(item["port"] if item["port"] != "*" else "all"))
            count = count + 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = BlockIPListWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

