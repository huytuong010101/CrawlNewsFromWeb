# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'News.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from tuoitre import *
import os
from PyQt5 import QtCore, QtGui, QtWidgets
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\venv\\Lib\\site-packages\\PyQt5\\Qt\\Plugins\\platforms"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 154)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: red")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("color: green")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEnabled(False)
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 11)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.loadListNews)
        self.pushButton_2.clicked.connect(self.showNew)

    def loadListNews(self):
        self.comboBox.setEnabled(False)
        self.listNews = getListArticle()
        self.comboBox.clear()
        for item in self.listNews:
            self.comboBox.addItem(item["title"])
        if len(self.listNews) != 0:
            self.comboBox.setEnabled(True)
            self.pushButton_2.setEnabled(True)

    def showNew(self):

        self.Form = QtWidgets.QMainWindow()
        self.Form.resize(600, 600)
        self.textBrowser = QtWidgets.QTextBrowser(self.Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 500, 500))
        self.textBrowser.setObjectName("textBrowser")

        html = getArticle(self.listNews[self.comboBox.currentIndex ()])["body"]
        print(html)
        self.textBrowser.setHtml(str(html))
        self.Form.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Load báo mới hôm nay"))
        self.pushButton_2.setText(_translate("MainWindow", "ĐỌC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
