import os
from selenium.webdriver import ActionChains
from PIL import Image
import parcer
import random
import telebot
import time
import constant
from dataclasses import dataclass, field
from telebot import types
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from constant import token, t_option, screen_url1, screen_url2, channel_id, s_money, \
    t_dogon, cor_time, endpicture, weekstart, endweek, daystart, endday
from messages import second_message, third_message, dogon_message, bug_message, itog_dogon_message, \
    first_message, itog_sec_dogon_message


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
    itg_price: float = field(default=0)  # цена итога опциона
    itg_price1: float = field(default=0)  # цена итога опциона пятизначная
    itg_price2: float = field(default=0)  # цена итога опциона четырехзначная
    resume: str = field(default='')  # направление опциона
    em1: str = field(default='')  # эмодзи первой части валюты
    em2: str = field(default='')  # эмодзи второй части валюты
    plus: bool = field(default=False)  # True, если опцион в плюс
    minus: bool = field(default=False)  # True, если опцион в минус
    vozvrat: bool = field(default=False)  # True, если опцион возврат
    buy: bool = field(default=False)  # если опцион на покупку
    dogon2: str = field(default='')  # картинка догон дополнительный
    sell: bool = field(default=False)  # True, если опцион на продажу
    dgn: bool = field(default=False)  # True, если нужен догон
    dgn_price: float = field(default=0)  # цена входа в догон
    dgn_itg: float = field(default=0)  # цена итога догона
    dgn_itg1: float = field(default=0)  # цена итога догона пятизначная
    dgn_itg2: float = field(default=0)  # цена итога догона четырехзначная
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
    dgn_time: int = field(default=0)  # время догона в сек
    str_dgn_time: str = field(default='')  # время догона словами
    korrect: float = field(default=0)  # корректировка цены входа
    round: int = field(default=0)  # параметры округления

    def __post_init__(self):
        self.opt_data = datetime.now()
        self.opt_time = datetime.now()
        self.dog_time = datetime.now()

    def ins_data(self, nname, nresume):  # внесение данных из справочника
        self.name = nname
        self.resume = nresume
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
            self.dogon2 = name_list.get('dogon2')
        if 'ПРОДАВАТЬ' in self.resume:
            self.sell = True
        else:
            self.buy = True

    def kor_dogon_price(self):  # корректировка цены входа в догон
        if self.buy:
            self.dgn_price = round((self.dgn_price - self.korrect), self.round)
        if self.sell:
            self.dgn_price = round((self.dgn_price + self.korrect), self.round)

    def kor_price(self):  # корректировка цены входа
        if self.buy:
            self.price = round((self.price - self.korrect), self.round)
        if self.sell:
            self.price = round((self.price + self.korrect), self.round)

    def error(self, text):  # запись об ошибке
        self.bug = True
        self.bug_text = text

    def dogon_itogi(self):  # выбор более благоприятной цены итогов
        itogi_dogon = self.dgn_itg1 - self.dgn_price
        if self.buy:
            if itogi_dogon > 0:
                self.dgn_itg = self.dgn_itg1
            else:
                self.dgn_itg = self.dgn_itg1
        elif self.sell:
            if itogi_dogon < 0:
                self.dgn_itg = self.dgn_itg1
            else:
                self.dgn_itg = self.dgn_itg1

    def itogi(self):  # выбор более благоприятной цены итогов
        itogi_price = self.itg_price1 - self.price
        if self.buy:
            if itogi_price > 0:
                self.itg_price = self.itg_price1
            else:
                self.itg_price = self.itg_price1
        elif self.sell:
            if itogi_price < 0:
                self.itg_price = self.itg_price1
            else:
                self.itg_price = self.itg_price1

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

    def timedogon(self):
        tdg = random.choice(t_dogon)
        if tdg['intname'] == 1:
            self.dgn1 = True
        else:
            self.dgn2 = True
        self.dgn_time = tdg['time']
        self.str_dgn_time = tdg['name']


bot = telebot.TeleBot(token)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


