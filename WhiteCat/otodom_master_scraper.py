import requests
from bs4 import BeautifulSoup
from time import sleep

homes_page_number = 10;
max_homes_page_number = 140;

while homes_page_number < max_homes_page_number:

    def get_listing(url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        html = None
        links = None
        print("I'm starting")
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            listing_section = soup.select('.col-md-content > article > div > header > h3 > a')
          # listing_section = soup.select('.offers.list > article > .offer-item__content > div > h2 > a')

            links = [link['href'].strip() for link in listing_section]
        return links

    # parse a single item to get information
    def parse(url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        r = requests.get(url, headers=headers, timeout=10)
        sleep(2)

        info = []
        id_text = '-'
        location_text = '-'
        size_text = '-'
        price_text = '-'
        title_text = '-'
        rooms_number_text = '-'
        floor_text = '-'
        market_text = '-'
        type_of_building_text = '-'
        building_material_text = '-'
        window_text = '-'
        heating_text = '-'
        construction_year_text = '-'
        trim_condition_text = '-'
        form_of_the_property_text = '-'
        avaliable_from_text = '-'
        attic_text = '-'
        roof_text = '-'
        covering_text = '-'
        position_text = '-'
        description_text = '-'

        if r.status_code == 200:
            print('Processing..' + url)
            html = r.text
            soup = BeautifulSoup(html, 'lxml')

            title = soup.find("h1")
            if title is not None:
                title_text = title.text.strip()

            try:
                id = soup.find("div", {'class': 'left'}).findNext('p')
                if id is not None:
                    id_text = id.text.strip('Rs').replace('Nr oferty w Otodom: ', '')
            except AttributeError:
                id_text = "-"

            try:
                location = soup.find('p', {'class': 'address-text'})
                if location is not None:
                    location_text = location.text.strip('Rs')
            except AttributeError:
                location_text = "-"

            try:
                size = soup.find('li', {'class': 'param_m'})
                if size is not None:
                    size_text = size.text.strip('Rs').replace('Powierzchnia ', '').replace(' m²', '')
            except AttributeError:
                size_text = "-"

            try:
                rooms_number = soup.select('.room-lane > .big')
                if rooms_number is not None:
                    rooms_number_text = rooms_number[0].text.strip('Rs')
            except AttributeError:
                rooms_number_text = "-"

            try:
                floor = soup.find('li', {'class': 'param_floor_no'}).findNext('span')
                if floor is not None:
                    floor_text = floor.text.strip()
            except AttributeError:
                floor_text = "-"
#copy
            try:
                market = soup.find('strong', text='Rynek:').previous_element
                if market is not None:
                    market_text = market.text.strip().replace('Rynek: ', '')
            except AttributeError:
                market_text = "-"

            try:
                type_of_building = soup.find('strong', text='Rodzaj zabudowy:').previous_element
                if type_of_building is not None:
                    type_of_building_text = type_of_building.text.strip().replace('Rodzaj zabudowy: ', '')
            except AttributeError:
                type_of_building_text = "-"

            try:
                window = soup.find('strong', text='Okna:').previous_element
                if window is not None:
                    window_text = window.text.strip().replace('Okna: ', '')
            except AttributeError:
                window_text = "-"

            try:
                heating = soup.find('strong', text='Ogrzewanie:').previous_element
                if heating is not None:
                    heating_text = heating.text.strip().replace('Ogrzewanie: ', '')
            except AttributeError:
                heating_text = "-"

            try:
                construction_year = soup.find('strong', text='Rok budowy:').previous_element
                if construction_year is not None:
                    construction_year_text = construction_year.text.strip().replace('Rok budowy: ', '')
            except AttributeError:
                construction_year_text = "-"

            try:
                trim_condition = soup.find('strong', text='Stan wykończenia:').previous_element
                if trim_condition is not None:
                    trim_condition_text = trim_condition.text.strip().replace('Stan wykończenia: ', '')
            except AttributeError:
                trim_condition_text = "-"

            try:
                form_of_the_property = soup.find('strong', text='Forma własności:').previous_element
                if form_of_the_property is not None:
                    form_of_the_property_text = form_of_the_property.text.strip().replace('Forma własności: ', '')
            except AttributeError:
                form_of_the_property_text = "-"


            try:
                avaliable_from = soup.find('strong', text='Dostępne od:').previous_element
                if avaliable_from is not None:
                    avaliable_from_text = avaliable_from.text.strip().replace('Dostępne od: ', '')
            except AttributeError:
                avaliable_from_text = "-"


            try:
                building_material = soup.find('strong', text='Materiał budynku:').previous_element
                if building_material is not None:
                    building_material_text = building_material.text.strip().replace('Materiał budynku: ', '')
            except AttributeError:
                building_material_text = "-"

            try:
                attic = soup.find('strong', text='Poddasze:').previous_element
                if attic is not None:
                    attic_text = attic.text.strip().replace('Poddasze: ', '')
            except AttributeError:
                attic_text = "-"

            try:
                roof = soup.find('strong', text='Dach:').previous_element
                if roof is not None:
                    roof_text = roof.text.strip().replace('Dach: ', '')
            except AttributeError:
                roof_text = "-"

            try:
                covering = soup.find('strong', text='Pokrycie:').previous_element
                if covering is not None:
                    covering_text = covering.text.strip().replace('Pokrycie: ', '')
            except AttributeError:
                covering_text = "-"
            try:
                position = soup.find('strong', text='Położenie:').previous_element
                if position is not None:
                    position_text = position.text.strip().replace('Położenie: ', '')
            except AttributeError:
                position_text = "-"

            try:
                position = soup.find('strong', text='Położenie:').previous_element
                if position is not None:
                    position_text = position.text.strip().replace('Położenie: ', '')
            except AttributeError:
                position_text = "-"

            try:
                position = soup.find('strong', text='Położenie:').previous_element
                if position is not None:
                    position_text = position.text.strip().replace('Położenie: ', '')
            except AttributeError:
                position_text = "-"

            try:
                czynsz = soup.find('strong', text='Czynsz:').previous_element
                if czynsz is not None:
                    czynsz_text = czynsz.text.strip().replace('Czynsz: ', '')
            except AttributeError:
                czynsz_text = "-"

            try:
                description = soup.select('.text-contents > div > p')
                if description is not None:
                    description_text = description[0].text.strip('Rs')
            except AttributeError:
                description_text = "-"


            price = soup.select('div > .box-price-value')
            if price is not None:
                price_text = price[0].text.strip('Rs').replace(' zł', '').replace(' ', '')

            # images = soup.select('#bigGallery > li > a')
            # img = [image['href'].strip() for image in images]
            # images = '^'.join(img)

            info.append('"'+url+'"')
            info.append('"'+id_text+'"')
            info.append('"'+title_text+'"')
            info.append('"'+size_text+'"')
            info.append('"'+price_text+'"')
            info.append('"'+location_text+'"')
            info.append('"'+rooms_number_text+'"')
            info.append('"'+floor_text+'"')
            info.append('"'+market_text+'"')
            info.append('"'+type_of_building_text+'"')
            info.append('"'+building_material_text+'"')
            info.append('"'+trim_condition_text+'"')
            info.append('"'+window_text+'"')
            info.append('"'+heating_text+'"')
            info.append('"'+construction_year_text+'"')
            info.append('"'+form_of_the_property_text+'"')
            info.append('"'+avaliable_from_text+'"')
            info.append('"'+attic_text+'"')
            info.append('"'+roof_text+'"')
            info.append('"'+covering_text+'"')
            info.append('"'+position_text+'"')
            info.append('"'+description_text+'"')
            print(id_text)
            print(title_text)
            print(size_text)
            print(price_text)
            print(location_text)
            print(rooms_number_text)
            print(floor_text)
            print(market_text)
            print(type_of_building_text)
            print(building_material_text)
            print(trim_condition_text)
            print(window_text)
            print(heating_text)
            print(construction_year_text)
            print(form_of_the_property_text)
            print(avaliable_from_text)
            print(attic_text)
            print(roof_text)
            print(covering_text)
            print(position_text)
            print(description_text)

        return ','.join(info)

    home_links = None
    homes_info = []
    homes_links = get_listing('https://www.otodom.pl/sprzedaz/mieszkanie/krakow/?search%5Bdescription%5D=1&search%5Bdist%5D=0&search%5Bsubregion_id%5D=410&search%5Bcity_id%5D=38&nrAdsPerPage=72&page=' + str(homes_page_number))

    [homes_info.append(parse(home_link)) for home_link in homes_links]
    if len(homes_info) > 0:
        with open('database_homies.csv', 'a+', encoding='utf-8') as f:
            f.write('\n'.join(homes_info))

        homes_page_number+=1
        print('Page Number: ' + str(homes_page_number))