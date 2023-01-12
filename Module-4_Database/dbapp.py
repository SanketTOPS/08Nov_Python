import sqlite3

try:
    dbcon=sqlite3.connect("mydb.db")
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,sub) values('sanket','python'),('komal','java'),('binal','php'),('rutvi','angular'),('disha','react')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted successfully!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set sub='c++' where id=5"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated successfully!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted successfully!")
except Exception as e:
    print(e)"""

# Show Data
cur=dbcon.cursor()
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)
