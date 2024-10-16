import sqlite3 as sql

def read_db():
    date_list =[]
    temp_list = []
    connection = sql.Connection('sqldb.db')
    cursor = connection.cursor()
    cursor.execute("select * from temp")
    rows = cursor.fetchall()
    for i in rows:
        date_list.append(i[0])
        temp_list.append(i[1])
    return date_list,temp_list
    

if __name__ == '__main__':
    read_db()