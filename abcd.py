stack = []
ostack=[]
def PUSH(stack,el):
    stack.append(el)

def ODDN():
    for i in stack:
        if i%2==1:
            PUSH(ostack,i)
            print(ostack)

def LARGE():
    ostack.sort()
    z=ostack[-1]
    print("The list in ascending order is ",ostack)
    print("The largest number is ",z)

x = int(input("How many numbers you want to enter?"))
for i in range(x):
    y =int(input("Enter the number="))
    PUSH(stack,y)

ODDN()
LARGE()
