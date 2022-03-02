from models.database import CursorFromConnectionPool

class JobHistory:
    def __init__(self, empno, startdate, enddate, job, sal, comm, deptno, chgdesc):
        self.empno = empno
        self.startdate = startdate
        self.enddate = enddate
        self.job = job
        self.sal = sal
        self.comm = comm
        self.deptno = deptno
        self.chgdesc = chgdesc

    def __repr__(self):
        return f"<JobHistory (empno = {self.empno}), (startdate = {self.startdate}), (enddate = {self.enddate}), (job = {self.job}), (sal = {self.sal})>"
    
    @classmethod
    def show_all_data(cls):
        with CursorFromConnectionPool() as cursor:
            cursor.execute("SELECT * FROM jobhist")
            user_data = cursor.fetchall()
            for data in user_data:
                print(cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    
    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            try:
                cursor.execute(f"INSERT INTO jobhist VALUES ({self.empno}, '{self.startdate}', {self.enddate}, '{self.job}', {self.sal}, {self.comm}, {self.deptno}, '{self.chgdesc}')")
                print("Successfully Added entry to Database ::jobhist::!!!")
            except:
                pass
            finally:
                print("Add here")

    