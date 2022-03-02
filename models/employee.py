from models.database import CursorFromConnectionPool

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
        return f"<Employee (empno = {self.empno}), (ename = {self.ename}), (job = {self.job}), (mgr = {self.mgr}), (sal = {self.sal})>"

    @classmethod
    def show_all_data(cls):
        with CursorFromConnectionPool() as cursor:
            cursor.execute("SELECT * FROM emp")
            user_data = cursor.fetchall()
            for data in user_data:
                print(cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    
    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            try:
                cursor.execute(f"INSERT INTO emp VALUES ({self.empno}, '{self.ename}', '{self.job}', {self.mgr}, '{self.hiredate}', {self.sal}, {self.comm}, {self.deptno})")
                print("Successfully Added entry to Database ::emp::!!!")
            except:
                pass
            finally:
                print("Add here")

    