from models.department import Department
from models.employee import Employee
from models.database import Database
from models.job_history import JobHistory

Database.initialise(database="demo", user="postgres", password="password", host="localhost")

# dept_demo = Department(97, 'demo_dname2', 'demo_location')
# emp_demo = Employee(9998,'SMITH','CLERK',9999,'17-DEC-88',800,"NULL",20)
# jobhist_demo = JobHistory(9999,'17-DEC-88',"NULL",'demo_job',999,"NULL",99,'demo_hire')

# dept_demo.save_to_db()
# emp_demo.save_to_db()
# jobhist_demo.save_to_db()


# jobhist_demo.show_all_data()