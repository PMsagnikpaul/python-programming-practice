import pickle
f=open('Person.dat','wb')
l=["Rolex","Vikram","Chandan","Abhay","Kaithi"]
pickle.dump(l,f)
f.close()

