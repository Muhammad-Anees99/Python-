import math
num=int(input("Enter a number whose square root you want:"))
if(num>=0):
    print(f'{math.sqrt(num)} is square root of {num}')
else:
    num1=-(num)
    print(f'{math.sqrt(num1)}j is square root of {num}')
    