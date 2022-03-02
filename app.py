from tasks.department import Department
from tasks.employee import Employee
from tasks.database import Database
from tasks.job_history import JobHistory

Database.initialise(database="demo", user="postgres", password="password", host="localhost")

# dept_demo = Department(97, 'demo_dname2', 'demo_location')
# jobhist_demo = JobHistory(9999,'17-DEC-88',"NULL",'demo_job',999,"NULL",99,'demo_hire')
# dept_demo.save_to_db()
# jobhist_demo.save_to_db()


# dept_from_db = dept_demo.load_from_db_by_loc('demo_location')

# print(dept_from_db)