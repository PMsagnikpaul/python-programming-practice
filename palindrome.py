stack=[]
def push(s):
    sp=""
    for i in s:
        stack.append(i)
        sp=sp+i
    print(sp)
    return sp
    

s="MOM"
x=push(s)

def pop():
    sd=""
    n=len(stack)
    for i in range(n):
        sd+= stack.pop()
    print(sd)
    return sd
    

y=pop()

if x==y:
    print("it is a palindrome")

else:
    print("it is not a palindrome")
