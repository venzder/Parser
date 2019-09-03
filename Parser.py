import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent



headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3',
           'user-agent': UserAgent().random}


def get_url_pages(start_url, headers):
    lst = []
    while True:
        try:
            session = requests.Session()
            request = session.get(url, headers=headers)
            soup = bs(request.content, 'lxml')
            url = f"https://realty.yandex.ru{soup.find('a', attrs={'class': 'Pager__radio-link'})['href']}"
            lst.append(url)
        except:
            break
    return lst



def get_hrefs(start_url, headers):
    all_hrefs = []
    url = start_url
    i = 0
    while True:
        session = requests.Session()
        session.proxies = proxies
        request = session.get(url, headers=headers)
        status_code = request.status_code
        if status_code == 200:
            soup = bs(request.content, 'lxml')
            divs = soup.find_all('li', attrs={'class': 'OffersSerpItem OffersSerpItem_view_desktop OffersSerpItem_format_full OffersSerp__list-item OffersSerp__list-item_type_offer'})
            hrefs = []
            for div in divs:
                href = div.find('a', attrs={'class': 'Link Link_js_inited Link_size_m Link_theme_islands SerpItemLink OffersSerpItem__link'})['href']
                hrefs.append({
                    'href': href
                })
            all_hrefs += hrefs
            if divs:
                url = f'{start_url}?page={i+1}'
            else:
                break
        else:
            print(f'Возникла ошибка {status_code}')
        i += 1


proxies = {'http': '144.217.163.138:8080'}

def get_all_hrefs(url, headers, proxies):
    session = requests.Session()
    session.proxies = proxies
    request = session.get(url, headers=headers)
    s = request.status_code
    soup = bs(request.content, 'lxml')
    divs = soup.find_all('li', attrs={'class': 'OffersSerpItem OffersSerpItem_view_desktop OffersSerpItem_format_full OffersSerp__list-item OffersSerp__list-item_type_offer'})

    print(s, divs)

# def get_cityes_yandex():



# def get_yandex_url(city, region, metro):
#
#
# def yandex_parser(yandex_url, headers):
#     session = requests.Session()
#     request = session.get(yandex_url, headers=headers)
#     if request.status_code == 200:
#         soup = bs(request.content, 'html.parser')
#         divs = soup.find_all('div', attrs={})



# print(get_all_hrefs('https://realty.yandex.ru/sankt-peterburg/kupit/kvartira/?page=0', headers))
print(get_all_hrefs('https://realty.yandex.ru/sankt-peterburg/kupit/kvartira/', headers, proxies))