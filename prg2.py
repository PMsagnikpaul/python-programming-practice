f=open("myfile.txt","r")
def alcount():
    upper=0
    lower=0
    digit=0
    spch=0
    s=f.read()
    for i in s:
        if i.isupper()==True:
            upper+=1
        if i.islower()==True:
            lower+=1
        if i.isdigit()==True:
            digit+=1
        if i.isalnum()==False:
            spch+=1
    print("Number of uppercase characters=",upper)
    print("Number of lowercase characters=",lower)
    print("Number of digits=",digit)
    print("Number of special characters=",spch)

alcount()
