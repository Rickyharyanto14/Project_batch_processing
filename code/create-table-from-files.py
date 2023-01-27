#import library
import pandas as pd
from sqlalchemy import create_engine
import os


#declare the file path
file_path = r"C:\\Users\\ASUS\\.vscode\\batch_processing\\source\\users_w_postal_code.csv"
file_name = os.path.basename(file_path).split(".")[0]

#parsing username email from domain
df = pd.read_csv(file_path, sep=',')
df['email'] =  df['email'].apply(lambda x: x.split('@')[0])

engine = create_engine('postgresql://postgres:RH2000@localhost:5432/postgres')
df.to_sql(file_name,engine)

print(df)