# Task 1
# Write a Python program to list employee numbers, 
# names and their managers and save in a xlsx file.
import sys
  
# setting path
sys.path.append('../models')
from models.database import CursorFromConnectionPool
# from . import models.database.Database

def solve():
    with CursorFromConnectionPool() as cursor:
        cursor.execute(
            "select e1.empno, e1.ename, e2.ename from emp as e1 INNER JOIN emp as e2 on (e1.mgr = e2.empno);"
        )
        single_data = cursor.fetchone()
        print(single_data)

# if __name__ == "__main__":
# solve()
