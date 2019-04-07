#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a zip file whose filename increments

#from zipfile import ZipFile
import zipfile, os

def backupToZip(folder):
    #Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on files
    # already exists

    number = 1
    while True:
        #basename returns the tail of the path
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    #if line 5 not commented, do 27 instead of 28
    # backupZip = ZipFile(zipFilename, 'w')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the ZIP files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')

backupToZip('/mnt/c/Users/vicas/Documents/Universidad/Recursos Python/Ejercicios Libro/Chapter09')
