
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel,
    QPushButton

)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from database.database import (
    get_all_students,
    get_dashboard_analytics
)



class DashboardPage(QWidget):

    def __init__(self, main_window):

        super().__init__()

        self.main_window = main_window

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        sidebar = QVBoxLayout()
        sidebar.setContentsMargins(0, 0, 0, 0)
        sidebar.setSpacing(12)

        logo = QLabel("Student Dashboard")
        logo.setStyleSheet("font-size:20px;font-weight:bold;color:white;")

        sidebar.addWidget(logo)

        dashboard_btn = QPushButton("Dashboard")
        dashboard_btn.clicked.connect(self.load_analytics)
        sidebar.addWidget(dashboard_btn)

        subjects_btn = QPushButton("Subjects")
        subjects_btn.clicked.connect(self.open_subject)
        sidebar.addWidget(subjects_btn)

        student_btn = QPushButton("Students")
        student_btn.clicked.connect(self.view_student)
        sidebar.addWidget(student_btn)

        enrollment_btn = QPushButton("Enrollment")
        enrollment_btn.clicked.connect(self.main_window.show_add_student)
        sidebar.addWidget(enrollment_btn)


        sidebar.addStretch()

        logout_btn = QPushButton("Logout")
        logout_btn.clicked.connect(self.main_window.show_login)
        sidebar.addWidget(logout_btn)

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar)
        sidebar_widget.setFixedWidth(210)
        sidebar_widget.setStyleSheet(""" QWidget {
                background-color: #202D49;
            }

            QPushButton {
                background-color: #344563;
                color: white;
                border: none;
                padding: 12px;
                text-align: left;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #5378B8;
            }""")

        content = QVBoxLayout()
        content.setContentsMargins(25, 20, 25, 20)
        content.setSpacing(15)

        title = QLabel("Student Dashboard")
        title.setStyleSheet("font-size:28px;font-weight:bold;color:#202D49;")

        content.addWidget(title)

        stats_layout = QHBoxLayout()

        self.total_students = QLabel("Total Students: 0")
        self.total_subjects = QLabel("Total Subjects selection: 0")

        for label in [self.total_students, self.total_subjects]:
            label.setStyleSheet("""
                background-color: white;
                border: 1px solid #dddddd;
                border-radius: 8px;
                padding: 20px;
                font-size: 16px;
                font-weight: bold;
                            
            """)

            stats_layout.addWidget(label)
        content.addLayout(stats_layout)

        chart_title = QLabel("Subjects per student")
        chart_title.setStyleSheet("font-size:20px;font-weight:bold;")

        content.addWidget(chart_title)

        self.figure = Figure(figsize = (7,4))
        self.canvas = FigureCanvasQTAgg(self.figure)
        content.addWidget(self.canvas)

        content.addStretch()

        content_widget = QWidget()
        content_widget.setLayout(content)
        content_widget.setStyleSheet("background-color: #F5F7FB;")

        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(content_widget)

        self.setLayout(main_layout)
        self.load_analytics()



    def load_analytics(self):
        students = get_all_students()
        names,counts = get_dashboard_analytics()

        self.total_students.setText("Total Students: " + str(len(students)))

        self.total_subjects.setText("Total Subject Selections: " + str(sum(counts)))

        self.figure.clear()
        chart = self.figure.add_subplot(111)

        if names:
            chart.bar(names, counts, color = "#537888")
            chart.set_xlabel("Students")
            chart.set_ylabel("Number of Subjects")
            chart.set_title("Subject selected per student")
            chart.tick_params(axis='x', labelrotation=35)
        else:
            chart.text(
                0.5,0.5,
                "No student record yet",
                ha="center", va="center"
            )
            chart.set_axis_off()

        self.figure.tight_layout()
        self.canvas.draw()

    def view_student(self):
         self.main_window.view_student_page.load_students()
         self.main_window.show_view_student()
    def open_subject(self):
        self.main_window.show_subjects()

