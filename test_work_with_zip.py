from zipfile import ZipFile
import os
import shutil
import csv
from PyPDF2 import PdfReader


zip_path = 'resources/file.zip'


def create_zip():
    newzip = ZipFile(os.path.abspath('file.zip'), "w")
    newzip.write('CSV.csv')
    newzip.write('PDF.pdf')
    newzip.write('XLS.xls')
    newzip.write('XLSX.xlsx')
    newzip.close()


def move_zip_in_new_folder():
    file_path = "file.zip"
    destination_path = "resources"
    os.mkdir('resources')
    shutil.move(file_path, destination_path)


def extract_zip():
    with ZipFile(zip_path) as zip_file:
        print(zip_file.namelist())
        zip_file.extractall('resources')


create_zip()
move_zip_in_new_folder()
extract_zip()


def test_read_csv():
    with open('resources/CSV.csv') as csv_file:
        data = ''
        table = csv.reader(csv_file)
        for line_number, line in enumerate(table, 1):
            if line_number == 3:
                data = str(line)
        print(data)
        assert ("['2;Dima;dima@gmail.com']") == data



def test_read_pdf():
    pdf_file = 'resources/PDF.pdf'
    pdf_file_data = PdfReader(pdf_file)
    page = pdf_file_data.pages[0]
    text = page.extract_text()
    print(text)
    assert 'Пример PDF файла' in text


def test_clean_resources():
    shutil.rmtree('resources')


