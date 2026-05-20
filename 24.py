try:
    file = open("sample.txt" 'W')
    file.write("This is created file")
    file.close()
except FileNotFoundError:
    print("this not found check again created or not")
