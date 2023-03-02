import csv
import time

import requests
from ymaps import SearchClient
import datetime


#response = requests.get("type=&&page_size=10&page=1&key=ruoqhu5955")
#data = response.json()
#print(1)
api_key = '9fa2ee91-694a-4fd2-adbc-b3b7e0c1a633'
client = SearchClient(api_key)
d = datetime.datetime.today()

def restoraunts():
    token = 'ruoqhu5955'
    request = 'Рестораны'
    locale='ru_RU'
    fields = 'items.point,items.rubrics,items.caption,items.address,items.context,items.attribute_groups,items.external_content,items.contact_groups,items.schedule'
    offset = 0
    type = 'branch'
    page_size = 10
    page = 1
    all_post_rest = []
    city_id = 8163397094867289
    while page <= 3:
        try:
            response = requests.get('https://catalog.api.2gis.com/3.0/items?',
                                    params={
                                        'q': request,
                                        'fields': fields,
                                        'locale': locale,
                                        'page_size': page_size,
                                        'page': page,
                                        'key': token,
                                        'city_id': city_id,
                                        'type': 'branch'


                                    })
            data = response.json()['result']['items']
            page+=1
            all_post_rest.extend(data)
        except KeyError:
            break
    return all_post_rest

def kalyan():
    request = 'Кальянные'
    token = 'ruoqhu5955'
    locale = 'ru_RU'
    fields = 'items.point,items.rubrics,items.caption,items.address,items.context,items.attribute_groups,items.external_content,items.contact_groups,items.schedule'
    offset = 0
    type = 'branch'
    page_size = 10
    page = 1
    all_post_kalyan = []
    city_id = 8163397094867289
    while page <= 5:
        try:
            response = requests.get('https://catalog.api.2gis.com/3.0/items?',
                                    params={
                                        'q': request,
                                        'fields': fields,
                                        'locale': locale,
                                        'page_size': page_size,
                                        'page': page,
                                        'key': token,
                                        'city_id': city_id,
                                        'type': 'branch'
                                    })
            data = response.json()['result']['items']
            page += 1
            all_post_kalyan.extend(data)
        except KeyError:
            break
    return all_post_kalyan

def kafe_cofeinya():
    request = 'Кафе кофейни'
    token = 'ruoqhu5955'
    locale = 'ru_RU'
    fields = 'items.point,items.rubrics,items.caption,items.address,items.context,items.attribute_groups,items.external_content,items.contact_groups,items.schedule'
    offset = 0
    type = 'branch'
    page_size = 10
    page = 1
    all_post_kafe = []
    city_id = 8163397094867289
    while page <= 5:
        try:
            response = requests.get('https://catalog.api.2gis.com/3.0/items?',
                                    params={
                                        'q': request,
                                        'fields': fields,
                                        'locale': locale,
                                        'page_size': page_size,
                                        'page': page,
                                        'key': token,
                                        'city_id': city_id,
                                        'type': 'branch'
                                    })
            data = response.json()['result']['items']
            page += 1
            all_post_kafe.extend(data)
        except KeyError:
            break
    return all_post_kafe

def breakfast():
    request = 'Завтраки'
    token = 'ruoqhu5955'
    locale = 'ru_RU'
    fields = 'items.point,items.rubrics,items.caption,items.address,items.context,items.attribute_groups,items.external_content,items.contact_groups,items.schedule'
    offset = 0
    type = 'branch'
    page_size = 10
    page = 1
    all_post_breakfast = []
    city_id = 8163397094867289
    while page <= 5:
        try:
            response = requests.get('https://catalog.api.2gis.com/3.0/items?',
                                    params={
                                        'q': request,
                                        'fields': fields,
                                        'locale': locale,
                                        'page_size': page_size,
                                        'page': page,
                                        'key': token,
                                        'city_id': city_id,
                                        'type': 'branch'
                                    })
            data = response.json()['result']['items']
            page += 1
            all_post_breakfast.extend(data)
        except KeyError:
            break
    return all_post_breakfast
def karaoke():
    request = 'Караоке'
    token = 'ruoqhu5955'
    locale = 'ru_RU'
    fields = 'items.point,items.rubrics,items.caption,items.address,items.context,items.attribute_groups,items.external_content,items.contact_groups,items.schedule'
    offset = 0
    type = 'branch'
    page_size = 10
    page = 1
    all_post_karaoke = []
    city_id = 8163397094867289
    while page <= 5:
        try:
            response = requests.get('https://catalog.api.2gis.com/3.0/items?',
                                    params={
                                        'q': request,
                                        'fields': fields,
                                        'locale': locale,
                                        'page_size': page_size,
                                        'page': page,
                                        'key': token,
                                        'city_id': city_id,
                                        'type': 'branch'
                                    })
            data = response.json()['result']['items']
            page += 1
            all_post_karaoke.extend(data)
        except KeyError:
            break
    return all_post_karaoke

