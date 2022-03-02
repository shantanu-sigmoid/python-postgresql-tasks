# Task 1
# Write a Python program to list employee numbers, 
# names and their managers and save in a xlsx file.
import os,sys
# path = '/Users/shantanu/Desktop/python-postgresql-tasks/models'
# os.environ['PATH'] += ':'+path
p = os.path.abspath('../models')
print(p)
sys.path.insert(1,p)
# print(os.environ['PATH'])

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('/Users/shantanu/Desktop/python-postgresql-tasks/models'))))
# print(sys.path)
# from ..models import database
# from models.database import CursorFromConnectionPool

# from ..models.database import CursorFromConnectionPool
# from . import models.database.Database


import pandas as pd

def solve():
    with database.CursorFromConnectionPool() as cursor:
        cursor.execute(
            "select e1.empno, e1.ename, e2.ename from emp as e1 INNER JOIN emp as e2 on (e1.mgr = e2.empno);"
        )
        single_data = cursor.fetchone()
        single_data.insert(0, (i[0] for i in cursor.description))
        print(single_data)

# TODO: Learn strftime to finalize this
def convert_list_to_xlsx(data):
    df = pd.DataFrame(data)
    for i in range(len(df)):
        df[i][1] = pd.to_datetime(df[i][1]).dt.strftime("%Y/%m/%d")
    .to_excel('./data/output.xlsx', header=True, index = True)

if __name__ == "__main__":
    solve()
