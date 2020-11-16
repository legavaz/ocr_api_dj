from api_ocr_app.ocr.ot_tools import request_api_1c
from django.db import models

def load_customers_from_1c():
    customers = request_api_1c('hs/Customer/all')

    models.Model.from_db()

    for item in customers:
        print(item)


# для целей тестирования
if __name__ == "__main__":
    load_customers_from_1c()
