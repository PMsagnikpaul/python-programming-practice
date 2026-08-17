import pickle
f=open('Person.dat','rb')
d=pickle.load(f)
print(d)
f.close()
