import sys,os
import subprocess
from pdf2image import convert_from_path
from .ot_tools import get_files

# Для Windows
def return_name(file_name):
    f_n =   'file_name'
    arr_f_n =   os.path.basename(file_name).split('.')
    if len(arr_f_n)>0:
        f_n =   arr_f_n[0]
        f_n =   f_n.replace(' ','_')

    return f_n

def png_to_txt(file_name,path):
    out_put = path+'\\'+return_name(file_name)
    lang = '-l rus+eng'
    command = 'tesseract.exe {0} {1} {2}'.format(file_name, out_put, lang)
    print('COMMAND: ', command)
    subprocess.call(command)


def ocr(filename, path):
    images = convert_from_path(filename)
    i = 0
    f_n = return_name(filename)
    for target_list in images:
        i = i+1
        f_name = path+'\\'+f_n+'_{0}.png'.format(i)
        target_list.save(f_name)
        png_to_txt(f_name,path)


# main
# file_in 	= r'C:\Users\dvi\Desktop\Договор ФА000134 от 08.05.2020.pdf'
# out_path 	= '\Temp\out'
    
DIR_NAME = r'\\l-pack\net\Сканер\Dergunov'
m = get_files(DIR_NAME)
print(m)

# print(return_name(file_in))

# ocr(file_in, out_path)

