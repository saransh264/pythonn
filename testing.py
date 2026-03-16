import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
if (int(timestamp)<12):
    print("Good Morning Sir")
elif ( int(timestamp)>=12 and int(timestamp)<= 16):
    print("Good Afternoon Sir")
else :                         
    print("Good Evening Sir")
    

#This program greets the user based on the current time of day in 24-hour format.