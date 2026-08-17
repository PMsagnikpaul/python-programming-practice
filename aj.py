import pickle
#create

def Create():
    try:
        f = open("country.dat","ab")
        fr=open("country.dat","rb")
        d=pickle.load(fr)
        fr.close()
        cont=input("Enter the country name=")
        cap =input ("Enter the countrie's capital=")
        if cont in d.keys():
            print("Country already exists")
        else:
            fw = open("country.dat","wb")
            d[cont]= cap
            pickle.dump(d,f)
            fw.close()
    except :
        pickle.dump({"country":"capital"},f)
        print("Rerun this code")
    finally:
        f.close()

def Read():
    f1=open("country.dat", "rb")
    x= pickle.load(f1)
    if len(x)!=0:
        print(x)

def Update():
    f2=open("country.dat", "rb")
    d=pickle.load(f2)
    f2.close()
    con=input("Enter the country name to update=")
    if con in d.keys():
        cap =input("Enter the countrie's new capital=")
        d[con]=cap
        f3=open("country.dat", "wb")
        pickle.dump(d,f3)
        f3.close()
    else:
        print("Country doesn't exists")

def Delete():
    f4=open("country.dat", "rb")
    d=pickle.load(f4)
    f4.close()
    con=input("Enter the country name to update=")
    if con in d.keys():
        d.pop(con)
        f3=open("country.dat", "wb")
        pickle.dump(d,f3)
        f3.close()
    else:
        print("Country doesn't exists")


if __name__=="__main__":
    choice=int(input("Enter your choice="))
    if choice==1:
        Create()
    elif choice==2:
        Read()
    elif choice==3:
        Update()
    elif choice==4:
        Delete()
