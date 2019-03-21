from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import requests
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.URL = "localhost"
        self.title = "PyQt5 Tables"
        self.top = 100
        self.left = 100
        self.width = 700
        self.height = 600
      #  self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowIcon(QtGui.QIcon("sentinel.png"))
        self.p = 0
        self.n = 0
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.creatingTables()
        VBox = QVBoxLayout()
        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        f1 = QFrame()
        f2 = QFrame()
        self.pos = QLabel("Positives : 1", self)
        self.pos.setStyleSheet("color: rgb(239, 41, 41);\n"
                      "font-weight:700;")
        self.posVal = QLabel(self)
        h1.addWidget(self.pos)
        h1.addWidget(self.posVal)
        f1.setLayout(h1)
        self.neg = QLabel("Negatives : "+str(len(self.results)-1), self)
        self.neg.setStyleSheet("color: rgb(31, 255, 88);\n"
                      "font-weight:700;")
        self.negVal = QLabel(self)
        h2.addWidget(self.neg)
        h2.addWidget(self.negVal)
        f2.setLayout(h2)
        self.reRunButton = QPushButton("Rerun Scan", self)
        self.reRunButton.clicked.connect(self.rerun)
        self.getFilesButton = QPushButton("Get Suspected Files", self)
        self.getFilesButton.clicked.connect(self.suspectedFiles)
        VBox.addWidget(f1)
        VBox.addWidget(f2)
        VBox.addWidget(self.reRunButton)
        VBox.addWidget(self.getFilesButton)
        rightFrame = QFrame()
        rightFrame.setLayout(VBox)
        HBox = QHBoxLayout()
        HBox.addWidget(self.tableWidget)
        HBox.addWidget(rightFrame)


        self.setLayout(HBox)

        self.show()

    def creatingTables(self):
        self.output = requests.post("http://" + self.URL + ":5000/getchkrScanResults").json()
        print(self.output)
        self.results = self.output["results"]
        print(self.results)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.results))
        self.tableWidget.setColumnCount(2)
        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setHorizontalHeaderLabels(["Rootkit Sigature", "Result"])
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        #self.tableWidget.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))

        #self.tableWidget.setStyleSheet()

        count = 0
        for i in self.results :
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(i['infection_name'])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(str(i['scan_result'])))
            if str(i['scan_result'])=='found':
               self.p = self.p+1;
            else:
                self.n = self.n+1;
            count = count+1

        # self.posVal.setText("0")
        # self.negVal.setText(str(len(self.results)))


    def rerun(self):
         self.creatingTables()

    def suspectedFiles(self):

        import os
        os.system('python ' + 'suspectedFiles.py' + ' & disown')

        self.files = requests.post("http://" + self.URL + ":5000/getSuspectFiles").json()['files']

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.files))
        self.tableWidget.setColumnCount(1)
        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setHorizontalHeaderLabels(["Files"])
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


        # self.tableWidget.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))

        # self.tableWidget.setStyleSheet()

        count = 0
        for i in self.files:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(i))
            count = count + 1


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
