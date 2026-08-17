#WAP to accept 3 angles o a triangle and tell if it is a isosceles ,
#equilateral,right angle triangle.

x=int(input("Enter 1st angle="))
y=int(input("Enter 2nd angle="))
z=int(input("Enter 3rd angle="))

if x+y+z == 180:
    if x == 90 or y == 90 or z == 90:
        print("It is a right angle triangle")
    if x==y!=z or y==z!=x or x==z!=y:
        print("It is an isosceles triangle")
    if x==y==z:
        print("It is an equilateral triangle")
    

else:
    print("Gadha r moto kaaj korben na thik angle din nahole kelabo")
