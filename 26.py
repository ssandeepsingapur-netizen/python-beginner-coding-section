import datetime

now = datetime.datetime.now()
print(now)

if now.hour > 12:
    print("Good afternoon!")
elif 12<= now.hour < 18:
    print("Good evening!")
else:
    print("Good night!")