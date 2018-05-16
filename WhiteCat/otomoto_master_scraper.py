import requests
from bs4 import BeautifulSoup
from time import sleep

cars_page_number = 1;
max_cars_page_number = 8444;

while cars_page_number < max_cars_page_number:

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
            listing_section = soup.select('.offers.list > article > .offer-item__content > div > h2 > .offer-title__link')
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
        location_text = '-'
        price_text = '-'
        title_text = '-'
        offer_text = '-'
        category_text = '-'
        mark_text ='-'
        model_text = '-'
        engine_code_text ='-'
        version_text ='-'
        year_of_production_text ='-'
        mileage_text = '-'
        capacity_text ='-'
        vin_text = "-"
        power_text = '-'
        fuel_type_text = '-'
        transmission_text = "-"
        drive_text = "-"
        type_text = "-"
        number_of_doors_text = "-"
        number_of_seats_text = "-"
        colour_text= "-"
        country_origin_text = "-"
        registered_in_poland_text = "-"
        condition_text = "-"
        equipment_text = "-"
        images = '-'
        description_text = '-'
        id_text = "-"

        if r.status_code == 200:
            print('Processing..' + url)
            html = r.text
            soup = BeautifulSoup(html, 'lxml')

            title = soup.find("h1")
            if title is not None:
                title_text = title.text.strip()
            try:
                id = soup.find("span", text='ID: ').find_next_sibling("span", class_="offer-meta__value")
                if id is not None:
                    id_text = id.text.strip()
            except AttributeError:
                id_text = "-"

            try:
                offer = soup.find('span', text='Oferta od').findNext('div')
                if offer is not None:
                    offer_text = offer.text.strip()
            except AttributeError:
                offer_text = "-"

            try:
                location = soup.find('span', {'class': 'seller-box__seller-address__label'})
                if location is not None:
                    location_text = location.text.strip()
            except AttributeError:
                location_text = "-"

            try:
                category = soup.find('span', text='Kategoria').findNext('div')
                if category is not None:
                    category_text = category.text.strip()
            except AttributeError:
                category_text = "-"
            try:
                mark = soup.find('span', text='Marka pojazdu').findNext('div')
                if mark is not None:
                    mark_text = mark.text.strip()
            except AttributeError:
                mark_text = "-"
            try:
                model = soup.find('span', text='Model pojazdu').findNext('div')
                if model is not None:
                    model_text = model.text.strip()
            except AttributeError:
                model_text = "-"

            try:
                engine_code = soup.find('span', text='Wersja').findNext('div')
                if engine_code is not None:
                    engine_code_text = engine_code.text.strip()
            except AttributeError:
                engine_code_text = "-"
            try:
                year_of_production = soup.find('span', text='Rok produkcji').findNext('div')
                if year_of_production is not None:
                    year_of_production_text = year_of_production.text.strip()
            except AttributeError:
                year_of_production_text = "-"

            try:
                mileage = soup.find('span', text='Przebieg').findNext('div')
                if mileage is not None:
                    mileage_text = mileage.text.strip()
            except AttributeError:
                mileage_text = "-"

            try:
                capacity = soup.find('span', text='Pojemność skokowa').findNext('div')
                if capacity is not None:
                    capacity_text = capacity.text.strip()
            except AttributeError:
                capacity_text = "-"

            try:
                vin = soup.find('span', text='VIN').findNext('div')
                if vin is not None:
                    vin_text = vin.text.strip()
            except AttributeError:
                vin_text = "-"

            try:
                power = soup.find('span', text='Moc').findNext('div')
                if power is not None:
                    power_text = power.text.strip()
            except AttributeError:
                power_text = "-"

            try:
                fuel_type = soup.find('span', text='Rodzaj paliwa').findNext('div')
                if fuel_type is not None:
                    fuel_type_text = fuel_type.text.strip()
            except AttributeError:
                fuel_type_text = "-"

            try:
                transmission = soup.find('span', text='Skrzynia biegów').findNext('div')
                if transmission is not None:
                    transmission_text = transmission.text.strip()
            except AttributeError:
                transmission_text = "-"

            try:
                drive = soup.find('span', text='Napęd').findNext('div')
                if drive is not None:
                    drive_text = drive.text.strip()
            except AttributeError:
                drive_text = "-"

            try:
                type = soup.find('span', text='Typ').findNext('div')
                if type is not None:
                    type_text = type.text.strip()
            except AttributeError:
                type_text = "-"

            try:
                number_of_doors = soup.find('span', text='Liczba drzwi').findNext('div')
                if number_of_doors is not None:
                    number_of_doors_text = number_of_doors.text.strip()
            except AttributeError:
                number_of_doors_text = "-"

            try:
                number_of_seats = soup.find('span', text='Liczba miejsc').findNext('div')
                if number_of_seats is not None:
                    number_of_seats_text = number_of_seats.text.strip()
            except AttributeError:
                number_of_seats_text = "-"

            try:
                colour = soup.find('span', text='Kolor').findNext('div')
                if colour is not None:
                    colour_text= colour.text.strip()
            except AttributeError:
                colour_text = "-"

            try:
                country_origin = soup.find('span', text='Kraj pochodzenia').findNext('div')
                if country_origin is not None:
                    country_origin_text = country_origin.text.strip()
            except AttributeError:
                country_origin_text = "-"

            try:
                registered_in_poland = soup.find('span', text='Pierwsza rejestracja').findNext('div')
                if registered_in_poland is not None:
                    registered_in_poland_text = registered_in_poland.text.strip()
            except AttributeError:
                registered_in_poland_text = "-"

            try:
                condition = soup.find('span', text='Stan').findNext('div')
                if condition is not None:
                    condition_text = condition.text.strip()
            except AttributeError:
                condition_text = "-"

            # equipment = soup.select('.offer-features__item')
            # if equipment is not None:
            #     equipment_text = equipment.text.strip()
            # print(equipment_text)


            price = soup.select('div > .offer-price__number')
            if price is not None:
                price_text = price[0].text.strip('Rs').replace(',', '').replace(' ', '').replace('PLN', '').replace('\n', '')

            # images = soup.select('#bigGallery > li > a')
            # img = [image['href'].strip() for image in images]
            # images = '^'.join(img)

            info.append('"'+url+'"')
            info.append('"'+id_text+'"')
            info.append('"'+title_text+'"')
            info.append('"'+location_text+'"')
            info.append('"'+price_text+'"')
            info.append('"'+offer_text+'"')
            info.append('"'+category_text+'"')
            info.append('"'+mark_text+'"')
            info.append('"'+model_text+'"')
            info.append('"'+engine_code_text+'"')
            info.append('"'+year_of_production_text+'"')
            info.append('"'+mileage_text+'"')
            info.append('"'+vin_text+'"')
            info.append('"'+power_text+'"')
            info.append('"'+drive_text+'"')
            info.append('"'+fuel_type_text+'"')
            info.append('"'+transmission_text+'"')
            info.append('"'+capacity_text+'"')
            info.append('"'+type_text+'"')
            info.append('"'+number_of_doors_text+'"')
            info.append('"'+number_of_seats_text+'"')
            info.append('"'+colour_text+'"')
            info.append('"'+registered_in_poland_text+'"')
            info.append('"'+country_origin_text+'"')
            info.append('"'+condition_text+'"')

        return ','.join(info)

    car_links = None
    cars_info = []
    cars_links = get_listing('https://www.otomoto.pl/osobowe/?page=' + str(cars_page_number))

    [cars_info.append(parse(car_link)) for car_link in cars_links]
    if len(cars_info) > 0:
        with open('database_cars.csv', 'a+', encoding='utf-8') as f:
            f.write('\n'.join(cars_info))

        cars_page_number+=1
        print(cars_page_number)