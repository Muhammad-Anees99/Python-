s1,s2,s3,s4,s5=eval(input("Enter marks in five subjects:"))
avg=(s1+s2+s3+s4+s5)/5
if(avg>=80):
    print("Your marks are outstanding")
if(avg>=70 and avg<=80):
    print("Your marks are good")
if(avg>=60 and avg<=70):
    print("Your marks are Average")
if(avg<=50):
    print("Your are below average!")