def bar():
    request = 'Бар'
    token = 'ruoqhu5955'
    locale = 'ru_RU'
    fields = 'items.point,items.rubrics,items.caption,items.address,items.context,items.attribute_groups,items.external_content,items.contact_groups,items.schedule'
    offset = 0
    type = 'branch'
    page_size = 10
    page = 1
    all_post_bar = []
    city_id = 8163397094867289
    while page <= 5:
        try:
            response = requests.get('https://catalog.api.2gis.com/3.0/items?',
                                    params={
                                        'q': request,
                                        'fields': fields,
                                        'locale': locale,
                                        'page_size': page_size,
                                        'page': page,
                                        'key': token,
                                        'city_id': city_id,
                                        'type': 'branch'
                                    })
            data = response.json()['result']['items']
            page += 1
            all_post_bar.extend(data)
        except KeyError:
            break

    return all_post_bar

data = kafe_cofeinya()
with open("restaurants.csv", mode="w", encoding='utf-8') as w_file:
    objects = ["Название", "Категория", "Кухня", "Ценовой диапозон",  "Адрес", "Режим работы", "Телефон", "Сайт", "Фото", "ID", "lat", "lon"]
    file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
    file_writer.writeheader()
    for dat in data:
        kitchen = ''
        price = ''
        name = dat['caption']
        g = 0
        try:
            address = dat['address_name']
            lat = dat['point']['lat']
            lon = dat['point']['lon']
            print(lat, lon)
            category = dat['rubrics'][0]['name']
            print(category)
            phot = dat['external_content'][0]['main_photo_url']
            id = dat['id']
        except KeyError:
            continue
        try:
            pricee = dat['attribute_groups'][0]['attributes']
            for pric in pricee:
                if 'Средний чек' in pric['name']:
                    price = pric['name']
                if 'кухня' in pric['name']:
                    kitchen += pric['name'] + ', '
        except KeyError:
            pass
        a = client.search(f'{name}, Киров, {address}', results=1)
        try:
            phone = a['features'][0]['properties']['CompanyMetaData']['Phones'][0]['formatted']
        except KeyError:
            phone = ''
        try:
            url = a['features'][0]['properties']['CompanyMetaData']['url']
        except KeyError:
            url = ''
        try:
            Monday = f"{dat['schedule']['Mon']['working_hours'][0]['from']}-{dat['schedule']['Mon']['working_hours'][0]['to']}"
            Tuesday = f"{dat['schedule']['Tue']['working_hours'][0]['from']}-{dat['schedule']['Tue']['working_hours'][0]['to']}"
            Wednesday = f"{dat['schedule']['Wed']['working_hours'][0]['from']}-{dat['schedule']['Wed']['working_hours'][0]['to']}"
            Thursday = f"{dat['schedule']['Thu']['working_hours'][0]['from']}-{dat['schedule']['Thu']['working_hours'][0]['to']}"
            Friday = f"{dat['schedule']['Fri']['working_hours'][0]['from']}-{dat['schedule']['Fri']['working_hours'][0]['to']}"
            Saturday = f"{dat['schedule']['Sat']['working_hours'][0]['from']}-{dat['schedule']['Sat']['working_hours'][0]['to']}"
            Sunday = f"{dat['schedule']['Sun']['working_hours'][0]['from']}-{dat['schedule']['Sun']['working_hours'][0]['to']}"
        except KeyError:
            continue
        schedule = []
        schedule.append(Monday)
        schedule.append(Tuesday)
        schedule.append(Wednesday)
        schedule.append(Thursday)
        schedule.append(Friday)
        schedule.append(Saturday)
        schedule.append(Sunday)
        if kitchen != '':
            kitchen = str(kitchen)
        weekday = d.weekday() + 1
        print(schedule)
        file_writer.writerow({"Название": name, "Категория": category, "Кухня": kitchen, "Ценовой диапозон": price, "Адрес": address, "Режим работы": schedule, "Телефон": phone, "Сайт": url, "Фото": phot, "ID": id, "lat": lat, "lon": lon})
        print(name)
        if kitchen != '':
            print(kitchen)
        print(address)
        print(url)
        print(phone)
        print(category)
        print(id)
        if weekday == 1:
            if Monday == '08:0023:00':
                print('Круглосуточно')
            else:
                print(Monday)
        elif weekday == 2:
            if Tuesday == '08:0023:00':
                print('Круглосуточно')
            else:
                print(Tuesday)
        elif weekday == 3:
            if Wednesday == '08:0023:00':
                print('Круглосуточно')
            else:
                print(Wednesday)
        elif weekday == 4:
            if Thursday == '08:0023:00':
                print('Круглосуточно')
            else:
                print(Thursday)
        elif weekday == 5:
            if Friday == '08:00-23:00':
                print('Круглосуточно')
            else:
                print(Friday)
        elif weekday == 6:
            if Saturday == '08:00-23:00':
                print('Круглосуточно')
            else:
                print(Saturday)
        elif weekday == 7:
            if Sunday == '08:00-23:00':
                print('Круглосуточно')
            else:
                print(Sunday)
        print(phot)
        print('\n')



print(1)