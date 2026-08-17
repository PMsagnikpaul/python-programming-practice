import csv
Student={}
L=list()
num=int(input('How many records do you want to store?'))
for i in range(1,num+1):
    name=input('Enter Name:')
    marks=float(input('Enter Percentage :'))
    Student['name']=name
    Student['marks']=marks
    L.append(Student)
    Student={}
file=open('E:\practcs\student.csv','w')
fields=['name','marks']
with file:
    wrt=csv.DictWriter(file,fieldnames=fields)
    wrt.writeheader()
    wrt.writerows(L)

stud=input('Enter the Name you want to Search:')
file=open('student.csv')
flag=True

with file:
    rdr=csv.DictReader(file,fieldnames=fields)
    for row in rdr:
        if(row['name']==stud):
            print('Percentage=',row['marks'])
            flag=False
            break
if(flag==True):
    print('Record of',stud,'is not found')
