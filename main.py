import requests
from bs4 import BeautifulSoup as Bs
from fake_headers import Headers


def scrapping(lst_keywords):
    url = 'https://habr.com/ru/all/'
    headers = Headers(os='win', headers=True).generate()
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('Ошибка')
    else:
        soup = Bs(response.text, features='html.parser')
        result = soup.findAll('article')
        for el in result:
            title = el.find('h2').text
            el_text = el.find('div', class_='tm-article-body tm-article-snippet__lead').text
            date = el.find('time')['title']
            link = "https://habr.com" + el.find('a', class_='tm-article-snippet__title-link').get('href')
            hubs = el.find('div', class_='tm-article-snippet__hubs').text
            for item in lst_keywords:
                if item in title.lower() or item in el_text.lower() or item in hubs.lower():
                    print(f'{date} - {title} - {link}')


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    scrapping(KEYWORDS)