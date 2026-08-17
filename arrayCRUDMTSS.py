l=[]

# create

def PUSH():
    n = int(input("Enter the number of elements="))
    for i in range(n):
        el = int(input("Enter the element="))
        l.append(el)

# Searching

def SEARCH():
    x = int(input("Which number you want to search ="))
    if x in l:
        print("The number is present.")
    else:
        print("The number is not present.")


# traversal

def TRAVERSAL():
    for i in l:
        print(i)

# sorting

def SORT():
    dl =l
    dl.sort()
    print(dl)

    dl.sort(reverse=True)
    print(dl)


#merging

def MEARGE():
    y = eval(input("Enter the list ="))
    l.extend(y)
    print(l)

#pop

def POP():
    if len(l)==0:
        print("List is empty. Enter the list.")
        PUSH()
    else:
        print("How do you want to delete the element?")
        print(" 1 for deleting w.r.t. position and 2 for deleting w.r.t. element")
        inp = int(input("Enter your choice for deletion"))
        if inp == 1:
            h = int(input("Enter the position of which you want to delete="))
            l.pop(h)
            print(l)
        elif inp == 2:
            k = int(input("Enter the element which you want to delete="))
            l.remove(k)
            print(l)
        else:
            print("Enter right choice")
            
if __name__=="__main__":
    while True:
        print("Enter 1 for push operation")
        print("Enter 2 for Search operation")
        print("Enter 3 for traversal operation")
        print("Enter 4 for sort operation")
        print("Enter 5 for mearge operation")
        print("Enter 6 for pop operation")
        ch = int(input("Enter your choice="))

        if ch == 1:
            PUSH()
        elif ch == 2:
            SEARCH()
        elif ch == 3:
            TRAVERSAL()
        elif ch == 4:
            SORT()
        elif ch == 5:
            MEARGE()
        elif ch == 6:
            POP()
        else:
            print("Enter right choice")
            break
            
        