def option_poll():
    questions = ["Цена пойдёт вверх 🟢", "Цена пойдёт вниз 🔴"]
    message = bot.send_poll(
        channel_id,
        "Определите куда пойдёт движение цены:",
        questions,
        is_anonymous=True,
        allows_multiple_answers=False,
    )
    # Save some info about the poll the bot_data for later use in receive_poll_answer}


def start_message(day):  # запуск страртового сообщения
    t_message = []

    if day == 0:
        text_message = '<a href="' + weekstart + '">&#8205;</a>'
        text_message = text_message + '<b>Доброе утро 🙋 Начинаем торговую неделю ☝</b>\n'
        text_message = text_message + '\n<b>Как вступить в команду и бесплатно получать круглосуточные сигналы 👇</b>\n'
        text_message = text_message + 'https://teletype.in/@smoke_fx/eT7QbEdEB\n'
        text_message = text_message + '\n<i>Получить полный доступ по ссылке</i> 👇\n'
        text_message = text_message + 'https://t.me/SmokeFXchatbot'
    else:
        text_message = '<a href="' + daystart + '">&#8205;</a>'
        text_message = text_message + '<b>Доброе утро 🌞 Начинаем торговлю 📈\n</b>'
        text_message = text_message + '\n<b>Как вступить в команду и бесплатно получать круглосуточные сигналы 👇</b>\n'
        text_message = text_message + 'https://teletype.in/@smoke_fx/eT7QbEdEB\n'
        text_message = text_message + '\n<i>Получить полный доступ по ссылке</i> 👇\n'
        text_message = text_message + 'https://t.me/SmokeFXchatbot'
    t_message.append(text_message)
    t_message = '\n'.join(t_message)
    try:
        bot.send_message(channel_id, t_message, disable_web_page_preview=False,
                         parse_mode='HTML')  # отправка первого сообщения
    except Exception as error:
        err_text = "Ошибка отправки приветствия! - " + str(error)
        print(err_text)


def final_message(day):  # запуск последнего сообщения
    t_message = []
    if day == 4:
        text_message = '<a href="' + endweek + '">&#8205;</a>'
        text_message = text_message + '<b>Завершаем торговую неделю❕ Всем хороших выходных 🙋</b>\n'
        text_message = text_message + '\n<b>Как вступить в команду и бесплатно получать круглосуточные сигналы 👇</b>\n'
        text_message = text_message + 'https://teletype.in/@smoke_fx/eT7QbEdEB\n'
        text_message = text_message + '\n<i>Получить полный доступ по ссылке</i> 👇\n'
        text_message = text_message + 'https://t.me/SmokeFXchatbot'
    else:
        text_message = '<a href="' + endday + '">&#8205;</a>'
        text_message = text_message + '<b>Завершаем торговлю❕ Продолжим завтра в 7-00 по МСК 🕘</b>\n'
        text_message = text_message + '\n<b>Как вступить в команду и бесплатно получать круглосуточные сигналы 👇</b>\n'
        text_message = text_message + 'https://teletype.in/@smoke_fx/eT7QbEdEB\n'
        text_message = text_message + '\n<i>Получить полный доступ по ссылке</i> 👇\n'
        text_message = text_message + 'https://t.me/SmokeFXchatbot'
    t_message.append(text_message)
    t_message = '\n'.join(t_message)
    try:
        bot.send_message(channel_id, t_message, disable_web_page_preview=False,
                         parse_mode='HTML')  # отправка последнего сообщения
    except Exception as error:
        err_text = "Ошибка отправки последнего сообщения! - " + str(error)
        print(err_text)


