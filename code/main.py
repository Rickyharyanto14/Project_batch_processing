#import library
import psycopg2
import pandas as pds
import pandas.io.sql as sqlio



#connect to potsgresql
try:
  conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=111111")
  print("Connection success")
except:
  print("An exception occurred")


#using cursor to open and making transaction in database
cur = conn.cursor()
cur.execute("Select * from public.siswa")

#showing the result and commit
all = cur.fetchall()
one = cur.fetchone()
conn.commit()


for record in all:
    print(str(record[0]) +"-"+ record[1])
    
data = sqlio.read_sql_query("Select * from public.siswa", conn)
# Now data is a pandas dataframe having the results of above query.
data.head()