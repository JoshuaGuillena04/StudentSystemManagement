# 1.Project Title

**Student management system**

# 2.Project Description
The student management system is a desktop application that designed to help the administrator or user to manage student record.
This system allows to:
* Create an account and log in
* Add new Student information
* Select Subjects for each student
* View the student information
* Update student record
* Delete student records
* Store student information in SQLite Database
The system address to a simple way to manage student record instead of handling student information manually.

# 3.Project Objectives
The Main Objective of this System are: 
1. to Create simple student management application.
2. Allows the user to securely login and register account.
3. to store student information in a database
4. to allow the administrator or the user to add, view, update and delete
5. allowing the user to select subject for each student
6. to provide simple and user -friendly graphical interface




# 4.Features

**4.1 User Registration** – user can create account by providing the username, password and confirm password. This system checks if the username exists before creating account.

**4.2 Login**– register users can log in using their username and password.

**4.3 Dashboard** – after logging in the user taken to the dashboard panel where you can choose what should you do, in dashboard panel there are 3 buttons for add Student, View Student, and Logout.

**4.4 add student** – the user can enter the student information such as 
* Full name
* Address
* Age
* Contact
* Email
* Course
* Year Level
* The user can also choose the subject they want maximum of 10 subjects.
  
**4.5 Verify student**– after the user enter the information and selected subject you will pass to verification page where you can verify the information that you enter are correct.
  
**4.6 View students** – the system will display the registered students, the user can select view student information, update student information, and delete the student information.

**4.7 Update student** – the user can modify the existing student information and also can add and remove subjects.

**4.8 Delete student** – the user can select a student and delete student record.

**4.9 logout** – the user can log out in dashboard and return to login page.

# 5.Technologies Used
Programming language : python
Gui: PyQt6
Database: SQLite(sqlite3)
Others: Json used to store selected Subject in the database

# 6.Project Structure
StudentManagementSystem/

│

├── database/

│   └── database.py

│

├── authentication/

│   ├── login.py

│   └── register.py

│

├── features/

│   ├── add_student.py

│   ├── view_student.py

│   ├── update_student.py

│   ├── student_detail.py

│   └── verify_student.py

│
├── subjects/

│   └── subjects.py

│
├── Ui/	 

│   └──dashboard 

│

└── main.py


