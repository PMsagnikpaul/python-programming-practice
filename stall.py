import os
import mysql.connector as db
mycon=db.connect(host='localhost',user='root',password ='12345678',database='DiwaliMela' ,port="3307")
mycur=mycon.cursor()
Total=0
def Item():
	I=int(input('Enter The Item No:'))
	n=int(input('Enter The Quantity:'))
	sql=("Select amount from store where I_No = %s",I)
	mycur.execute(sql)
	mycon.commit()
	value=(I,)
	rec=mycur.fetchone()
	if(rec==None):
		print('Wrong Item No Entered:')
	else:
		for i in rec:
			for j in i:
				q=j*n
				Total+=q
				return Total
		
def Close():
	os.system('cls')
	print('\n Thank You, Visit Again')
	quit()


while(True):
    
    os.system('cls')
    print('------------WELCOME TO SPAUL STALL--------\n\n')
    print('\n\n Press 1 to Create a New Bill')
    print('Press 2 to close the application')
    choice=int(input('Enter Your Choice:'))
    if (choice==1):
            os.system('cls')
            Item()
            New=input('Do you want to add another item?[Y/N]:')
            if (New=='Y'):
                    Item()
            else:
                    print('Total Bill =',Total)
    Total=0

