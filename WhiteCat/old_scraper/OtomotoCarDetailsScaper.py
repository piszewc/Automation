import requests
from bs4 import BeautifulSoup

reqDetails = requests.get('https://www.otomoto.pl/oferta/jeep-cherokee-3-2-l-v6-instalacja-lpg-start-stop-key-less-go-kamera-cofania-ID6yMW4N.html')
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
        car_id = element.find("span", text='ID: ').find_next_sibling("span", class_="offer-meta__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_id"] = car_id
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_id"] = ""


for element in selectedCarDetails:
    try:
        car_offer_type = element.find("span", text='Oferta od').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_offer_type"] = car_offer_type
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_offer_type"] = ""


for element in selectedCarDetails:
    try:
        car_category = element.find("span", text='Kategoria').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_category"] = car_category
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_category"] = ""


for element in selectedCarDetails:
    try:
        car_mark = element.find("span", text='Marka').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_mark"] = car_mark
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_mark"] = ""


for element in selectedCarDetails:
    try:
        car_model = element.find("span", text='Model').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_model"] = car_model
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_model"] = ""


for element in selectedCarDetails:
    try:
        car_year = element.find("span", text='Rok produkcji').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_year"] = car_year
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_year"] = ""


for element in selectedCarDetails:
    try:
        car_mileage = element.find("span", text='Przebieg').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_mileage"] = car_mileage
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_mileage"] = ""

for element in selectedCarDetails:
    try:
        car_displacement = element.find("span", text='Pojemność skokowa').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_displacement"] = car_displacement
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_displacement"] = ""

for element in selectedCarDetails:
    try:
        car_power = element.find("span", text='Moc').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_power"] = car_power
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_power"] = ""

for element in selectedCarDetails:
    try:
        car_fuel_type = element.find("span", text='Rodzaj paliwa').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_fuel_type"] = car_fuel_type
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_fuel_type"] = ""

for element in selectedCarDetails:
    try:
        car_transmission = element.find("span", text='Skrzynia biegów').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_transmission"] = car_transmission
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_transmission"] = ""

for element in selectedCarDetails:
    try:
        car_drive = element.find("span", text='Napęd').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_drive"] = car_drive
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_drive"] = ""

for element in selectedCarDetails:
    try:
        car_type = element.find("span", text='Typ').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_type"] = car_type
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_type"] = ""

for element in selectedCarDetails:
    try:
        car_doors_number = element.find("span", text='Liczba drzwi').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_doors_number"] = car_doors_number
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_doors_number"] = ""

for element in selectedCarDetails:
    try:
        car_seats_number = element.find("span", text='Liczba miejsc').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_seats_number"] = car_seats_number
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_seats_number"] = ""

for element in selectedCarDetails:
    try:
        car_color = element.find("span", text='Kolor').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_color"] = car_color
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_color"] = ""

for element in selectedCarDetails:
    try:
        car_vat_margin = element.find("span", text='VAT marża').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_vat_margin"] = car_vat_margin
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_vat_margin"] = ""

for element in selectedCarDetails:
    try:
        car_country = element.find("span", text='Kraj pochodzenia').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_country"] = car_country
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_country"] = ""

for element in selectedCarDetails:
    try:
        car_condition = element.find("span", text='Stan').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_condition"] = car_condition
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_condition"] = ""

for element in selectedCarDetails:
    try:
        car_vin = element.find("span", text='VIN').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_vin"] = car_vin
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_vin"] = ""

for element in selectedCarDetails:
    try:
        car_faktura_vat = element.find("span", text='Faktura VAT').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_faktura_vat"] = car_faktura_vat
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_faktura_vat"] = ""

for element in selectedCarDetails:
    try:
        car_first_registration = element.find("span", text='Pierwsza rejestracja').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_first_registration"] = car_first_registration
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_first_registration"] = ""

for element in selectedCarDetails:
    try:
        car_first_registration = element.find("span", text='Pierwsza rejestracja').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_first_registration"] = car_first_registration
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_first_registration"] = ""
for element in selectedCarDetails:
    try:
        car_registration_poland = element.find("span", text='Zarejestrowany w Polsce').find_next_sibling("div", class_="offer-params__value").get_text().strip()
        DetailsLobbying[element.a.get_text().strip()]["car_registration_poland"] = car_registration_poland
    except AttributeError:
        DetailsLobbying[element.a.get_text().strip()]["car_registration_poland"] = ""
for element in selectedCarDetails:
    try:
        car_first_user = element.find("span", text='Pierwszy właściciel').find_next_sibling("div", class_="offer-params__value").get_text().strip()
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
    print("ID " + DetailsLobbying[item]["car_id"] + "\n\t" + "Cena: " + DetailsLobbying[item]["car_offer_price"] + "\n\t" + "Oferta od: " + DetailsLobbying[item]["car_offer_type"] + "\n\t" + "Kategoria: " + DetailsLobbying[item]["car_category"] + "\n\t" + "Marka: " + DetailsLobbying[item]["car_mark"] + "\n\t" + "Model: " + DetailsLobbying[item]["car_model"] + "\n\t" + "Rok produkcji: " + DetailsLobbying[item]["car_year"] + "\n\t" + "Przebieg: " + DetailsLobbying[item]["car_mileage"] + "\n\t" + "Pojemność skokowa: " + DetailsLobbying[item]["car_displacement"] + "\n\t" + "Moc: " + DetailsLobbying[item]["car_power"] + "\n\t" + "Rodzaj paliwa: " + DetailsLobbying[item]["car_fuel_type"] + "\n\t" + "Skrzynia biegów: " + DetailsLobbying[item]["car_transmission"] + "\n\t" + "Napęd: " + DetailsLobbying[item]["car_drive"] + "\n\t" + "Typ: " + DetailsLobbying[item]["car_type"] + "\n\t" + "Liczba drzwi: " + DetailsLobbying[item]["car_doors_number"] + "\n\t" + "Liczba miejsc: " + DetailsLobbying[item]["car_seats_number"] + "\n\t" + "Kolor: " + DetailsLobbying[item]["car_color"] + "\n\t" + "VAT marża: " + DetailsLobbying[item]["car_vat_margin"] + "\n\t" + "Kraj pochodzenia: " + DetailsLobbying[item]["car_country"] + "\n\t" + "Stan: " + DetailsLobbying[item]["car_condition"] + "\n\t" + "VIN: " + DetailsLobbying[item]["car_vin"]+ "\n\t" + "Zarejestrowany w Polsce: " +DetailsLobbying[item]["car_registration_poland"]+ "\n\t" + "Faktura VAT: " + DetailsLobbying[item]["car_faktura_vat"]+ "\n\t" + "Pierwsza rejestracja: " +DetailsLobbying[item]["car_first_registration"]+ "\n\t" + "Pierwszy właściciel: " +DetailsLobbying[item]["car_first_user"]+ "\n\t" + "Wyposażenie: " +DetailsLobbying[item]["car_equipement"]+ "\n\t" + "Opis: " +DetailsLobbying[item]["car_description"])