def last_message():  # запуск последнего сообщения
    f_message = '<a href="' + endpicture + '">&#8205;</a>'
    f_message = f_message + '<b>Получай полный доступ к закрытой группе Smoke FX! 👌</b>\n'
    f_message = f_message + '\n<i>Полная аналитика прогноза + авторские стратегии в МТ4 + более ' \
                            '2ОО точек входа в день!  📌</i>\n'
    f_message = f_message + '\n<b>Что получает участник ЗАКРЫТОЙ группы:</b>\n'
    f_message = f_message + '\n👉 <b>Расширенную аналитику</b> на каждый торговый прогноз + резюме <b>по каждой</b> ' \
                            'валютной паре ❗️\n'
    f_message = f_message + '👉 Более <b>2ОО прогнозов</b> ежедневно + прогнозы в ночное время ❕\n'
    f_message = f_message + '👉 <b>Бесплатную подписку</b> на все <b>обновления и курсы</b> закрытой группы ❕\n'
    f_message = f_message + '👉 Доступ к курсам <b>по обучению от Smoke FX</b> (<i> в разработке, дата релиза ' \
                            'не раньше 07.07.21 </i>)\n'
    f_message = f_message + '\nЕсли тебе недостаточно просто сигналов и ты хочешь получать расширенную аналитику ' \
                            'рынка, тогда получай ПОЛНЫЙ доступ прямо сейчас 🔥 \n'
    f_message = f_message + '\nДля того что бы получить доступ, и торговать с моей командой, нажми на кнопку ниже <b>' \
                            '"Получить ПОЛНЫЙ доступ"</b> ❗️\n'
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Получить ПОЛНЫЙ доступ ✅", url="https://t.me/SmokeFXchatbot")
    keyboard.add(url_button)
    try:
        bot.send_message(channel_id, text=f_message, disable_web_page_preview=False,
                         parse_mode='HTML', reply_markup=keyboard)  # отправка последнего сообщения
    except Exception as error:
        err_text = "Ошибка отправки последнего сообщения! " + str(error)
        print(err_text)


def exit_main(start_time, driver, log_data, itog: int):  # выход из main
    if driver is not None:
        driver.quit()
    itog_time = datetime.now() - start_time
    result = [int(itog_time.total_seconds()), log_data.name, log_data.minus, itog]
    return result


def mouse_move(action, element):
    action.move_to_element(element).perform()
    action.move_by_offset(xoffset=200, yoffset=200).perform()
    action.move_to_element(element).perform()


def screenshot(driver):  # Создание скриншота
    try:
        element = driver.find_element_by_xpath('/html/body/div[2]/div[1]')
        try:
            element.screenshot("shot.png")
            img = Image.open("shot.png")
            img = img.crop((0, constant.y1crop, constant.xcrop, constant.ycrop))
            # img = img.crop((0, 0, 1427, 800))
            img.save("screenshot.png")
            return 0
        except Exception as error:
            print("Ошибка записи скриншота - " + str(error))
            return 1
    except NoSuchElementException:
        print('Не могу снять скриншот')
        return 1


def itog_second_dogon_message(
        log_data):  # сообщение об итоге догона для испаноязычного канала(входные данные, итоговые данные)
    dgn_res = 0
    if log_data.buy:
        dgn_res = log_data.dgn_itg - log_data.dgn_price
    elif log_data.sell:
        dgn_res = log_data.dgn_price - log_data.dgn_itg
    if dgn_res > 0:
        log_data.plus = True  # Внесение в лог параметра ПЛЮС
        return True
    else:
        log_data.minus = True
        # print('Минус')
        return False


