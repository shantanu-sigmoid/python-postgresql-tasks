from models.department import Department
from models.employee import Employee
from models.database import Database
from models.job_history import JobHistory
from models.database import CursorFromConnectionPool
import pandas as pd


def run_query(query):
    with CursorFromConnectionPool() as cursor:
        cursor.execute(query)
        query_result = cursor.fetchall()
        query_result.insert(0, [cursor.description[i].name for i in range(len(cursor.description))])
        return query_result

def convert_list_to_xlsx(data, path):
    df = pd.DataFrame(data)
    df.to_excel(path, header =False, index = False)


Database.initialise(database="demo", user="postgres", password="password", host="localhost")

# dept_demo = Department(97, 'demo_dname2', 'demo_location')
# emp_demo = Employee(9998,'SMITH','CLERK',9999,'17-DEC-88',800,"NULL",20)
# jobhist_demo = JobHistory(9999,'17-DEC-88',"NULL",'demo_job',999,"NULL",99,'demo_hire')

# dept_demo.save_to_db()
# emp_demo.save_to_db()
# jobhist_demo.save_to_db()


update_enddate_as_curdate_query = "UPDATE jobhist SET enddate = current_date \
        where enddate is NULL;"
select_query = "SELECT  emp.ename, jh.empno, dept.dname, \
    round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation,\
    round((enddate - startdate)/30) as emp_month_spent \
    from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"
query = update_enddate_as_curdate_query + select_query
path = "./data/task_2.xlsx"
convert_list_to_xlsx(run_query(query), path)