hrs=eval(input("Enter hours(Between 1 and 12):"))
d=eval(input("Enter am or pm:"))
if(d=='am'):
    print(f'{hrs} : 00 {d}')
else:
    forpm=12+hrs
    print(f'{forpm} : 00 {d}')