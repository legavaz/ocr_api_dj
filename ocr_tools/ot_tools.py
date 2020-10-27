import os
import tempfile


def get_files(m_DIR_NAME, ext=('pdf,jpg,png')):
    files = []
    with os.scandir(m_DIR_NAME) as listFiles:
        for file in listFiles:
            if file.name[-3] in ext:
                files.append(file.path)
    return files


def mk_dir(m_path):
    
    # with tempfile.TemporaryDirectory() as directory:
    #     print('Создана временная директория %s' % directory)
    
    result = False
    path = os.getcwd()  
    try:
        os.makedirs(path+m_path)
        result = True
    except OSError:
        print("Создать директорию %s не удалось" % m_path)
    return result


if __name__ == "__main__":
    # DIR_NAME = r'\\l-pack\net\Сканер\Dergunov'
    # m = get_files(DIR_NAME)
    # print(m, len(m), 'файла')
    out_path 	= '\Temp\out'
    res = mk_dir(out_path)
