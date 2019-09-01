import requests
from bs4 import BeautifulSoup as bs


headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/76.0.3809.132 Safari/537.36'}


def get_hrefs(url, headers):
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('li', attrs={'class': 'OffersSerpItem OffersSerpItem_view_desktop OffersSerpItem_format_full OffersSerp__list-item OffersSerp__list-item_type_offer'})
        for div in divs:
            href = div.find('a', attrs={'class': 'Link Link_js_inited Link_size_m Link_theme_islands SerpItemLink OffersSerpItem__link'})['href']
            print(href)


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



get_hrefs('https://realty.yandex.ru/sankt-peterburg/kupit/kvartira/?page=0', headers)