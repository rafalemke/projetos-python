# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(718, 505)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"height: 30px")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setStyleSheet(u"height: 30px")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setStyleSheet(u"height: 30px")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setStyleSheet(u"height: 30px")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_outros = QPushButton(self.frame)
        self.btn_outros.setObjectName(u"btn_outros")
        self.btn_outros.setStyleSheet(u"height: 30px")

        self.horizontalLayout.addWidget(self.btn_outros)


        self.verticalLayout_2.addWidget(self.frame)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page_tables = QWidget()
        self.page_tables.setObjectName(u"page_tables")
        self.verticalLayout_8 = QVBoxLayout(self.page_tables)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.page_tables)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_file = QLineEdit(self.tables)
        self.txt_file.setObjectName(u"txt_file")

        self.horizontalLayout_3.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tables)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setStyleSheet(u"width:100px;\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_open)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(3, u"4");
        __qtreewidgetitem.setText(2, u"3");
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.tw_saida.setHeaderItem(__qtreewidgetitem)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setAllColumnsShowFocus(True)
        self.tw_saida.setWordWrap(False)
        self.tw_saida.header().setVisible(False)
        self.tw_saida.header().setCascadingSectionResizes(False)
        self.tw_saida.header().setHighlightSections(True)
        self.tw_saida.header().setProperty("showSortIndicator", False)
        self.tw_saida.header().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"width: 80px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")

        self.verticalLayout_3.addWidget(self.btn_importar)

        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_extornar = QPushButton(self.frame_2)
        self.btn_extornar.setObjectName(u"btn_extornar")

        self.verticalLayout_3.addWidget(self.btn_extornar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.pages.addWidget(self.page_tables)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout = QVBoxLayout(self.page_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pages.addWidget(self.page_home)
        self.page_cadastro = QWidget()
        self.page_cadastro.setObjectName(u"page_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.page_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.page_cadastro)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.page_cadastro)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.page_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.page_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.horizontalLayout_5.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.page_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.page_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.page_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.page_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.page_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.page_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.page_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.page_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.page_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.page_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.page_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.pages.addWidget(self.page_cadastro)
        self.page_contato = QWidget()
        self.page_contato.setObjectName(u"page_contato")
        font2 = QFont()
        font2.setPointSize(20)
        self.page_contato.setFont(font2)
        self.label_15 = QLabel(self.page_contato)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(210, 20, 271, 61))
        self.label_15.setFont(font)
        self.pages.addWidget(self.page_contato)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.label_16 = QLabel(self.page_sobre)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(240, 40, 181, 51))
        self.label_16.setFont(font)
        self.pages.addWidget(self.page_sobre)

        self.verticalLayout_2.addWidget(self.pages)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.btn_pg_cadastro = QPushButton(self.centralwidget)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")

        self.horizontalLayout_2.addWidget(self.btn_pg_cadastro)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Tables", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btn_outros.setText(QCoreApplication.translate("MainWindow", u"Outros", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Valor Nfe", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"UN", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Un", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_extornar.setText(QCoreApplication.translate("MainWindow", u"Extornar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"TreeWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#241f31;\">Innova</span></p><p align=\"center\"><span style=\" font-size:36pt; color:#241f31;\">Sistema de Gerenciamento</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tela de Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Repetir Senha: ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Perfil: ", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"User", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Admin", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Tela de Contato", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sobre: ", None))
        self.label_4.setText("")
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_5.setText("")
    # retranslateUi

