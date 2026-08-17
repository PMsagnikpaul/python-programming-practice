import mysql.connector as db2
conn=db2.connect(host="localhost",user="root",password="12345678",database="school",port="3307")
cur=conn.cursor()

def CREATE():
    x=input("enter table name=")
    y=int(input("enter the number of fields="))
    d={}
    i=0
    while i!=y:
        a = input("enter field name=")
        b = input("enter datatype of the field and size=")
        d[a]=b
        i+=1
    print(d)

    for i in d:
        s = str(i)+" "+str(d[i]) +" , "
    z = s.rstrip(" ,")
    query= "create table "+x + " ( " + z +" );"
    print(query)

    cur.execute(query)
        
CREATE()
