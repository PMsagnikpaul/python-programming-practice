import mysql.connector as db
conn = db.connect(host="localhost",user="root",password="12345678",database="school",port="3307")
print(conn)

cur = conn.cursor()
print(cur)
#x = input("enter table name: ")
#query="desc "+x+";"
#cur.execute(query)
#print(cur)
#result=cur.fetchall()
#print(result)

def SHOWS():
    x = input("enter table name: ")
    query="desc "+x+";"
    cur.execute(query)
    print(cur)
    result=cur.fetchall()
    for i in result:
        print(i)

def SHOWD():
    x = input("enter table name: ")
    query1="select * from "+x+";"
    cur.execute(query1)
    print(cur)
    result=cur.fetchall()
    for i in result:
        print(i)


def INPUT():
    fn=tuple()
    fv=tuple()
    d={}
    x = input("enter table name: ")
    result=cur.fetchall()
    for i in result:
        for j in i:
            key=j
            fn+=(key,)
            val=input("enter "+str(j))
            fv+=(val,)
            d[key]=val
            break
    print(d)
    query="insert into "+x+" values "+str(fv)+";"
    cur.execute(query)
    r=cur.fetchall()
    print(r)

    

SHOWS()
SHOWD()
INPUT()
