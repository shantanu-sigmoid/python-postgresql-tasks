from task_1 import convert_list_to_xlsx, run_query

# Task 2
# Write a python program to list the Total compensation given till his/her last date 
# or till now of all the employees till date in a xlsx file.
# columns required: Emp Name, Emp No, Dept Name, Total Compensation, Months Spent in Organization 
if __name__ == "__main__":
    update_enddate_as_curdate_query = "UPDATE jobhist SET enddate = current_date \
        where enddate is NULL;"
    select_query = "SELECT  emp.ename, jh.empno, dept.dname, \
        round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation,\
        round((enddate - startdate)/30) as emp_month_spent \
        from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"
    query = update_enddate_as_curdate_query + select_query
    path = "./data/task_2.xlsx"
    convert_list_to_xlsx(run_query(query), path)