from tasks.database import CursorFromConnectionPool

class Department:
    def __init__(self, dept_no, dept_name, location):
        self.deptno = dept_no
        self.dname = dept_name
        self.loc = location

    def __repr__(self):
        return f"<Department (deptno = {self.deptno}), (dname = {self.dname}), (loc = {self.loc})>"
    
    @classmethod
    def load_from_db_by_loc(cls, location):
        with CursorFromConnectionPool() as cursor:
            # Note the (loc,) to make it a tuple!
            cursor.execute('SELECT * FROM dept WHERE loc=%s', (location,))
            user_data = cursor.fetchone()
            # Will return <Department (no = ), (dname = ), (loc = )>
            return cls(user_data[0], user_data[1], user_data[2])

    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            cursor.execute(f"INSERT INTO dept VALUES ({self.deptno}, '{self.dname}', '{self.loc}')")
            # cursor.execute(f'SELECT * FROM dept')
            # all_data = cursor.fetchall()
            # print(all_data)

    