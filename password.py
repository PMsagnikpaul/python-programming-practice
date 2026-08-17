x= input("enter the password=")
dc=uc=sc=0
y = len(x)

for i in x:
    if i.isdigit():
        dc+=1
    if i.isupper():
        uc+=1
    if i.isalnum()==False:
        sc+=1   
if y > 8 and y < 16:
    if x[0].isalnum():
        if dc >=2 and uc>=1 and sc>=1   :
            print(" pasword is valid")
        else:
            print("password is not valid 3")
    else:
        print("password is not valid 2")
else:
    print("password is not valid 1")
      
