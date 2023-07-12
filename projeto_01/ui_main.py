# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableView, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1175, 836)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(182, 182, 182);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(182, 182, 182);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setFamilies([u"Chaparral Pro"])
        font.setPointSize(16)
        font.setBold(True)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(213, 213, 213);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 104, 104);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_pg_import = QPushButton(self.frame)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setMinimumSize(QSize(0, 35))
        self.btn_pg_import.setFont(font)
        self.btn_pg_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(213, 213, 213);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 104, 104);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_pg_import)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 35))
        self.btn_tables.setBaseSize(QSize(0, 0))
        self.btn_tables.setFont(font)
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(213, 213, 213);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 104, 104);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(213, 213, 213);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 104, 104);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(213, 213, 213);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 104, 104);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pages = QStackedWidget(self.frame)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(213, 213, 213);")
        self.pg_aahome = QWidget()
        self.pg_aahome.setObjectName(u"pg_aahome")
        self.verticalLayout = QVBoxLayout(self.pg_aahome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_aahome)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"background-color: rgb(213, 213, 213);")

        self.verticalLayout.addWidget(self.label)

        self.btn_pg_cadastro = QPushButton(self.pg_aahome)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_pg_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_pg_cadastro.setSizePolicy(sizePolicy2)
        self.btn_pg_cadastro.setMinimumSize(QSize(155, 27))
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout.addWidget(self.btn_pg_cadastro)

        self.pages.addWidget(self.pg_aahome)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_10 = QVBoxLayout(self.pg_import)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_17 = QLabel(self.pg_import)
        self.label_17.setObjectName(u"label_17")
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_17)

        self.progressBar = QProgressBar(self.pg_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_10.addWidget(self.progressBar)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_files = QLineEdit(self.pg_import)
        self.txt_files.setObjectName(u"txt_files")
        self.txt_files.setMinimumSize(QSize(0, 28))
        font2 = QFont()
        font2.setPointSize(12)
        self.txt_files.setFont(font2)
        self.txt_files.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);")
        self.txt_files.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.txt_files)

        self.btn_open_xml = QPushButton(self.pg_import)
        self.btn_open_xml.setObjectName(u"btn_open_xml")
        self.btn_open_xml.setMinimumSize(QSize(120, 28))
        self.btn_open_xml.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_xml.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-top-right-radius: 10px;\n"
"	font-size: 16px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_open_xml)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.pg_import)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.btn_importar_xml = QPushButton(self.pg_import)
        self.btn_importar_xml.setObjectName(u"btn_importar_xml")
        self.btn_importar_xml.setMinimumSize(QSize(0, 33))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.btn_importar_xml.setFont(font3)
        self.btn_importar_xml.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importar_xml.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_importar_xml)

        self.label_5 = QLabel(self.pg_import)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.pages.addWidget(self.pg_import)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.pg_cadastro)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_17.addWidget(self.label_25)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(150, 150))
        self.label_6.setSizeIncrement(QSize(0, 0))
        self.label_6.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.label_6.setFont(font4)
        self.label_6.setTabletTracking(False)
        self.label_6.setFocusPolicy(Qt.NoFocus)
        self.label_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"")
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setLineWidth(2)
        self.label_6.setMidLineWidth(0)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setPixmap(QPixmap(u"imgs/add_user.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setMargin(-20)
        self.label_6.setIndent(0)

        self.horizontalLayout_17.addWidget(self.label_6)

        self.label_26 = QLabel(self.pg_cadastro)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_17.addWidget(self.label_26)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(25, -1, 40, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setBaseSize(QSize(0, 0))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setMargin(20)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 1px solid gray;\n"
"border-radius: None;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")

        self.horizontalLayout_5.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(25, -1, 40, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(15)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 1px solid gray;\n"
"border-radius: None;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(25, -1, 40, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setMargin(18)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 1px solid gray;\n"
"border-radius: None;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(25, -1, 40, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(18)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.txt_senha2 = QLineEdit(self.pg_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 1px solid gray;\n"
"border-radius: None;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.txt_senha2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(42, -1, 847, 0)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setBaseSize(QSize(0, 0))
        self.label_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setMargin(0)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy4)
        self.cb_perfil.setMinimumSize(QSize(200, 25))
        self.cb_perfil.setMaximumSize(QSize(200, 200))
        self.cb_perfil.setAutoFillBackground(False)
        self.cb_perfil.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;\n"
"padding-left: 5px;")
        self.cb_perfil.setEditable(False)
        self.cb_perfil.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cb_perfil.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.cb_perfil, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 33))
        self.btn_cadastrar.setFont(font3)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_tables = QWidget()
        self.pg_tables.setObjectName(u"pg_tables")
        self.gridLayout = QGridLayout(self.pg_tables)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.pg_tables)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_8 = QVBoxLayout(self.tables)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_6.addWidget(self.tw_estoque)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_5.addWidget(self.tw_saida)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")
        sizePolicy.setHeightForWidth(self.btn_gerar.sizePolicy().hasHeightForWidth())
        self.btn_gerar.setSizePolicy(sizePolicy)
        self.btn_gerar.setMinimumSize(QSize(100, 32))
        self.btn_gerar.setBaseSize(QSize(0, 0))
        self.btn_gerar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_gerar)

        self.btn_extornar = QPushButton(self.frame_2)
        self.btn_extornar.setObjectName(u"btn_extornar")
        self.btn_extornar.setMinimumSize(QSize(100, 32))
        self.btn_extornar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_extornar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_extornar)

        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(100, 32))
        self.btn_importar.setCursor(QCursor(Qt.ForbiddenCursor))
        self.btn_importar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_importar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"padding:5px")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(0, 33))
        self.btn_grafico.setFont(font3)
        self.btn_grafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grafico.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_grafico)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 33))
        self.btn_excel.setFont(font3)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(147, 147, 147);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_excel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 1px solid gray;\n"
