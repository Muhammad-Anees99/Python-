u=eval(input("Enter units consumed:"))
if(u<=100):
    bill=13.85*u+0.1*u+0.43*u+35
    total=0.12*bill+bill
    bill2=0.1*total+total
if(u<=200 and u>100):
    bill=15.86*u+0.1*u+0.43*u+35
    total=0.12*bill+bill
    bill2=0.1*total+total
if(u<=300 and u>200):
    bill=16.83*u+0.1*u+0.43*u+35
    total=0.12*bill+bill
    bill2=0.1*total+total
if(u<=700 and u>300):
    bill=13.85*u+0.1*u+0.43*u+35
    total=0.12*bill+bill
    bill2=0.1*total+total
if(u>700):
    bill=20.94*u+0.1*u+0.43*u+35
    total=0.12*bill+bill
    bill2=0.1*total+total
print("Your payable before duedate:",total)
print("Your payable after duedate:",bill2)
