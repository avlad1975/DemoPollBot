import requests
from bs4 import BeautifulSoup
from constant import URL, HEADERS, s_money
import lxml


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):  # возвращает рандомное значение валюта - резюме из 12 валют на сайте
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('table', class_='closedTbl')
    rows = items.find_all('a', class_='arial_14 bold middle center')
    currency = []
    for row in rows:
        name = row.get_text()
        resume = row.parent.parent.findNextSibling('tr').findNextSibling('tr').findNext('td').findNext(
            'td').get_text().upper()
        row.parent.parent.findNextSibling('tr').findNextSibling('tr').findNext('td').findNext('td').get_text()
        if 'АКТИВНО' in resume:
            resume_2 = row.parent.parent.findNextSibling('tr').findNextSibling('tr').findNext('td').findNext(
                'td').findNext(
                'td').get_text().upper()
            if resume == resume_2:
                name_list = next((item for item in s_money if item["name"] == name), False)
                if name_list:
                    currency.append({
                        'name': name,
                        'resume': resume,
                    })

    print(currency)
    return currency


def get_price(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('table', class_='closedTbl')
    rows = items.find_all('a', class_='arial_14 bold middle center')
    currency = []
    for row in rows:
        name = row.get_text()
        resume = row.parent.parent.findNextSibling('tr').findNextSibling('tr').findNext('td').findNext('td').get_text()
        price = row.findNextSiblings('p')[0].get_text()
        price = price.replace(',', '.')
        try:
            price = float(price)
        except ValueError:
            print('Ошибка преобразования')

        name_list = next((item for item in s_money if item["name"] == name), False)
        if name_list:
            currency.append({
                'name': name,
                'resume': resume,
                'price': price
            })
    return currency


def parse(check):
    resume = ''
    html = get_html(URL)
    if html.status_code == 200:
        if check == 'name':
            resume = get_content(html.text)
        if check == 'price':
            resume = get_price(html.text)
    else:
        print('Ошибка доступа к сайту')
    return resume


if __name__ == '__main__':
    parse('name')
