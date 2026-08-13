import os

folders = input("Please provide list of folders names with spaces in between :").split()

for folder in folders:

     try:
        files = os.listdir(folder)
     except  FileNotFoundError: 
        print("Please provide a valid folder name, looks like thi folder does not exist: " + folder)
        break
     except PermissionError:
        break 
        print("No access to this folder :" + folder)

        print("==== listing files for the folder - " + folder)


     for file in files:
       print(file)


