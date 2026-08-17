import mysql.connector as db2
conn=db2.connect(host="localhost",user="root",password="12345678",database="school",port="3307")
cur=conn.cursor()


class db:
    def Show(self):
        x=input("enter table name")
        query="select * from "+x+";"
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            print(i)

    def Showd(self):
        x=input("enter table name")
        query="desc "+x+";"
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            print(i)

    def Input(self):
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
        conn.commit()


    def Update(self):
        try:
            x=input("enter the table")
            query="desc "+x+";"
            cur.execute(query)
            result=cur.fetchall()
            for i in result:
                if i[3]=='PRI':
                    p=i[0]
            field=input("Enter the field name to update ")
            ID=input("Enter your "+p)
            data=input("Enter the new data")
            query="update "+x+" set "+field+" = "+data+" where "+p+" = "+ID+";"
            print(query)
            cur.execute(query)
            conn.commit()
            print("Update Successfull")
        except Exception as e:
            print(e)

    def Del(self):
        try:
            x=input("enter the table")
            query="desc "+x+";"
            cur.execute(query)
            result=cur.fetchall()
            for i in result:
                if i[3]=='PRI':
                    p=i[0]
            ID=input("Enter your "+p)
            query="delete from "+x+" where "+p+" = "+ID+";"
            print(query)
            cur.execute(query)
            conn.commit()
            print("Delete successfull")
        except Exception as e:
            print(e)
    

if __name__=="__main__":
    while True:
        print("Enter 1 for Input operation")
        print("Enter 2 for Update operation")
        print("Enter 3 for Delete operation")
        print("Enter 4 for Show operation")

        ch=int(input("Enter your choice== "))
        x=db()
        if ch==1:
            x.Input()
        elif ch==2:
            x.Update()
        elif ch==3:
            x.Del()
        elif ch==4:
            x.Show()

        else:
            print("enter right choice ")
            break
            




        







    
