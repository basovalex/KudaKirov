import csv
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from ymaps import SearchClient
import datetime
import time
from selenium.webdriver.common.keys import Keys

#response = requests.get("type=&&page_size=10&page=1&key=ruoqhu5955")
#data = response.json()
#print(1)
api_key = '9fa2ee91-694a-4fd2-adbc-b3b7e0c1a633'
client = SearchClient(api_key)
d = datetime.datetime.today()


def bany():
    with open("banya_parser.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_banya = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("bany.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]

                    count1 += 1
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    # element.send_keys("Сатир,бар")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    # try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    # except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[20]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[22]
                        if url == '':
                            url = row[23]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_banya.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_banya
def basa_otdiha():
    with open("23345334.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_basa = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("basa_otdiha.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]

                    count1 += 1
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    # element.send_keys("Сатир,бар")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    # try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    # except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[19]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[20]
                        if url == '':
                            url = row[21]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_basa.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_basa
def restoraunts():
    with open("4343434.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_rest = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("restaurants.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]

                    count1 += 1
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    # element.send_keys("Сатир,бар")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    # try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    # except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[19]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[21]
                        if url == '':
                            url = row[22]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_rest.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_rest

def kalyan():
    with open("098789.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_kalyan = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("kalyan.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]

                    count1 += 1
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    # element.send_keys("Сатир,бар")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    # try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    # except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[18]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[20]
                        if url == '':
                            url = row[21]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_kalyan.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_kalyan

