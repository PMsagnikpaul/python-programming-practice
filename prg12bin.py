import pickle
def Count():
    f=open('Person.dat','rb')
    try:
        L=pickle.load(f)
    except:
        print('Unable to open')
    n=len(L)
    return n


print('Total Number of Records=',Count())