"border-radius: None;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.txt_filtro)

        self.tb_estoque = QTableView(self.tab_2)
        self.tb_estoque.setObjectName(u"tb_estoque")

        self.verticalLayout_11.addWidget(self.tb_estoque)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.pages.addWidget(self.pg_tables)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(self.pg_sobre)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 200))
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_19 = QLabel(self.pg_sobre)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setMinimumSize(QSize(300, 0))
        self.label_19.setMaximumSize(QSize(16777215, 16777215))
        self.label_19.setStyleSheet(u"margin: 50px")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_19)

        self.pages.addWidget(self.pg_sobre)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_13 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_16 = QLabel(self.pg_contato)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 200))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_16)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_13.addWidget(self.label_20)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.label_23 = QLabel(self.pg_contato)
        self.label_23.setObjectName(u"label_23")
        sizePolicy4.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy4)
        self.label_23.setMinimumSize(QSize(100, 100))
        self.label_23.setMaximumSize(QSize(100, 100))
        self.label_23.setSizeIncrement(QSize(100, 100))
        self.label_23.setBaseSize(QSize(100, 100))
        self.label_23.setStyleSheet(u"")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setMargin(0)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"padding-right: 100px")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_21)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(35, -1, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.label_24 = QLabel(self.pg_contato)
        self.label_24.setObjectName(u"label_24")
        sizePolicy4.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy4)
        self.label_24.setMinimumSize(QSize(100, 100))
        self.label_24.setMaximumSize(QSize(100, 100))
        self.label_24.setSizeIncrement(QSize(100, 100))
        self.label_24.setBaseSize(QSize(100, 100))
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_24)

        self.label_22 = QLabel(self.pg_contato)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"padding-right: 120px")

        self.horizontalLayout_14.addWidget(self.label_22)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.pages.addWidget(self.pg_contato)

        self.verticalLayout_3.addWidget(self.pages)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#2c2c2c;\">Lorem Ipsum</span></p><p align=\"center\"><span style=\" font-size:36pt; color:#444444;\">Sistema de Gerenciamento</span></p><p align=\"center\"><br/><img src=\"imgs/logo.png\"/></p></body></html>", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">IMPORTAR XML</p></body></html>", None))
        self.txt_files.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML --->", None))
        self.btn_open_xml.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_4.setText("")
        self.btn_importar_xml.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_5.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastrar Usu\u00e1rio</p></body></html>", None))
        self.label_25.setText("")
        self.label_6.setText("")
        self.label_26.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nome: </span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rio: </span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Senha: </span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Senha: </span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Perfil: </span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Estoque</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(15, QCoreApplication.translate("MainWindow", u"Data Sa\u00edda", None));
        ___qtreewidgetitem.setText(14, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Valor Produto", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Unidade medida", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Valor Nfe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"CNPJ_emitente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data_emiss\u00e3o", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data_sa\u00edda", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar sa\u00edda", None))
        self.btn_extornar.setText(QCoreApplication.translate("MainWindow", u"Extornar", None))
        self.btn_importar.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Registros Gerais</p></body></html>", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setText("")
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Geral", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Sobre</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Este sistema faz a importa\u00e7\u00e3o de arquivos XML e faz o controle do estoque de acordo com a entrada e sa\u00edda de notas apontadas pelo usu\u00e1rio.</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Contatos</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Desenvolvedor: Rafael Lemke</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"imgs/whats.png\"/></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">(81) 97121-0005</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"imgs/email.png\"/></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">rafael.acllemke@gmail.com</span></p></body></html>", None))
    # retranslateUi

