import os

#specify the directory you want to list
directory_path = '/path/to/directory'

#list all files and directories in the specified directory
contents = os.listdir(directory_path)

#print each files and directory name
for item in contents:
    print(item)