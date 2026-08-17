import pickle
def Employee():
    data=dict()
    f=open('employ.dat','rb')
    fx=open('newemp.dat','ab+')
    try:
        d=pickle.load(f)
        for i in d:
            if(d[i]>45000):
                data[i]=d[i]
        pickle.dump(data,fx)               
    except:
         f.close()

Employee()  
