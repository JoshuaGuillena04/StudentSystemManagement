import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from database.database import create_database
from authentication.login import LoginPage
from authentication.register import RegisterPage

from ui.dashboard import DashboardPage
from features.verify import VerifyPage
from features.student_detail import StudentDetailPage

from operations.add_student import AddStudentPage
from operations.view_student import ViewStudentPage
from operations.update_student import UpdateStudentPage
from style.style import STYLE
from features.subject_page import SubjectPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Student Management System")

        self.pending_student = None

        self.pages = QStackedWidget()

        self.login_page = LoginPage(self)
        self.register_page = RegisterPage(self)

        self.dashboard_page = DashboardPage(self)

        self.add_student_page = AddStudentPage(self)
        self.view_student_page = ViewStudentPage(self)
        self.update_student_page = UpdateStudentPage(self)

        self.verify_page = VerifyPage(self)
        self.student_detail_page = StudentDetailPage(self)

        self.subject_page = SubjectPage(self)
        self.pages.addWidget(self.subject_page)

        self.pages.addWidget(self.login_page)
        self.pages.addWidget(self.register_page)
        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.add_student_page)
        self.pages.addWidget(self.view_student_page)
        self.pages.addWidget(self.update_student_page)
        self.pages.addWidget(self.verify_page)
        self.pages.addWidget(self.student_detail_page)


        self.setCentralWidget(self.pages)

        self.show_login()


    def show_login(self):

        self.pages.setCurrentWidget(
            self.login_page
        )


    def show_register(self):

        self.pages.setCurrentWidget(
            self.register_page
        )


    def show_dashboard(self):

        self.pages.setCurrentWidget(
            self.dashboard_page
        )


    def show_add_student(self):

        self.pages.setCurrentWidget(
            self.add_student_page
        )


    def show_view_student(self):
        #self.setCurrentWidget(self.view_student_page)
        self.pages.setCurrentWidget(
            self.view_student_page
        )


    def show_update_student(self):

        self.pages.setCurrentWidget(
            self.update_student_page
        )


    def show_verify(self):

        self.pages.setCurrentWidget(
            self.verify_page
        )


    def show_student_detail(self):

        self.pages.setCurrentWidget(
            self.student_detail_page
        )

    # def open_subjects(self):
    #     self.main_window.show_subjects()

    def show_subjects(self):
        self.pages.setCurrentWidget(self.subject_page)




def main():

    create_database()

    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)

    window = MainWindow()

    window.resize(800, 600)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()