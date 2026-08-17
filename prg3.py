def filet():
    f=open("myfile.txt","r")
    s=f.read()
    l=s.split(" ")
    count=0
    for i in l:
        if len(i)==5:
            count+=1
    print("Number of 5 letter words=",count)
filet()
