f=open("data.csv","r+")
m=f.read()
print(m)
if len(m)==0:
    print("No content is there")
    y="NAME"+","+"ROLL NUMBER"+","+"PHONE "+","+"EMAIL"+"\n"
    f.write(y)
    s = int(input("How many inputs you want to enter:"))
    for i in range(s):
        N = input("Enter your name:")
        R = input("Enter your roll number:")
        P = input("Enter your phone number:")
        E = input("Enter your email:")
        x = N+","+ R+","+P+","+E+"\n"
        f.write(x)
else:
    print("Content is present")
    s = int(input("How many inputs you want to enter:"))
    for i in range(s):
        N = input("Enter your name:")
        R = input("Enter your roll number:")
        P = input("Enter your phone number:")
        E = input("Enter your email:")
        x = N+","+ R+","+P+","+E+"\n"
        f.write(x)
f.close()
