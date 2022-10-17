from zipfile import ZipFile
import os
import shutil
import csv
from PyPDF2 import PdfReader
import xlrd


zip_path = 'resources/file.zip'


def create_zip():
    newzip = ZipFile(os.path.abspath('file.zip'), "w")
    newzip.write('CSV.csv')
    newzip.write('PDF.pdf')
    newzip.write('XLS.xls')
    newzip.write('XLSX.xlsx')
    newzip.write('TXT.txt')
    newzip.write('donut.png')
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


def test_read_xls():
    xls_file = xlrd.open_workbook_xls('resources/XLS.xls')
    xls_sheet = xls_file.sheet_by_index(0)
    xls_cell_value = xls_sheet.cell_value(rowx=0, colx=1)
    xls_row_value = xls_sheet.row_values(rowx=1, start_colx=0)
    xls_column_value = xls_sheet.col_values(colx=1)
    print(xls_cell_value)
    print(xls_row_value)
    print(xls_column_value)
    assert xls_cell_value == 'First Name'
    assert xls_row_value == [1.0, 'Dulce', 'Abril', 'Female', 'United States', 32.0, '15/10/2017', 1562.0]
    assert xls_column_value == ['First Name', 'Dulce', 'Mara', 'Philip', 'Kathleen', 'Nereida', 'Gaston', 'Etta', 'Earlean', 'Vincenza']


def test_read_txt():
    with open('resources/TXT.txt') as txt_file:
        txt_data = txt_file.read()
        print(txt_data)
        assert 'Test tetete\n2nd row' in txt_data


def test_png_size():
    png_size = os.path.getsize('resources/donut.png')
    assert png_size == 50194


def test_clean_resources():
    shutil.rmtree('resources')



