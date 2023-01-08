import pymysql

schema_name = "freedb_remotedb"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F',
                       db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM freedb_remotedb.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()
