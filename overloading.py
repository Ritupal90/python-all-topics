"""Overloading=whenever class contains more than one mehods
     with same nme and different types 
     parameters called overloading."""

   #example:-

class A:
    def ritu(self,a,b):
        sum=a+b
        print(sum)
    def ritu(self,a,b,c):
        s=a+b+c
        print(s)
obj=A()
obj.ritu(2,2,2)