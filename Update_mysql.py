import pymysql
schema_name = "freedb_remotedb"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE freedb_remotedb.users SET id = '10' WHERE name = 'john'")

cursor.close()
conn.close()