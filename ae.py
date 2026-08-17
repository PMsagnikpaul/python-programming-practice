import pickle
f=open("sp.dat","wb")
l=["sagnik","subhojeet","niladri"]
s= pickle.dump(l,f)
f.close()

f=open("sp.dat","rb")
a=pickle.load(f)
print(a)
f.close()
