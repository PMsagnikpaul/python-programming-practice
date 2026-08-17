f=open("myfile.txt","r")
g=open("uppercase.txt","w")
def upper():
    e=f.read()
    for i in e:
        if i.isupper==True:
            g.write(i)
    g.close()
    f.close()
upper()
