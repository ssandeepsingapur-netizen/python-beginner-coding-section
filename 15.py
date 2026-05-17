import datetime
if datetime.datetime.now().hour < 12:
    print("more buses expected at this time ")
elif datetime.datetime.now().hour < 17:
    print("less busses expected at this time")
 
    