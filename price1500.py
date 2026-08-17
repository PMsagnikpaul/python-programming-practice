d={}
import pickle
def Store():
    n = int(input("How many records you want to enter="))
    for i in range(n):
        x = input("Enter the product name=")
        y =input("Enter the manufacturer=")
        z = int(input("Enter the price="))
        l=[y,z]
        d[x]=l
    
    f=open("Product.dat","wb")
    pickle.dump(d,f)
    f.close()


def Find():
    g=open("Product.dat","rb")
    m=pickle.load(g)
    count=0
    for j in m:
        if m[j][-1] >1500:
            count+=1
            print("product",j,"Manufacturer",g[j][0])
    print("Number of products with price more than 1500 =",count)

Store()
Find()
