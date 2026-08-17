#Wapp to do CRUD operation to store the value in key value pair in the python
#dictionary and thar dictionary file will be stored in a binary operation.

import pickle

#create

def CREATE():
    try:
        f=open("data.bin","rb")
        l=pickle.load(f)
        f.close()
        x = int(input("enter the number of records="))
        for i in range(x):
            d = {}
            k="Name"
            nam = input("enter the name")
            d[k]=nam
            p = "PhNo"
            ph = input("enter the phone number")
            d[p]=ph
            m = "Address"
            add = input("enter the address")
            d[m]=add
            l.append(d)
        f1=open("data.bin","wb")
        pickle.dump(l,f1)
        f1.close()
    except:
        f5=open("data.bin","wb")
        pickle.dump([],f5)
        f5.close()
        print("File created rerun the programme")
#read

def READ():
    f1=open("data.bin", "rb")
    y= pickle.load(f1)
    if len(y)!=0:
        print("Reading the file we get")
        print(y)
    f1.close()


#update

def UPDATE():
    f6=open

#delete
    
def DELETE():
    f2=open("data.bin", "rb")
    l=pickle.load(f2)
    con=int(input("Enter the id whom you want to remove="))
    if len(l)>con:
        l.pop(con-1)
        f3=open("data.bin", "wb")
        pickle.dump(l,f3)
        f3.close()
    else:
        print("The person doesn't exists !")

    f4=open("data.bin", "rb")
    d=pickle.load(f4)
    print("Removing the unwanted person !!")
    
if __name__=="__main__":
    while True:
        print("Enter 1 for Create operation")
        print("Enter 2 for Read operation")
        print("Enter 3 for Delete operation")
        
        ch = int(input("Enter your choice="))

        if ch == 1:
            CREATE()
        elif ch == 2:
            READ()
        elif ch == 3:
            DELETE()
        
        else:
            print("Enter right choice")
            break


