import os
def crawl():
    for folderName, subfolders, filenames in os.walk('/home/lupus/Documents/Portfolio/projects/Odin'):
        print("Folder: " + folderName)
        print("Subfolders in " + folderName + ' are: ' + str(subfolders))
        print("Files in " + folderName + ' are: ' + str(filenames))
        print()
print(crawl())
