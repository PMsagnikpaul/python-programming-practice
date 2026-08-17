import csv

def SHOW():
    f=open(r"E:\\file_handling\strr.csv","r")
    f1=open(r"E:\\file_handling\tes.txt","w")
    with f:
        rdr=csv.DictReader(f)
        li=[]
        for i in rdr:
            print(i)
            li.append(i)
        f1.write(str(li))
        


SHOW()
    
    
    
