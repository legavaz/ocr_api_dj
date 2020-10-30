import os
import subprocess
import tempfile
from pdf2image import convert_from_path
from ocr_tools.ot_tools import get_files, mk_dir


def return_name(file_name):
    f_n = 'file_name'
    arr_f_n = os.path.basename(file_name).split('.')
    if len(arr_f_n) > 0:
        f_n = arr_f_n[0]
        f_n = f_n.replace(' ', '_')
    return f_n


def png_to_txt(imagefile, path):
    out_put = path + '\\' + return_name(imagefile)
    lang = '-l rus+eng'
    command = 'tesseract.exe {0} {1} {2}'.format(
        imagefile, out_put, lang)
    print('COMMAND: ', command)
    subprocess.call(command)


class OcrObj:
    """
    создает объект
    Параметр (filename:string)
    На входе файл pdf, на выходе текстовый файл
    """

    def __init__(self, filename):
        self.filename = filename
        self.short = return_name(filename)

    def ocr(self, path):
        images = convert_from_path(self.filename)
        i = 0
        f_n = self.short

        for target_list in images:
            i = i + 1
            f_name = path + '\\' + f_n + '_{0}.png'.format(i)
            target_list.save(f_name)
            png_to_txt(f_name, path)


DIR_NAME = r'\\l-pack\net\Сканер\OFF2-13 IT1C\Baldina'
files = get_files(DIR_NAME)
temp_dir = r'\temp'
mk_dir(temp_dir)
for file in files:
    with tempfile.TemporaryDirectory() as temp_path:
        # print(temp_path)
        m = OcrObj(file)
        # m.ocr(temp_path)
        m.ocr(temp_dir)

# ocr(file_in, out_path)
