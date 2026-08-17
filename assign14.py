n =(input("Enter a sentence:"))
m = n.split(" ")
y= []
for i in m:
    x = len(i)
    y.append(x)
y.sort(reverse=True)
print(y[0])
