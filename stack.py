import pickle
class stack:
    l=[]
    n=6
    def __init__(self):
        try:
            f=open("stack.dat",mode="rb")
            self.l=pickle.load(f)
            f.close()
        except:
            self.l=[]

    def Push(self,a):
        if len(self.l)<self.n:
            self.l.append(a)
        else:
            print("Overflow")

    def Pop(self):
        if len(self.l)==0:
            print("Underflow")
        else:
            self.l.pop()

    def Display(self):
        print(self.l)

    def close(self):
        f=open("stack.dat",mode="wb")
        pickle.dump(self.l,f)
        f.close()

if __name__=="__main__":
    while True:
        s=stack()
        choice=int(input("Enter your choice (1 for push, 2 for pop, 3 for display) ="))
        if choice==1:
            a = input("Enter the element you want to push=")
            s.Push(a)
            s.close()
        elif choice==2:
            s.Pop()
            s.close()
        elif choice==3:
            s.Display()
        else:
            s.close()
            print("Incorrect choice")
            break
