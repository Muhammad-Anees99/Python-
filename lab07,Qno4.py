import math
def triarea(a,b,c):
    'prints area of triangles'
    s=(a+b+c)/2
    area=(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    return area
a1,b1,c1=eval(input("Enter three sides of triangle (Format:a,b,c):"))
area1=triarea(a1,b1,c1)
a2,b2,c2=eval(input("Enter three sides of triangle (Format:a,b,c):"))
area2=triarea(a2,b2,c2)
a3,b3,c3=eval(input("Enter three sides of triangle (Format:a,b,c):"))
area3=triarea(a3,b3,c3)
print(f'Areas are as follows: {area1},{area2},{area3}')