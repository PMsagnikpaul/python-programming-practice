#Design a class-
#a) void num_cal(int num, char ch)with one integer argument and one character
#argument, computes the square of integer argument if choice ch is 's' otherwise
#find it's cube.
#b) void num_calc(int a, int b, char ch)with two integer arguments if ch is 'p'
#else adds the integers

class num :
    def num_cal(i,c):
        if c == "s":
            i = i**2
        else:
            i = i**3
        print("your result is ",i)
    def num_calc(a,b,ch):
        s=0
        p=1
        if ch=="p":
            p=a*b
            print("result ",p)
        else:
            s=a+b
            print("result ",s)
            

obj=num
obj.num_cal(2,"s")
obj.num_calc(2,5,"p")

