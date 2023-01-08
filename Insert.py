import pymysql

schema_name = "freedb_remotedb"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into freedb_remotedb.users (name, id) VALUES ('john', 5)")

cursor.close()
conn.close()