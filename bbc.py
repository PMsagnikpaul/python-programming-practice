def ch(M,N):
    for i in range(N):
        if M[i]%5==0:
            M[i]//=5
        if M[i]%3==0:
            M[i]//=3
    N=N*5
L=[25,8,75,12]
u=4
ch(L,u)
print(L,u)
for i in L:
    
    print(i,end="#")
