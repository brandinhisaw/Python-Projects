import os
import time

currentDirectory = os.getcwd()

dirList = os.listdir()

for file in dirList:
    if file.endswith('.txt'):
        modifiedTime = os.path.getmtime(file)
        print(time.ctime(modifiedTime))
        print(os.path.join(currentDirectory, file))
