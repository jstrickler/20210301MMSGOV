import os
import shutil
from shutil import copyfile

copyDir = "/home/kali/Desktop"
count = 0

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg"):
            shutil.copy(os.path.join(root, file), copyDir)
            count +=1
            
count = str(count)
print('A total of ' + count + ' images were found and placed in the directory ' + copyDir)
            
