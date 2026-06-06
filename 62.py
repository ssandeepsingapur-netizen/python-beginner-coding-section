import os
def show_file(folder):
    files = os.listdir(folder)
    for file in files:
        path = os.path.join(folder,file)
        if os.path.isdir(path):
            print("folder:",file)
            show_files(path)

        else:
            print("file :",file)

file_name = input("enter file name")
show_file(file_name)
