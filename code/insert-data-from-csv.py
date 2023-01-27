#import library
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

open_file = "C:\\Users\\ASUS\\.vscode\\batch_processing\\source\\kodepos.csv"
df = pd.read_csv(open_file,sep=",")

engine = create_engine('postgresql://postgres:RH2000@localhost:5432/postgres')
df.to_sql("from_file_table", engine)