def kafe_cofeinya():
    with open("2323.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_kafe = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("kofeinya_cafe.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                count1 += 1
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    #element.send_keys("Огонек Советская улица, 13")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    # try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    # except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[20]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[21]
                        if url == '':
                            url = row[22]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_kafe.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.NoSuchWindowException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_kafe



def breakfast():
    with open("breakfast_parser.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_breakfast = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("breakfast.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]

                    count1 += 1
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    # element.send_keys("Сатир,бар")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    # try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    # except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[20]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[23]
                        if url == '':
                            url = row[24]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_breakfast.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_breakfast
def karaoke():
    with open("karaoke_parser.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_karaoke = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("karaoke.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]

                    count1 += 1
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    # element.send_keys("Сатир,бар")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    # try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    # except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[18]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[19]
                        if url == '':
                            url = row[20]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_karaoke.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_karaoke

def bar():
    with open("bar_parser.csv", encoding="utf8") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        count1 = 0
        all_post_bar = []
        option = Options()
        option.add_argument("--disable-infobars")
        browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
        browser.get('https://2gis.ru/kirov')
        with open("bar.csv", mode="w", encoding='utf-8') as w_file:
            objects = ["Название", "Категория", "Кухня", "Ценовой диапозон", "Адрес", "Режим работы", "Телефон",
                       "Сайт", "Фото", "ID", "lat", "lon"]
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=objects)
            file_writer.writeheader()
            for row in reader:
                try:
                    zaved = []
                    # print(row[0])
                    name_1 = f"{row[0]}, {row[3]}"
                    name = row[0]
                    phone = row[16]
                    adress = row[3]

                    count1 += 1
                    if count1 == 1:
                        continue
                    element = browser.find_element(By.XPATH,
                                                   '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/form/div/input')
                    element.click()
                    element.send_keys(f"{row[0]}, {row[1]}, {row[3]}")
                    #element.send_keys("Сатир,бар")
                    element.send_keys(Keys.ENTER)
                    time.sleep(2)

                    try:
                        element = browser.find_element(By.XPATH,
                                                       '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div')
                        element.click()
                        time.sleep(2)
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
                    category = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span').text

                    #try:
                    ss_photo = browser.find_element(By.CLASS_NAME,
                                                    '_1mvlnoc')
                    ss_photo.click()
                    #except selenium.common.exceptions.NoSuchElementException:
                    #    search_clear = browser.find_element(By.XPATH,
                    #                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    #    search_clear.click()
                    #    continue
                    time.sleep(2)
                    s_img = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/img').get_attribute(
                        "src")
                    btn_back = browser.find_element(By.XPATH, '//*[@id="photoViewer"]/div/div/div[1]/button')
                    btn_back.click()
                    time.sleep(1)
                    element1 = browser.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a')
                    element1.click()
                    time.sleep(1)
                    count = 0
                    kitchen = ''
                    price = ''
                    try:
                        elementt = browser.find_element(By.CLASS_NAME, '_z3fqkm')
                        # '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]'
                        elementt.click()
                        time.sleep(1)
                        try:
                            count += 1
                            elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                            # print(elementserr)
                            for obj in elementserr:
                                if "Средний чек" in obj.text:
                                    price = obj.text
                                if "кухня" in obj.text:
                                    kitchen += obj.text + ' '
                        except selenium.common.exceptions.NoSuchElementException:
                            print("Ошибка")
                    except selenium.common.exceptions.NoSuchElementException:
                        count += 1
                        elementserr = browser.find_elements(By.CLASS_NAME, '_er2xx9')  # .text
                        # print(elementserr)
                        for obj in elementserr:
                            # print(obj.text)
                            if "Средний чек" in obj.text:
                                price = obj.text
                            if "кухня" in obj.text:
                                kitchen += obj.text + ' '
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    id = row[-1].replace('https://2gis.com/firm/', '')
                    url = row[19]
                    lat = row[-3]
                    lon = row[-2]
                    if url == '':
                        url = row[21]
                        if url == '':
                            url = row[22]
                    try:
                        Monday = row[12].split(";")[0].replace("Пн:", '')
                    except IndexError:
                        Monday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Tuesday = row[12].split(";")[1].replace("Вт:", '')
                    except IndexError:
                        Tuesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Wednesday = row[12].split(";")[2].replace("Ср:", '')
                    except IndexError:
                        Wednesday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Thursday = row[12].split(";")[3].replace("Чт:", '')
                    except IndexError:
                        Thursday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Friday = row[12].split(";")[4].replace("Пт:", '')
                    except IndexError:
                        Friday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Saturday = row[12].split(";")[5].replace("Сб:", '')
                    except IndexError:
                        Saturday = "Сегодня не работает (уточните время на сайте)"
                    try:
                        Sunday = row[12].split(";")[6].replace("Вс:", '')
                    except IndexError:
                        Sunday = "Сегодня не работает (уточните время на сайте)"
                    schedule = []
                    schedule.append(Monday)
                    schedule.append(Tuesday)
                    schedule.append(Wednesday)
                    schedule.append(Thursday)
                    schedule.append(Friday)
                    schedule.append(Saturday)
                    schedule.append(Sunday)
                    zaved.append(name)
                    zaved.append(category)
                    zaved.append(kitchen)
                    zaved.append(price)
                    zaved.append(adress)
                    zaved.append(schedule)
                    zaved.append(phone)
                    zaved.append(url)
                    zaved.append(s_img)
                    zaved.append(id)
                    zaved.append(lat)
                    zaved.append(lon)
                    print(zaved)
                    all_post_bar.append(zaved)
                    # print(data)
                    # break
                    if count == 10:
                        break
                except selenium.common.exceptions.NoSuchElementException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.ElementNotInteractableException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                except selenium.common.exceptions.WebDriverException:
                    search_clear = browser.find_element(By.XPATH,
                                                        '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/form/div/div/button')
                    search_clear.click()
                    continue
                file_writer.writerow(
                    {"Название": zaved[0], "Категория": zaved[1], "Кухня": zaved[2], "Ценовой диапозон": zaved[3],
                     "Адрес": zaved[4], "Режим работы": zaved[5], "Телефон": zaved[6], "Сайт": zaved[7], "Фото": zaved[8],
                     "ID": zaved[9], "lat": zaved[10], "lon": zaved[11]})
        return all_post_bar

data = bany()
print(data)
data = basa_otdiha()
print(data)
data = restoraunts()
print(data)
data = kalyan()
print(data)
data = breakfast()
print(data)
data = karaoke()
print(data)
data = bar()
print(data)




#print(data)