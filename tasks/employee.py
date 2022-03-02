from tasks.database import CursorFromConnectionPool

class Employee:
    def __init__(self, empno, ename, job, mgr, hiredate, sal, comm, deptno):
        self.empno = empno
        self.ename = ename
        self.job = job
        self.mgr = mgr
        self.hiredate = hiredate
        self.sal = sal
        self.comm = comm
        self.deptno = deptno

    def __repr__(self):
        return f"<Employee (empno = {self.empno}), (ename = {self.ename}), (job = {self.job}, (mgr = {self.mgr}), (sal = {self.sal}))>"
    
    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            try:
                cursor.execute(f"INSERT INTO emp VALUES ({self.empno}, '{self.ename}', '{self.job}', {self.mgr}, '{self.hiredate}', {self.sal}, {self.comm}, {self.deptno})")
            except:
                pass
            finally:
                print("Add here")
            # cursor.execute(f'SELECT * FROM emp')
            # all_data = cursor.fetchall()
            # print(all_data)

    