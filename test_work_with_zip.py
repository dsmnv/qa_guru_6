import zipfile
import os
import shutil


def test_create_zip():
    newzip = zipfile.ZipFile(os.path.abspath('file.zip'), "w")
    newzip.write('resources/CSV.csv')
    newzip.write('resources/JPEG.jpeg')
    newzip.write('resources/PDF.pdf')
    newzip.write('resources/XLS.xls')
    newzip.write('resources/XLSX.xlsx')


def test_move_zip_in_new_folder():
    file_path = "file.zip"
    destination_path = "resources"
    shutil.move(file_path, destination_path)


def test_remove_zip():
    os.remove('resources/file.zip')
