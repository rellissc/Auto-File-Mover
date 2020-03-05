import os
import shutil
import fnmatch

WatchedFolder = 'D:/Downloads'

Settings = {
    'Monitor Resolution': '2560, 1440'
}

PathDef = {
    'Wallpapers': 'D:/Google Drive/Photos/Wallpapers'
}

FileDef = {
    '.mp4': 'D:/Downloads/Video',
    '.png': 'D:/Downloads/Images',
    '.jpg': 'D:/Downloads/Images',
    '.exe': 'D:/Downloads/Installers'
}


def FileMove(Target, Dest):
    shutil.move(WatchedFolder + '/' + Target, Dest)
    print('Copied to Folder')


def FileDelete(Target, Type):
    print('Found an ' + Type + ' named ' + Target + '.')
    InstallerDelResp = input('Do you want to delete it?')
    if InstallerDelResp == 'yes' or InstallerDelResp == 'y':
        os.remove(WatchedFolder + '/' + Target)
        print('Deleted File')
    else:
        print('Ok, copying ' + Target + 'to the ' + Type + ' default folder.')
        shutil.move(WatchedFolder + '/' + Target, FileDef[Type])


def MoveByName():
    for File in os.listdir(WatchedFolder):
        # MP4 Checker
        if File.endswith(".mp4"):
            print("MP4 Found")
            if fnmatch.fnmatch(File, '*Test*'):
                print('Test Example Found named ' + File)
                FileMove(File, FileDef['.mp4'])
            else:
                print('Specific .mp4 not found. Moving file named ' + File + ' to default folder.')
                FileMove(File, FileDef['.mp4'])
        # .png Checker
        elif File.endswith(".png"):
            print("PNG Found")
            FileMove(File, FileDef['.png'])
        # .jpg Checker
        elif File.endswith(".jpg"):
            print("jpg Found")
            FileMove(File, FileDef['.jpg'])
        # Installer/.exe Checker
        elif File.endswith(".exe"):
            FileDelete(File, '.exe')


MoveByName()

print('Finished File check of ' + WatchedFolder)
