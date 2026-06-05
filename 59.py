import os
def show_files(Folder):
    files = os.listdir(Folder)
    for file in files:
        path = os.path.join(Folder, file)
        if os.path.isdir(path):
            print("Folder:",file)

            show_files(path)
        else:
            print("file:",file)

Folder_name = input("enter the folder path:")
show_files(Folder_name)
