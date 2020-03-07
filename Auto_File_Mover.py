import os
import shutil
import fnmatch

WatchedFolder = 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir'


KeywordDef = {
    'Wallpaper': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Wallpapers',
    'specific video': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Video/VideoTest'
}

FileTypeDef = {
    '.docx': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Documents',
    '.mp4': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Video',
    '.png': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Images',
    '.jpg': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Images',
    '.txt': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Documents',
    '.exe': 'C:/Users/relli/Documents/PythonScripts/Auto-File-Mover/testDir/Installers'
}


def FileMove(Target, Dest):
    if os.path.isdir(Dest) is True:
        pass
    else:
        os.mkdir(Dest)
    shutil.move(WatchedFolder + '/' + Target, Dest)
    print('Move Complete.')


#  todo reincorporate into MoveByName Function.
def FileDelete(Target, Type):
    print('Found an ' + Type + ' named ' + Target + '.')
    InstallerDelResp = input('Do you want to delete it?')
    if InstallerDelResp == 'yes' or InstallerDelResp == 'y':
        os.remove(WatchedFolder + '/' + Target)
        print('Deleted File.')
    else:
        print('Ok, copying ' + Target + 'to the ' + Type + ' default folder.')
        shutil.move(WatchedFolder + '/' + Target, FileTypeDef[Type])


def MoveByName(TargetDir):
    for File in os.listdir(TargetDir):
        for FileType in FileTypeDef:
            if File.endswith(FileType):
                print(File + " Found.")
                messageText='Specific ' + FileType + ' not found. Moving file named ' + File + ' to default folder.'
                destinationText=FileTypeDef[FileType]
                for keyword in KeywordDef:
                    if fnmatch.fnmatch(File, '*' + keyword + '*'):
                        messageText=keyword + ' Found named ' + File
                        destinationText=KeywordDef[keyword]
                print(messageText)
                FileMove(File,destinationText)
            else:
                print("No match")


MoveByName(WatchedFolder)

print('Finished File check of ' + WatchedFolder + '.')
