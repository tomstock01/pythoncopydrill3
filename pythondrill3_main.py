# Python Version: 2.7.12
# Author: Tom Stock
# Python Drill 3, moving files based on date modified

import os
import time
import shutil


now = time.time()  # gets current time
docs = os.listdir(r'C:\Users\thoma\Desktop\folderc') # searches source folder for documents in it
for i in range(len(docs)):
    x = docs[i]
    y = 'C:\\Users\\thoma\\Desktop\\folderc\\' + x # gets complete file path from the folder with the documents
    modtime = os.stat(y).st_mtime # reads the last modified date of each file
    past24 = (now - 86400)  # gets the time of 24 hours ago
    if modtime > past24:  # compares the last modified time vs 24 hours ago
        shutil.copy(y, 'C:\\Users\\thoma\\Desktop\\folderd') # moves file that were modified within last 24 hours
        print y





