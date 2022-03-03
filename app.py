from models.department import Department
from models.employee import Employee
from models.job_history import JobHistory
from models.database import Engine,Database
import pandas as pd
import logging


# def run_query(query):
#     with CursorFromConnectionPool() as cursor:
#         cursor.execute(query)
#         query_result = cursor.fetchall()
#         query_result.insert(0, [cursor.description[i].name for i in range(len(cursor.description))])
#         return query_result

# def convert_list_to_xlsx(data, path):
#     df = pd.DataFrame(data)
#     df.to_excel(path, header =False, index = False)


if(__name__ == "__main__"):
    # Configure logging
    logging.basicConfig(filename='./log/system.log', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
    # Connecting to database
    Database.initialise(database="demo", user="postgres", password="password", host="localhost")
    # Connecting to engine
    connection_string = "postgresql://postgres:password@localhost:5432/demo"
    engine_demo = Engine(connection_string)
    engine = engine_demo.make_engine()
    # Creating dummy data
    dept_demo = Department(97, 'demo_dname2', 'demo_location')
    emp_demo = Employee(9998,'SMITH','CLERK',9999,'17-DEC-88',800,"NULL",20)
    jobhist_demo = JobHistory(9999,'17-DEC-88',"NULL",'demo_job',999,"NULL",99,'demo_hire')

    # Rough work
    df= pd.read_excel("./data/task_2.xlsx")
    print(df)
    df.to_sql('task_2_data', engine, if_exists="replace", index = False)