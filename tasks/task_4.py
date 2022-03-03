import pandas as pd

# Task 4
# From the xlsx in 2) create another xlsx to list total compensation given at Department level till date. 
# Columns: Dept No, Dept,Name, Compensation
if __name__ == "__main__":

    # Read task_2 data and convert it to dataframe
    path = "../data/task_2for4.xlsx"
    df = pd.read_excel(path)
    # Group by dataframe by deptno and dname and add total_compensation
    grp_df = df.groupby(["deptno", "dname"]).agg({"total_compensation": sum}).reset_index().rename(columns = {"deptno": "Dept No", "dname": "Dept Name", "total_compensation": "Compensation"})
    # Put it back to data in xlsx format named task_4.xlsx
    grp_df.to_excel("../data/task_4.xlsx", header =True, index = False)