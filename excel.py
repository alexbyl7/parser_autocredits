import csv
import xlwt
from xlwt import Workbook


def export_xls(headers, data):
    wb = Workbook(encoding='cp1251')

    sheet = wb.add_sheet('Лист 1', cell_overwrite_ok=True)
    sheet.col(0).width = 1000
    sheet.col(1).width = 5000
    sheet.col(2).width = 15000
    sheet.col(3).width = 15000
    sheet.col(4).width = 10000
    sheet.col(5).width = 5000

    style_bold = xlwt.easyxf('font: bold 1')

    for с, d in enumerate(headers):
        sheet.write(0, с, d, style_bold)

    for r, s in enumerate(data):
        for col, d in enumerate(s):
            row = r+1
            sheet.write(row, col, d)

            eol_count = str(d).count('\n')
            if eol_count > 0:
                sheet.row(row).height_mismatch = True
                sheet.row(row).height = sheet.row(row).height * (eol_count + 1)

    wb.save('data.xls')


def export_csv(headers, data):
    f = open('./data.csv', 'w', encoding='cp1251')
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

    # close the file
    f.close()
