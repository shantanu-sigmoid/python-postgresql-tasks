import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="demo", user='postgres', password='password', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select * from emp;")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print(data)

#Closing the connection
conn.close()
# Connection established to: (
#    'PostgreSQL 12.0, compiled by Visual C++ build 1914, 64-bit',
# )