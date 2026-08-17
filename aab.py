def ReplaceZero():
    l=[]
    x = int(input("How many numbers you want to enter="))
    for i in range(x):
        y = int(input("Enter the element="))
        l.append(y)
    print("The list you entered is:",l)
    for j in range(x):
        if j+1<x:
            if l[j] == 0:
                l[j]=l[j+1]
    print("The new list is:",l)
        
ReplaceZero()     
    
