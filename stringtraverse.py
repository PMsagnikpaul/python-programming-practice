s=input("Enter the sentence:")
uv=uc=lv=lc=sp=dig=0
for i in s:
    if i.isupper()==True:
        if i in "AEIOU":
            uv+=1
        else:
            uc+=1
    elif i.islower()==True:
        if i in "aeiou":
            lv+=1
        else:
            lc+=1
    elif i.isdigit() == True:
        dig+=1
    else:
        sp+=1

print("No.of uppercase vowels=",uv)
print("No.of uppercase consonant=",uc)
print("No.of lowercase vowels=",lv)
print("No.of lowercase consonant=",lc)
print("No.of digit =",dig)
print("No.of special characters=",sp)

l=s.split()
print("No. of words=",len(l))

print("Changing the case :")
print(s.swapcase())

print("First character capital:")
print(s.title())
