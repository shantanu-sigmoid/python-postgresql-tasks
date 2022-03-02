from tasks.department import Department
from tasks.employee import Employee
from tasks.database import Database

Database.initialise(database="demo", user="postgres", password="password", host="localhost")

# dept_demo = Department(97, 'demo_dname2', 'demo_location')
emp_demo = Employee(9999,'demo_name','demo',9999,'17-DEC-89',800,"NULL",20)
# dept_demo.save_to_db()
emp_demo.save_to_db()


# dept_from_db = dept_demo.load_from_db_by_loc('demo_location')

# print(dept_from_db)