import psycopg2

#making connection with database
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=RH2000")
cur  = conn.cursor()

#declare the file path
open_file = "C:\\Users\\ASUS\\.vscode\\batch_processing\\source\\users_w_postal_code.csv"

with open(open_file,'r') as f:
    next(f)
    cur.copy_from(f,'latihan_users',sep=',',columns=('email','name','phone','postal_code'))
conn.commit()