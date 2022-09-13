import parser
import excel
from datetime import datetime

if __name__ == '__main__':
    start_time = datetime.now()

    headers = ['№', 'Банки', 'Наименование кредита', 'Процентная ставка', 'Срок кредита', 'Цель кредита']

    data = []

    data = data + parser.parse_ipakyulibank()
    data = data + parser.parse_infinbank()
    data = data + parser.parse_kapital24()
    data = data + parser.parse_sqb()
    data = data + parser.parse_tengebank()

    excel.export_xls(headers, data)

    total_time = datetime.now() - start_time
    total_sec = str(total_time.total_seconds()).split('.')[0]
    print("Время выполнения: ", total_sec, ' сек')
