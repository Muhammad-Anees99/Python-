# check if numbers are closed
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
if(x-y<=10 and y-x<=10):
    print(f'{x} and {y} are closed!')
else:
    print("Entered numbers are not closed")