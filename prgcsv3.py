import csv
def CopyLG():
    sum=0
    f=open('Product.csv','r')
    f2=open('LG.csv','w')
    L=[]
    with f:
        rdr=csv.reader(f)
        for d in rdr:
            if(d!=[] and d[1]=='LG'):
                sum=sum+int(d[2])
                L.append(d) 
                wrt=csv.writer(f2)
                wrt.writerows(L)
                L=[]
        print('Sum of all LG Products=',sum)                 
             
        
CopyLG()
