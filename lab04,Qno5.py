import math
x=complex(input("Enter a complex number:"))
y=x.conjugate()
b=x*y
z=b.real
a=math.sqrt((z))
print(f'Magnitude of entered complex number is:{a:.02f}')