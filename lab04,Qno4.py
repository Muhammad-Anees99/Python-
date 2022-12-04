import math
x=complex(input("Enter a complex number:"))
y=x.real
z=x.imag
a=math.sqrt((y**2)+(z**2))
print(f'Magnitude of entered complex number is:{a:.02f}')
