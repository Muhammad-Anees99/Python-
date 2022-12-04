import math
a,b,c=eval(input("Enter three sides of triangle(separated by commas) :"))
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)
if(area>=0):
 print(f"The area of entered triangle is: {math.sqrt(area)}")
else:
    print("You entered invalid triangle")