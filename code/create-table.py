#import library
import psycopg2
import csv

#connect to potsgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=111111")
cur  = conn.cursor()


#create table 
cur.execute("""
            CREATE TABLE IF NOT EXISTS latihan_users(id serial PRIMARY KEY
            ,email text,name text,phone text,postal_code text)
"""
)

#declare file path
open_file = "C:\\Users\\ASUS\\.vscode\\batch_processing\\source\\users_w_postal_code.csv"

#read data and insert into database
with open(open_file) as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader) #skip header
    for row in csv_reader:
        cur.execute("INSERT INTO latihan_users VALUES ( default, %s, %s, %s,%s) ON CONFLICT DO NOTHING", row)
    
#to commit changes
conn.commit()