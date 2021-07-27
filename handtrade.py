# файл по общей торговле
import os
import constant
import random
import time
import telebot
from dataclasses import dataclass, field
from selenium.webdriver import ActionChains
from pollfile import poll
from datetime import datetime, timedelta
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from constant import screen_url1, screen_url3, channel_id, s_money, t_option, t_dogon, \
    cor_time, url_list, handoption, token
from messages import bug_message, first_poll_message, second_poll_message, dogon_poll_message, dogon_poll_sec_message, \
    third_poll_message, itog_poll_dogon_message, fourth_poll_message, none_poll_message


@dataclass  # Класс структуры храннения данных в списке
class Option:
    name: str = field(default='')  # название валюты
    p_plus: str = field(default='')  # картинка плюс
    p_minus: str = field(default='')  # картинка минус
    p_vozvrat: str = field(default='')  # картинка возврата
    p_buy: str = field(default='')  # картинка покупка
    p_sell: str = field(default='')  # картинка продажа
    p_dgn: str = field(default='')  # картинка догон
    p_bug: str = field(default='')  # картинка баг
    price: float = field(default=0)  # цена входа
    itg_price: float = field(default=0)  # цена итога опциона пятизначная
    resume: str = field(default='')  # направление опциона
    em1: str = field(default='')  # эмодзи первой части валюты
    em2: str = field(default='')  # эмодзи второй части валюты
    plus: bool = field(default=False)  # True, если опцион в плюс
    minus: bool = field(default=False)  # True, если опцион в минус
    vozvrat: bool = field(default=False)  # True, если опцион возврат
    buy: bool = field(default=False)  # если опцион на покупку
    sell: bool = field(default=False)  # True, если опцион на продажу
    dgn: bool = field(default=False)  # True, если нужен догон
    # dgn_first: bool = field(default=False)  # True, если нужен первый догон
    # dgn_second: bool = field(default=False)  # True, если нужен второй догон
    dgn_price1: float = field(default=0)  # цена входа в догон
    dgn_price2: float = field(default=0)  # цена входа во второй догон
    dgn_itg1: float = field(default=0)  # цена итога догона пятизначная
    dgn_itg2: float = field(default=0)  # цена итога второго догона
    dgn1: bool = field(default=False)  # True, если догон на 1 мин
    dgn2: bool = field(default=False)  # True, если догон на 2 мин
    bug: bool = field(default=False)  # True, если был сбой
    bug_text: str = field(default='')  # Текст ошибки
    opt_data: datetime = field(init=False)  # дата опциона
    opt_time: datetime = field(init=False)  # время входа в опцион
    dogs_time: datetime = field(init=False)  # время входа в догон
    vh_timer: int = field(default=0)  # время поиска точки входа
    dog_timer: int = field(default=0)  # время поиска точки входа в догон
    option_time: int = field(default=0)  # время опциона в сек
    str_time: str = field(default='')  # время опциона словами
    dgn_time1: int = field(default=0)  # время догона в сек
    str_dgn_time1: str = field(default='')  # время догона словами
    dgn_time2: int = field(default=0)  # время второго догона в сек
    str_dgn_time2: str = field(default='')  # время второго догона словами
    korrect: float = field(default=0)  # корректировка цены входа
    signal5min: str = field(default='')  # прогноз по сигналу 5 минут
    signal1min: str = field(default='')  # прогноз по сигналу 1 минута
    signal15min: str = field(default='')  # прогноз по сигналу 15 минут
    signal30min: str = field(default='')  # прогноз по сигналу 30 минут
    level1: float = field(default=0)  # уровень поддержки
    level2: float = field(default=0)  # уровень сопротивления
    pivot1: float = field(default=0)  # первая точка разворота
    pivot2: float = field(default=0)  # вторая точка разворота
    round: int = field(default=0)  # параметры округления
    signalsila: int = field(default=0)  # параметры силы сигнала

    def __post_init__(self):
        self.opt_data = datetime.now()
        self.opt_time = datetime.now()
        self.dog_time = datetime.now()

    def ins_data(self):  # внесение данных из справочника
        name_list = next((item for item in s_money if item["name"] == self.name), False)
        if name_list:
            self.em1 = name_list.get('em1')
            self.em2 = name_list.get('em2')
            self.p_plus = name_list.get('plus')
            self.p_minus = name_list.get('minus')
            self.p_buy = name_list.get('buy')
            self.p_sell = name_list.get('sell')
            self.p_dgn = name_list.get('dogon')
            self.p_vozvrat = name_list.get('vozvrat')
            self.p_bug = name_list.get('bug')
            time_option = random.choice(t_option)
            self.option_time = time_option['time']  # время опциона
            self.str_time = time_option['name']
            self.korrect = name_list.get('korrect')
            self.round = name_list.get('round')
        if 'ПРОДАВАТЬ' in self.resume:
            self.sell = True
        else:
            self.buy = True

    def kor_dogon_price(self, dog):  # корректировка цены входа в догон
        if nayob:
            if dog == 1:
                if self.buy:
                    self.dgn_price1 = round((self.dgn_price1 - self.korrect), self.round)
                if self.sell:
                    self.dgn_price1 = round((self.dgn_price1 + self.korrect), self.round)
            if dog == 2:
                if self.buy:
                    self.dgn_price2 = round((self.dgn_price2 - self.korrect), self.round)
                if self.sell:
                    self.dgn_price2 = round((self.dgn_price2 + self.korrect), self.round)
        else:
            print('Без наеба')

    def kor_price(self):  # корректировка цены входа
        if nayob:
            if self.buy:
                self.price = round((self.price - self.korrect), self.round)
            if self.sell:
                self.price = round((self.price + self.korrect), self.round)
        else:
            print('без наеба')

    def kor_level(self):  # корректировка цены входа
        self.level2 = round((self.price + self.korrect / 2 * random.randint(22, 48)), self.round)
        self.level1 = round((self.price - self.korrect / 2 * random.randint(20, 54)), self.round)

    def error(self, text):  # запись об ошибке
        self.bug = True
        self.bug_text = text

    def itogi(self):  # выбор более благоприятной цены итогов
        itogi_price = self.itg_price - self.price
        if self.buy:
            if itogi_price > 0:
                self.itg_price = self.itg_price
            else:
                self.itg_price = self.itg_price
        elif self.sell:
            if itogi_price < 0:
                self.itg_price = self.itg_price
            else:
                self.itg_price = self.itg_price

    def comparing_lists(self):  # расчет итога опциона
        itog_price = self.itg_price - self.price
        if itog_price == 0:
            self.vozvrat = True
        elif self.buy:
            if itog_price > 0:
                self.plus = True
            elif itog_price < 0:
                self.dgn = True
        elif self.sell:
            if itog_price < 0:
                self.plus = True
            elif itog_price > 0:
                self.dgn = True

    def timedogon(self, dog):
        tdg = random.choice(t_dogon)
        if dog == 1:
            self.dgn_time1 = tdg['time']
            self.str_dgn_time1 = tdg['name']
        elif dog == 2:
            self.dgn_time2 = tdg['time']
            self.str_dgn_time2 = tdg['name']


