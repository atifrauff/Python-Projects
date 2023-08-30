# importing os module to access files in pc
import os

# making a class for accessing and renaming files in pc
class Files:
# method for showing files in pc
    def showFiles(self):
        files = os.listdir("Images Folder")
        for file in files:
            print(file)

# method for renaming files in pc
    def renameFiles(self):
        files = os.listdir("Images Folder")
        i = 1
        for file in files:
            if file.endswith(".jpeg"):
                os.rename(f"Images Folder/{file}",f"Images Folder/{i}.jpeg")
                i = i + 1  

# method for new renamed .jpeg files
    def newFiles(self):
        files = os.listdir("Images Folder")
        for file in files:
            if file.endswith(".jpeg"):
                print("The JPEG file:   ",file)

file = Files()
file.showFiles()
file.newFiles()
