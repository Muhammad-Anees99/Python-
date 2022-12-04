a=eval(input("Enter first number:"))
print("___________________")
b=eval(input("Enter second number:"))
print("___________________")
c=eval(input("Enter third number:"))
print("___________________")
if(a>=c):
    if(a>=b):
       greatest=a
    else:
       greatest=b
if(c>=a):
    if(c>=b):
        greatest=c
    else:
        greatest=b
print(str(greatest)+' is greatest!')