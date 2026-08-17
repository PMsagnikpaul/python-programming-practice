f=open("myfile.txt", "r")
def Aword():
    e=f.read()
    l=e.split(" ")
    count=0
    for i in l:
        if i[0] == "A":
            count+=1
    return count
x=Aword()
print("Number of words starting with A=",x)
