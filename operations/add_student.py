from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QMessageBox,
    QListWidget, QStackedWidget
)

from subjects.subjects import get_subjects


class AddStudentPage(QWidget):

    def __init__(self, main_window):

        super().__init__()

        self.setStyleSheet("""QWidget{background-color: #EAF2F8;}
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
    }""")

        self.main_window = main_window
        self.student_data = {}

        main_layout = QVBoxLayout()

        self.panel = QStackedWidget()

        self.student_panel = QWidget()
        self.subject_panel = QWidget()

        self.panel.addWidget(self.student_panel)
        self.panel.addWidget(self.subject_panel)

        main_layout.addWidget(self.panel)
        self.setLayout(main_layout)

        self.create_student_panel()
        self.create_subject_panel()


    def create_student_panel(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(100, 50,100, 50)
        layout.setSpacing(10)

        title = QLabel("Add Student Information")
        title.setStyleSheet("font-size: 28px; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        fullname_label = QLabel("Full Name")
        layout.addWidget(fullname_label)
        self.fullname = QLineEdit()
        self.fullname.setPlaceholderText("Enter Full Name")
        layout.addWidget(self.fullname)

        Address_label = QLabel("Address")
        layout.addWidget(Address_label)
        self.address = QLineEdit()
        self.address.setPlaceholderText("Enter Address")
        layout.addWidget(self.address)


        Age_label = QLabel("Age")
        layout.addWidget(Age_label)
        self.age = QLineEdit()
        self.age.setPlaceholderText("Enter Age")
        layout.addWidget(self.age)

        Contact_label = QLabel("Contact")
        layout.addWidget(Contact_label)
        self.contact = QLineEdit()
        self.contact.setPlaceholderText("Enter Contact")
        layout.addWidget(self.contact)


        Email_label = QLabel("Email")
        layout.addWidget(Email_label)
        self.email = QLineEdit()
        self.email.setPlaceholderText("Enter Email")
        layout.addWidget(self.email)


        course_label = QLabel("Course")
        layout.addWidget(course_label)
        self.course = QComboBox()
        self.course.addItems([
            "BSCS",
            "BSIT",
            "BSCpE"
        ])
        layout.addWidget(self.course)


        yearlvl_label = QLabel("Year")
        layout.addWidget(yearlvl_label)
        self.yearlvl = QComboBox()
        self.yearlvl.addItems([
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th"
        ])
        layout.addWidget(self.yearlvl)


        buttons = QHBoxLayout()

        self.backbtn = QPushButton("Back")
        self.backbtn.clicked.connect(self.main_window.show_dashboard)
        buttons.addWidget(self.backbtn)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.go_to_subjects)
        buttons.addWidget(self.next_button)

        layout.addLayout(buttons)

        self.student_panel.setLayout(layout)

    def create_subject_panel(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(100,40,100,40)

        title = QLabel("Select Student Subjects")
        title.setStyleSheet("font-size: 28px; font-weight: bold;")
        layout.addWidget(title)

        subject_label = QLabel("Select Subject")
        layout.addWidget(subject_label)

        self.subject_list = QListWidget()
        layout.addWidget(self.subject_list)

        self.selected_label = QLabel("Selected Subjects: 0/10")
        layout.addWidget(self.selected_label)

        self.selected_subjects = QListWidget()
        layout.addWidget(self.selected_subjects)

        # Add and Remove buttons
        subject_buttons = QHBoxLayout()

        self.add_subject_button = QPushButton("Add Subject")
        self.add_subject_button.clicked.connect(self.add_subject)
        subject_buttons.addWidget(self.add_subject_button)

        self.remove_subject_button = QPushButton("Remove Subject")
        self.remove_subject_button.clicked.connect(self.remove_subject)
        subject_buttons.addWidget(self.remove_subject_button)

        layout.addLayout(subject_buttons)

        # Back and Next buttons
        navigation_buttons = QHBoxLayout()

        self.subject_back_button = QPushButton("Back")
        self.subject_back_button.clicked.connect(self.go_back_to_student)
        navigation_buttons.addWidget(self.subject_back_button)

        self.subject_next_button = QPushButton("Next")
        self.subject_next_button.clicked.connect(self.go_to_verify)
        navigation_buttons.addWidget(self.subject_next_button)

        layout.addLayout(navigation_buttons)

        self.subject_panel.setLayout(layout)

        self.load_subjects()


    def load_subjects(self):

        self.subject_list.clear()

        subjects = get_subjects()

        for subject in subjects:
            self.subject_list.addItem(subject)

    def go_to_subjects(self):

        fullname = self.fullname.text().strip()
        address = self.address.text().strip()
        age = self.age.text().strip()
        contact = self.contact.text().strip()
        email = self.email.text().strip()

        if fullname == "":
            QMessageBox.warning(self, "Error", "Please enter full name.")
            return

        if address == "":
            QMessageBox.warning(self, "Error", "Please enter address.")
            return

        if age == "":
            QMessageBox.warning(self, "Error", "Please enter age.")
            return

        if contact == "":
            QMessageBox.warning(self, "Error", "Please enter contact.")
            return

        if email == "":
            QMessageBox.warning(self, "Error", "Please enter email.")
            return

        try:
            age = int(age)

            if age <= 0:
                raise ValueError

        except ValueError:
            QMessageBox.warning(
                self, "Error", "Please enter a valid age."
            )
            return

        # Save student information temporarily
        self.student_data = {
            "fullname": fullname,
            "age": age,
            "address": address,
            "contact": contact,
            "email": email,
            "course": self.course.currentText(),
            "year_level": self.yearlvl.currentText()
        }

        # Open subject selection panel
        self.panel.setCurrentWidget(self.subject_panel)


    def add_subject(self):

        if self.selected_subjects.count() >= 10:

            QMessageBox.warning(
                self,
                "Limit",
                "You can only select 10 subjects."
            )

            return

        item = self.subject_list.currentItem()

        if item is None:
            QMessageBox.warning(
                self, "Subject", "Please select a subject first."
            )
            return

        subject = item.text()

        for i in range(self.selected_subjects.count()):

            if self.selected_subjects.item(i).text() == subject:

                QMessageBox.warning(
                    self,
                    "Subject",
                    "Subject is already selected."
                )

                return

        self.selected_subjects.addItem(subject)

        self.selected_label.setText(
            "Selected Subjects: "
            + str(self.selected_subjects.count())
            + "/10"
        )



    def remove_subject(self):

        row = self.selected_subjects.currentRow()

        if row >= 0:

            self.selected_subjects.takeItem(row)

            self.selected_label.setText(
                "Selected Subjects: "
                + str(self.selected_subjects.count())
                + "/10"
            )

    def go_back_to_student(self):

        self.panel.setCurrentWidget(self.student_panel)

    def go_to_verify(self):

        if self.selected_subjects.count() == 0:
            QMessageBox.warning(
                self, "Error", "Please select at least one subject."
            )
            return

        subjects = []

        for i in range(self.selected_subjects.count()):
            subjects.append(
                self.selected_subjects.item(i).text()
            )

        # Add selected subjects to student information
        data = self.student_data.copy()
        data["subjects"] = subjects

        self.main_window.pending_student = data
        self.main_window.verify_page.load_data(data)
        self.main_window.show_verify()

