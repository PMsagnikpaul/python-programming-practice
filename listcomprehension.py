l=[]
for i in range(1,11):
    l.append(i)
print(l)

#list comprehension

x = [i for i in range(1,11,2)]
print(x)


y=[]
for c in range(1,11):
    if c%2!=0:
        y.append("Paul")
    else:
        y.append("Sagnik")
print(y)

v= "Paul"
y = [v if c%2!=0 else "Sagnik" for c in range(1,11)]
print(y)
