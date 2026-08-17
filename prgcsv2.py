import csv
def ReadCopy():
    f=open("org.csv","r")
    f2=open("new.csv","w")
    L=[]
    with f:
        rdr=csv.reader(f)
        for d in rdr:
            if(d!=[] and d[1]>"80"):
                L.append(d) 
                wrt=csv.writer(f2)
                wrt.writerows(L)
                L=[]
        
ReadCopy()
