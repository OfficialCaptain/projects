import os
def crawl():
    for folderName, subfolders, filenames in os.walk(input('Please enter a directory: ')):
        print("Folder: " + folderName)
        print("Subfolders in " + folderName + ' are: ' + str(subfolders))
        print("Files in " + folderName + ' are: ' + str(filenames))
        print()
print(crawl())
