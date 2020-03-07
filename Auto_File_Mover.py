import os
import shutil
import fnmatch

WatchedFolder = 'D:/Downloads'

KeywordDef = {
    'Wallpaper': 'D:/Google Drive/Photos/Wallpapers',
    'specific video': 'D:/Google Drive/Video/VideoTest'
}

FileTypeDef = {
    '.docx': 'D:/Downloads/Documents',
    '.mp4': 'D:/Downloads/Video',
    '.png': 'D:/Downloads/Images',
    '.jpg': 'D:/Downloads/Images',
    '.txt': 'D:/Downloads/Documents',
    '.exe': 'D:/Downloads/Installers'
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
                for keyword in KeywordDef:
                    if fnmatch.fnmatch(File, '*' + keyword + '*'):
                        print(keyword + ' Found named ' + File)
                        FileMove(File, KeywordDef[keyword])
                    else:
                        print('Specific ' + FileType + ' not found. Moving file named ' + File + ' to default folder.')
                        FileMove(File, FileTypeDef[FileType])


MoveByName(WatchedFolder)

print('Finished File check of ' + WatchedFolder + '.')
