import requests
from bs4 import BeautifulSoup
from time import sleep
from multiprocessing import Pool


def get_listing(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    html = None
    links = None

    r = requests.get(url, headers=headers, timeout=10)

    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        listing_section = soup.select('article > div > header > h3 > a' )
        links = [link['href'].strip() for link in listing_section]
    return links

    # parse a single item to get information


def parse(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    r = requests.get(url, headers=headers, timeout=10)
    sleep(2)

    info = []
    title_text = '-'
    room_size_text = '-'
    room_number_text = '-'
    security_text_text = '-'
    price_text = '-'
    title_text = '-'
    images = '-'
    description_text = '-'

    if r.status_code == 200:
        print('Processing..' + url)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('h1')
        if title is not None:
            title_text = title.text.strip()

        price = soup.select('.param_price > span > strong')
        if price is None:
            price_text = ""
        if price is not None:
            price_text = price[0].text.strip('Rs').replace(',', '')

        size = soup.select('.param_m > span > strong')
        if size is None:
            room_size_text = ""
        if size is not None:
            room_size_text = size[0].text.strip('Rs').replace(',', '')


        room_number = soup.select('.room-lane > .big')
        if room_number is None:
            room_number_text = ""
        if room_number is not None:
            room_number_text = room_number[0].text.strip('Rs').replace(',', '')

        media = soup.select('.sub-list')
        if media is None:
            media_text = ""
        if media is not None:
            media_text = media[0].text.strip()

        security = soup.select('.params-list > li > .dotted-list')
        if security is None:
         security_text = ""
        if security is not None:
         security_text = security[0].text.strip()

        description = soup.select('.text-contents > div')
        if description is None:
            description_text = ""
        if description is not None:
            description_text = description[0].text.strip()


        #        price = soup.select('div > .xxxx-large')
#        if price is not None:
#            price_text = price[0].text.strip('Rs').replace(',', '')
#
#        images = soup.select('#bigGallery > li > a')
#        img = [image['href'].strip() for image in images]
#        images = '^'.join(img)

#        description = soup.select('#textContent > p')
#        if description is not None:
#            description_text = description[0].text.strip()


        info.append(url)
        info.append(title_text)
        info.append(price_text)
        print(url)
        print(title_text)
        print(price_text)
        print(room_size_text)
        print(room_number_text)
        print(media_text)
        print(security_text)
        print(description_text)



    return '\\'.join(info)


home_links = None
site_page = 1;
homes_info = []
homes_links = get_listing('https://www.otodom.pl/sprzedaz/mieszkanie/krakow/?search%5Bdist%5D=0&search%5Bsubregion_id%5D=410&search%5Bcity_id%5D=38')

if __name__ == '__main__':
    with Pool(10) as p:
         records = p.map(parse, homes_links)

    if len(records) > 0:
        with open('data_parallel.csv', 'a+', encoding='utf-8') as f:
            f.write('\n'.join(records))
