f=open("myfile.txt","r")
g=open("new.txt","w")
def upper():
    
    s=f.read()
    for i in s:
        if i.isupper()==True:
           
            g.write(i)
         
        
   
    f.close()
    g.close()

upper()
