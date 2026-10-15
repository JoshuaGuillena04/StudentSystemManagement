from PyQt6.QtWidgets import (
QWidget,
QVBoxLayout,
QLabel,
QComboBox,
QListWidget,
QPushButton
)
from subjects.subjects import SUBJECTS

class SubjectPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        title = QLabel("Subjects")
        title.setStyleSheet("""font-size: 28px; font-weight: bold; color: #202D49""")
        layout.addWidget(title)

        self.subject_list = QListWidget()
        layout.addWidget(self.subject_list)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(
            self.main_window.show_dashboard
        )
        layout.addWidget(back_btn)

        self.setLayout(layout)

        self.load_subjects()

    def load_subjects(self):
        self.subject_list.clear()

        for subject in SUBJECTS:
            self.subject_list.addItem(subject)

