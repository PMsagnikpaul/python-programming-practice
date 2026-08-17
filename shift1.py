def SwapShift(Arr):
    l=len(Arr)
    if(l%2!=0):
    	l=l-1
    for i in range(0,l,2):
    	Arr[i],Arr[i+1] = Arr[i+1],Arr[i] 
    return Arr



my_list = [1, 2, 3, 4, 5,6]
print(SwapShift(my_list))

def Shift(Arr, n):
    x  = Arr[-n:]+Arr[:-n]
    return x

my_list = [1, 2, 3, 4, 5, 6]
print(Shift(my_list, 4))




def R_Shift(Arr,n):
    Arr1=[]
    length=len(Arr)
    last=Arr[length-1]
    secondlast=Arr[length-2]
    Arr1.append(last)
    Arr1.append(secondlast)
    
    for i in range(0,length-2):
        Arr1.append(Arr[i])
   
    print(Arr1)


R_Shift([1,2,3,4,5,6],2)
