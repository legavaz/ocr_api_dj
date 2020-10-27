# ocr_api_dj
pip install pdf-tools

## API запросы:

## get (получить все записи)
http://127.0.0.1:8000/api/api/Source_table/

## post (добавить запись)
http://127.0.0.1:8000/api/api/Source_table/

Content-Type  - application/json
    {        
        "file_name_chr": "Привет"    
    }

## put  (изменить запись в строке добавить id)
http://127.0.0.1:8000/api/api/Source_table/5/
Content-Type  - application/json
    {        
        "file_name_chr": "Привет, мир"    
    }

## delete  (удалить запись в строке добавить id)
http://127.0.0.1:8000/api/api/Source_table/5/
Content-Type  - application/json
