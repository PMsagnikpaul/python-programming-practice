class gradation:
    n=""
    c=""
    s=""
    ch=0
    ph=0
    m=0
    cpm=0
    t=0
    g=0
    def __init__(self):
        global n
        n =input("Enter your name:-")
        self.c=input("Enter your class:-")
        self.s=input("Enter your section:-")
        self.ch=int(input("Enter your chemistry out of 100:-"))
        self.ph=int(input("Enter your physics out of 100:-"))
        self.m=int(input("Enter your maths out of 100:-"))
        self.com=int(input("Enter your computer out of 100:-"))

    def grade(self,i):
        if i>90:
            return ("A++")
        elif i>80:
            return ("A+")
        elif i>70:
            return ("A")
        elif i>60:
            return ("B+")
        elif i>50:
            return ("B")
        elif i>40:
            return ("C+")
        elif i>30:
            return ("C")
        else:
            return ("Jaa.. !!! Tumi exam a fail korecho!!")

    def total(self):
        self.t=self.ch+self.ph+self.m+self.com
        return self.t

    def percentage(self):
        self.g = (self.t/400)*100
        return self.g
    def printg(self):
        global n
        print(n,"of",self.c,"and",self.s,"Your marks are:- ")
        print("Chemistry - ",self.ch,"grade"<self.grade(self.ch))
        print("Physics - ",self.ph,"grade"<self.grade(self.ph))
        print("Maths - ",self.m,"grade"<self.grade(self.m))
        print("Computer - ",self.com,"grade"<self.grade(self.com))
        print("Your total marks=",self.total())
        p = self.percentage()
        print("Your percentage is =",p)
        print("Your percentage is =", self.grade(p)
              
g.gradation()
g.printg()
        
        
            
