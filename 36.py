import os
def show_files(folder):
    files = os.listdir(folder)
    for file in files:
        path = os.path.join(folder,file)
        if os.path.isdir(path):
            print("Folder:",file)
            show_files(path)
        else:
            print("file:",file)


folder_name = input("Enter the folder name:")
show_files(folder_name)
