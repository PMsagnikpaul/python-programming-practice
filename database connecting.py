import mysql.connector as db
conn=db.connect(host="localhost",user="root",password="12345678",database="school",port="3307")
print(conn)


cur=conn.cursor()       
print(cur)


def Show():
    x=input("enter table name")
    query="select * from "+x+";"
    cur.execute(query)
    result=cur.fetchall()
    for i in result:
        print(i)


def Showd():
    x=input("enter table name")
    query="desc "+x+";"
    cur.execute(query)
    result=cur.fetchall()
    for i in result:
        print(i)

Showd()

def Input():
    fn=tuple()
    fv=tuple()
    d={}
    x=input("enter table name")
    query="desc "+x+";"
    cur.execute(query)
    result=cur.fetchall()
    for i in result:
        for j in i:
            key=j
            fn+=(key,)
            val=input("enter "+str(j) )
            fv+=(val,)
            d[key]=val
            break
    print(d)
    print(fn)
    print(str(fn))
    query="insert into "+x+" values "+str(fv)+";"
    cur.execute(query)
    r=cur.fetchall()
    print(r)
        

Input()




