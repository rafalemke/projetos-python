# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1008, 831)
        Login.setStyleSheet(u"background-color: rgb(0, 74, 112);")
        self.horizontalLayout_2 = QHBoxLayout(Login)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"max-width: 300px;\n"
"margin-bottom: 50px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(250, 300))
        self.label.setMaximumSize(QSize(320, 200))
        self.label.setBaseSize(QSize(50, 50))
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.setAcceptDrops(True)
        self.label.setStyleSheet(u"padding-right:20px;\n"
"padding-top:50px")
        self.label.setPixmap(QPixmap(u"projeto_01/imgs/icon_title.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(-21)
        self.label.setIndent(0)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_user)

        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_password)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 120))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label_3.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

