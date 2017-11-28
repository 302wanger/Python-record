import os

for floderName, subfolders, filename in os.walk('Automate-The-Boring-Stuff-With-Python'):
    print('The current folder is  ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE   ' + folderName + ': ' + filename)

        print('')
