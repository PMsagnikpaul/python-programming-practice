import pickle
def Employee():
    f=open('employ.dat','rb')
    try:
        d=pickle.load(f)
        for i in d:
            if(d[i]>45000):
                print('Employee Name=',i)
    except:
         f.close()


Employee()




