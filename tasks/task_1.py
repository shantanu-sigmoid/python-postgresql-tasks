# Task 1
# Write a Python program to list employee numbers, 
# names and their managers and save in a xlsx file.
import os
import sys
# path = '/Users/shantanu/Desktop/python-postgresql-tasks/models'
# os.environ['PATH'] += ':'+path
p = os.path.abspath('../models')
print(p)
sys.path.insert(1, p)
# print(os.environ['PATH'])

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('/Users/shantanu/Desktop/python-postgresql-tasks/models'))))
# print(sys.path)
# from ..models import database
# from models.database import CursorFromConnectionPool

from ..models.database import CursorFromConnectionPool
# from . import models.database.Database

# TODO: Resolve importing database cursor from models above

import pandas as pd

def run_query(query):
    with CursorFromConnectionPool() as cursor:
        cursor.execute(query)
        query_result = cursor.fetchall()
        query_result.insert(0, [cursor.description[i].name for i in range(len(cursor.description))])
        return query_result

def convert_list_to_xlsx(data, location):
    df = pd.DataFrame(data)
    df.to_excel(location, header =False, index = False)

if __name__ == "__main__":
    query = "select e1.empno, e1.ename as emp_name, e2.ename as mgr_name  \
    from emp as e1 INNER JOIN emp as e2 on (e1.mgr = e2.empno);"
    path = "./data/task_1.xlsx"
    convert_list_to_xlsx(run_query(query), path)