nayob: bool
bot = telebot.TeleBot(token)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
strprice: str = ''


def mouse_move(action, element):
    action.move_to_element(element).perform()
    action.move_by_offset(xoffset=200, yoffset=200).perform()
    action.move_to_element(element).perform()


def start_message():  # запуск страртового сообщения
    t_message = []
    # text_message = '<a href="' + weekstart + '">&#8205;</a>'
    text_message = '<b>Торговая сессия в 18:ОО по МСК</b>'
    t_message.append(text_message)
    t_message = '\n'.join(t_message)
    try:
        bot.send_message(channel_id, t_message, disable_web_page_preview=False,
                         parse_mode='HTML')  # отправка первого сообщения
    except Exception as error:
        error_text = "Ошибка отправки приветствия! " + str(error)
        print(error_text)


def last_message():  # запуск последнего сообщения
    t_message = []
    # last_picture = '<a href="' + endweek + '">&#8205;</a>'
    text_message = '<b>Конец торговой сессии 🔒</b>'
    text_message = text_message + '\n<b>Свои результаты пишите в комментариях к последнему видео на нашем канале' \
                                  ' YouTube 👍</b>'
    t_message.append(text_message)
    # t_message.append(last_picture)
    t_message = '\n'.join(t_message)
    try:
        bot.send_message(channel_id, t_message, disable_web_page_preview=False,
                         parse_mode='HTML')  # отправка последнего сообщения
    except Exception as error:
        error_text = "Ошибка отправки последнего сообщения! " + str(error)
        print(error_text)


def screenshot(driver):  # Создание скриншота
    try:
        element = driver.find_element_by_xpath('/html/body/div[2]/div[1]')
        try:
            element.screenshot("shot.png")
            img = Image.open("shot.png")
            img = img.crop((0, constant.y1crop, constant.xcrop, constant.ycrop))
            img.save("screenshot.png")
            return 0
        except Exception as error:
            print("Ошибка записи скриншота " + str(error))
            return 1
    except NoSuchElementException as error:
        print('Не могу снять скриншот ' + str(error))
        return 1


