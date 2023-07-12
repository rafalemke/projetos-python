from os import access
import pandas as pd
from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import DataBase
from xml_files import Read_xml
import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date
import matplotlib.pyplot as plt







class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon("imgs/icon.ico")
        self.setWindowIcon(appIcon)

        self.pushButton.clicked.connect(self.checkLogin)


        
    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        
        autenticado = self.users.check_user(self.txt_user.text(), self.txt_password.text()).lower()

        if autenticado == "administrador" or autenticado == "user":
            self.w = MainWindow(self.txt_user.text(), autenticado.lower())
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
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        appIcon = QIcon("imgs/icon.ico")
        self.setWindowIcon(appIcon)
        self.user = username
        
        if user.lower() ==  "user":
            self.btn_pg_cadastro.setVisible(False)

        # -------------- Paginas do sistema ------------------#
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_aahome))
        self.btn_tables.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_tables))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contato))
        self.btn_pg_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_import.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_import))

        self.btn_cadastrar.clicked.connect(self.subscribe_user)
        
        # -------------- Arquivo XML -----------------------#
        self.btn_open_xml.clicked.connect(self.open_path)
        self.btn_importar_xml.clicked.connect(self.import_xml_files)

        # FILTRO
        self.txt_filtro.textChanged.connect(self.update_filter)

        # Gerar saida e estorno
        self.btn_gerar.clicked.connect(self.gerar_saida)
        self.btn_extornar.clicked.connect(self.gerar_estorno)

        self.btn_excel.clicked.connect(self.excel_file)

        self.btn_grafico.clicked.connect(self.graphic)

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

        cn = sqlite3.connect('docs/system.db')
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
        

        cn = sqlite3.connect('docs/system.db')
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
        
        self.tb_estoque.setStyleSheet(u" QHeaderView{ color:black}; color:black; font-size:15px;")

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("docs/system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_estoque.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()


    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()
        

        self.table_saida()
        self.table_estoque()
        self.table_geral()


    def update_filter(self, s):

        s = re.sub("[\W_]+", "", s)
        filter_str = f'Nfe LIKE "%{s}%"'
        self.model.setFilter(filter_str)


    def gerar_saida(self):

        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items_out.append(child.text(0))
        recurse(self.tw_estoque.invisibleRootItem())

        # Pergunta se usuario realmente deseja fazer isso.
        self.question('saida')


    def gerar_estorno(self):

        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))

        recurse(self.tw_saida.invisibleRootItem())
        self.question('estorno')


    def question(self, table):

        msgBox = QMessageBox()

        if table == "estorno":
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText("As selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")
        else:
            msgBox.setText("Deseja gerar saída das notas selecionadas?")
            msgBox.setInformativeText("As notas selecionadas serão baixadas no estoque. \n Clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")
        
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_table()
            else:
                data_saida = date.today()
                data_saida = data_saida.strftime('%d/%m/%Y')
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estoque(data_saida, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()


    def excel_file(self):

        con = sqlite3.connect('docs/system.db')
        result = pd.read_sql_query("SELECT * FROM Notas", con)
        result.to_excel("docs/Resumo de notas.xlsx", sheet_name='Notas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório de Notas")
        msg.setText("Relatório gerado com sucesso!")
        msg.exec()


    def graphic(self):

        con = sqlite3.connect('docs/system.db')
        estoque = pd.read_sql_query('SELECT * FROM Notas WHERE data_saida == ""', con)
        saida = pd.read_sql_query('SELECT * FROM Notas WHERE data_saida != ""', con)

        estoque = len(estoque)
        saida = len(saida)

        labels = "Estoque", "Saídas"
        sizes = [estoque, saida]
        fig1, axl = plt.subplots()
        axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        axl.axis("equal")

        plt.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()