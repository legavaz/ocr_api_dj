import os

def get_files(m_DIR_NAME,ext = ('pdf,jpg,png')):    
    files   =   []
    with os.scandir(m_DIR_NAME) as listFiles:
        for file in listFiles:
            if file.name[-3] in ext:                
                    files.append(file.path)
    return files


if __name__ == "__main__":    
    DIR_NAME = r'\\l-pack\net\Сканер\Dergunov'
    m = get_files(DIR_NAME)
    print(m,len(m),'файла')
    