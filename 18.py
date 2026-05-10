try:
    file = open("sample.txt","r+")
    data = file.read()
    print(data)
except:
    print("file not found")