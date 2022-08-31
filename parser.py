
import html_loader


def parse_ipakyulibank():
    print("Parse Ipakyuli Bank")

    # url = 'https://kapital24.uz/ru/crediting/udobnoe-avto-udobnaya-karta/'
    # url = 'https://kapital24.uz/ru/crediting/calc_auto.php?MODEL=&dev=&CALC_TYPE=CALC&LOAN_AMOUNT=133%2C288%2C572&LOAN_AMOUNT_RANGE=133%2C288%2C572&LOAN_LENGTH=36&LOAN_LENGTH_RANGE=36&LOAN_PERCENT=24.00&lang=ru&one=1&percent=1&collateralTypeId=1'
    url = 'https://ru.ipakyulibank.uz/physical/kredity/avtokredit/spark'

    soup = html_loader.get_soup(url)

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
    soup = html_loader.get_soup(url)

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
    soup = html_loader.get_soup(url)

    cont = soup.find_all('div', class_='g-container')

    idx = 1
    data = []

    for c in cont:
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

            s = [idx, 'Infinbank', title.text, percent, term, ' - ']
            data.append(s)

            idx += 1
            print()

    return data
