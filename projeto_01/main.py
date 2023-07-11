from os import access
from PySide6.QtWidgets import *
from PySide6 import QtCore
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import DataBase
from xml_files import Read_xml
import sqlite3
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel


class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.pushButton.clicked.connect(self.checkLogin)


        
    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_user.text(), self.txt_password.text()).lower()

        if autenticado == "administrador" or autenticado == "user":
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()    
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:

                # bloquear usuario

                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        if user.lower() ==  "user":
            self.btn_pg_cadastro.setVisible(False)

        # -------------- Paginas do sistema ------------------#
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_tables))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contato))
        self.btn_pg_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_import.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_import))

        self.btn_cadastrar.clicked.connect(self.subscribe_user)
        
        # -------------- Arquivo XML -----------------------#
        self.btn_open_xml.clicked.connect(self.open_path)
        self.btn_importar_xml.clicked.connect(self.import_xml_files)

        self.reset_table()


    def subscribe_user(self):
        if self.txt_senha.text() != self.txt_senha2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senha inválida")
            msg.setText("A senhas devem ser iguais!")
            msg.exec()
            return None

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha2.setText("")


    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str("Open Directory"),
                                                     "/home",
                                                     QFileDialog.ShowDirsOnly
                                                     | QFileDialog.DontResolveSymlinks)
        self.txt_files.setText(self.path)


    def import_xml_files(self):

        xml = Read_xml(self.txt_files.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = DataBase()
        db.conecta()

        cont = 1
        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont += 1
        
        # ATUALIZAR TABELA

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("Importação concluída")
        msg.exec()
        self.progressBar.setValue(0)


        db.close_connection()


    def table_estoque(self):
        self.tw_estoque.setStyleSheet("font-size: 15px;")
        self.tw_estoque.setStyleSheet("QHeaderView{ color:black}")

        cn = sqlite3.connect('projeto_01/docs/system.db')
        result = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida = ''", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            # faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
            
            self.x = i[0]
        
        self.tw_estoque.setSortingEnabled(True)

        for i in range(1,15):
            self.tw_estoque.resizeColumnToContents(i)


    def table_saida(self):
        self.tw_saida.setStyleSheet(u" QHeaderView{ color;black}; font-size: 15px;")
        

        cn = sqlite3.connect('projeto_01/docs/system.db')
        result = pd.read_sql_query("SELECT Nfe, serie, data_importacao, data_saida, usuario FROM Notas WHERE data_saida != ''", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            # faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_saida, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
            
            self.x = i[0]
        
        self.tw_saida.setSortingEnabled(True)

        for i in range(1,15):
            self.tw_saida.resizeColumnToContents(i)


    def table_geral(self):
        self.tb_estoque.setStyleSheet("font-size: 15px;")
        self.tb_estoque.setStyleSheet("QHeaderView{ color:black}")

        cn = sqlite3.connect('projeto_01/docs/system.db')
        result = pd.read_sql_query("SELECT * FROM Notas" , cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            # faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tb_estoque, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
            
            self.x = i[0]
        
        self.tb_estoque.setSortingEnabled(True)

        for i in range(1,15):
            self.tb_estoque.resizeColumnToContents(i)


    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()