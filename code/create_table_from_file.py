import pandas as pd
from sqlalchemy import create_engine

host = "localhost"
port = "5432"
dbname = "postgres2"
user = "postgres"
password = "admin"

df = pd.read_csv('C:/Users/Yunat/Documents/Downloads/project 3/source/users_w_postal_code.csv', sep=',')

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, dbname))

df.to_sql("users_w_postal_code", engine)

print('success')