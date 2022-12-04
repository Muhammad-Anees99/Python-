import math
def dis(x1,y1,x2,y2):
    result=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print('Distance between two entered points is', str(result))
    'finds distance between two points'
x1,y1=eval(input("Enter 1st Point (Format: a,b):"))
x2,y2=eval(input("Enter 2nd Point (Format: a,b):"))
dis(x1,y1,x2,y2)