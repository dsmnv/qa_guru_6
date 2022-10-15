from zipfile import ZipFile

zip = ZipFile('resources.zip')
print(zip.namelist())