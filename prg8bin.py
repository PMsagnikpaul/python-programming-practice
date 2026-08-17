import pickle
def Topper():
    f=open('std.dat','rb')
    try:
        d=pickle.load(f)
        for info in d:
            if(d[info]>90):
                print('Topper Name:',info)
                print('Topper Marks:',d[info])

    except:
        f.close()

Topper()
