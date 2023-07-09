# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(675, 538)
        Login.setStyleSheet(u"background-color: rgb(20, 43, 133);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 60, 551, 411))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0, 0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(150, 184, 241, 31))
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(152, 234, 241, 31))
        self.txt_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(200, 300, 151, 31))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 30, 121, 111))
        self.label.setStyleSheet(u"background-color: rgb(0,0,0,0);")
        self.label.setPixmap(QPixmap(u"projeto_01/icon_title.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"User", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText("")
    # retranslateUi

