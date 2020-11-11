import os
import requests


def analiz_func(name_vol, volume):
    print(name_vol, volume, type(volume))


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
    url = 'http://127.0.0.1:8000/api/file_add/'

    if obj.del_path_half == '':
        data_set = {"file": obj.filename, "source": obj.textField, "short": obj.short}
    else:
        data_set = {"file": obj.filename.replace(obj.del_path_half, ''), "source": obj.textField, "short": obj.short}

    resp = requests.post(url, data=data_set)
    print('api status:', resp)


class TestObj:
    filename = r'\\l-pack\net\Сканер\1C\4825047455\30102020\5047106900\doc02733320201030114838.pdf'
    short = 'short_name'
    del_path_half = r'\\l-pack\net\Сканер\1C'

    textField = """Прежде всего, внедрение современных методик однозначно определяет каждого участника как способного 
    принимать собственные решения касаемо анализа существующих паттернов поведения. А ещё элементы политического 
    процесса представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть смешаны с 
    не уникальными данными до степени совершенной неузнаваемости, из-за чего возрастает их статус бесполезности. С 
    учётом сложившейся международной обстановки, базовый вектор развития в значительной степени обусловливает 
    важность благоприятных перспектив. """


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
    # m = get_files(r'\\l-pack\net\Сканер\1C\4825047455\30102020')
    # print('Найдено:', len(m))

    # 02-11-2020
    test_request()
