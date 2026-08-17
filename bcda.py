#wpp to rename a table from a database by showing the list of tables from
#that particular user given database

import mysql.connector as m
x = input("enter the database name=")
try:
    mycon =m.connect(host="localhost", user="root", password="12345678",database =x,port=3307)
    mycur=mycon.cursor()
    mycur.execute("show tables")
    data=mycur.fetchall()
    for i in data:
        print(i)
    y=input("enter the table name you want to change=")
    if y not in data: 
        print("Table not found")
    else:
        z=input("enter the new name=")
        q1="alter table {} rename {}".format(y,z)
        mycur.execute(q1)
    mycon.commit()
except Exceptional as e:
    print("error- "+str(e))
