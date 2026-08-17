n =(input("Enter a sentence:"))
m = n.split(" ")
y= 0
for i in m:
    x = len(i)
    if y<x:
        y=x
print(y)
