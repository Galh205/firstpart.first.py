import pymysql

schema_name = "freedb_remotedb"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
statementToExecute = "CREATE TABLE `"+schema_name+"`.`users`(`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));"
cursor.execute(statementToExecute)

cursor.close()
conn.close()