def main(val_name):
    strprice = ''
    volute_text = None
    driver = None
    log_data = Option()
    start_time = datetime.now()  # фиксирование времени старта функции
    try:
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        time.sleep(8)
    except Exception as error:
        print("Задержка открытия окна - " + str(error))
        log_data.error("Задержка открытия окна")
        return exit_main(start_time, driver, log_data, 0)
    i = 0
    try:
        while i < 1:
            vol = parcer.parse('name')
            while len(vol) == 0:
                vol = parcer.parse('name')
            if len(vol) == 1 and vol[0]['name'] != val_name:
                i = 1
                volute_text = vol[0]
            elif len(vol) > 1:
                j = 0
                while j < 1:
                    volute_text = random.choice(vol)  # выбор валюты текущего опциона
                    if volute_text['name'] == val_name:
                        j = 0
                    else:
                        j = 1
                        i = 1
            else:
                i = 0
    except Exception as error:
        print("Задержка открытия окна 2 - " + str(error))
        log_data.error("Задержка открытия окна 2")
        return exit_main(start_time, driver, log_data, 0)
    log_data.ins_data(volute_text['name'], volute_text['resume'].upper())
    volute = log_data.name.replace('/', '')
    it = 0
    while it < 10:
        try:
            driver.get(screen_url1 + volute + screen_url2 + volute)  # открытие окна с котировками
            time.sleep(5)
            # driver.set_window_size(5000, 3100)
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
            strprice = driver.find_element_by_xpath(' html / body / div[2] / div[1] / div[1] / div[1] '
                                                    '/ div / table / tr[1] / td[2] / div / div[1] / div[1] / div / \
              div[2] / div / div[5] / div[2]')
            it = 10
        except Exception as error:
            print("Задержка открытия окна с котировками - " + str(error))
            it += 1
            print(it)
    try:
        t1 = datetime.now() + timedelta(hours=cor_time)  # ВРЕМЯ ОБЪЯВЛЕНИЯ ОПЦИОНА
        bot.send_message(channel_id, first_message(log_data),
                         disable_web_page_preview=False,
                         parse_mode='HTML')  # отправка первого сообщения
    except Exception as error:
        err_text = "Ошибка отправки первого сообщения! - " + str(error)
        print(err_text)
        log_data.error(err_text)
        return exit_main(start_time, driver, log_data, 0)

    i_color = 0
    # поиск точки входа для сигнала ПОКУПАТЬ
    if 'ПОКУПАТЬ' in log_data.resume:
        while i_color == 0:
            mouse_move(ActionChains(driver), strprice)
            tp = str(strprice.value_of_css_property("color"))
            if '38' in tp:
                i_color = 1
            else:
                i_color = 0
    # поиск точки входа для сигнала ПРОДАВАТЬ
    elif 'ПРОДАВАТЬ' in log_data.resume:
        while i_color == 0:
            mouse_move(ActionChains(driver), strprice)
            tp = str(strprice.value_of_css_property("color"))
            if '239' in tp:
                i_color = 1
            else:
                i_color = 0
    try:
        price = float(strprice.text)
        log_data.opt_time = (datetime.now() + timedelta(hours=cor_time))  # Внесение в лог параметра ВРЕМЯ
        log_data.vh_timer = (log_data.opt_time - t1).seconds  # ВнесениеВРЕМЯ ПОИСКА ТОЧКИ ВХОДА, С
        if price <= 0:
            err_text = "Ошибка определения цены"
            print(err_text)
            log_data.error(err_text)
            return exit_main(start_time, driver, log_data, 0)
    except ValueError:
        err_text = "Ошибка преобразования цены"
        log_data.error(err_text)
        return exit_main(start_time, driver, log_data, 0)
    log_data.price = price
    log_data.kor_price()
    if screenshot(driver) == 1:
        err_text = "Ошибка снятия скриншота"
        print(err_text)
    try:
        img = open('screenshot.png', 'rb')
        bot.send_photo(channel_id, img, caption=second_message(log_data), parse_mode='HTML')
    except Exception as error:
        err_text = "Ошибка отправки второго сообщения! - " + str(error)
        bug_message(log_data.p_bug, bot, channel_id)
        print(err_text)
        log_data.error(err_text)
        return exit_main(start_time, driver, log_data, 0)
    option_poll()
    time.sleep(log_data.option_time)  # Включение паузы после второго сообщения от 3 до 5 минут
    try:
        mouse_move(ActionChains(driver), strprice)
        log_data.itg_price1 = float(strprice.text)  # итоговая цена опциона пятизначная
        log_data.itogi()
    except ValueError:
        err_text = 'Ошибка преобразования'
        bug_message(log_data.p_bug, bot, channel_id)
        print(err_text)
        log_data.error(err_text)
        return exit_main(start_time, driver, log_data, 0)
    log_data.comparing_lists()  # подведение итогов опциона
    if log_data.dgn:  # включение догона
        log_data.timedogon()
        message_text = dogon_message(log_data)
        try:
            t3 = datetime.now() + timedelta(hours=cor_time)  # Внесение в лог параметра ВРЕМЯ ОБЪЯВЛЕНИЯ ДОГОНА
            bot.send_message(channel_id, message_text, disable_web_page_preview=False,
                             parse_mode='HTML')
        except Exception as error:
            err_text = "Ошибка отправки сообщения о догоне! - " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(err_text)
            log_data.error(err_text)
            return exit_main(start_time, driver, log_data, 0)
        time.sleep(10)
        i_color = 0
        if log_data.buy:
            while i_color == 0:
                mouse_move(ActionChains(driver), strprice)
                tp = str(strprice.value_of_css_property("color"))
                if '38' in tp:
                    i_color = 1
                else:
                    i_color = 0
        # поиск точки входа для сигнала ПРОДАВАТЬ
        elif log_data.sell:
            while i_color == 0:
                mouse_move(ActionChains(driver), strprice)
                tp = str(strprice.value_of_css_property("color"))
                if '239' in tp:
                    i_color = 1
                else:
                    i_color = 0
        try:
            if screenshot(driver) == 1:
                err_text = "Ошибка снятия скриншота"
                print(err_text)
            log_data.dgn_price = float(strprice.text)
            log_data.kor_dogon_price()
            log_data.dogs_time = datetime.now() + timedelta(
                hours=cor_time)  # Внесение в лог параметра ВРЕМЯ ОТКРЫТИЯ ДОГОНА
            log_data.dog_timer = (log_data.dogs_time - t3).seconds  # ВРЕМЯ ПОИСКА ТОЧКИ ВХОДА ДОГОНА, С
            if screenshot(driver) == 1:
                err_text = "Ошибка снятия скриншота"
                print(err_text)
            try:
                img = open('screenshot.png', 'rb')
                bot.send_photo(channel_id, img, caption=dogon_message(log_data), parse_mode='HTML')
            except Exception as error:
                err_text = "Ошибка отправки второго сообщения о догоне - " + str(error)
                bug_message(log_data.p_bug, bot, channel_id)
                print(err_text)
                log_data.error(err_text)
                return exit_main(start_time, driver, log_data, 0)
        except Exception as error:
            err_text = "Ошибка отправки второго сообщения о догоне! - " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(err_text)
            log_data.error(err_text)
            return exit_main(start_time, driver, log_data, 0)
        time.sleep(log_data.dgn_time)
    else:
        if screenshot(driver) == 1:
            err_text = "Ошибка снятия скриншота"
            print(err_text)
        try:
            img = open('screenshot.png', 'rb')
            bot.send_photo(channel_id, img, caption=third_message(log_data), parse_mode='HTML')
            return exit_main(start_time, driver, log_data, 1)
        except Exception as error:
            err_text = "Ошибка отправки итогового сообщения! - " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(err_text)
            log_data.error(err_text)
            return exit_main(start_time, driver, log_data, 0)
    if log_data.dgn:
        try:
            mouse_move(ActionChains(driver), strprice)
            log_data.dgn_itg1 = float(strprice.text)
        except ValueError:
            err_text = 'Ошибка преобразования цены итогов догона'
            bug_message(log_data.p_bug, bot, channel_id)
            print(err_text)
            log_data.error(err_text)
            return exit_main(start_time, driver, log_data, 0)
        log_data.dogon_itogi()
        if screenshot(driver) == 1:
            err_text = "Ошибка снятия скриншота"
            print(err_text)
        try:
            img = open('screenshot.png', 'rb')
            bot.send_photo(channel_id, img, caption=itog_dogon_message(log_data), parse_mode='HTML')
            # return exit_main(start_time, driver, log_data, 1)
        except Exception as error:
            err_text = "Ошибка отправки итогов догона! - " + str(error)
            bug_message(log_data.p_bug, bot, channel_id)
            print(err_text)
            log_data.error(err_text)
            return exit_main(start_time, driver, log_data, 0)
    if log_data.minus:
        time.sleep(random.randint(150, 360))
        try:
            bot.send_message(channel_id, itog_sec_dogon_message(log_data), disable_web_page_preview=False,
                             parse_mode='HTML')
        except Exception as error:
            err_text = "Ошибка отправки итогов догона! - " + str(error)
            print(err_text)
            log_data.error(err_text)
            return exit_main(start_time, driver, log_data, 0)
    return exit_main(start_time, driver, log_data, 1)


def mainbot():
    main('EUR/RUB')
    last_message()


if __name__ == '__main__':
    mainbot()
