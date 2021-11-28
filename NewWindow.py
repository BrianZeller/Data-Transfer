# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate, QDateTime, QTime

import contact_updated


class Ui_MainWindow(object):
    filePath = ""
    total = 0
    startDate = ""
    endDate = ""
    default = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 290, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 290, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 290, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(32)

        # path label
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(100, 230, 500, 51))
        self.label_path.setObjectName("label_path")


        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(160, 117, 450, 22))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(160, 160, 360, 61))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget1)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        # toDate:
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(QDateTime.currentDateTime().addDays(-365))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 2, 1, 1)


        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(QDateTime.currentDateTime())
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        self.gridLayout.addWidget(self.dateTimeEdit_2, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        # transfer button click event
        self.pushButton.clicked.connect(self.showDialog)
        self.pushButton_2.clicked.connect(self.openFileNameDialog)
        self.pushButton_3.clicked.connect(MainWindow.close)

        # radiobuttons
        self.radioButton.clicked.connect(self.check1)
        self.radioButton_2.clicked.connect(self.check2)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        # read date from txt file
        with open("savedData.txt", 'r') as showDate:
            Ui_MainWindow.startDate = showDate.readline()
        print(Ui_MainWindow.startDate)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Transfer"))
        self.pushButton_2.setText(_translate("MainWindow", "Chose CSV File"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Data Transfer"))
        self.radioButton_2.setText(_translate("MainWindow", "From Last Transfer Date: "))
        self.label.setText(_translate("MainWindow", Ui_MainWindow.startDate))
        self.radioButton.setText(_translate("MainWindow", "Set Timeframe"))
        self.label_4.setText(_translate("MainWindow", "From:"))
        self.label_5.setText(_translate("MainWindow", "    To:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

        self.label_path.setText(_translate("MainWindow", "Path:"))


    def showDialog(self):
        if not Ui_MainWindow.default:
            Ui_MainWindow.startDate = self.dateTimeEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            print("from:", Ui_MainWindow.startDate)
            Ui_MainWindow.endDate = self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            print("to: ", Ui_MainWindow.endDate)
        else:
            # Ui_MainWindow.startDate = self.dateTimeEdit.dateTime()
            print("from:", Ui_MainWindow.startDate)
            Ui_MainWindow.endDate = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
            print("to: ", Ui_MainWindow.endDate)

        print("test in showDialog:", Ui_MainWindow.filePath)
        
        num = contact_updated.getNum(Ui_MainWindow.filePath)
        
        progress = QtWidgets.QProgressDialog()
        progress.setWindowTitle("Please wait...")
        progress.setLabelText("Uploading...")
        progress.setCancelButtonText("Cancel")
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, num)

        temptotal = 0
        for i in range(2, num-2):
            progress.setValue(i)
            # message = ForTransferButtonTest.main(Ui_MainWindow.filePath)
            message, temp = contact_updated.main(Ui_MainWindow.filePath, i, Ui_MainWindow.startDate, Ui_MainWindow.endDate)
            temptotal = temptotal + temp
            # for debug only
            # message = "The file inputted into the program can not be found within the path"
            if progress.wasCanceled():
                QtWidgets.QMessageBox.warning(None, "Error", "Canceled", QtWidgets.QMessageBox.Yes)
                break
            self.settotal(temptotal)
        if(message):
            progress.setValue(num)
            QtWidgets.QMessageBox.warning(None, "Done", message, QtWidgets.QMessageBox.Yes)
        else:
            message = str(Ui_MainWindow.total) + " records has been transferred successfully."
            progress.setValue(num)
            self.resettotal()
            QtWidgets.QMessageBox.information(None, "Done", message, QtWidgets.QMessageBox.Yes)
            contact_updated.saveDate(Ui_MainWindow.endDate)

    def settotal(self, num):
        Ui_MainWindow.total = num

    def resettotal(self):
        Ui_MainWindow.total = 0

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "(*.csv);;Python Files (*.py)", options=options)
        if fileName:
            print("get from dialog:", fileName)
            Ui_MainWindow.filePath = fileName
            print("test:", Ui_MainWindow.filePath)

        self.label_path.setText(Ui_MainWindow.filePath)

    def check1(self):
        if self.radioButton.isChecked():
            self.radioButton_2.setChecked(False)
            Ui_MainWindow.default = False

    def check2(self):
        if self.radioButton_2.isChecked():
            self.radioButton.setChecked(False)
            Ui_MainWindow.default = True