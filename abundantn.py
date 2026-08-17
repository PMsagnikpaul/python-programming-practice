# to check a number is abundant number or not. abundant number is when sum
#of factors(excluding the nymber itself) is greater than the number.
#Ex = factors of 12= 3,2,1,12,4,6

count = 0
x = int(input("Enter the number="))
for i in range(1,x):
    if x%i==0:
        print(i)
        count+=i

if count>x:
    print("The number ",x, " is an abundant number")
else:       
    print("The number ",x, " is not an abundant number")
