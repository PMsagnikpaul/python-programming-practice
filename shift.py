def shift(Arr,n):
    l=len(Arr)
    for i in range(0,n):
        y=Arr[0]
        for j in range(0,l-1):
            Arr[j]=Arr[j+1]
        Arr[l-1]=y
    print(Arr)


Arr=[1,2,3,4,5,6]
n=int(input("Enter number:"))
shift(Arr,n)
