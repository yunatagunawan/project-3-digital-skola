import psycopg2 as psy

host = "localhost"
port = "5432"
dbname = "postgres2"
user = "postgres"
password = "admin"

conn = psy.connect("host={} dbname={} user={} password={}".format(host, dbname, user, password))
cur = conn.cursor()

# Create table

cur.execute("""

CREATE TABLE IF NOT EXISTS users_using_copy (
    id serial primary key,
            email text,
            name text,
            phone text,
            postal_code text
)

""")

with open('C:/Users/Yunat/Documents/Downloads/project 3/source/users_w_postal_code.csv') as f:
  next(f)
  cur.copy_from(f, "user_using_copy", sep=',', columns=('email', 'name', 'phone', 'postal_code'))

conn.commit()