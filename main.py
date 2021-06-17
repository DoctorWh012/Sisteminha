from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import QLine, Qt
from playsound import playsound


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Set Window
        self.setWindowTitle("Cadastro")
        self.window_layout = QFormLayout()
        self.setLayout(self.window_layout)
        #self.setFixedSize(300, 300)

        # Labels
        self.title = QLabel("Login Thing")
        self.title.setFont(QFont("HELVETICA", 25))
        self.title.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel("Nome")
        self.name_label.setFont(QFont("HELVETICA"))

        self.cpf_label = QLabel("CPF:")
        self.cpf_label.setFont(QFont("HELVETICA"))

        # Entry Boxes
        self.email_entry = QLineEdit(self)
        self.email_entry.setPlaceholderText("Digite seu email")

        self.email_confirm = QLineEdit(self)
        self.email_confirm.setPlaceholderText("Confirme seu email")

        self.password_entry = QLineEdit(self)
        self.password_entry.setPlaceholderText("Digite a sua senha")
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.password_confirm = QLineEdit(self)
        self.password_confirm.setPlaceholderText("Confirme sua senha")
        self.password_confirm.setEchoMode(QLineEdit.Password)

        self.name_entry = QLineEdit(self)
        self.name_entry.setPlaceholderText("Digite seu nome")

        self.cpf_entry = QLineEdit(self)
        self.cpf_entry.setPlaceholderText("000.000.000-00")
        self.cpf_entry.setMaxLength(11)

        # Button
        self.butao_login = QPushButton("Cadastrar")

        # Events
        self.butao_login.clicked.connect(self.somzinho)

        # Organize Layout
        self.window_layout.addRow(self.title)

        self.window_layout.addRow(self.name_label, self.name_entry)
        self.window_layout.addRow(self.cpf_label, self.cpf_entry)

        self.window_layout.addRow(self.email_entry, self.email_confirm)

        self.window_layout.addRow(self.password_entry, self.password_confirm)

        self.window_layout.addRow(self.butao_login)

        # show
        self.show()

    # ---------VALIDATION DEF-------

    def somzinho(self):
        emails_validos = ["@gmail.com", "@hotmail.com", "@outlook.com", "@a.com"]

        email = self.email_entry.text().strip()
        email_confirm = self.email_confirm.text().strip()

        password = self.password_entry.text().strip()
        password_confirm = self.password_confirm.text().strip()

        nome = self.name_entry.text().strip()

        mensagem_erro = str

        email_ok = True
        senha_ok = True

        # cpf validation
        try:
            cpf = int(self.cpf_entry.text().strip())
        except:
            self.erros("Insira um cpf valido")
            return
        if len(str(cpf)) != 11:
            self.erros("Insira um cpf valido")
            return

        # sees if the email is a valid email
        for x in emails_validos:
            if x not in email:
                email_ok = False
            elif x in email:
                email_ok = True
                break

        # sees if the email/pass and email_confirm/pass_confirm are the same
        if email != email_confirm:
            email_ok = False
        if password != password_confirm:
            senha_ok = False
        
        # runs if they are not the same
        if not email_ok or not senha_ok:
            if email:
                mensagem_erro = "Há algo de errado com sua senha"
            if senha_ok:
                mensagem_erro = "Há algo de errado com seu email"
            if not email and not senha_ok:
                mensagem_erro = "Há algo de errado com seu email e senha"
            
            # calls the error fun
            self.erros(mensagem_erro)
            return

        # saves email and pass if right
        else:
            self.save_email_pass(nome, email, password, cpf)
            playsound("nice.mp3")

    def save_email_pass(self, nome, email, password, cpf):
        # opens the txt in read mode
        t = open("logins.txt", "r")
        batata = t.readlines()
        t.close()

        # sees if the email is already on the txt
        for ems in batata:
            if email in ems:
                self.erros("Email ja cadastrado")
                return
        
        # opens the txt in append mode
        t = open("logins.txt", "a")

        # runs if the email is not on the txt
        t.write(f"\n{email}, {password}, {cpf}")
        self.sucesso("Cadastrado com sucesso!")
        t.close()

    def sucesso(srt, mensagem_sucesso):
        sucesso = QMessageBox()
        sucesso.setWindowTitle("Sucesso")
        sucesso.setText(mensagem_sucesso)
        x = sucesso.exec_()



    def erros(str, mensagem_erro):
        erro = QMessageBox()
        erro.setWindowTitle("Erro!!")
        erro.setText(mensagem_erro)
        x = erro.exec_()


# ---------MAIN WINDOW-----------

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.window_layout = QFormLayout()
        self.setLayout(self.window_layout)

        # Labels
        self.titulo = QLabel("Titulo ;-;")
        self.titulo.setFont(QFont("HELVETICA", 25))
        self.titulo.setAlignment(Qt.AlignCenter)

        # Buttons
        self.open_register = QPushButton("Registre-se")
        self.login = QPushButton("Log-in")

        # Events
        self.open_register.clicked.connect(self.open_register_window)

        # Organize Layout
        self.window_layout.addRow(self.open_register)
        self.window_layout.addRow(self.login)

        # Show
        self.show()

    def open_register_window(self):
        self.r_window = RegisterWindow()
        self.r_window.show()


if __name__ == "__main__":
    app = QApplication([])
    root = MainWindow()

    # Run
    app.exec_()
