import time
print("current time is :",time.ctime())
print("waiting for 2 seconds")
time.sleep(2)
print("Done")
print(time.strftime("%y:%m:%d:%h:%m:%s"))