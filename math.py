import math
from math import *
from tkinter import E
#we need to import each module we have to use just after importing math,from math import sqrt
#Otherwise we need to import each module of math by writing for example math.sqrt
# we can also import all modules at once by   "from math import * "
print(dir(math))
help(math.sqrt)
x=eval(input("Enter a number: "))
s=sqrt(x)
print(f"The square root of {x} is {s}")
# for trignometric functions angle is in radian
# we can convert it into math.degrees
print(sin(radians(30)))
print(pi)
# log(100,base) if we don't write base log will be equal to lnx
print(log(100,10))
print(exp(2))
# power
print(pow(2,4))
# ceil(x)  returns smallest integer greater than or equal to x
# floor(x)  returns smallest integer lesser than or equal to x
# factorial
print(factorial(9))
print(degrees(atan(1)))
print(degrees(atan2(1,1)))
print(degrees(atan2(-1,-1)))
# round of function
x=23.438790
print(round(x,2))

