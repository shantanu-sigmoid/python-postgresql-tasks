# Task 2
# Write a python program to list the Total compensation given till his/her last date 
# or till now of all the employees till date in a xlsx file.
# columns required: Emp Name, Emp No, Dept Name, Total Compensation, Months Spent in Organization 

def formatData():
    with database.CursorFromConnectionPool() as cursor:
        cursor.execute(
            "UPDATE jobhist SET enddate = current_date where enddate is NULL;"
        )
        cursor.execute(
            "SELECT  emp.ename, jh.empno, dept.dname, \
            round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation,\
            round((enddate - startdate)/30) as emp_month_spent \
            from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"
        )
        single_data = cursor.fetchone()
        print(single_data)

# Task 3
# Read and upload the above xlsx in 2) into a new table in the Postgres DB

def upload_to_postgres_in_XLSX():
    pass


if __name__ == "__main__":
    solve()