**Database/** - contains the database related functions.

**Authentication/** - contains the login and registration pages.

**Features/** - this hold major function of the system.

**Subjects/** - contains available subject information and subject related functions.

**Main.py** – acts as the main entry point of the application and controls the different pages.

# 7.Installation and Setup

Step 1 – install python 

Step 2 – install pyqt6 

Run in terminal: pip install pyqt6

Step 3 – Open the project folder in IDE (visual studio code, PyCharm)

Step 4 - Run the main python file.

# 8. How to Use the System
Step 1 – open the system with python main.py.

Step 2 – Register 
Open the system and create an account enter the username, password and confirmation password.

Step 3 – Login
Enter the registered username and password.

Step 4 – Open Dashboard
After successful login, the dashboard display

Step 5 – Add student
Click add student and enter the student information:

Full name:

Address: 

Age:

Contact:

Email:

Course:

Year Level:

Select Subjects:

Step 6 – Verify 
By clicking next to continue to verification page.

Step 7 – View Students
Return the dashboard and select view student the registered student will appear and you may choose view details, update, and delete.

Step 8 – View details 
Select student and you may see all their information.

Step 9 – Update
Select student and click update to modify student information.

Step 10 – delete
Select a student and click delete to delete student information

Step 11 – Logout 
Click log out to return to login page.

# 9.OOP Implementation
**Important Classes and Objects**

Classes:

Class DashboardPage(QWidget)

Class RegisterPage(QWidget)

Class AddstudentPage(QWidget)

Class ViewStudentPage(QWidget)

Class UpdateStudentPage(QWidget)

Class StudentDetailPage(QWidget)

Class VerifyPage(QWidget)

**Objects:**
QWidget – used as the base window/page.

QVBoxLayout – arranges widgets vertically.

QHBoxLayout – arranges widgets horizontally.

QGridLayout – used to arrange widgets in rows and columns.

QLabel – displays titles, labels, student information, and subjects.

 QLineEdit – allows the user to enter information such as name, address, contact, email, username, and password.
 
 QComboBox – allows the user to select options such as course and year level.
 
 QListWidget – displays available and selected subjects and the list of students.
 
QPushButton – creates buttons

QMessageBox – displays warning, information, success, and confirmation messages.

QTableWidget

QHeaderView

 QAbstractItemView
 
This object is used to build the applications Ui.

# OOP Concepts
**Inheritance:**
DashboardPage,

RegisterPage,

AddStudentPage,

ViewStudentPage,

StudentDetailPage,

UpdateStudentPage, 

And VerifyPage inherit from QWidget.

**Encapsulation:**

Each class has its own user interface elements, data and functions.

AddStudentpage Contains: 

•	Student input fields

•	Subject selection

•	add_subject()

•	remove_subject()

•	next_page()

**ViewStudentPage contains:**
•	Student list

•	load_students()

•	view_student()

•	update_student()

•	delete_student()

**VerifyPage contains:** 

•	Student information

•	Selected subjects

•	load_data()

•	submit_student()

•	go_back()

# 10.Database
The system uses SQlite as its database.

Then the system uses DATABASE = “student.db” to connect it, which is the file for database is student.db.

**User Table:**
| Column      | Type     | notes                       |
|----------   |----------|----------                    |
| id          |   INT    |    PRIMARY KEY AUTOINCREMENT |	
| username    | TEXT     | NOT NULL                     |
| password    | TEXT     | NOT NULL                     |



**Student Table:**

| Column     | Type | Notes                     |
|------------|------|---------------------------|
| id         | INT  | PRIMARY KEY AUTOINCREMENT |
| fullname   | TEXT | NOT NULL                  |
| age        | TEXT | NOT NULL                  |
| address    | TEXT | NOT NULL                  |
| contact    | TEXT | NOT NULL                  |
| email      | TEXT | NOT NULL                  |
| course     | TEXT | NOT NULL                  |
| Year_level | TEXT | NOT NULL                  |
| subjects   | TEXT | NOT NULL                  |


Create:
The system creates user accounts and student record.

The add_student() function insert the information into the database.

Read:

The system retrieves all student information, a specific student and user authentication information.

The get_all _student() function retrieves the student record.

Update:

The update_student() function modifies an existing student record.

Delete:

The delete_student() function remove a student using the student ID.

# 11.Screenshots

Login page - Shows the login interface where the user enter their username and password.
 
Register page - If the user does not have a account, the registration interface is for creating a new account.
 
Dashboard - The interface shows the dashboard with add student, view student and logout buttons.
 
Add student – This shows student information form and subject selection.
 
Verify – this shows the verify interface where you can verify if the information’s are correct before submitting it.
 
View student – this shows the list of registered student and you can even view their full information, modify their information and delete the student information.
# 12.Testing
| Feature           | Test                                      | Expected Result                         | Actual Result |
|-------------------|-------------------------------------------|------------------------------------------|---------------|
| Registration      | Enter valid username and password         | Create account                           | Success       |
| Registration      | Use existing username                     | Error message will display               | Success       |
| Login             | Enter correct username/password           | Enters the dashboard                     | Success       |
| Add Student       | Enter valid information                   | Student proceeds to verification         | Success       |
| Subject Selection | Select more than 10 subjects              | System prevents adding more subjects     | Success       |
| Subject Selection | Select the subject twice                  | System prevents duplicate subject        | Success       |
| View Student      | Select a student and click view           | Student information displays             | Success       |
| Update Student    | Modify student information                | Student record updated                   | Success       |
| Delete Student    | Select student and confirm deletion       | Student information deleted              | Success       |
| Logout            | Click logout                              | User returns to login page               | Success       |


# 13.Known Issues / Limitations

1.  No search student feature currently shown.

2. the maximum selected subject is currently 10.
   
3. The password is stored directly in the SQLite database rather than being hashed. The database code inserts the password directly into the user’s table.
   
4. The application is currently designed as a desktop application using PyQt6.

5.  The subject system depends on the subjects provided by the subject’s module.
  
# 14.Author

Name : Joshua C. Guillena

Section: CS26L (3581)


