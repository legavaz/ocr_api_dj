import sys
import os
import subprocess
import tempfile
from pdf2image import convert_from_path
from ot_tools import get_files, mk_dir


class ocr_obj():
    """
    Объект файл 
    обработка объекта
    """

    def return_name(self, file_name):
        f_n = 'file_name'
        arr_f_n = os.path.basename(file_name).split('.')
        if len(arr_f_n) > 0:
            f_n = arr_f_n[0]
            f_n = f_n.replace(' ', '_')
        return f_n

    def __init__(self, filename):
        self.filename = filename
        self.short = self.return_name(filename)

    def png_to_txt(self, imagefile,path):
        out_put = path+'\\'+self.return_name(imagefile)
        lang = '-l rus+eng'
        command = 'tesseract.exe {0} {1} {2}'.format(
            imagefile, out_put, lang)
        print('COMMAND: ', command)
        subprocess.call(command)

    def ocr(self, path):
        images = convert_from_path(self.filename)
        i = 0
        f_n = self.short

        for target_list in images:
            i = i+1
            f_name = path+'\\'+f_n+'_{0}.png'.format(i)
            target_list.save(f_name)
            self.png_to_txt(f_name, path)



DIR_NAME = r'\\l-pack\net\Сканер\OFF2-Programmisty'
files = get_files(DIR_NAME)
temp_dir    =   'temp'
mk_dir(temp_dir)
for file in files:
    with tempfile.TemporaryDirectory() as temp_path:
        print(temp_path)
        m = ocr_obj(file)
        # m.ocr(temp_path)
        m.ocr(temp_dir)
        


# ocr(file_in, out_path)
