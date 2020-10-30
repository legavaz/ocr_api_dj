import os
import requests, json


def get_files(m_DIR_NAME: str, ext=('pdf', 'jpg', 'png')):
    files = []
    with os.scandir(m_DIR_NAME) as listFiles:
        for file in listFiles:
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
    data_set = {'file_name_chr': obj.short,
                'structure_txt': 'произвольное предложение',
                }

    dj = json.load(data_set)

    # resp = requests.post(url, json=)
    # print('api status:', resp)

if __name__ == "__main__":
    print('sub function')
