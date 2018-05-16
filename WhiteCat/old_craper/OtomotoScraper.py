import requests
from bs4 import BeautifulSoup
import time


pageNumber = 1

while pageNumber < 2:
    req = requests.get(
        'https://www.otomoto.pl/osobowe/bmw/?page=' + str(
            pageNumber))
    soup = BeautifulSoup(req.text, "lxml")
    carDetails = soup.find_all(class_="offer-item__content")

    print("Page Number: " + str(pageNumber))

    lobbying = {}
    for element in carDetails:
        lobbying[element.a.get_text().strip()] = {}



    carDetails[0].a["href"]

    prefix = "www.otomoto.pl"




    for element in carDetails:
        lobbying[element.a.get_text().strip()]["link"] = element.a["href"]

    for element in carDetails:
        lobbying[element.a.get_text().strip()]["ID"] = element.a["data-ad-id"]


    carDetails[0].find("span", class_="offer-price__number")

    for element in carDetails:
        try:
           price__number = element.find("span", class_="offer-price__number").get_text().strip()
           lobbying[element.a.get_text().strip()]["price__number"] = price__number
        except AttributeError:
            lobbying[element.a.get_text().strip()]["price__number"] = ""
    for element in carDetails:
        try:
            year = element.find("li", class_="offer-item__params-item").get_text().strip()
            lobbying[element.a.get_text().strip()]["year"] = year
        except AttributeError:
            lobbying[element.a.get_text().strip()]["year"] = ""

    for element in carDetails:
        try:
            mileage = element.find("li", class_="offer-item__params-item").find_next_sibling("li", class_="offer-item__params-item").get_text().strip()
            lobbying[element.a.get_text().strip()]["mileage"] = mileage
        except AttributeError:
            lobbying[element.a.get_text().strip()]["mileage"] = ""

    for element in carDetails:
        try:
            engine_capacity = element.find("li", class_="offer-item__params-item").find_next_sibling("li", class_="offer-item__params-item").find_next_sibling("li", class_="offer-item__params-item").get_text().strip()
            lobbying[element.a.get_text().strip()]["engine_capacity"] = engine_capacity
        except AttributeError:
            lobbying[element.a.get_text().strip()]["engine_capacity"] = ""
    for element in carDetails:
        try:
            fuel_type = element.find("li", class_="offer-item__params-item").find_next_sibling("li", class_="offer-item__params-item").find_next_sibling("li", class_="offer-item__params-item").find_next_sibling("li", class_="offer-item__params-item").get_text().strip()
            lobbying[element.a.get_text().strip()]["fuel_type"] = fuel_type
        except AttributeError:
            lobbying[element.a.get_text().strip()]["fuel_type"] = ""

     #   for item in lobbying.keys():
     #       print(item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "ID: " + lobbying[item]["ID"] + "\n\t" + "Price Cut: " + lobbying[item]["price__number"]+ "\n\t" + "Year: " +lobbying[item]["year"] + "\n\t" + "Przebieg: " + lobbying[item]["mileage"]+ "\n\t" + "Silnik: " + lobbying[item]["engine_capacity"]+ "\n\t" + "Typ Paliwa: " + lobbying[item]["fuel_type"]+ "\n\t" + "\n\n")

    for item in lobbying.keys():



        reqDetails = requests.get(lobbying[item]["link"])
        soupe = BeautifulSoup(reqDetails.text, "lxml")
        selectedCarDetails = soupe.find_all(class_="page-offer")


        DetailsLobbying = {}
        for element in selectedCarDetails:
            DetailsLobbying[element.a.get_text().strip()] = {}

        #selectedCarDetails[0].find("span", class_="offer-price__number")

        for element in selectedCarDetails:
            try:
                car_offer_price = element.find("span", class_="offer-price__number").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_offer_price"] = car_offer_price
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_offer_price"] = ""

        for element in selectedCarDetails:
            try:
                car_id = element.find("span", text='ID: ').find_next_sibling("span",
                                                                             class_="offer-meta__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_id"] = car_id
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_id"] = ""

        for element in selectedCarDetails:
            try:
                car_offer_type = element.find("span", text='Oferta od').find_next_sibling("div",
                                                                                          class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_offer_type"] = car_offer_type
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_offer_type"] = ""

        for element in selectedCarDetails:
            try:
                car_category = element.find("span", text='Kategoria').find_next_sibling("div",
                                                                                        class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_category"] = car_category
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_category"] = ""

        for element in selectedCarDetails:
            try:
                car_mark = element.find("span", text='Marka').find_next_sibling("div",
                                                                                class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_mark"] = car_mark
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_mark"] = ""

        for element in selectedCarDetails:
            try:
                car_model = element.find("span", text='Model').find_next_sibling("div",
                                                                                 class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_model"] = car_model
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_model"] = ""

        for element in selectedCarDetails:
            try:
                car_year = element.find("span", text='Rok produkcji').find_next_sibling("div",
                                                                                        class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_year"] = car_year
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_year"] = ""

        for element in selectedCarDetails:
            try:
                car_mileage = element.find("span", text='Przebieg').find_next_sibling("div",
                                                                                      class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_mileage"] = car_mileage
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_mileage"] = ""

        for element in selectedCarDetails:
            try:
                car_displacement = element.find("span", text='Pojemność skokowa').find_next_sibling("div",
                                                                                                    class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_displacement"] = car_displacement
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_displacement"] = ""

        for element in selectedCarDetails:
            try:
                car_power = element.find("span", text='Moc').find_next_sibling("div",
                                                                               class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_power"] = car_power
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_power"] = ""

        for element in selectedCarDetails:
            try:
                car_fuel_type = element.find("span", text='Rodzaj paliwa').find_next_sibling("div",
                                                                                             class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_fuel_type"] = car_fuel_type
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_fuel_type"] = ""

        for element in selectedCarDetails:
            try:
                car_transmission = element.find("span", text='Skrzynia biegów').find_next_sibling("div",
                                                                                                  class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_transmission"] = car_transmission
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_transmission"] = ""

        for element in selectedCarDetails:
            try:
                car_drive = element.find("span", text='Napęd').find_next_sibling("div",
                                                                                 class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_drive"] = car_drive
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_drive"] = ""

        for element in selectedCarDetails:
            try:
                car_type = element.find("span", text='Typ').find_next_sibling("div",
                                                                              class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_type"] = car_type
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_type"] = ""

        for element in selectedCarDetails:
            try:
                car_doors_number = element.find("span", text='Liczba drzwi').find_next_sibling("div",
                                                                                               class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_doors_number"] = car_doors_number
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_doors_number"] = ""

        for element in selectedCarDetails:
            try:
                car_seats_number = element.find("span", text='Liczba miejsc').find_next_sibling("div",
                                                                                                class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_seats_number"] = car_seats_number
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_seats_number"] = ""

        for element in selectedCarDetails:
            try:
                car_color = element.find("span", text='Kolor').find_next_sibling("div",
                                                                                 class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_color"] = car_color
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_color"] = ""

        for element in selectedCarDetails:
            try:
                car_vat_margin = element.find("span", text='VAT marża').find_next_sibling("div",
                                                                                          class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_vat_margin"] = car_vat_margin
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_vat_margin"] = ""

        for element in selectedCarDetails:
            try:
                car_country = element.find("span", text='Kraj pochodzenia').find_next_sibling("div",
                                                                                              class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_country"] = car_country
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_country"] = ""

        for element in selectedCarDetails:
            try:
                car_condition = element.find("span", text='Stan').find_next_sibling("div",
                                                                                    class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_condition"] = car_condition
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_condition"] = ""

        for element in selectedCarDetails:
            try:
                car_vin = element.find("span", text='VIN').find_next_sibling("div",
                                                                             class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_vin"] = car_vin
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_vin"] = ""

        for element in selectedCarDetails:
            try:
                car_faktura_vat = element.find("span", text='Faktura VAT').find_next_sibling("div",
                                                                                             class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_faktura_vat"] = car_faktura_vat
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_faktura_vat"] = ""

        for element in selectedCarDetails:
            try:
                car_first_registration = element.find("span", text='Pierwsza rejestracja').find_next_sibling("div",
                                                                                                             class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_first_registration"] = car_first_registration
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_first_registration"] = ""
        for element in selectedCarDetails:
            try:
                car_registration_poland = element.find("span", text='Zarejestrowany w Polsce').find_next_sibling("div",
                                                                                                                 class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_registration_poland"] = car_registration_poland
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_registration_poland"] = ""
        for element in selectedCarDetails:
            try:
                car_first_user = element.find("span", text='Pierwszy właściciel').find_next_sibling("div",
                                                                                                    class_="offer-params__value").get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_first_user"] = car_first_user
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_first_user"] = ""

        for element in selectedCarDetails:
            try:
                car_equipement = element.find("div", class_='offer-features__row').get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_equipement"] = car_equipement
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_equipement"] = ""

        for element in selectedCarDetails:
            try:
                car_description = element.find("div", class_='offer-description').get_text().strip()
                DetailsLobbying[element.a.get_text().strip()]["car_description"] = car_description
            except AttributeError:
                DetailsLobbying[element.a.get_text().strip()]["car_description"] = ""

        for item in DetailsLobbying.keys():
            print(DetailsLobbying[item]["car_id"]+","+DetailsLobbying[item]["car_mark"]+","+DetailsLobbying[item]["car_model"]+","+DetailsLobbying[item]["car_offer_price"]+","+DetailsLobbying[item]["car_year"]+","+DetailsLobbying[item]["car_first_user"]+","+DetailsLobbying[item]["car_power"]+","+DetailsLobbying[item]["car_country"])

    pageNumber+=1

    #import os, csv
    #os.chdir("/Users/piotr/Dysk Google/PowerPrice")
    #
    #with open("lobbying.csv", "w") as toWrite:
    #    writer = csv.writer(toWrite, delimiter=",")
    #    writer.writerow(["name", "link", "date"])
    #    for a in lobbying.keys():
    #        writer.writerow([a.encode("utf-8"), lobbying[a]["link"], lobbying[a]["price__number"]])
