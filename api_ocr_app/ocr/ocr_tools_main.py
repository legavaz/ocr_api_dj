﻿import os
import subprocess
import tempfile
from pdf2image import convert_from_path
from api_ocr_app.ocr.ot_tools import get_files, mk_dir, post_obj,request_api_get


def return_name(file_name):
    f_n = 'file_name'
    arr_f_n = os.path.basename(file_name).split('.')
    if len(arr_f_n) > 0:
        f_n = arr_f_n[0]
        f_n = f_n.replace(' ', '_')
    return f_n


def png_to_txt(imagefile, path):
    if os.path.exists(imagefile):
        out_put = path + '\\' + return_name(imagefile)
        lang = '-l rus+eng'
        command = 'tesseract.exe {0} {1} {2}'.format(
            imagefile, out_put, lang)
        print('COMMAND: ', command)
        subprocess.call(command)


def read_txt(path: str):
    txt_files = get_files(path, ('txt',))
    text_from_file = ''
    for mfile in txt_files:
        print('чтение файла:', mfile)
        with open(mfile, encoding='utf-8') as txt_file:
            line_txt = txt_file.readlines()
            for line in line_txt:
                if len(line.strip()) > 0:
                    text_from_file = text_from_file + line

    return text_from_file


class OcrObj:
    """
    filename = Полное имя файла
    temp_path = Временная директория хранения файлов
    short = Короткое имя файла
    textField = Результат текст полученный из изображения
    del_path_half = Удалить часть пути из filename при передачи данных api

    создает объект
    Параметр (filename:string)
    На входе файл pdf, на выходе текстовый файл
    """

    def __init__(self, filename, temp_path,del_path_half=''):
        self.filename = filename
        self.temp_path = temp_path
        self.short = return_name(filename)

        # Проверка что запись существует в бд
        r_data = request_api_get(filtr_val=self.short)

        if len(r_data) == 0:
            self.textField = ''
            self.del_path_half = del_path_half
            self.ocr_post()
        else:
            print(self.short, 'существует')

    def ocr_post(self):
        """

        :return:
        """
        images = convert_from_path(self.filename)
        i = 0
        f_n = self.short
        path_pack = self.temp_path + '\\' + self.short
        if mk_dir(path_pack, False):
            for target_list in images:
                i = i+1
                f_name = path_pack + '\\' + f_n + '_{0}.png'.format(i)
                target_list.save(f_name)

                # анализ пакета файлов
                png_to_txt(f_name, path_pack)

            self.textField = read_txt(path_pack)
            post_obj(self)


def main_func():

    scan_path_dir = r'\\l-pack\net\Сканер\1C\4825047455\30102020'
    del_path_half = r"\\l-pack\net\Сканер"
    # temp_dir = r'D:\py\ocr_dj_api\project_api_ocr\ocr_tools\temp'
    files = get_files(scan_path_dir)
    print('найдено файлов для анализа:', len(files))
    for file in files:
        with tempfile.TemporaryDirectory() as temp_path:
            # print(temp_path)
            # воспользуемся временной папкой
            m = OcrObj(filename=file, temp_path=temp_path,del_path_half=del_path_half)

            # по старому
            # m = OcrObj(filename=file, temp_path=temp_dir)
            # print(m.textField)


def testing():
    print('+++')
    m = read_txt(r'D:\py\ocr_dj_api\project_api_ocr\ocr_tools\temp\doc02208820201026115605')
    print(m)


main_func()
