import pandas as pd
import sys
sys.path.append("../")
from models.database import Engine,Database

def upload_xlsx_to_postgre_database(xlsx_path, new_database):
    # Create engine object
    connection_string = "postgresql://postgres:password@localhost:5432/demo"
    engine_demo = Engine(connection_string)
    engine = engine_demo.make_engine()
    # Reading excel file
    df = pd.read_excel(xlsx_path)
    # Uploading from excel to database
    try:
        df.to_sql(new_database, engine, if_exists = "replace", index = False)
        print(f"Data successfully uploaded to table : {new_database}")
    except:
        print(f"Exception occurred while uploading data to table : {new_database}")

# Task 3
    # Read and upload the above xlsx in 2) into a new table in the Postgres DB
if __name__ == "__main__":
    # Connecting to the database demo
    Database.initialise(database="demo", user="postgres", password="password", host="localhost")
    path = "../data/task_2.xlsx"
    upload_xlsx_to_postgre_database(path, "copy_of_task_2_data")