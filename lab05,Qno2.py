#length cm to inches
cm=eval(input("Enter lenth(in centimeter):"))
inch=cm/2.54
if(cm>0):
    print(f'{cm} cm={inch} inches')
else:
    print("You entered invalid number")