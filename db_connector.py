import pymysql


def add_user(user_id, username):
    schema_name = "freedb_remotedb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('{username}', {user_id})")

    cursor.close()
    conn.close()
    return user_id


def get_user(user_id):
    schema_name = "freedb_remotedb"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # Selecting data into table
    cursor.execute(f"SELECT * user_name FROM {schema_name}.users where user_id='{user_id}';")

    cursor.close()
    conn.close()


def update_user(user_name, new_name):
    schema_name = "freedb_remotedb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Updating data inside the table
    cursor.execute("UPDATE freedb_remotedb.users SET id = user_id WHERE user_id = '{user_id}';")

    cursor.close()
    conn.close()


def delete_user(user_id):
    schema_name = "freedb_remotedb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_galh205', passwd='tFzZjGQ8p#@7g*F',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # delete data from the table
    cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}'")

    cursor.close()
    conn.close()
    return user_id


