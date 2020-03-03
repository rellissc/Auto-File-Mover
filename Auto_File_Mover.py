import os
import shutil
import fnmatch

WatchedFolder = 'D:/Downloads'

FileTypeDefaults = {'.mp4': 'Insert Directory Here', '.png': 'Insert Directory Here', '.jpg': 'Insert Directory Here'}


def MoveByName():
    for File in os.listdir(WatchedFolder):
        if File.endswith(".mp4"):
            print("MP4 Found")
            if fnmatch.fnmatch(File, '*Test*'):
                print('Video Found named ' + File)
                shutil.move(WatchedFolder + '/' + File, "E:/Game install files/Valve/temporary/VR/New")
                print('Copied to Folder' + File)
            else:
                print('Specific .mp4 not found. Moving file named ' + File + ' to default folder.')
                shutil.move(WatchedFolder + '/' + File, "E:/Game install files/Valve/temporary")
                print('Copied to Folder')
        elif File.endswith(".png"):
            print("PNG Found")
        elif File.endswith(".jpg"):
            print("jpg Found")


MoveByName()

print('Finished File check of ' + WatchedFolder)
