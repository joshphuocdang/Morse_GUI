# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Morse_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from time import sleep
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi
import RPi.GPIO as GPIO

LED = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)

def dot():
    GPIO.output(LED, GPIO.HIGH)
    sleep(1)
    GPIO.output(LED, GPIO.LOW)
    sleep(1)

def dash():
    GPIO.output(LED, GPIO.HIGH)
    sleep(3)
    GPIO.output(LED, GPIO.LOW)
    sleep(1)      

def short_space():
    sleep(2)

def long_space():
    sleep(6)
    

def blinkSOS(c):
    if c == 'A':
        dot()
        dash()
    if c == 'B':
        dash()
        dot()
        dot()
        dot()
    if c == 'C':
        dash()
        dot()
        dash()
        dot()
    if c == 'D':
        dash()
        dot()
        dot()
    if c == 'E':
        dot()
    if c == 'F':
        dot()
        dot()
        dash()
        dot()
    if c == 'G':
        dash()
        dash()
        dot()
    if c == 'H':
        dot()
        dot()
        dot()
        dot()
    if c == 'I':
        dot()
        dot()
    if c == 'J':
        dot()
        dash()
        dash()
        dash()
    if c == 'K':
        dash()
        dot()
        dash()
    if c == 'L':
        dot()
        dash()
        dot()
        dot()
    if c == 'M':
        dash()
        dash()
    if c == 'N':
        dash()
        dot()
    if c == 'O':
        dash()
        dash()
        dash()
    if c == 'P':
        dot()
        dash()
        dash()
        dot()
    if c == 'Q':
        dash()
        dash()
        dot()
        dash()
    if c == 'R':
        dot()
        dash()
        dot()
    if c == 'S':
        dot()
        dot()
        dot()
    if c == 'U':
        dot()
        dot()
        dash()
    if c == 'V':
        dot()
        dot()
        dot()
        dash()
    if c == 'W':
        dot()
        dash()
        dash()
    if c == 'X':
        dash()
        dot()
        dot()
        dash()
    if c == 'Y':
        dash()
        dot()
        dash()
        dash()
    if c == 'Z':
        dash()
        dash()
        dot()
        dot()
    else: pass


class Ui_MainWindow(object):
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 170, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 83, 271, 61))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 261, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.displaySOS)
        
    def displaySOS(self):
        message = self.textEdit.toPlainText()
        self.textEdit.clear()
        for character in message:
            character = character.upper()
            blinkSOS(character)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send SOS message"))
        self.label.setText(_translate("MainWindow", "Enter Your SOS message!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

