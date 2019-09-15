import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import re


headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3',
           'user-agent': UserAgent().random}


def get_hrefs(start_url, headers, all_proxies):
    all_hrefs = []
    url = start_url
    i = 0
    while True:
        proxy = all_proxies[i]
        try:
            session = requests.Session()
            session.proxies = proxy
            request = session.get(url, headers=headers)
        except requests.exceptions.RequestException:
            request = False
        if request:
            response_url = request.url
            match = re.fullmatch('.+captcha.+', response_url)
            if match:
                print(f'Прокси с параметрами {proxy} заблокирован.')
            else:
                status_code = request.status_code
                if status_code == 200:
                    soup = bs(request.content, 'lxml')
                    divs = soup.find_all('li', attrs={'class': 'OffersSerpItem OffersSerpItem_view_desktop OffersSerpItem_format_full OffersSerp__list-item OffersSerp__list-item_type_offer'})
                    if divs:
                        hrefs = []
                        for div in divs:
                            href = div.find('a', attrs={'class': 'Link Link_js_inited Link_size_m Link_theme_islands SerpItemLink OffersSerpItem__link'})['href']
                            hrefs.append({
                                'href': href
                            })
                        all_hrefs += hrefs
                        url = f'{start_url}?page={i+1}'
                    else:
                        break
                else:
                    print(f'Возникла ошибка {status_code}')
        else:
            print(f'Соединение с прокси {proxy} невозможно')
        i += 1
    return all_hrefs

proxies = {'http': '144.217.163.138:8080'}

def get_all_hrefs(url, headers, proxies):
    session = requests.Session()
    session.proxies = proxies
    request = session.get(url, headers=headers)
    response_url = request.url
    s = request.status_code
    soup = bs(request.content, 'lxml')
    divs = soup.find_all('li', attrs={'class': 'OffersSerpItem OffersSerpItem_view_desktop OffersSerpItem_format_full OffersSerp__list-item OffersSerp__list-item_type_offer'})

    print(s, divs)
    print(response_url)




# print(get_all_hrefs('https://realty.yandex.ru/sankt-peterburg/kupit/kvartira/?page=0', headers))
print(get_all_hrefs('https://realty.yandex.ru/sankt-peterburg/kupit/kvartira/', headers, proxies))