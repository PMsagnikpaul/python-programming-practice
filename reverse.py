def reverse():
    f=open("myfile.txt","r")
    s=f.readlines()
    l=s[::-1]
    f.close()
    
    g=open("myfile.txt","w")
    
    for i in l:
        g.write(i)
    g.close()

    f=open("myfile.txt","r")
    s=f.read()
    print(s)
reverse()
