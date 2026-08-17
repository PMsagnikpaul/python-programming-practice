import mysql.connector as m
x=input("enter the database name=")
mycon=m.connect(host="localhost",user="root",password="12345678",database=x,port=3307)
mycur=mycon.cursor()
y=input("enter the table name =")
q1="select * from {}".format(y)
mycur.execute(q1)
data=mycur.fetchall()
for i in data:
    print(i)
