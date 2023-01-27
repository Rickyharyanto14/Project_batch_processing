#import library
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

#declare the file path
open_file = "C:\\Users\\ASUS\\.vscode\\batch_processing\\source\\kodepos.csv"

#create variable to read the file
df = pd.read_csv(open_file,sep=",")

#making connection and import
engine = create_engine('postgresql://postgres:111111@localhost:5432/postgres')
df.to_sql("from_file_table", engine)