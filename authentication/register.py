from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from database.database import register_user

class RegisterPage(QWidget):

    def __init__(self, main_window):

        super().__init__()
        self.setStyleSheet("""
            QWidget {
                background-color: #EAF2F8;
            }

            QPushButton {
                background-color: #202D49;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #344563;
            }

            QLineEdit, QComboBox, QListWidget {
                background-color: white;
                color: black;
                border: 1px solid #B8C7D9;
                border-radius: 5px;
                padding: 6px;
            }
        """)

        self.main_window = main_window
        

        layout = QVBoxLayout()
        layout.setContentsMargins(150,50,150,50)
        layout.setSpacing(10)

        title = QLabel("Register")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""font-family: Times New Roman;font-size: 35px;font-weight: bold;""")
        layout.addWidget(title)


        username_label = QLabel("Username")
        layout.addWidget(username_label)
        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter Username")
        layout.addWidget(self.username)


        password_label = QLabel("Password")
        layout.addWidget(password_label)
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        layout.addWidget(self.password)


        confirm_password_label = QLabel("Confirm Password")
        layout.addWidget(confirm_password_label)
        self.confirm_password = QLineEdit()
        self.confirm_password.setPlaceholderText(
            "Confirm Password"
        )
        self.confirm_password.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        layout.addWidget(self.confirm_password)

        register_button = QPushButton("Create Account")
        register_button.clicked.connect(
            self.register
        )
        layout.addWidget(register_button)

        back_button = QPushButton("Back to Login")
        back_button.clicked.connect(
            self.main_window.show_login
        )
        layout.addWidget(back_button)

        layout.addSpacing(150)

        self.setLayout(layout)


    def register(self):

        username = self.username.text().strip()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if username == "":

            QMessageBox.warning(
                self,
                "Error",
                "Please enter username."
            )

            return

        if password == "":

            QMessageBox.warning(
                self,
                "Error",
                "Please enter password."
            )

            return

        if password != confirm_password:

            QMessageBox.warning(
                self,
                "Error",
                "Passwords do not match."
            )

            return

        success = register_user(
            username,
            password
        )

        if success:

            QMessageBox.information(
                self,
                "Success",
                "Registration successful."
            )

            self.username.clear()
            self.password.clear()
            self.confirm_password.clear()

            self.main_window.show_login()

        else:

            QMessageBox.warning(
                self,
                "Error",
                "Username already exists."
            )