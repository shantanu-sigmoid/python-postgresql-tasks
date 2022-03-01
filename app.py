from tasks.department import Department
from tasks.database import Database

Database.initialise(database="demo", user="postgres", password="password", host="localhost")

dept = Department(97, 'demo_dname2', 'demo_location')

# dept.save_to_db()


dept_from_db = dept.load_from_db_by_loc('demo_location')

print(dept_from_db)