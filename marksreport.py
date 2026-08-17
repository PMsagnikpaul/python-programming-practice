name = input("Enter your name:-")
cl = int(input("Enter your class:-"))
sec = input("Enter your section:-")
phy = int(input("Enter your marks in physics:-"))
chem = int(input("Enter your marks in chemistry:-"))
ma = int(input("Enter your marks in maths:-"))
pe = int(input("Enter your marks in physical education:-"))
comp = int(input("Enter your marks in computer science:-"))
eng = int(input("Enter your marks in english:-"))
total = phy +chem + ma + pe + comp + eng
per = total/600*100
if per<100 and per>30:
    print("Dear",name,"of class",cl,", section", sec, "have successfully passed the exam")
    if per>90:
        print("Grade = A+")
    elif per>80 and per<90:
        print("Grade = A")
    elif per>70 and per<80:
        print("Grade = B+")
    elif per>60 and per<70:
        print("Grade = B")
    elif per>50 and per<60:
        print("Grade = c+")
    elif per>40 and per<50:
        print("Grade = c+")
    elif per>30 and per<40:
        print("Grade = c+")
else:
    print("Dear",name,"of class",cl,", section", sec, "have failed in the exam !!")
print("Total marks physics:- ",phy)
print("Total marks chemistry:-",chem)
print("Total marks maths:-",ma)
print("Total marks physical education:- ",pe)
print("Total marks computer science:-",comp)
print("Total marks english:- ",eng)
print("Total marks obtained",total)
print("Percentage obtained",per)
