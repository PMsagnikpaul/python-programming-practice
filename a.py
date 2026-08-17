n =(input("Enter a sentence:"))
m = ""
x= len(n)
for i in range(0,x):
    if i%2==0:
        y=n[i].lower()
    else:
        y=n[i].upper()
    m = m+y
print(m)
