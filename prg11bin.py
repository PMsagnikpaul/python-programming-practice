import pickle
def CountS():
    f=open('Names.dat','rb')
    try:
        L=pickle.load(f)
    except:
        print('Unable to Open')
    count=0
    for x in L:
        if(x[0]=='S'):
            print(x)
            count+=1
    print('No of People whose name starting with S=',count)


CountS()
