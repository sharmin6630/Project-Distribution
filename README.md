# Project-Distribution-G33

SUST CSE Thesis/Project Distribution System is a web project where student can give submit their preference supervisors list to authorities. Then, authorities can assign supervisor to student groups.

## Project

The project is using Django framework and sqlite3 at the backend.

### Guidelines

- clone this repo: git clone https://github.com/CSE-446-2016/Project-Distribution-G33.git
- create a virtual environment in the project folder
- install the packages from requirement.txt: pip install -r requirement.txt
- connect backend by: python manage.py migrate
- run: python manage.py runserver
- open localhost (http://localhost:8000) to view in the browser


### Functionalities

- Student can create and update their profile, fill thesis/project form and give the preference list, see teachers list and view their profile
- Teacher can create and update their profile
- Admin can view filled forms by students in a table, assign supervisors, perform queries based on CGPA, see summary charts of students' cgpa, total students, etc.
- Admin can see summary charts of student's CGPA presented in a bar chart and see the the number of students who can take project and thesis in a pie-chart.
- There is a noticeboard where all the notices posted by any teacher or admin will be displayed. All users can view the noticeboard with date of creation and author's  information. Teacher and admin can also update or delete any existing notice.
