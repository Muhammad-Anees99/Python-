s=input("Enter your marital status (M/U):")
g=input("Enter your gender (M/F):")
age=eval(input("Enter your age:"))
if(s=='M' or s=='U'and g=='M'and age>30 or s=='U'and g=='F'and age>25):
    print("Congratulations!")
    print("You are eligible for Insurance!")
else:
    print("We are sorry!")
    print("You are not eligible for Insurance")