s=input("Enter your marital status (M/U):")
g=input("Enter your gender (M/F):")
age=eval(input("Enter your age:"))
if(s=='M'):
    print("Congratulations!")
    print("You are eligible for Insurance!")
else:
  if(g=='M'):
     if(age>30):
        print("Congratulations!")
        print("You are eligible for Insurance!")
     else:
            print("We are sorry!")
            print("You are not eligible for Insurance")
            if(age>25):
             print("Congratulations!")
             print("You are eligible for Insurance!")
            else:
              print("We are sorry!")
              print("You are not eligible for Insurance")