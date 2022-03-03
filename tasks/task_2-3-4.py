from task_1 import convert_list_to_xlsx, run_query
import pandas as pd
from ..models.database import Engine

def upload_xlsx_to_postgre_database(xlsx_path, new_database):
    # Create engine object
    connection_string = "postgresql://postgres:password@localhost:5432/demo"
    engine_demo = Engine(connection_string)
    engine = engine_demo.make_engine()
    # Reading excel file
    df = pd.read_excel(xlsx_path)
    # Uploading from excel to database
    df.to_sql(new_database, engine, if_exists = "replace", index = False)

if __name__ == "__main__":
    # Task 2
    # Write a python program to list the Total compensation given till his/her last date 
    # or till now of all the employees till date in a xlsx file.
    # columns required: Emp Name, Emp No, Dept Name, Total Compensation, Months Spent in Organization 
    update_enddate_as_curdate_query = "UPDATE jobhist SET enddate = current_date \
        where enddate is NULL;"
    select_query = "SELECT  emp.ename, jh.empno, dept.dname, \
        round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation,\
        round((enddate - startdate)/30) as emp_month_spent \
        from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"
    query = update_enddate_as_curdate_query + select_query
    path = "./data/task_2.xlsx"
    convert_list_to_xlsx(run_query(query), path)

    # Task 3
    # Read and upload the above xlsx in 2) into a new table in the Postgres DB
    upload_xlsx_to_postgre_database(path, "copy_of_task_2_data")
