# wpp to create a class called "circle" which have a constructor to hold the
#data of a variable "radius" and two functions called area and perimeter which
#will return the values.

import pickle
class circle:
    pi = 22/7
    r = 0
    def input(self,x):
        self.r=x
    def area(self):
        return self.pi*(self.r**2)
    def perimeter(self):
        return 2 * self.pi *self.r


x=circle()
print(x)
f =open("aag.dat","wb")
pickle.dump(x,f)
f.close()
    
