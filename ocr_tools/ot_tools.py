import os
import requests, json


def get_files(m_DIR_NAME: str, ext=('pdf', 'jpg', 'png')):
    files = []
    with os.scandir(m_DIR_NAME) as listFiles:
        for file in listFiles:
            if os.path.isdir(file.path):
                m_files = get_files(file.path, ext)
                files = files + m_files
            else:
                if file.name[-3:] in ext:
                    files.append(file.path)
    return files



def mk_dir(m_path: str, current: True):
    """

    :param m_path: путь, директорория
    :param current: добавить относительный путь
    :return: Истина, Ложь
    """

    result = False

    if os.path.exists(m_path):
        result = True
    else:
        path = ''
        if current:
            path = os.getcwd()

        try:
            os.makedirs(path + m_path)
            result = True
        except OSError:
            print("Создать директорию %s не удалось" % m_path)

    return result


def post_obj(obj):
    url = 'http://127.0.0.1:8000/api/api/Source_table/'
    data_set = {'file_name_chr': obj.filename,
                'structure_txt': obj.textField,
                }

    resp = requests.post(url, data=data_set)
    print('api status:', resp)


class TestObj:
    filename = 'test1'
    textField = """
                test1, new text
                sdlfljlsdkfjsf
                adlfkajdsfasdlfkjaldfj
                lajdfaslkdfj
                """

def test_request():
    """
    Тестирование апи запросов на базе произвользого объекта
    :return:
    """
    a = TestObj
    post_obj(a)

def test_getFiles(dir_path: str):
    get_files(dir_path)

if __name__ == "__main__":
    print('sub function')
    m = get_files(r'\\l-pack\net\Сканер\1C\4825047455\30102020')
    print('Найдено:', len(m))

    # 02-11-2020
    # test_request()

