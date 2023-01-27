import psycopg2
import csv

#connect to potsgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=RH2000")
cur  = conn.cursor()
open_file = "C:\\Users\\ASUS\\.vscode\\batch_processing\\source\\users_w_postal_code.csv"

#create table 
cur.execute("""
            CREATE TABLE IF NOT EXISTS latihan_users(id serial PRIMARY KEY
            ,email text,name text,phone text,postal_code text)
"""
)

with open(open_file) as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader) #skip header
    for row in csv_reader:
        cur.execute("INSERT INTO latihan_users VALUES ( default, %s, %s, %s,%s) ON CONFLICT DO NOTHING", row)
    
conn.commit()