def exit_main(start_time, driver, log_data):  # выход из main
    itog_time = datetime.now() - start_time
    result = [int(itog_time.total_seconds()), log_data.name, log_data.minus]
    try:
        driver.quit()
    except Exception as error:
        print('Драйвер не выгружен ' + str(error))
    return result


def trade_main(val_name):
    global strprice
    driver = None
    log_data = Option()
    start_time = datetime.now()  # фиксирование времени старта функции
    i = 0
    while i < 1:
        position = url_list[random.randint(0, 26)]  # выбор рандомной строки из словаря валют
        if val_name == position.get('name'):
            continue
        else:
            log_data.name = position.get('name')
            i = 1
    log_data.ins_data()
    volute = log_data.name.replace('/', '')
    try:
        # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver = webdriver.Chrome(chrome_options=chrome_options)
    except Exception as error:
        # print("Задержка открытия окна " + str(error))
        log_data.error("Задержка открытия окна " + str(error))
        return exit_main(start_time, driver, log_data)
    it = 0
    link = screen_url1 + volute + screen_url3 + volute
    while it < 10:
        try:
            driver.get(link)  # открытие окна с котировками
            time.sleep(5)
            driver.set_window_size(1552, 840)
            driver.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]"
                "/div[2]/div[2]/div[1]/div[1]/div[1]").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "/html/body/div[2]/div[3]/div/div/div[1]/div/div/div/div/div/div[5]/div/div").click()
            time.sleep(2)
            str_indicator = driver.find_element_by_class_name("input-3n5_2-hI")
            str_indicator.send_keys('Donchian Channels')
            driver.find_element_by_class_name('title-1gYObTuJ').click()
            str_indicator.clear()
            str_indicator.send_keys('Pivot Points High Low')
            driver.find_element_by_class_name('title-1gYObTuJ').click()
            driver.find_element_by_class_name('close-2sL5JydP').click()
            time.sleep(2)
            strprice = driver.find_element_by_xpath('html/body/div[2]/div[1]/div[1]/div[1]/div/table/tr[1]/td[2]/div'
                                                    '/div[1]/div[1]/div/div[2]/div/div[5]/div[2]')
            it = 10
        except Exception as error:
            print("Задержка открытия окна с котировками " + str(error))
        it += 1
    time.sleep(5)
    if screenshot(driver) == 1:
        error_text = "Ошибка снятия скриншота"
        print(error_text)
    try:
        img = open('screenshot.png', 'rb')
        bot.send_message(channel_id, first_poll_message(log_data), disable_web_page_preview=False,
                         parse_mode='HTML')
        bot.send_photo(channel_id, img, caption=second_poll_message(link), parse_mode='HTML')
    except Exception as error:
        error_text = "Ошибка отправки сообщения со скриншотом! " + str(error)
        bug_message(log_data.p_bug, bot, channel_id)
        print(error_text)
        log_data.error(error_text)
        return exit_main(start_time, driver, log_data)
    variant = poll('Определите направление движения цены 📈 📉 \n\nДлительность опроса: 6О сек ⏰ \n\nВход в '
                   'рынок: 5 минут 🕔 ')
    if variant[0] == variant[1]:
        try:
            bot.send_message(channel_id, none_poll_message(), disable_web_page_preview=False,
                             parse_mode='HTML')  # отправка последнего сообщения
        except Exception as error:
            error_text = "Ошибка отправки последнего сообщения! " + str(error)
            print(error_text)
        return exit_main(start_time, driver, log_data)
    if variant[0] > variant[1]:
        log_data.resume = 'ПОКУПАТЬ'
        log_data.buy = True
        log_data.sell = False
    else:
        log_data.resume = "ПРОДАВАТЬ"
        log_data.sell = True
        log_data.buy = False
    mouse_move(ActionChains(driver), strprice)
    try:
        price = float(strprice.text)
        log_data.opt_time = (datetime.now() + timedelta(hours=cor_time))  # Внесение в лог параметра ВРЕМЯ
        if price <= 0:
            error_text = "Ошибка определения цены"
            print(error_text)
            log_data.error(error_text)
            return exit_main(start_time, driver, log_data)
    except ValueError as error:
        error_text = "Ошибка преобразования цены " + str(error)
        log_data.error(error_text)
        return exit_main(start_time, driver, log_data)
    log_data.price = price
    log_data.option_time = handoption
    if screenshot(driver) == 1:
        error_text = "Ошибка снятия скриншота"
        print(error_text)
    try:
        img = open('screenshot.png', 'rb')
        bot.send_photo(channel_id, img, caption=third_poll_message(log_data), parse_mode='HTML')
    except Exception as error:
        error_text = "Ошибка отправки сообщения о догоне! " + str(error)
        bug_message(log_data.p_bug, bot, channel_id)
        print(error_text)
        log_data.error(error_text)
        return exit_main(start_time, driver, log_data)
    time.sleep(log_data.option_time)  # Включение паузы после второго сообщения от 3 до 5 минут
    try:
        mouse_move(ActionChains(driver), strprice)
        log_data.itg_price = float(strprice.text)  # итоговая цена опциона пятизначная
        log_data.itogi()
    except ValueError as error:
        error_text = 'Ошибка преобразования ' + str(error)
        bug_message(log_data.p_bug, bot, channel_id)
        print(error_text)
        log_data.error(error_text)
        return exit_main(start_time, driver, log_data)
    log_data.comparing_lists()  # подведение итогов опциона
    if log_data.dgn:  # включение догона
        log_data.timedogon(1)
        if screenshot(driver) == 1:
            error_text = "Ошибка снятия скриншота"
            print(error_text)
        try:
            img = open('screenshot.png', 'rb')
            bot.send_photo(channel_id, img, caption=dogon_poll_message(log_data, link), parse_mode='HTML')
        except Exception as error:
            error_text = "Ошибка отправки сообщения о догоне! " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(error_text)
            log_data.error(error_text)
            return exit_main(start_time, driver, log_data)
        variant = poll(
            'Определите направление движения цены (перекрытие) 📈 📉 \n\nДлительность опроса: 6О сек ⏰ \n\nВход в '
            'рынок: 3 минуты 🕔 ')
        if variant[0] == variant[1]:
            try:
                bot.send_message(channel_id, none_poll_message(),
                                 disable_web_page_preview=False,
                                 parse_mode='HTML')  # отправка последнего сообщения
            except Exception as error:
                error_text = "Ошибка отправки сообщения об итогах голосования! " + str(error)
                print(error_text)
            return exit_main(start_time, driver, log_data)
        if variant[0] > variant[1]:
            log_data.buy = True
            log_data.sell = False
        else:
            log_data.sell = True
            log_data.buy = False
        mouse_move(ActionChains(driver), strprice)
        log_data.dogs_time = datetime.now() + timedelta(
            hours=cor_time)  # Внесение в лог параметра ВРЕМЯ ОТКРЫТИЯ ДОГОНА
        try:
            log_data.dgn_price1 = float(strprice.text)
            if screenshot(driver) == 1:
                error_text = "Ошибка снятия скриншота"
                print(error_text)
            img = open('screenshot.png', 'rb')
            bot.send_photo(channel_id, img, caption=dogon_poll_sec_message(log_data), parse_mode='HTML')
        except Exception as error:
            error_text = "Ошибка отправки второго сообщения о догоне " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(error_text)
            log_data.error(error_text)
            return exit_main(start_time, driver, log_data)
        time.sleep(182)
    else:
        if screenshot(driver) == 1:
            error_text = "Ошибка снятия скриншота"
            print(error_text)
        try:
            img = open('screenshot.png', 'rb')
            bot.send_photo(channel_id, img, caption=fourth_poll_message(log_data), parse_mode='HTML')
            return exit_main(start_time, driver, log_data)
        except Exception as error:
            error_text = "Ошибка отправки итогового сообщения! " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(error_text)
            log_data.error(error_text)
            return exit_main(start_time, driver, log_data)
    if log_data.dgn:
        try:
            mouse_move(ActionChains(driver), strprice)
            log_data.dgn_itg1 = float(strprice.text)
        except ValueError:
            error_text = 'Ошибка преобразования цены итогов догона'
            bug_message(log_data.p_bug, bot, channel_id)
            print(error_text)
            log_data.error(error_text)
            return exit_main(start_time, driver, log_data)
        if screenshot(driver) == 1:
            error_text = "Ошибка снятия скриншота"
            print(error_text)
        try:
            img = open('screenshot.png', 'rb')
            bot.send_photo(channel_id, img, caption=itog_poll_dogon_message(log_data), parse_mode='HTML')
            return exit_main(start_time, driver, log_data)
        except Exception as error:
            error_text = "Ошибка отправки итогов догона! " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(error_text)
            log_data.error(error_text)
            return exit_main(start_time, driver, log_data)
    return exit_main(start_time, driver, log_data)


if __name__ == '__main__':
    trade_main('EUR/CHF')
