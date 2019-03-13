# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reports.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import requests
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
# from quickScanResult import quickScanWindow
URL = "localhost:5000"
class Ui_MainWindow(object):
    def creatingTables(self):
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 621, 271))
        self.tableWidget.setRowCount(len(self.output['files']))
        self.tableWidget.setColumnCount(4)
        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setHorizontalHeaderLabels(["File Path", "File Hash", "Scan Time", "User Name"])
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        count = 0
        for item in self.output['files']:
            print(item["file"])
            self.tableWidget.setItem(count, 0, QTableWidgetItem(item["file"]))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(item["hash"]))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(item["time"]))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(item["user"]))
            count = count + 1

        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        # self.tableWidget.clicked.connect(self.on_click)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.output = requests.post('http://%s/getScheduledFiles' % URL).json()
        # print(self.output)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.tableView = QtWidgets.QTableView(self.centralwidget)
        # self.tableView.setEnabled(True)
        # self.tableView.setGeometry(QtCore.QRect(10, 100, 621, 271))
        # self.tableView.setSizeIncrement(QtCore.QSize(15, 12))
        # self.tableView.setBaseSize(QtCore.QSize(12, 12))
        # self.tableView.setSortingEnabled(False)
        # self.tableView.setObjectName("tableView")
        self.creatingTables()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 390, 201, 41))
        self.pushButton.setObjectName("pushButton")
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 390, 201, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 390, 201, 41))
        self.pushButton_3.setObjectName("pushButton_3")
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

    def on_click(self):
        print("Kshitij CHutiya")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Quick Scan"))
        self.pushButton.clicked.connect(self.quickScanClick)
        self.label_2.setText(_translate("MainWindow", "Scheduled Files"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_2.clicked.connect(self.refresh)
        self.pushButton_3.setText(_translate("MainWindow", "Delete File"))

    def quickScanClick(self):
        row = self.tableWidget.currentRow()
        firstColumnInRow = self.tableWidget.item(row, 0)
        print(firstColumnInRow)
        import os
        os.system('python ' + 'quickScanResult.py' + ' ' + firstColumnInRow.text() + ' & disown')

    def refresh(self):
        self.tableWidget.setRowCount(0)
        self.output = requests.post('http://%s/getScheduledFiles' % URL).json()
        self.tableWidget.setRowCount(len(self.output['files']))
        count = 0
        for item in self.output['files']:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(item["file"]))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(item["hash"]))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(item["time"]))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(item["user"]))
            count = count + 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(['reports.py'])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.setupUi(MainWindow, "./backchodi.file")
    MainWindow.show()
    sys.exit(app.exec_())

