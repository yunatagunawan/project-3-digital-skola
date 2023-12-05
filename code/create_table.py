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

CREATE TABLE IF NOT EXISTS latihan_users(
    id serial primary key,
            email text,
            name text,
            phone text,
            postal_code text
)

""")

conn.commit()