import mysql.connector as m
mycon =m.connect(host="localhost",user="root",password="12345678",database="work",port=3307)
mycur=mycon.cursor()
def search(E):
    sql="select * from employee where EMP_NO={}".format(E)
    mycur.execute(sql)
    data=mycur.fetchall()
    if data ==None:
        print("No such employee is there")
    else:
        for i in data:
            print(i[0],i[1],i[2],i[3],end=" ")
            print()

E=int(input("enter the employee number you want to search:"))
search(E)
