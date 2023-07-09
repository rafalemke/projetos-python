import typing
import PySide2.QtCore
from PySide2.QtWidgets import(QApplication, QMainWindow, QWidget, QMessageBox)
from ui_login import Ui_Login
import sys
from ui_main import Ui_MainWindow
from database import DataBase

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.open_system)

    def open_system(self):
        if self.txt_password.text() == "123":
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print("Senha inválida!")
    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        ######### Páginas do sistema ##############################################
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_home))
        self.btn_tables.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_tables))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_contato))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_cadastro))

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

    def subscribe_user(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas Divergentes")
            msg.setText("As senhas digitadas DEVEM ser iguais!")
            msg.exec_()
            return None
        
        
        nome = self.txt_nome.text()
        usuario = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, usuario, password, access)
        db.close_connection()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de Usurário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")
            





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

