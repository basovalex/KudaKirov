from bs4 import BeautifulSoup
import requests
import random
import datetime
import telebot
from telebot import types
import geopy.distance
from geopy.geocoders import Nominatim
import csv
from heapq import nsmallest
from random import randint
import textwrap
import json
import time
import datetime

bot = telebot.TeleBot("5773105775:AAFb328ZrXSoIyCpcO0nAoQZp7_Tzl6ekXo")
@bot.message_handler(commands=['start'])
def start(message):
    global datees
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🔎Категории")
    btn2 = types.KeyboardButton(text="📍 Найти ближайшие", request_location=True)
    btn3 = types.KeyboardButton("📅 Афиша")
    btn4 = types.KeyboardButton("🎲Случайное")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, 'Подбери заведение по категории, найди ближайшее или случайное заведение Кирова.\nЖми кнопки внизу 👇', reply_markup=markup)
    func.random = 7
    datees = []

@bot.message_handler(content_types=['text'])
def func(message):
    global datees
    try:
        if message.text == '🔎Категории':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("🍽Ресторан")
            btn2 = types.KeyboardButton("☕Кофейня/Кафе")
            btn3 = types.KeyboardButton("🍹Бар")
            btn4 = types.KeyboardButton("🍳Завтраки")
            btn5 = types.KeyboardButton("💨Кальян")
            btn6 = types.KeyboardButton("🎤Караоке")
            btn7 = types.KeyboardButton("🏡База отдыха")
            btn8 = types.KeyboardButton("🧖‍♂Бани/Сауны")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
            markup.add(types.KeyboardButton('⏪Вернутся в главное меню'))
            bot.send_message(message.chat.id, 'Выберите, что ищем', reply_markup=markup)
            func.randomi = 1

        elif message.text == 'Проверить подписку 🔄':
            channel = 'https://t.me/kirovchano'
            if message.chat.type == 'private':
                status = ['creator', 'administrator', 'member']
                check = False
                for stat in status:
                    if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                        check = True
                if check == True:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton("🍽Ресторан")
                    btn2 = types.KeyboardButton("☕Кофейня/Кафе")
                    btn3 = types.KeyboardButton("🍹Бар")
                    btn4 = types.KeyboardButton("🍳Завтраки")
                    btn5 = types.KeyboardButton("💨Кальян")
                    btn6 = types.KeyboardButton("🎤Караоке")
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
                    markup.add(types.KeyboardButton('⏪Вернутся в главное меню'))
                    bot.send_message(message.chat.id, 'Выберите, что ищем', reply_markup=markup)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    btn1 = types.KeyboardButton("Проверить подписку 🔄")
                    markup.add(btn1)
                    bot.send_message(message.chat.id,
                                     f'Ты до сих пор не подписался. Подпишись на канал: {channel}. Чтобы пользоваться нашим ботом',
                                     reply_markup=markup)


        elif message.text == '⏪Вернутся в главное меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("🔎Категории")
            btn2 = types.KeyboardButton(text="📍 Найти ближайшие", request_location=True)
            btn3 = types.KeyboardButton("📅 Афиша")
            btn4 = types.KeyboardButton("🎲Случайное")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id,
                             'Подбери заведение по категории, найди ближайшее или случайное заведение Кирова.\nЖми кнопки внизу 👇',
                             reply_markup=markup)
            func.random = 7
            datees = []


        elif message.text == '📅 Афиша':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("🎥 Кино")
            btn2 = types.KeyboardButton("🎭 Театры")
            btn3 = types.KeyboardButton("🎤 Концерты")
            btn4 = types.KeyboardButton("🏛️ События")
            btn5 = types.KeyboardButton("🖻 Выставки")
            btn6 = types.KeyboardButton("📊 Тренинги")
            btn7 = types.KeyboardButton("🎯 Мастер-классы")
            btn8 = types.KeyboardButton("👟 Экскурсии")
            btn9 = types.KeyboardButton("🔈 Лекции")
            btn10 = types.KeyboardButton("⚽ Спорт")
            btn11 = types.KeyboardButton("🥳 Вечеринки")
            btn12 = types.KeyboardButton("🚴‍♂ Активным")
            btn13 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12,btn13)
            bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=markup)
            func.random = 8

        elif message.text == '🎥 Кино':

            global ob_objects
            global count1
            global objects
            global dates
            global afisha

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count1 = 0
            g = "https://kirov-portal.ru/afisha/cinema/"
            r = requests.get(g)
            soup = BeautifulSoup(r.text, "html.parser")
            soup = soup.find_all('div', class_='eventsBlock')
            for num in soup:
                p = num.find_all('div', class_='Item')
                for nam in p:
                    objects.append(nam)
            ob_objects = objects
            datees = []
            afisha = []
            for i in range(3):
                count1 += 1
                objecd = objects[i]
                name = objecd.find('div', class_='robotoBold').find('a').string
                age = objecd.find('div').find('div').find_all('div')[3].string
                description = objecd.find('div', class_='roboto').string
                description = textwrap.fill("Краткое описание:" + description, 40)
                url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                out = open("img.jpg", "wb")
                out.write(img.content)
                out.close()
                info = types.InlineKeyboardMarkup(row_width=2)
                info.add(
                    types.InlineKeyboardButton(text="Купить билеты📥", callback_data=f'info_{count1}'))
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                about = soup.find('div', class_='newsContent').text[0:500]
                inf = soup.find_all('div', class_='roboto')[3].find_all('div', style='display: table-row;')
                top = ''
                for descr in inf:
                    top += descr.find_all('div')[0].text + ' ' + descr.find_all('div')[1].text + '\n'
                if len(about) > 1000:
                    about = about[:20] + '...'
                dates = []
                items = soup.find('div', id='eventSchedule').find_all('div', class_='Item')
                for item in items:
                    k = item.find('div', class_='robotoBold').text + ', ' + item.find('div', class_='Date').text
                    dates.append(k)
                print(dates)
                datees.append(dates)
                schedules = soup.find('div', id = "scheduleBlock").find_all('div', class_='scheduleTable')
                info_message = []
                o = []
                status = schedules[0].get('class')[1]
                for schedule in schedules:
                    status1 = schedule.get('class')[1]
                    if status == status1:
                        kino = schedule.find('div', class_='robotoBold').text + '\n' + schedule.find('div', style='color:#808184; font-size:10px; margin-top:3px;').text
                        url1=schedule.find('a').get('href')
                        format = schedule.find_all('div', class_='td')[1].find('div',
                                                                               style='display:table-cell; width:84px; font-size:12px; font-weight:bold;').text
                        seanses = schedule.find_all('div', class_='td')[1].find('div', class_='seanceList').find_all('span')
                        seanse = ''
                        for i in seanses:
                            try:
                                if i.get('class')[0] == "NA":
                                    pass#seanse += i.text + '' + ' '
                                else:
                                    seanse += i.text + ' '
                            except TypeError:
                                seanse += i.text + ' '
                        if seanse == '':
                            seanse = "Сеансов на этот день больше нет"
                        u = f"*Название кинотеатра:* {kino.replace('Телефон:', '*Телефон:*')}\n{url1}\n{format}\n *Сеансы:* {seanse}"
                        o.append(u)
                    else:
                        info_message.append(o)
                        o = []
                        kino = schedule.find('div', class_='robotoBold').text + '\n' + schedule.find('div',
                                                                                                     style='color:#808184; font-size:10px; margin-top:3px;').text
                        url1 = schedule.find('a').get('href')
                        format = schedule.find_all('div', class_='td')[1].find('div',
                                                                               style='display:table-cell; width:84px; font-size:12px; font-weight:bold;').text
                        seanses = schedule.find_all('div', class_='td')[1].find('div', class_='seanceList').find_all(
                            'span')
                        seanse = ''
                        for i in seanses:
                            try:
                                if i.get('class')[0] == "NA":
                                    pass#seanse += '*' + i.text + '*' + ' '
                                else:
                                    seanse += i.text + ' '
                            except TypeError:
                                seanse += i.text + ' '
                        if seanse == '':
                            seanse = "Сеансов на этот день больше нет"
                        u = f"*Название кинотеатра:* {kino.replace('Телефон:', '*Телефон:*')}\n{url1}\n{format}\n *Сеансы:* {seanse}"
                        o.append(u)
                    status = schedule.get('class')[1]
                info_message.append(o)


                bot.send_photo(message.chat.id, photo=open('img.jpg','rb'),
                               caption=f"[{name}]({url}) {age}\n\n {about}\n\nКинотеатры: {cinema} \n\n {top}",
                               parse_mode='Markdown', reply_markup=info)
                func.rand = 10
                objects.remove(objecd)
                afisha.append(info_message)
            print(datees)


        elif message.text == '🎭 Театры':
            global teatrs
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count1 = 0
            teatrs = []
            g = "https://kirov-portal.ru/afisha/theatre/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
            objects = soup
            for i in range(3):
                count1 += 1
                objecd = objects[i]
                name = objecd.find('div', class_='robotoBold').find('a').string
                age = objecd.find_all('div')[1].find('div').string
                try:
                    description = objecd.find('div', class_='roboto').string
                    description = textwrap.fill("Краткое описание: " + description, 40)
                except AttributeError:
                    description = ''
                url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                try:
                    cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                    date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                except IndexError:
                    description = objecd.find_all('div', class_='verdana')[1].find('div').string
                    cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                    date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                out = open("img.jpg", "wb")
                out.write(img.content)
                out.close()
                img = open('img.jpg', 'rb')
                info = types.InlineKeyboardMarkup(row_width=2)
                info.add(
                    types.InlineKeyboardButton(text="Расписание/Где купить📥", callback_data=f'teatr1_{count1}'))
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                about = soup.find('div', class_='newsContent').text[0:500]
                inf = soup.find_all('div', class_='roboto')[3].find_all('div', style='display: table-row;')
                top = ''
                for descr in inf:
                    top += descr.find_all('div')[0].text + ' ' + descr.find_all('div')[1].text + '\n'
                if len(about) > 1000:
                    about = about[:20] + '...'
                teatr = []
                items = soup.find_all('div', class_='scheduleTable')#.find_all('div', class_='Item')
                for item in items:
                    date_teatr = item.find_all('div', class_='roboto')[0].find('b').text
                    time_teatr = item.find_all('div', class_='roboto')[0].text.replace(date_teatr, '').strip().replace('\t', '')
                    place_teatr = item.find('div', class_='robotoBold').text.strip()
                    adress_teatr = item.find('div', style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all('div')[0].text.strip()
                    phone_teatr = item.find('div', style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all('div')[1].text.strip()
                    price_teatr = item.find('div', class_='roboto', style ='display:table-cell; font-size:16px;').text.strip()
                    if time_teatr == '':
                        dat_teatr = f"{date_teatr}"
                    else:
                        dat_teatr = f"{date_teatr}, {time_teatr}"
                    if adress_teatr == '':
                        plac_teatr = f"{place_teatr.replace(',', '')}"
                    else:
                        plac_teatr = f"{place_teatr}, {adress_teatr}"
                    if phone_teatr == 'Телефон:':
                        phone_teatr = 'Не указан'
                    phone_teatr = phone_teatr.replace("Телефон:", "")
                    if "Театр на Спасской" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://ekvus-kirov.ru/afisha/show/")
                    elif "Руки Вверх" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/ruki-vverkh-bar-kirov/schedule")
                    elif "Органный зал" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovorgan.ru/afisha/")
                    elif "Драматический театр" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovdramteatr.ru/shows/")
                    elif "Театр кукол" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovkukla.ru/afisha")
                    elif "Филармония" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://www.philarmonia43.ru/events/")
                    elif "ОДНТ" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirov.kassy.ru/venue/kogauk-oblastnojj-dom-narodnogo-tvorchestva-oktyabrskijj-pr-kt-38-46/")
                    elif "Родина" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttp://xn----8sbkbujyfr.xn--p1ai/afisha/")
                    elif "Mr. Green" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/mister-green")
                    elif "Квартира" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/kvartira-kirov?source=search-page")
                    elif "СКЦ Семья" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/semia-kirov/schedule")
                    elif "Атмосфера" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/atmosfera-kirov/schedule")
                    elif "Конструктор-Практик" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/konstruktor-praktik")
                    elif "ДК железнодорожников" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://dkrzdkirov.ru/afisha/")
                    elif "Цирк" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/theatre/places/tsirk-57efcca6685ae0c36a5a5797/schedule")
                    elif "Тир" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://vk.com/tir_kot")
                    elif "GAUDI" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://gaudikirov.ru/afisha/")
                    else:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\n{url}")
                teatrs.append(teatr)
                print(teatrs)
                bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'),
                               caption=f"[{name}]({url}) {age}\n\n {about}\n\nТеатры: {cinema} \n\n {top}",
                               parse_mode='Markdown', reply_markup=info)
                func.rand = 11
                objects.remove(objecd)

        elif message.text == '🎤 Концерты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count1 = 0
            teatrs = []
            g = "https://kirov-portal.ru/afisha/concert/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
            objects = soup
            for i in range(3):
                count1 += 1
                objecd = objects[i]
                name = objecd.find('div', class_='robotoBold').find('a').string
                age = objecd.find_all('div')[1].find('div').string
                try:
                    description = objecd.find('div', class_='roboto').string
                    description = textwrap.fill("Краткое описание: " + description, 40)
                except AttributeError:
                    description = ''
                url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                try:
                    cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                    date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                except IndexError:
                    description = objecd.find_all('div', class_='verdana')[1].find('div').string
                    cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                    date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                out = open("img.jpg", "wb")
                out.write(img.content)
                out.close()
                img = open('img.jpg', 'rb')
                info = types.InlineKeyboardMarkup(row_width=2)
                info.add(
                    types.InlineKeyboardButton(text="Расписание/Где купить📥", callback_data=f'teatr1_{count1}'))
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                about = soup.find('div', class_='newsContent').text[0:500]
                inf = soup.find_all('div', class_='roboto')[3].find_all('div', style='display: table-row;')
                top = ''
                for descr in inf:
                    top += descr.find_all('div')[0].text + ' ' + descr.find_all('div')[1].text + '\n'
                if len(about) > 1000:
                    about = about[:20] + '...'
                teatr = []
                items = soup.find_all('div', class_='scheduleTable')  # .find_all('div', class_='Item')
                for item in items:
                    date_teatr = item.find_all('div', class_='roboto')[0].find('b').text
                    time_teatr = item.find_all('div', class_='roboto')[0].text.replace(date_teatr, '').strip().replace(
                        '\t', '')
                    place_teatr = item.find('div', class_='robotoBold').text.strip()
                    adress_teatr = \
                    item.find('div', style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                        'div')[0].text.strip()
                    phone_teatr = \
                    item.find('div', style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                        'div')[1].text.strip()
                    price_teatr = item.find('div', class_='roboto',
                                            style='display:table-cell; font-size:16px;').text.strip()
                    if time_teatr == '':
                        dat_teatr = f"{date_teatr}"
                    else:
                        dat_teatr = f"{date_teatr}, {time_teatr}"
                    if adress_teatr == '':
                        plac_teatr = f"{place_teatr.replace(',', '')}"
                    else:
                        plac_teatr = f"{place_teatr}, {adress_teatr}"
                    if phone_teatr == 'Телефон:':
                        phone_teatr = 'Не указан'
                    if "Театр на Спасской" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://ekvus-kirov.ru/afisha/show/")
                    elif "Органный зал" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovorgan.ru/afisha/")
                    elif "Драматический театр" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovdramteatr.ru/shows/")
                    elif "Театр кукол" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovkukla.ru/afisha")
                    elif "Филармония" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://www.philarmonia43.ru/events/")
                    elif "ОДНТ" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirov.kassy.ru/venue/kogauk-oblastnojj-dom-narodnogo-tvorchestva-oktyabrskijj-pr-kt-38-46/")
                    elif "Родина" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://xn----8sbkbujyfr.xn--p1ai/afisha/")
                    elif "Mr. Green" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/mister-green")
                    elif "Квартира" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/kvartira-kirov?source=search-page")
                    elif "СКЦ Семья" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/semia-kirov/schedule")
                    elif "Атмосфера" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/atmosfera-kirov/schedule")
                    elif "Конструктор-Практик" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/konstruktor-praktik")
                    elif "ДК железнодорожников" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://dkrzdkirov.ru/afisha/")
                    elif "Цирк" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/theatre/places/tsirk-57efcca6685ae0c36a5a5797/schedule")
                    elif "Тир" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://vk.com/tir_kot")
                    elif "GAUDI" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://gaudikirov.ru/afisha/")
                    elif "Руки Вверх" in place_teatr:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/ruki-vverkh-bar-kirov/schedule")
                    else:
                        teatr.append(
                            f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\n{url}")
                teatrs.append(teatr)
                print(teatrs)
                bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'),
                               caption=f"[{name}]({url}) {age}\n\n {about}\n\n{cinema} \n\n {top}",
                               parse_mode='Markdown', reply_markup=info)
                func.rand = 11
                objects.remove(objecd)

        elif message.text == '🏛️ События':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count1 = 0
            teatrs = []
            g = "https://kirov-portal.ru/afisha/events/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
            objects = soup
            for i in range(3):
                count1 += 1
                objecd = objects[i]
                name = objecd.find('div', class_='robotoBold').find('a').string
                age = objecd.find_all('div')[1].find('div').string
                try:
                    description = objecd.find('div', class_='roboto').string
                    description = textwrap.fill("Краткое описание: " + description, 40)
                except AttributeError:
                    description = ''
                url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                try:
                    cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                    try:
                        date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                    except IndexError:
                        date = cinema.strip()
                        cinema = ''
                except IndexError:
                    #description =  objecd.find_all('div', class_='roboto')[1].find('div').string
                    cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                    date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                out = open("img.jpg", "wb")
                out.write(img.content)
                out.close()
                img = open('img.jpg', 'rb')
                info = types.InlineKeyboardMarkup(row_width=2)
                info.add(
                    types.InlineKeyboardButton(text="Расписание/Где купить📥", callback_data=f'teatr_{count1}'))
                r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                about = soup.find('div', class_='newsContent').text[0:500]
                inf = soup.find_all('div', class_='roboto')[3].find_all('div', style='display: table-row;')
                top = ''
                for descr in inf:
                    top += descr.find_all('div')[0].text + ' ' + descr.find_all('div')[1].text + '\n'
                if len(about) > 1000:
                    about = about[:20] + '...'
                teatr = []
                items = soup.find_all('div', class_='scheduleTable', limit=3)  # .find_all('div', class_='Item')
                countt = 0
                for item in items:
                    countt+=1
                    date_teatr = item.find_all('div', class_='roboto')[0].find('b').text
                    time_teatr = item.find_all('div', class_='roboto')[0].text.replace(date_teatr, '').strip().replace(
                        '\t', '')
                    place_teatr = item.find('div', class_='robotoBold').text.strip()
                    adress_teatr = \
                        item.find('div',
                                  style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                            'div')[0].text.strip()
                    phone_teatr = \
                        item.find('div',
                                  style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                            'div')[1].text.strip()
                    price_teatr = item.find('div', class_='roboto',
                                            style='display:table-cell; font-size:16px;').text.strip()
                    #print(items[-1])
                    if item == items[-1]:
                        teatr.append(
                            f"{name}\n*ДАТА:* {date_teatr}, {time_teatr}\n*МЕСТО:* {place_teatr}, {adress_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\n[ПОДРОБНЕЕ...]({url})")
                    else:
                        teatr.append(
                            f"{name}\n*ДАТА:* {date_teatr}, {time_teatr}\n*МЕСТО:* {place_teatr}, {adress_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}")

                teatrs.append(teatr)
                #teatrs.append(f"[...]({url})")
                print(teatrs)
                bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'),
                               caption=f"[{name}]({url}) {age}\n\n {about}\n\n {cinema} \n\n {top}",
                               parse_mode='Markdown', reply_markup=info)
                func.rand = 13
                objects.remove(objecd)

        elif message.text == '🖻 Выставки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/exhibition/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
            objects = soup
            for i in range(3):
                count += 1
                objecd = objects[i]
                name = objecd.find('div', class_='robotoBold').find('a').string
                age = objecd.find_all('div')[1].find('div').string
                try:
                    description = objecd.find('div', class_='roboto').string
                    description = textwrap.fill("Краткое описание: " + description, 40)
                except AttributeError:
                    description = ''
                url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                try:
                    cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                    try:
                        date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                    except IndexError:
                        date = cinema.strip()
                        cinema = ''
                except IndexError:
                    description =  objecd.find_all('div', class_='roboto')[1].find('div').string
                    cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                    date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                out = open("img.jpg", "wb")
                out.write(img.content)
                out.close()
                img = open('img.jpg', 'rb')
                info = types.InlineKeyboardMarkup(row_width=2)
                info.add(
                    types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                if cinema == '':
                    bot.send_photo(message.chat.id, photo=img,
                                   caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                   parse_mode='Markdown', reply_markup=info)
                else:
                    bot.send_photo(message.chat.id, photo=img,
                                   caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                   parse_mode='Markdown', reply_markup=info)
                func.rand = 12
                objects.remove(objecd)

        elif message.text == '📊 Тренинги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/training/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            try:
                soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
                objects = soup
                for i in range(3):
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                        break
                    count += 1
                    objecd = objects[i]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        try:
                            date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                        except IndexError:
                            date = cinema.strip()
                            cinema = ''
                    except IndexError:
                        try:
                            description = objecd.find_all('div', class_='roboto')[1].find('div').string
                        except IndexError:
                            description = objecd.find_all('div', class_='verdana')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                    if cinema == '':
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    else:
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    func.rand = 12
                    objects.remove(objecd)
            except IndexError:
                bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')

        elif message.text == '🎯 Мастер-классы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/master-klassy/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            try:
                soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
                objects = soup
                for i in range(3):
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                        break
                    count += 1
                    objecd = objects[i]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        try:
                            date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                        except IndexError:
                            date = cinema.strip()
                            cinema = ''
                    except IndexError:
                        try:
                            description = objecd.find_all('div', class_='roboto')[1].find('div').string
                        except IndexError:
                            description = objecd.find_all('div', class_='verdana')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                    if cinema == '':
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    else:
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    func.rand = 12
                    objects.remove(objecd)
            except IndexError:
                bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')




        elif message.text == '👟 Экскурсии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/ekskursii/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
            objects = soup
            for i in range(3):
                print(i)
                if objects == []:
                    bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                    break
                count += 1
                try:
                    objecd = objects[i]
                except IndexError:
                    objecd = objects[-1]
                name = objecd.find('div', class_='robotoBold').find('a').string
                age = objecd.find_all('div')[1].find('div').string
                try:
                    description = objecd.find('div', class_='roboto').string
                    description = textwrap.fill("Краткое описание: " + description, 40)
                except AttributeError:
                    description = ''
                url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                try:
                    cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                    try:
                        date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                    except IndexError:
                        date = cinema.strip()
                        cinema = ''
                except IndexError:
                    try:
                        description =   objecd.find_all('div', class_='roboto')[1].find('div').string
                    except IndexError:
                        description =   objecd.find_all('div', class_='verdana')[1].find('div').string
                    cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                    date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                out = open("img.jpg", "wb")
                out.write(img.content)
                out.close()
                img = open('img.jpg', 'rb')
                info = types.InlineKeyboardMarkup(row_width=2)
                info.add(
                    types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                if cinema == '':
                    bot.send_photo(message.chat.id, photo=img,
                                   caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                   parse_mode='Markdown', reply_markup=info)
                else:
                    bot.send_photo(message.chat.id, photo=img,
                                   caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                   parse_mode='Markdown', reply_markup=info)
                func.rand = 12
                objects.remove(objecd)

        elif message.text == '🔈 Лекции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/lekcii/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
            objects = soup
            for i in range(3):
                print(i)
                if objects == []:
                    bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                    break
                count += 1
                try:
                    objecd = objects[i]
                except IndexError:
                    objecd = objects[-1]
                name = objecd.find('div', class_='robotoBold').find('a').string
                age = objecd.find_all('div')[1].find('div').string
                try:
                    description = objecd.find('div', class_='roboto').string
                    description = textwrap.fill("Краткое описание: " + description, 40)
                except AttributeError:
                    description = ''
                url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                try:
                    cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                    try:
                        date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                    except IndexError:
                        date = cinema.strip()
                        cinema = ''
                except IndexError:
                    try:
                        description =   objecd.find_all('div', class_='roboto')[1].find('div').string
                    except IndexError:
                        description =   objecd.find_all('div', class_='verdana')[1].find('div').string
                    cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                    date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                out = open("img.jpg", "wb")
                out.write(img.content)
                out.close()
                img = open('img.jpg', 'rb')
                info = types.InlineKeyboardMarkup(row_width=2)
                info.add(
                    types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                if cinema == '':
                    bot.send_photo(message.chat.id, photo=img,
                                   caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                   parse_mode='Markdown', reply_markup=info)
                else:
                    bot.send_photo(message.chat.id, photo=img,
                                   caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                   parse_mode='Markdown', reply_markup=info)
                func.rand = 12
                objects.remove(objecd)

        elif message.text == '⚽ Спорт':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/sport/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            try:
                soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
                objects = soup
                for i in range(3):
                    print(i)
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                        break
                    count += 1
                    try:
                        objecd = objects[i]
                    except IndexError:
                        objecd = objects[-1]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        try:
                            date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                        except IndexError:
                            date = cinema.strip()
                            cinema = ''
                    except IndexError:
                        try:
                            description =   objecd.find_all('div', class_='roboto')[1].find('div').string
                        except IndexError:
                            description =   objecd.find_all('div', class_='verdana')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                    if cinema == '':
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    else:
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    func.rand = 12
                    objects.remove(objecd)
            except IndexError:
                bot.send_message(message.chat.id, 'Никаких новостей нет 💨')
                func.rand = 12

        elif message.text == '🥳 Вечеринки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/club/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            try:
                soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
                objects = soup
                for i in range(3):
                    print(i)
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                        break
                    count += 1
                    try:
                        objecd = objects[i]
                    except IndexError:
                        objecd = objects[-1]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        try:
                            date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                        except IndexError:
                            date = cinema.strip()
                            cinema = ''
                    except IndexError:
                        try:
                            description =   objecd.find_all('div', class_='roboto')[1].find('div').string
                        except IndexError:
                            description =   objecd.find_all('div', class_='verdana')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                    if cinema == '':
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    else:
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    func.rand = 12
                    objects.remove(objecd)
            except IndexError:
                bot.send_message(message.chat.id, 'Никаких новостей нет 💨')
                func.rand = 12

        elif message.text == '🚴‍♂ Активным':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Подбираем 🔄', reply_markup=markup)
            objects = []
            count = 0
            g = "https://kirov-portal.ru/afisha/aktivnym/"
            r = requests.get(g)
            soup1 = BeautifulSoup(r.text, "html.parser")
            try:
                soup = soup1.find_all('div', id='searchBlock')[1].find_all('div', class_='Item')
                objects = soup
                for i in range(3):
                    print(i)
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                        break
                    count += 1
                    try:
                        objecd = objects[i]
                    except IndexError:
                        objecd = objects[-1]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        try:
                            date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                        except IndexError:
                            date = cinema.strip()
                            cinema = ''
                    except IndexError:
                        try:
                            description =   objecd.find_all('div', class_='roboto')[1].find('div').string
                        except IndexError:
                            description =   objecd.find_all('div', class_='verdana')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                    if cinema == '':
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    else:
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    func.rand = 12
                    objects.remove(objecd)
            except IndexError:
                bot.send_message(message.chat.id, 'Никаких новостей нет 💨')
                func.rand = 12


        elif message.text == '⬅Назад' and func.random == 8:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("🎥 Кино")
            btn2 = types.KeyboardButton("🎭 Театры")
            btn3 = types.KeyboardButton("🎤 Концерты")
            btn4 = types.KeyboardButton("🏛️ События")
            btn5 = types.KeyboardButton("🖻 Выставки")
            btn6 = types.KeyboardButton("📊 Тренинги")
            btn7 = types.KeyboardButton("🎯 Мастер-классы")
            btn8 = types.KeyboardButton("👟 Экскурсии")
            btn9 = types.KeyboardButton("🔈 Лекции")
            btn10 = types.KeyboardButton("⚽ Спорт")
            btn11 = types.KeyboardButton("🥳 Вечеринки")
            btn12 = types.KeyboardButton("🚴‍♂ Активным")
            btn13 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
            bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=markup)
            func.random = 8





        elif message.text == '🎤Караоке':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать заведения с караоке?', reply_markup=markup)
            func.random = 6

        elif message.text == '🧖‍♂Бани/Сауны':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать базы отдыха?', reply_markup=markup)
            func.random = 9

        elif message.text == '🏡База отдыха':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать базы отдыха?', reply_markup=markup)
            func.random = 8

        elif message.text == '🍽Ресторан':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать рестораны?', reply_markup=markup)
            func.random = 1

        elif message.text == '☕Кофейня/Кафе':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать кофейни/кафе?', reply_markup=markup)
            func.random = 2
        elif message.text == '💨Кальян':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать кальянные?', reply_markup=markup)
            func.random = 3
        elif message.text == '🍹Бар':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать бары?', reply_markup=markup)
            func.random = 4
        elif message.text == '🍳Завтраки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton(text="📍 Найти ближайший", request_location=True)
            btn2 = types.KeyboardButton("🎲Случайные")
            btn3 = types.KeyboardButton("⬅️Назад")
            btn4 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Как искать заведения с завтраками?', reply_markup=markup)
            func.random = 5

        elif message.text == '🎲Случайное':
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("all_objects.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("all_objects.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            print(name)
                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')


                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}](https://2gis.ru/kirov/firm/{id})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1
        elif message.text == '🎲Случайные' and func.random == 9:
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("bany.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("bany.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            print(name)
                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace(
                                '-', ':')
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1
        elif message.text == '🎲Случайные' and func.random == 8:
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("basa_otdiha.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("basa_otdiha.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            print(name)
                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace(
                                '-', ':')
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1

        elif message.text == '🎲Случайные' and func.random == 6:
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("karaoke.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("karaoke.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            print(name)
                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1

        elif message.text == '🎲Случайные' and func.random == 5:
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("breakfast.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("breakfast.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1
        elif message.text == 'Показать ещё⤵' and location.random == 1:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("restaurants.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все рестораны 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    bot.send_photo(message.chat.id, photo=img,
                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count += 1
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё⤵' and location.random == 2:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("kofeinya_cafe.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все кафе/кофейни 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    if url == '':
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')

                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    print(name)
                                    print(min_dist)
                                    rest.remove(min_dist)
                                    break
                            count += 1
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)

        elif message.text == 'Показать ещё⤵' and location.random == 3:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("kalyan.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все кальянные 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    if url == '':
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count += 1
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)

        elif message.text == 'Показать ещё⤵' and location.random == 4:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("bar.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все бары 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    if url == '':
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')

                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count += 1
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё⤵' and location.random == 5:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("breakfast.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все заведения с завтраками 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    if url == '':
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')

                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count += 1
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё⤵' and location.random == 6:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("karaoke.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все заведения с караоке 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    if url == '':
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')

                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count += 1
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё⤵' and location.random == 7:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("all_objects.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все заведения 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            try:
                                if count == 0:
                                    pass
                                else:
                                    lat = row1[10]
                                    lon = row1[11]
                                    coords_2 = (lat, lon)
                                    if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                        name = row1[0]
                                        kitchen = row1[2]
                                        category = row1[1]
                                        price = row1[3]
                                        address = row1[4]
                                        schedule = row1[5].split(sep=',')
                                        phone = row1[6]
                                        url = row1[7]
                                        phot = requests.get(row1[8])
                                        id = row1[9]
                                        out = open("img.jpg", "wb")
                                        out.write(phot.content)
                                        out.close()
                                        img = open('img.jpg', 'rb')
                                        week = datetime.datetime.today().weekday() + 1
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)

                                        schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                        if url == '':
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')

                                        else:
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                        rest.remove(min_dist)
                                        break
                                count += 1
                            except ValueError:
                                continue
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё⤵' and location.random == 8:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("basa_otdiha.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все заведения 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            try:
                                if count == 0:
                                    pass
                                else:
                                    lat = row1[10]
                                    lon = row1[11]
                                    coords_2 = (lat, lon)
                                    if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                        name = row1[0]
                                        kitchen = row1[2]
                                        category = row1[1]
                                        price = row1[3]
                                        address = row1[4]
                                        schedule = row1[5].split(sep=',')
                                        phone = row1[6]
                                        url = row1[7]
                                        phot = requests.get(row1[8])
                                        id = row1[9]
                                        out = open("img.jpg", "wb")
                                        out.write(phot.content)
                                        out.close()
                                        img = open('img.jpg', 'rb')
                                        week = datetime.datetime.today().weekday() + 1
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)

                                        schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                        if url == '':
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')

                                        else:
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                        rest.remove(min_dist)
                                        break
                                count += 1
                            except ValueError:
                                continue
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё⤵' and location.random == 9:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for k in range(3):
                    with open("bany.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        try:
                            min_dist = min(rest)
                        except ValueError:
                            bot.send_message(message.chat.id, 'Вы просмотрели все заведения 💨')
                            break
                        count = 0
                        for row1 in file_reader:
                            try:
                                if count == 0:
                                    pass
                                else:
                                    lat = row1[10]
                                    lon = row1[11]
                                    coords_2 = (lat, lon)
                                    if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                        name = row1[0]
                                        kitchen = row1[2]
                                        category = row1[1]
                                        price = row1[3]
                                        address = row1[4]
                                        schedule = row1[5].split(sep=',')
                                        phone = row1[6]
                                        url = row1[7]
                                        phot = requests.get(row1[8])
                                        id = row1[9]
                                        out = open("img.jpg", "wb")
                                        out.write(phot.content)
                                        out.close()
                                        img = open('img.jpg', 'rb')
                                        week = datetime.datetime.today().weekday() + 1
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)

                                        schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                        if url == '':
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')

                                        else:
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                        rest.remove(min_dist)
                                        break
                                count += 1
                            except ValueError:
                                continue
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё ⤵' and func.rand == 10:
            count1 = 0
            datees = []
            afisha = []
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for i in range(3):
                    count1+=1
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все новости связанные с кино 💨')
                        break
                    try:
                        objecd = objects[i]
                    except IndexError:
                        objecd = objects[-1]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find('div').find('div').find_all('div')[3].string
                    description = objecd.find('div', class_='roboto').string
                    description = textwrap.fill("Краткое описание:" + description, 40)
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Купить билеты📥", callback_data=f'info_{count1}'))
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, "html.parser")
                    about = soup.find('div', class_='newsContent').text[0:500]
                    inf = soup.find_all('div', class_='roboto')[3].find_all('div', style='display: table-row;')
                    top = ''
                    for descr in inf:
                        top += descr.find_all('div')[0].text + ' ' + descr.find_all('div')[1].text + '\n'
                    if len(about) > 1000:
                        about = about[:20] + '...'
                    print(about)
                    print(top)
                    dates = []
                    items = soup.find('div', id='eventSchedule').find_all('div', class_='Item')
                    for item in items:
                        k = item.find('div', class_='robotoBold').text + ', ' + item.find('div', class_='Date').text
                        dates.append(k)
                    print(dates)
                    datees.append(dates)
                    schedules = soup.find('div', id="scheduleBlock").find_all('div', class_='scheduleTable')
                    info_message = []
                    o = []
                    status = schedules[0].get('class')[1]
                    for schedule in schedules:
                        status1 = schedule.get('class')[1]
                        if status == status1:
                            kino = schedule.find('div', class_='robotoBold').text + '\n' + schedule.find('div',
                                                                                                         style='color:#808184; font-size:10px; margin-top:3px;').text
                            url1 = schedule.find('a').get('href')
                            format = schedule.find_all('div', class_='td')[1].find('div',
                                                                                   style='display:table-cell; width:84px; font-size:12px; font-weight:bold;').text
                            seanses = schedule.find_all('div', class_='td')[1].find('div', class_='seanceList').find_all(
                                'span')
                            seanse = ''
                            for i in seanses:
                                try:
                                    if i.get('class')[0] == "NA":
                                        seanse += '~~' + i.text + '~~' + ' '
                                    else:
                                        seanse += i.text + ' '
                                except TypeError:
                                    seanse += i.text + ' '
                            print(kino)
                            print(url1)
                            print(format)
                            print(seanse)
                            print('\n')
                            u = f"*Название кинотеатра:* {kino.replace('Телефон:', '*Телефон:*')}\n{url1}\n{format}\n *Сеансы:* {seanse}"
                            o.append(u)
                        else:
                            info_message.append(o)
                            o = []
                            kino = schedule.find('div', class_='robotoBold').text + '\n' + schedule.find('div',
                                                                                                         style='color:#808184; font-size:10px; margin-top:3px;').text
                            url1 = schedule.find('a').get('href')
                            format = schedule.find_all('div', class_='td')[1].find('div',
                                                                                   style='display:table-cell; width:84px; font-size:12px; font-weight:bold;').text
                            seanses = schedule.find_all('div', class_='td')[1].find('div', class_='seanceList').find_all(
                                'span')
                            seanse = ''
                            for i in seanses:
                                try:
                                    if i.get('class')[0] == "NA":
                                        seanse += '~~' + i.text + '~~' + ' '
                                    else:
                                        seanse += i.text + ' '
                                except TypeError:
                                    seanse += i.text + ' '
                            print(kino)
                            print(url1)
                            print(format)
                            print(seanse)
                            print('\n')
                            u = f"*Название кинотеатра:* {kino.replace('Телефон:', '*Телефон:*')}\n{url1}\n{format}\n *Сеансы:* {seanse}"
                            o.append(u)
                        status = schedule.get('class')[1]
                    info_message.append(o)

                    print(info_message)
                    bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'),
                                   caption=f"[{name}]({url}) {age}\n\n {about}\n\nКинотеатры: {cinema} \n\n {top}",
                                   parse_mode='Markdown', reply_markup=info)
                    func.rand = 10
                    objects.remove(objecd)
                    afisha.append(info_message)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё ⤵' and func.rand == 11:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for i in range(3):
                    count1 += 1
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все события 💨')
                        break
                    try:
                        objecd = objects[i]
                    except IndexError:
                        objecd = objects[-1]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        #date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                    except IndexError:
                        #description = objecd.find_all('div', class_='verdana')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        #date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Расписание/Где купить📥", callback_data=f'teatr1_{count1}'))
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, "html.parser")
                    about = soup.find('div', class_='newsContent').text[0:500]
                    inf = soup.find_all('div', class_='roboto')[3].find_all('div', style='display: table-row;')
                    top = ''
                    for descr in inf:
                        top += descr.find_all('div')[0].text + ' ' + descr.find_all('div')[1].text + '\n'
                    if len(about) > 1000:
                        about = about[:20] + '...'
                    teatr = []
                    items = soup.find_all('div', class_='scheduleTable')  # .find_all('div', class_='Item')
                    for item in items:
                        date_teatr = item.find_all('div', class_='roboto')[0].find('b').text
                        time_teatr = item.find_all('div', class_='roboto')[0].text.replace(date_teatr, '').strip().replace(
                            '\t', '')
                        place_teatr = item.find('div', class_='robotoBold').text.strip()
                        adress_teatr = \
                        item.find('div', style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                            'div')[0].text.strip()
                        phone_teatr = \
                        item.find('div', style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                            'div')[1].text.strip()
                        price_teatr = item.find('div', class_='roboto',
                                                style='display:table-cell; font-size:16px;').text.strip()
                        if time_teatr == '':
                            dat_teatr = f"{date_teatr}"
                        else:
                            dat_teatr = f"{date_teatr}, {time_teatr}"
                        if adress_teatr == '':
                            plac_teatr = f"{place_teatr.replace(',', '')}"
                        else:
                            plac_teatr = f"{place_teatr}, {adress_teatr}"
                        if phone_teatr == 'Телефон:':
                            phone_teatr = 'Не указан'
                        if "Театр на Спасской" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://ekvus-kirov.ru/afisha/show/")
                        elif "Органный зал" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovorgan.ru/afisha/")
                        elif "Драматический театр" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovdramteatr.ru/shows/")
                        elif "Театр кукол" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirovkukla.ru/afisha")
                        elif "Филармония" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://www.philarmonia43.ru/events/")
                        elif "ОДНТ" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://kirov.kassy.ru/venue/kogauk-oblastnojj-dom-narodnogo-tvorchestva-oktyabrskijj-pr-kt-38-46/")
                        elif "Родина" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://xn----8sbkbujyfr.xn--p1ai/afisha/")
                        elif "Mr. Green" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/mister-green")
                        elif "Квартира" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/kvartira-kirov?source=search-page")
                        elif "СКЦ Семья" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/semia-kirov/schedule")
                        elif "Атмосфера" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/atmosfera-kirov/schedule")
                        elif "Конструктор-Практик" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/konstruktor-praktik")
                        elif "ДК железнодорожников" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://dkrzdkirov.ru/afisha/")
                        elif "Цирк" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/theatre/places/tsirk-57efcca6685ae0c36a5a5797/schedule")
                        elif "Тир" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://vk.com/tir_kot")
                        elif "GAUDI" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://gaudikirov.ru/afisha/")
                        elif "Руки Вверх" in place_teatr:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\nhttps://afisha.yandex.ru/kirov/concert/places/ruki-vverkh-bar-kirov/schedule")
                        else:
                            teatr.append(
                                f"*{name}*\n*ДАТА:* {dat_teatr}\n*МЕСТО:* {plac_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\n{url}")
                    teatrs.append(teatr)
                    print(teatrs)
                    bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'),
                                   caption=f"[{name}]({url}) {age}\n\n {about}\n\n{cinema.strip()} \n\n {top}",
                                   parse_mode='Markdown', reply_markup=info)
                    objects.remove(objecd)
                    func.random == 8
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё ⤵' and func.rand == 12:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for i in range(3):
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все новости 💨')
                        break
                    try:
                        objecd = objects[i]
                    except IndexError:
                        objecd = objects[-1]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        try:
                            date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                        except IndexError:
                            date = cinema.strip()
                            cinema = ''
                    except IndexError:
                        description = objecd.find_all('div', class_='roboto')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Подробнее📥", callback_data='info', url=url))
                    if cinema == '':
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    else:
                        bot.send_photo(message.chat.id, photo=img,
                                       caption=f"[{name}]({url}) {age}\n\n {description}\n\nМеста проведения: {cinema}\n\n{date}",
                                       parse_mode='Markdown', reply_markup=info)
                    func.rand = 12
                    func.random == 8
                    objects.remove(objecd)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)
        elif message.text == 'Показать ещё ⤵' and func.rand == 13:
            channel = '@kirovchano'
            status = ['creator', 'administrator', 'member']
            check = False
            datees = []
            for stat in status:
                if stat == bot.get_chat_member(chat_id="@kirovchano", user_id=message.from_user.id).status:
                    check = True
            if check == True:
                for i in range(3):
                    if objects == []:
                        bot.send_message(message.chat.id, 'Вы просмотрели все события 💨')
                        break
                    try:
                        objecd = objects[i]
                    except IndexError:
                        objecd = objects[-1]
                    name = objecd.find('div', class_='robotoBold').find('a').string
                    age = objecd.find_all('div')[1].find('div').string
                    try:
                        description = objecd.find('div', class_='roboto').string
                        description = textwrap.fill("Краткое описание: " + description, 40)
                    except AttributeError:
                        description = ''
                    url = 'https://kirov-portal.ru' + objecd.find('div', class_='robotoBold').find('a').get('href')
                    img = requests.get('https://kirov-portal.ru' + objecd.find('img').get('src'))
                    try:
                        cinema = objecd.find_all('div', class_='roboto')[1].find('div').string
                        try:
                            date = objecd.find_all('div', class_='roboto')[1].find_all('div')[1].string.strip()
                        except IndexError:
                            date = cinema.strip()
                            cinema = ''
                    except IndexError:
                        # description =  objecd.find_all('div', class_='roboto')[1].find('div').string
                        cinema = objecd.find_all('div', class_='verdana')[0].find('div').string
                        date = objecd.find_all('div', class_='verdana')[0].find_all('div')[1].string.strip()
                    out = open("img.jpg", "wb")
                    out.write(img.content)
                    out.close()
                    img = open('img.jpg', 'rb')
                    info = types.InlineKeyboardMarkup(row_width=2)
                    info.add(
                        types.InlineKeyboardButton(text="Расписание/Где купить📥", callback_data=f'teatr_{count1}'))
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, "html.parser")
                    about = soup.find('div', class_='newsContent').text[0:500]
                    inf = soup.find_all('div', class_='roboto')[3].find_all('div', style='display: table-row;')
                    top = ''
                    for descr in inf:
                        top += descr.find_all('div')[0].text + ' ' + descr.find_all('div')[1].text + '\n'
                    if len(about) > 1000:
                        about = about[:20] + '...'
                    teatr = []
                    items = soup.find_all('div', class_='scheduleTable', limit=3)  # .find_all('div', class_='Item')
                    countt = 0
                    for item in items:
                        countt += 1
                        date_teatr = item.find_all('div', class_='roboto')[0].find('b').text
                        time_teatr = item.find_all('div', class_='roboto')[0].text.replace(date_teatr, '').strip().replace(
                            '\t', '')
                        place_teatr = item.find('div', class_='robotoBold').text.strip()
                        adress_teatr = \
                            item.find('div',
                                      style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                                'div')[0].text.strip()
                        phone_teatr = \
                            item.find('div',
                                      style='color:#808184; font-size:10px; line-height:16px; margin-top:3px;').find_all(
                                'div')[1].text.strip()
                        price_teatr = item.find('div', class_='roboto',
                                                style='display:table-cell; font-size:16px;').text.strip()
                        # print(items[-1])
                        if item == items[-1]:
                            teatr.append(
                                f"{name}\n*ДАТА:* {date_teatr}, {time_teatr}\n*МЕСТО:* {place_teatr}, {adress_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}\n[ПОДРОБНЕЕ...]({url})")
                        else:
                            teatr.append(
                                f"{name}\n*ДАТА:* {date_teatr}, {time_teatr}\n*МЕСТО:* {place_teatr}, {adress_teatr}\n*ТЕЛЕФОН:* {phone_teatr}\n*СТОИМОСТЬ БИЛЕТА:* {price_teatr}")

                    teatrs.append(teatr)
                    # teatrs.append(f"[...]({url})")
                    print(teatrs)
                    bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'),
                                   caption=f"[{name}]({url}) {age}\n\n {about}\n\n {cinema} \n\n {top}",
                                   parse_mode='Markdown', reply_markup=info)
                    func.random == 8
                    func.rand = 13
                    objects.remove(objecd)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Проверить подписку 🔄")
                markup.add(btn1)
                bot.send_message(message.chat.id,
                                 f'Привет, чтобы полноценно пользоваться ботом подпишись на канал: {channel}',
                                 reply_markup=markup)

        elif message.text == '⬅Назад' and func.randomi == 10:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Показать ещё ⤵")
            btn2 = types.KeyboardButton("⬅️Назад")
            btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, "Возвращаем обратно", reply_markup=markup)
            func.rand = qwert
        elif message.text == '⬅️Назад' and func.randomi == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("🍽Ресторан")
            btn2 = types.KeyboardButton("☕Кофейня/Кафе")
            btn3 = types.KeyboardButton("🍹Бар")
            btn4 = types.KeyboardButton("🍳Завтраки")
            btn5 = types.KeyboardButton("💨Кальян")
            btn6 = types.KeyboardButton("🎤Караоке")
            btn7 = types.KeyboardButton("🏡База отдыха")
            btn8 = types.KeyboardButton("🧖‍♂Бани/Сауны")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
            markup.add(types.KeyboardButton('⏪Вернутся в главное меню'))
            bot.send_message(message.chat.id, 'Выберите, что ищем', reply_markup=markup)



        elif message.text == '🎲Случайные' and func.random == 4:
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("bar.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("bar.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1

        elif message.text == '🎲Случайные' and func.random == 3:
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("kalyan.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("kalyan.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                            print(name)
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1

        elif message.text == '🎲Случайные' and func.random == 2:
            bot.send_message(message.chat.id, 'Подбираем...🔄')
            with open("kofeinya_cafe.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("kofeinya_cafe.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:

                            name = row[0]

                            kitchen = row[2]
                            category = row[1]
                            price = row[3].replace('Средний чек', '')
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count += 1

        elif message.text == '🎲Случайные' and func.random == 1:
            with open("restaurants.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                len_objects = sum(1 for row in file_reader)
            with open("restaurants.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for l in range(3):
                    #print()
                    num_run = randint(0, len_objects)
                    num_run1 = randint(0, len_objects)
                    num_run2 = randint(0, len_objects)
                    for row in file_reader:
                        if count == 0:
                            pass
                        elif count == num_run or count == num_run1 or count == num_run2:
                            name = row[0]
                            #print(count)
                            kitchen = row[2]
                            category = row[1]
                            price = row[3]
                            address = row[4]
                            schedule = row[5].split(sep=',')
                            phone = row[6]
                            url = row[7]
                            phot = requests.get(row[8])
                            id = row[9]
                            out = open("img.jpg", "wb")
                            out.write(phot.content)
                            out.close()
                            img = open('img.jpg', 'rb')
                            week = datetime.datetime.today().weekday() + 1
                            markup = types.InlineKeyboardMarkup()
                            button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                            markup.add(button1)

                            schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                            if url == '':
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')

                            else:
                                if phone != '':
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                else:
                                    if kitchen == '':
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)
                                        if price == '':
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            bot.send_photo(message.chat.id, photo=img,
                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                           reply_markup=markup, parse_mode='Markdown')
                        count+=1
        elif len(datees) > 0:
            coun = 0
            coun1 = 0
            for i in datees:
                coun += 1
                coun1 = 0
                for g in i:
                    coun1 += 1
                    if message.text == g and message_day == coun:
                        print(coun, coun1, g)
                        print(afisha)
                        for kino in afisha[coun - 1][coun1 - 1]:
                            print()
                            urll = kino.split()[6]
                            print(kino.split())
                            markup = types.InlineKeyboardMarkup()
                            button1 = types.InlineKeyboardButton("ЗАБРОНИРОВАТЬ", url=urll)
                            markup.add(button1)
                            about_afisha = kino.replace(kino.split()[6] + '\n', '')
                            bot.send_message(message.chat.id,
                                             about_afisha, parse_mode='Markdown', reply_markup=markup)


        else:
            log = 0
            with open("all_objects.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                nam = (str(message.text)).lower()
                for row in file_reader:
                    #print(row[0])
                    nam1 = row[0].lower()
                    print(nam1)
                    print(nam)
                    if nam in nam1:

                        name = row[0]
                        kitchen = row[2]
                        category = row[1]
                        price = row[3]
                        address = row[4]
                        schedule = row[5].split(sep=',')
                        phone = row[6]
                        url = row[7]
                        phot = requests.get(row[8])
                        id = row[9]
                        out = open("img.jpg", "wb")
                        out.write(phot.content)
                        out.close()
                        img = open('img.jpg', 'rb')
                        week = datetime.datetime.today().weekday() + 1
                        markup = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                        markup.add(button1)

                        schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace("-",
                                                                                                                 ' ')
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        btn1 = types.KeyboardButton("🔎Категории")
                        btn2 = types.KeyboardButton(text="📍 Найти ближайшие", request_location=True)
                        btn3 = types.KeyboardButton("📅 Афиша")
                        btn4 = types.KeyboardButton("🎲Случайное")
                        markup.add(btn1, btn2, btn3, btn4)
                        if url == '':
                            if phone != '':
                                if kitchen == '':
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                else:
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                            else:
                                if kitchen == '':
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                else:
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')

                        else:
                            if phone != '':
                                if kitchen == '':
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                else:
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                       reply_markup=markup, parse_mode='Markdown')
                            else:
                                if kitchen == '':
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                else:
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    if price == '':
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        bot.send_photo(message.chat.id, photo=img,
                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                       reply_markup=markup, parse_mode='Markdown')
                        log+=1
                if log == 0:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    btn1 = types.KeyboardButton("🔎Категории")
                    btn2 = types.KeyboardButton(text="📍 Найти ближайшие", request_location=True)
                    btn3 = types.KeyboardButton("📅 Афиша")
                    btn4 = types.KeyboardButton("🎲Случайное")
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id,
                                     'Подбери заведение по категории, найди ближайшее или случайное заведение Кирова.\nЖми кнопки внизу 👇',
                                     reply_markup=markup)
                    func.random = 7

    except ValueError:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("🔎Категории")
        btn2 = types.KeyboardButton(text="📍 Найти ближайшие", request_location=True)
        btn3 = types.KeyboardButton("📅 Афиша")
        btn4 = types.KeyboardButton("🎲Случайное")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,
                         'Произошла ошибка попробуйте еще раз ❌', reply_markup=markup)
    except IndexError:
        bot.send_message(message.chat.id,
                         'Никаких новостей нет')
    except AttributeError or telebot.apihelper.ApiTelegramException:
        bot.send_message(message.chat.id,
                         'Попробуйте еще раз выбрать нужную вам категорию или вернитесь в главное меню или напишите команду /start')



@bot.message_handler(content_types=['location'])
def location(message):
    global rest
    global coords_1
    if message.location is not None and func.random == 1:
        location.random = 1
        rest = []
        with open("restaurants.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            coords_1 = (message.location.latitude, message.location.longitude)
            for row in file_reader:
                if count == 0:
                    pass
                else:
                    lat = row[10]
                    lon = row[11]
                    coords_2 = (lat, lon)
                    distance = geopy.distance.geodesic(coords_1, coords_2).km
                    if distance <= 5:
                        rest.append(distance)
                count+=1
            if rest == []:
                bot.send_message(message.chat.id, 'У вас поблизости нет никаких ресторанов 💨')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Показать ещё⤵")
                btn2 = types.KeyboardButton("⬅️Назад")
                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, 'Ищем ближайшие рестораны..', reply_markup=markup)
                for k in range(3):
                    with open("restaurants.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        min_dist = min(rest)
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    print(name, url)
                                    schedule = schedule[week-1].replace(']', '').replace("'", '').replace('[', '').replace("-", ' ')
                                    if url == '':
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')

                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count+=1
    elif message.location is not None and func.random == 9:
        location.random = 9
        rest = []
        with open("bany.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            coords_1 = (message.location.latitude, message.location.longitude)
            for row in file_reader:
                try:
                    if count == 0:
                        pass
                    else:
                        lat = row[10]
                        lon = row[11]
                        coords_2 = (lat, lon)
                        distance = geopy.distance.geodesic(coords_1, coords_2).km
                        if distance <= 50:
                            rest.append(distance)
                    count+=1
                except ValueError:
                    continue
            if rest == []:
                bot.send_message(message.chat.id, 'У вас поблизости нет никаких заведений 💨')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Показать ещё⤵")
                btn2 = types.KeyboardButton("⬅️Назад")
                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, 'Ищем ближайшие заведения', reply_markup=markup)
                for k in range(3):
                        with open("bany.csv", encoding='utf-8') as r_file:
                            file_reader = csv.reader(r_file, delimiter=",")
                            min_dist = min(rest)
                            count = 0
                            for row1 in file_reader:
                                try:
                                    if count == 0:
                                        pass
                                    else:
                                        lat = row1[10]
                                        lon = row1[11]
                                        coords_2 = (lat, lon)
                                        if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                            name = row1[0]
                                            kitchen = row1[2]
                                            category = row1[1]
                                            price = row1[3].replace('Средний чек', '')
                                            address = row1[4]
                                            schedule = row1[5].split(sep=',')
                                            phone = row1[6]
                                            url = row1[7]
                                            phot = requests.get(row1[8])
                                            id = row1[9]
                                            out = open("img.jpg", "wb")
                                            out.write(phot.content)
                                            out.close()
                                            img = open('img.jpg', 'rb')
                                            week = datetime.datetime.today().weekday() + 1
                                            markup = types.InlineKeyboardMarkup()
                                            button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                            markup.add(button1)

                                            schedule = schedule[week-1].replace(']', '').replace("'", '').replace('[', '').replace("-", ' ')
                                            if url == '':
                                                if phone != '':
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')

                                            else:
                                                if phone != '':
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                            rest.remove(min_dist)
                                            break
                                    count+=1
                                except ValueError:
                                    continue
    elif message.location is not None and func.random == 8:
        location.random = 8
        rest = []
        with open("basa_otdiha.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            coords_1 = (message.location.latitude, message.location.longitude)
            for row in file_reader:
                try:
                    if count == 0:
                        pass
                    else:
                        lat = row[10]
                        lon = row[11]
                        coords_2 = (lat, lon)
                        distance = geopy.distance.geodesic(coords_1, coords_2).km
                        if distance <= 50:
                            rest.append(distance)
                    count+=1
                except ValueError:
                    continue
            if rest == []:
                bot.send_message(message.chat.id, 'У вас поблизости нет никаких заведений 💨')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Показать ещё⤵")
                btn2 = types.KeyboardButton("⬅️Назад")
                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, 'Ищем ближайшие заведения', reply_markup=markup)
                for k in range(3):
                        with open("basa_otdiha.csv", encoding='utf-8') as r_file:
                            file_reader = csv.reader(r_file, delimiter=",")
                            min_dist = min(rest)
                            count = 0
                            for row1 in file_reader:
                                try:
                                    if count == 0:
                                        pass
                                    else:
                                        lat = row1[10]
                                        lon = row1[11]
                                        coords_2 = (lat, lon)
                                        if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                            name = row1[0]
                                            kitchen = row1[2]
                                            category = row1[1]
                                            price = row1[3].replace('Средний чек', '')
                                            address = row1[4]
                                            schedule = row1[5].split(sep=',')
                                            phone = row1[6]
                                            url = row1[7]
                                            phot = requests.get(row1[8])
                                            id = row1[9]
                                            out = open("img.jpg", "wb")
                                            out.write(phot.content)
                                            out.close()
                                            img = open('img.jpg', 'rb')
                                            week = datetime.datetime.today().weekday() + 1
                                            markup = types.InlineKeyboardMarkup()
                                            button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                            markup.add(button1)

                                            schedule = schedule[week-1].replace(']', '').replace("'", '').replace('[', '').replace("-", ' ')
                                            if url == '':
                                                if phone != '':
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                             url=f'https://2gis.ru/kirov/firm/{id}')
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')

                                            else:
                                                if phone != '':
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    if kitchen == '':
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        markup = types.InlineKeyboardMarkup()
                                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                        markup.add(button1)
                                                        if price == '':
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                                        else:
                                                            bot.send_photo(message.chat.id, photo=img,
                                                                           caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                           reply_markup=markup, parse_mode='Markdown')
                                            rest.remove(min_dist)
                                            break
                                    count+=1
                                except ValueError:
                                    continue
    elif message.location is not None and func.random == 7:
        location.random = 7
        rest = []
        with open("all_objects.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            coords_1 = (message.location.latitude, message.location.longitude)
            for row in file_reader:
                try:
                    if count == 0:
                        pass
                    else:
                        lat = row[10]
                        lon = row[11]
                        coords_2 = (lat, lon)
                        distance = geopy.distance.geodesic(coords_1, coords_2).km
                        if distance <= 5:
                            rest.append(distance)
                    count+=1
                except ValueError:
                    continue
            if rest == []:
                bot.send_message(message.chat.id, 'У вас поблизости нет никаких заведений 💨')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Показать ещё⤵")
                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
                markup.add(btn1, btn3)
                bot.send_message(message.chat.id, 'Ищем ближайшие заведения', reply_markup=markup)
                for k in range(3):
                    #try:
                        with open("all_objects.csv", encoding='utf-8') as r_file:
                            file_reader = csv.reader(r_file, delimiter=",")
                            min_dist = min(rest)
                            count = 0
                            for row1 in file_reader:
                                if count == 0:
                                    pass
                                else:
                                    lat = row1[10]
                                    lon = row1[11]
                                    coords_2 = (lat, lon)
                                    if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                        name = row1[0]
                                        kitchen = row1[2]
                                        category = row1[1]
                                        price = row1[3].replace('Средний чек', '')
                                        address = row1[4]
                                        schedule = row1[5].split(sep=',')
                                        phone = row1[6]
                                        url = row1[7]
                                        phot = requests.get(row1[8])
                                        id = row1[9]
                                        out = open("img.jpg", "wb")
                                        out.write(phot.content)
                                        out.close()
                                        img = open('img.jpg', 'rb')
                                        week = datetime.datetime.today().weekday() + 1
                                        markup = types.InlineKeyboardMarkup()
                                        button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                        markup.add(button1)

                                        schedule = schedule[week-1].replace(']', '').replace("'", '').replace('[', '').replace("-", ' ')
                                        if url == '':
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                         url=f'https://2gis.ru/kirov/firm/{id}')
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')

                                        else:
                                            if phone != '':
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                if kitchen == '':
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    markup = types.InlineKeyboardMarkup()
                                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                    markup.add(button1)
                                                    if price == '':
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                                    else:
                                                        bot.send_photo(message.chat.id, photo=img,
                                                                       caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                       reply_markup=markup, parse_mode='Markdown')
                                        rest.remove(min_dist)
                                        break
                                count+=1
                    #except ValueError:
                    #    continue

    elif message.location is not None and func.random == 2:
        location.random = 2
        rest = []
        with open("kofeinya_cafe.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            coords_1 = (message.location.latitude, message.location.longitude)
            for row in file_reader:
                if count == 0:
                    pass
                else:
                    lat = row[10]
                    lon = row[11]
                    coords_2 = (lat, lon)
                    distance = geopy.distance.geodesic(coords_1, coords_2).km
                    if distance <= 5:
                        rest.append(distance)
                count+=1
            if rest == []:
                bot.send_message(message.chat.id, 'У вас поблизости нет никаких кафе  💨')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Показать ещё⤵")
                btn2 = types.KeyboardButton("⬅️Назад")
                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, 'Ищем ближайшие кафе..', reply_markup=markup)
                for k in range(3):
                    with open("kofeinya_cafe.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        min_dist = min(rest)
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                print(coords_1, coords_2)
                                print(geopy.distance.geodesic(coords_1, coords_2).km)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    rest.remove(min_dist)
                                    name = row1[0]
                                    print(name)
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3]
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    name1 = row1[0]
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[',
                                                                                                            '').replace(
                                        '-', ':')
                                    if url == '':
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    print(min_dist)
                                    break
                            count += 1


    elif message.location is not None and func.random == 3:
        location.random = 3
        rest = []
        with open("kalyan.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            coords_1 = (message.location.latitude, message.location.longitude)
            for row in file_reader:
                if count == 0:
                    pass
                else:
                    lat = row[10]
                    lon = row[11]
                    coords_2 = (lat, lon)
                    distance = geopy.distance.geodesic(coords_1, coords_2).km
                    if distance <= 5:
                        rest.append(distance)
                count += 1
            if rest == []:
                bot.send_message(message.chat.id, 'У вас поблизости нет никаких кальянных  💨')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Показать ещё⤵")
                btn2 = types.KeyboardButton("⬅️Назад")
                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, 'Ищем ближайшие кальянных..', reply_markup=markup)
                for k in range(3):
                    with open("kalyan.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        min_dist = min(rest)
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    print(name)
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3].replace('Средний чек', '')
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    if url == '':
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')

                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count += 1

    elif message.location is not None and func.random == 4:
        location.random = 4
        rest = []
        with open("bar.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            coords_1 = (message.location.latitude, message.location.longitude)
            for row in file_reader:
                if count == 0:
                    pass
                else:
                    lat = row[10]
                    lon = row[11]
                    coords_2 = (lat, lon)
                    distance = geopy.distance.geodesic(coords_1, coords_2).km
                    if distance <= 5:
                        rest.append(distance)
                count += 1
            if rest == []:
                bot.send_message(message.chat.id, 'У вас поблизости нет никаких баров  💨')
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton("Показать ещё⤵")
                btn2 = types.KeyboardButton("⬅️Назад")
                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, 'Ищем ближайшие бары..', reply_markup=markup)
                for k in range(3):
                    with open("bar.csv", encoding='utf-8') as r_file:
                        file_reader = csv.reader(r_file, delimiter=",")
                        min_dist = min(rest)
                        count = 0
                        for row1 in file_reader:
                            if count == 0:
                                pass
                            else:
                                lat = row1[10]
                                lon = row1[11]
                                coords_2 = (lat, lon)
                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:
                                    name = row1[0]
                                    kitchen = row1[2]
                                    category = row1[1]
                                    price = row1[3].replace('Средний чек', '')
                                    address = row1[4]
                                    schedule = row1[5].split(sep=',')
                                    phone = row1[6]
                                    url = row1[7]
                                    phot = requests.get(row1[8])
                                    id = row1[9]
                                    out = open("img.jpg", "wb")
                                    out.write(phot.content)
                                    out.close()
                                    img = open('img.jpg', 'rb')
                                    week = datetime.datetime.today().weekday() + 1
                                    markup = types.InlineKeyboardMarkup()
                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                    markup.add(button1)
                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[', '').replace('-', ':').replace('Вс:', '').replace('Пн:', '').replace('Вт:', '').replace('Ср:', '').replace('Чт:', '').replace('Пт:', '').replace('Сб:', '')
                                    if url == '':
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Показать на карте",
                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')

                                    else:
                                        if phone != '':
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                        else:
                                            if kitchen == '':
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                            else:
                                                markup = types.InlineKeyboardMarkup()
                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)
                                                markup.add(button1)
                                                if price == '':
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                                else:
                                                    bot.send_photo(message.chat.id, photo=img,
                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",
                                                                   reply_markup=markup, parse_mode='Markdown')
                                    rest.remove(min_dist)
                                    break
                            count += 1

    elif message.location is not None and func.random == 5:

        location.random = 5

        rest = []

        with open("breakfast.csv", encoding='utf-8') as r_file:

            file_reader = csv.reader(r_file, delimiter=",")

            count = 0

            coords_1 = (message.location.latitude, message.location.longitude)

            for row in file_reader:

                if count == 0:

                    pass

                else:

                    lat = row[10]

                    lon = row[11]

                    coords_2 = (lat, lon)

                    distance = geopy.distance.geodesic(coords_1, coords_2).km

                    if distance <= 5:
                        rest.append(distance)

                count += 1

            if rest == []:

                bot.send_message(message.chat.id, 'У вас поблизости нет никаких заведений 💨')

            else:

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

                btn1 = types.KeyboardButton("Показать ещё⤵")

                btn2 = types.KeyboardButton("⬅️Назад")

                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")

                markup.add(btn1, btn2, btn3)

                bot.send_message(message.chat.id, 'Ищем ближайшие заведения..', reply_markup=markup)

                for k in range(3):

                    with open("breakfast.csv", encoding='utf-8') as r_file:

                        file_reader = csv.reader(r_file, delimiter=",")

                        min_dist = min(rest)

                        count = 0

                        for row1 in file_reader:

                            if count == 0:

                                pass

                            else:

                                lat = row1[10]

                                lon = row1[11]

                                coords_2 = (lat, lon)

                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:

                                    name = row1[0]

                                    kitchen = row1[2]

                                    category = row1[1]

                                    price = row1[3]

                                    address = row1[4]

                                    schedule = row1[5].split(sep=',')

                                    phone = row1[6]

                                    url = row1[7]

                                    phot = requests.get(row1[8])

                                    id = row1[9]

                                    out = open("img.jpg", "wb")

                                    out.write(phot.content)

                                    out.close()

                                    img = open('img.jpg', 'rb')

                                    week = datetime.datetime.today().weekday() + 1

                                    markup = types.InlineKeyboardMarkup()

                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                    markup.add(button1)

                                    print(name, url)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[',
                                                                                                            '').replace(
                                        "-", ' ')

                                    if url == '':

                                        if phone != '':

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                        else:

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')


                                    else:

                                        if phone != '':

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                        else:

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                    rest.remove(min_dist)

                                    break

                            count += 1

    elif message.location is not None and func.random == 6:

        location.random = 6

        rest = []

        with open("karaoke.csv", encoding='utf-8') as r_file:

            file_reader = csv.reader(r_file, delimiter=",")

            count = 0

            coords_1 = (message.location.latitude, message.location.longitude)

            for row in file_reader:

                if count == 0:

                    pass

                else:

                    lat = row[10]

                    lon = row[11]

                    coords_2 = (lat, lon)

                    distance = geopy.distance.geodesic(coords_1, coords_2).km

                    if distance <= 5:
                        rest.append(distance)

                count += 1

            if rest == []:

                bot.send_message(message.chat.id, 'У вас поблизости нет никаких заведения 💨')

            else:

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

                btn1 = types.KeyboardButton("Показать ещё⤵")

                btn2 = types.KeyboardButton("⬅️Назад")

                btn3 = types.KeyboardButton("⏪Вернутся в главное меню")

                markup.add(btn1, btn2, btn3)

                bot.send_message(message.chat.id, 'Ищем ближайшие заведения..', reply_markup=markup)

                for k in range(3):

                    with open("karaoke.csv", encoding='utf-8') as r_file:

                        file_reader = csv.reader(r_file, delimiter=",")

                        min_dist = min(rest)

                        count = 0

                        for row1 in file_reader:

                            if count == 0:

                                pass

                            else:

                                lat = row1[10]

                                lon = row1[11]

                                coords_2 = (lat, lon)

                                if min_dist == geopy.distance.geodesic(coords_1, coords_2).km:

                                    name = row1[0]

                                    kitchen = row1[2]

                                    category = row1[1]

                                    price = row1[3]

                                    address = row1[4]

                                    schedule = row1[5].split(sep=',')

                                    phone = row1[6]

                                    url = row1[7]

                                    phot = requests.get(row1[8])

                                    id = row1[9]

                                    out = open("img.jpg", "wb")

                                    out.write(phot.content)

                                    out.close()

                                    img = open('img.jpg', 'rb')

                                    week = datetime.datetime.today().weekday() + 1

                                    markup = types.InlineKeyboardMarkup()

                                    button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                    markup.add(button1)

                                    print(name, url)

                                    schedule = schedule[week - 1].replace(']', '').replace("'", '').replace('[',
                                                                                                            '').replace(
                                        "-", ' ')

                                    if url == '':

                                        if phone != '':

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                        else:

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Показать на карте",

                                                                                     url=f'https://2gis.ru/kirov/firm/{id}')

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({f'https://2gis.ru/kirov/firm/{id}'})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')


                                    else:

                                        if phone != '':

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}\n📞Телефон: {phone}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                        else:

                                            if kitchen == '':

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                            else:

                                                markup = types.InlineKeyboardMarkup()

                                                button1 = types.InlineKeyboardButton("Сайт/меню", url=url)

                                                markup.add(button1)

                                                if price == '':

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                                else:

                                                    bot.send_photo(message.chat.id, photo=img,

                                                                   caption=f"[{name}]({url})\n\n🔎Категория: {category}\n👨‍🍳Кухня: {kitchen}\n💵Ценовой диапазон: {price}\n [🗂Отзывы](https://2gis.ru/kirov/firm/{id}/tab/reviews)\n📍Адрес: [{address}](https://2gis.ru/kirov/firm/{id})\n🕑Режим работы: {schedule}",

                                                                   reply_markup=markup, parse_mode='Markdown')

                                    rest.remove(min_dist)

                                    break

                            count += 1





    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю.\nВыберите нужную вам категорию')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global message_day
    global qwert
    for i in range(1, count1+1):
        if call.data == f'info_{i}':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            #print(datees)
            #print(i)
            message_day = i
            dates = datees[i-1]
            for n in dates:
                markup.add(types.KeyboardButton(n))
            markup.add(types.KeyboardButton('⬅Назад'))
            bot.send_message(call.message.chat.id, 'Расписание фильма\nВыберите дату показа:', reply_markup=markup)
            qwert = func.rand
            #print(func.rand)
            func.randomi = 10
            #print(afisha)
            print(afisha)
    for i in range(1, count1+1):
        if call.data == f'teatr_{i}':
            #print(teatrs)
            for t in teatrs[i-1]:
                bot.send_message(call.message.chat.id, t, parse_mode='Markdown')
            qwert = func.rand
            func.randomi = 10
    for i in range(1, count1+1):
        if call.data == f'teatr1_{i}':
            for t in teatrs[i-1]:
                urll = t.split()[-1]
                print(t.split()[-1])
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("ЗАБРОНИРОВАТЬ", url=urll)
                markup.add(button1)
                bot.send_message(call.message.chat.id, t.replace(urll, ''), parse_mode='Markdown', reply_markup=markup)
            qwert = func.rand
            func.randomi = 10





bot.polling(none_stop=True)


