from tasks.database import CursorFromConnectionPool

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
        return f"<JobHistory (empno = {self.empno}), (startdate = {self.startdate}), (enddate = {self.enddate}, (job = {self.job}), (sal = {self.sal}))>"
    
    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            try:
                # cursor.execute(f"INSERT INTO jobhist VALUES ({self.empno}, '{self.startdate}', {self.enddate}, '{self.job}', {self.sal}, {self.comm}, {self.deptno}, '{self.chgdesc}')")
                print("Successfully Added entry to Database ::jobhist::!!!")
            except:
                pass
            finally:
                print("Add here")
            cursor.execute(f'SELECT * FROM jobhist')
            all_data = cursor.fetchall()
            print(all_data)

    