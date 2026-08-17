import pickle
def Search(name):
    flag=False
    f=open('country.dat','rb')
    try:
        d=pickle.load(f)
        for info in d:
            if(info==name):
                print('Capital of',info,'is=',d[info])
                flag=True
                break
    except:
        f.close()

    if(flag==False):
        print(name,'is not found')


name=input('Enter the Country Name:')
Search(name)

