#Qno.1
from binascii import Incomplete


num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))
print("You have entered ",num1,"and",num2)
print(num1,"is",(num1/num2)*100,"% of",num2)
#Qno.2
num3=float(input("Enter a number: "))
print("Integral part is: ",int(num3))
print("The fractional part is :",num3-2)
#Qno.3
x=eval(input("Enter a 3-digit number: "))
a=x%10
x=x//10
b=x%10
c=x//10

print(c)
print(b)
print(a)
print(c,"+",b,"+",a,"=",a+b+c)
# formated String
y=eval(input("Enter first number: "))
z=eval(input("Enter second number: "))
print(f"First number is {y} And second number is {z}")
#Qno.4
ticketa=eval(input("How many tickets of category A have been sold :"))
ticketb=eval(input("How many tickets of category B have been sold :"))
ticketc=eval(input("How many tickets of category C have been sold :"))
Income =(ticketa*1000+ticketb*700+ticketc*500)
print(f"Total income generated from ticket is :{Income}")
#Qno.5
import math
j,k,l=eval(input("Enter three sides of triangle(separated by commas) :"))
s=(j+k+l)/2
area=s*(s-j)*(s-k)*(s-l)
print(f"Thearea of entered triangle is: {math.sqrt(area)}")