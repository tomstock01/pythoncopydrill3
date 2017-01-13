# Python Version: 2.7.12
# Author: Tom Stock
# Python Drill 3, moving files based on date modified

import os
import time
import shutil


def filecopy(src, dst):
    now = time.time()  # gets current time
    docs = os.listdir(src) # searches source folder for documents in it
    for i in docs:
        y = src + '\\' + i # gets complete file path from the folder with the documents
        modtime = os.stat(y).st_mtime # reads the last modified date of each file
        past24 = (now - 86400)  # gets the time of 24 hours ago
        if modtime > past24:  # compares the last modified time vs 24 hours ago
            shutil.copy(y, dst) # copies file that were modified within last 24 hours
            print y


def main():
    fromFolder = 'C:\\Users\\thoma\\Desktop\\folderc'
    toFolder = 'C:\\Users\\thoma\\Desktop\\folderd'
    filecopy(fromFolder, toFolder)

if __name__ == "__main__":
    main()
