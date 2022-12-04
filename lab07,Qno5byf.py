
def elecbill(u):
    'elec bill calculator'
u=eval(input("Enter units consumed>>"))
if(u<=100):
    up=13.85
if(u<=200 and u>100):
    up=15.86
if(u<=300 and u>200):
    up=16.83
if(u<=700 and u>300):
    up=18.54
if(u>700):
    up=20.94
elecbill(u)
up=13.85 and 15.86 and 16.83 and 18.54 and 20.94
bill=up*u+0.1*u+0.43*u+35
total=0.12*bill+bill
bill2=0.1*total+total
print("Your payable before duedate:",total)
print("Your payable after duedate:",bill2)


