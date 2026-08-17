import csv
def ReadInfo():
     f=open('E:\practcs\Staff.csv','r')
     count=0
     with f:
         rdr=csv.reader(f)
         for data in rdr:
             if(data[2]=='Finance' and data[1]>'60000'):
                 print(data)
                 count+=1

     print('No of employees in Finance Dept earning more than Rs 60000=',count)


ReadInfo()
