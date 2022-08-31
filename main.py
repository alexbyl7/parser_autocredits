import parser
import excel

if __name__ == '__main__':
    headers = ['№', 'Банки', 'Наименование кредита', 'Процентная ставка', 'Срок кредита', 'Цель кредита']

    data = []

    # parser.parse_ipakyulibank()
    # parser.parse_kapital24()

    d = parser.parse_infinbank()
    for s in d:
        data.append(s)

    # print(data)

    excel.export_xls(headers, data)

