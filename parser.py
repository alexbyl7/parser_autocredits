import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import csv

def get_html_requests(url):
     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
     r = requests.get(url)
     return r.text

def get_html_webdriver(url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    driver.close()
    return html

def parse_ipakyulibank():
    print("Parse Ipakyuli Bank")

    # url = 'https://kapital24.uz/ru/crediting/udobnoe-avto-udobnaya-karta/'
    # url = 'https://kapital24.uz/ru/crediting/calc_auto.php?MODEL=&dev=&CALC_TYPE=CALC&LOAN_AMOUNT=133%2C288%2C572&LOAN_AMOUNT_RANGE=133%2C288%2C572&LOAN_LENGTH=36&LOAN_LENGTH_RANGE=36&LOAN_PERCENT=24.00&lang=ru&one=1&percent=1&collateralTypeId=1'
    url = 'https://ru.ipakyulibank.uz/physical/kredity/avtokredit/spark'

    html = get_html_webdriver(url)
    soup = BeautifulSoup(html, 'html.parser')

    res = soup.find_all(class_='flex lg4 xs12')
    # print(res)
    # exit()

    for i in range(len(res)):
        s = res[i].getText()
        if s.find('ПРОЦЕНТНАЯ СТАВКА') > 0:
            print(s)
        if s.find('СРОК') > 0:
            print(s)

def parse_kapital24():
    print("Parse Kapital24 Bank")

    url = 'https://kapital24.uz/ru/crediting/udobnoe-avto-udobnaya-karta/'
    # url = 'https://kapital24.uz/ru/crediting/calc_auto.php?MODEL=&dev=&CALC_TYPE=CALC&LOAN_AMOUNT=133%2C288%2C572&LOAN_AMOUNT_RANGE=133%2C288%2C572&LOAN_LENGTH=36&LOAN_LENGTH_RANGE=36&LOAN_PERCENT=24.00&lang=ru&one=1&percent=1&collateralTypeId=1'

    # driver = webdriver.Firefox()
    # driver.get(url)
    # # TODO: выставить параметры через драйвер
    # time.sleep(1)
    # html = driver.page_source
    # driver.close()

    html = get_html_webdriver(url)
    soup = BeautifulSoup(html, 'html.parser')

    res = soup.find_all('div')
    # print(res)

    for i in range(len(res)):
        s = res[i].getText()
        if s.find('процент') > 0:
            print(s)
        if s.find('срок') > 0:
            print(s)

def parse_infinbank():
    print('Парсим сайт Infinbank...', '\n')

    url = 'https://www.infinbank.com/ru/private/credits/'

    html = get_html_webdriver(url)
    soup = BeautifulSoup(html, 'html.parser')

    r = 0
    f = open('./data.csv', 'w', encoding='cp1251')
    writer = csv.writer(f)
    header = ['№', 'Банки', 'Наименование кредита', 'Процентная ставка', 'Срок кредита', 'Цель кредита']
    writer.writerow(header)

    conts = soup.find_all('div', class_='g-container')

    for c in conts:
        title = c.find('a', class_='news-preview__link plastic-in-content__link dlink')
        if title is not None:
            percent = ''
            term = ''
            print(title.text)
            desc = c.find_all('b', class_='owner-list__title')
            value = c.find_all('p', class_='owner-list__text')
            for i in range(len(desc)):
                print(desc[i].text, ': ', value[i].text)
                if desc[i].text.find('Процентная ставка') >= 0:
                    percent = value[i].text;
                if desc[i].text.find('Срок кредита') >= 0:
                    term = value[i].text;

            data = [1, 'Infinbank', title.text, percent, term, '']
            writer.writerow(data)

            print()

    # close the file
    f.close()



    # res1=driver.get(url)
    # button = driver.find_element_by_class_name("slide-out-btn")
    # button.click()

    # print(res1)

    # html = get_html(url)
    # price = get_elements(html, 'div', 'catalog-product-min-price__current')
    # caption = get_elements(html, 'div', 'catalog-product__rating')

    # res = get_elements(html, 'input', 'form-control input-lg')
    # res = get_elements(html, 'row', 'form-group form-group-lg')

    # print(html)

    # soup = BeautifulSoup(html, 'html.parser')
    # # res = soup.find_all('div', class_=class_name)
    # # res = soup.find_all('div', '')
    # # for link in soup.find_all('p'):
    # #     print(link)
    #
    # res = soup.find_all(class_='flex lg4 xs12');
    #
    # print(soup.find_all(class_='flex lg4 xs12'))
    #
    # for i in range(len(res)):
    #     if res[i].get("name") == "LOAN_PERCENT":
    #         percent = res[i].get("value")
    #
    # exit()
    #
    # percent = 0;
    # length = 0;
    #
    # for i in range(len(res)):
    #     if res[i].get("name") == "LOAN_PERCENT":
    #         percent = res[i].get("value")
    #     if res[i].get("name") == "LOAN_LENGTH":
    #         length = res[i].get("value")
    #
    # # percent = res[4].get('value')
    # #.value("LOAN_PERCENT")
    # # index("LOAN_PERCENT")
    # print(html)
    # print("Res =", res)
    # print("Percent = ", percent)
    # print("Length = ", length)
