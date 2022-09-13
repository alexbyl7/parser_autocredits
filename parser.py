import html_loader
import re

idx = 1

def parse_ipakyulibank():
    bank = "Ipakyuli Bank"
    print("Парсим сайт " + bank + "...\n")

    url = 'https://ru.ipakyulibank.uz/physical/kredity/avtokredit'

    soup = html_loader.get_soup(url)

    res = soup.find_all(class_='flex carloan lg12')

    data = []
    global idx

    for r in res:
        title = r.find('h3')
        if title is not None:
            percent = ''
            term = ''
            print(title.text)
            a = [d for d in r.find_all('div') if not d.find('div')]
            # s = r.find('div', class_='flex subheading my-3 xs12 md6')
            for b in a:
                if b.text.find('Процентная ставка') > 0:
                    percent = b.find('b').text
                    print(percent)
                if b.text.find('Срок кредита') > 0:
                    term = b.find('b').text
                    print(term)

            s = [idx, bank, title.text, percent, term, ' - ']
            data.append(s)

            idx += 1
            print()

    data.append(['', '', '', '', '', ''])

    return data


def parse_kapital24():
    bank = "Kapital24 Bank"
    print("Парсим сайт " + bank + "...\n")

    url = 'https://kapital24.uz/ru/crediting/'
    soup = html_loader.get_soup(url)

    res = soup.find_all(class_='desc')

    data = []
    global idx

    for r in res:
        title = r.find('h3')
        if title is not None:
            percent = ''
            term = ''
            print(title.text)
            a = r.find_all('div', class_='item-prop')
            for c in a:
                b = c.find('b')
                span = c.find('span')
                if b:
                    if b.text.find('Ставка') >= 0:
                        percent = span.text
                        print(percent)
                    if b.text.find('Срок') >= 0:
                        term = span.text
                        print(term)

            s = [idx, bank, title.text, percent, term, ' - ']
            data.append(s)

            idx += 1
            print()

    data.append(['', '', '', '', '', ''])

    return data

def parse_infinbank():
    bank = "Infin Bank"
    print("Парсим сайт " + bank + "...\n")

    url = 'https://www.infinbank.com/ru/private/credits/'
    soup = html_loader.get_soup(url)

    cont = soup.find_all('div', class_='g-container')

    data = []
    global idx

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

            s = [idx, bank, title.text, percent, term, ' - ']
            data.append(s)

            idx += 1
            print()

    data.append(['', '', '', '', '', ''])

    return data

def parse_sqb():
    bank = "SQB Bank"
    print("Парсим сайт " + bank + "...\n")

    print("Парсим список кредитов с главной страницы")
    url_main = "https://sqb.uz"
    url_credits = url_main + "/individuals/credits/"
    url_list = []
    soup = html_loader.get_soup(url_credits)
    res = soup.find_all('a', class_='kmaStylesSqbNewCredits__readMorebtn')
    for r in res:
        ref = r.get('href')
        if len(ref) > 0:
            url_list.append(url_main + ref)

    print("Список страниц: ", *url_list, sep="\n")

    data = []
    global idx

    for url_idx in range(len(url_list)):
        url = url_list[url_idx]
        print("Страница ", url_idx+1, " из ", len(url_list))

        soup = html_loader.get_soup(url)
        res = soup.find_all('div', class_='credit_data_inner')

        for c in res:
            title = c.find('h1')
            if title is not None:
                print(title.text)
                percent = ''
                term = ''
                a = c.find_all('div', class_='kmaStylesSqbNewCredits__TopInfoDescItem')
                for b in a:
                    desc = b.find('div', class_='kmaStylesSqbNewCredits__TopInfoDescSubTitle').text.lower()
                    value = b.find('div', class_='kmaStylesSqbNewCredits__TopInfoDescTitle')
                    if desc.find('ставка') >= 0 or desc.find('годовых') >= 0:
                        percent = value.text
                        print(percent)
                    if desc.find('срок') >= 0 or desc.find('погашение') >= 0 or desc.find('использования') >= 0:
                        term = value.text
                        print(term)

                s = [idx, bank, title.text, percent, term, ' - ']
                data.append(s)

                idx += 1
                print()

    data.append(['', '', '', '', '', ''])

    return data

def parse_tengebank():
    bank = "Tenge Bank"
    print("Парсим сайт " + bank + "...\n")

    print("Парсим список кредитов с главной страницы")
    url = 'https://tengebank.uz/ru/credits/avtocredit'
    soup = html_loader.get_soup(url)

    res_main = soup.find_all('div', class_='card__content_wrap')

    data = []
    global idx

    for r_main in res_main:
        title = r_main.find(class_='card__title')
        if title is not None:
            ref = title.get('href')

            soup = html_loader.get_soup(ref)
            res = soup.find_all('tr')

            percent = ''
            term = ''

            for r in res:
                a = r.find_all('td')
                if len(a) == 2:
                    if a[0].text.find("Ставка") >= 0 > a[0].text.find("долг"):
                        percent = re.sub(r"[\t]*", "", a[1].text)
                        while percent[-1] == '\n':
                            percent = percent[:-1]
                        print(percent)
                    if a[0].text.find("Срок") >= 0:
                        term = a[1].text
                        print(term)

            s = [idx, bank, title.text, percent, term, ' - ']
            data.append(s)

            idx += 1
            print()

    data.append(['', '', '', '', '', ''])

    return data