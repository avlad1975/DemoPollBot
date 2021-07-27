import datetime
import os

# channel_id = os.environ.get("channel_id")
# ycrop = int(os.environ.get("ycrop"))
# y1crop = int(os.environ.get("y1crop"))
# xcrop = int(os.environ.get("xcrop"))
# otchet_id = os.environ.get("otchet_id")  # куда отправлять отчет
# handoption = int(os.environ.get("handoption"))
# cor_time = int(os.environ.get("cor_time"))
# timeoption = int(os.environ.get("timeoption"))
ycrop = 800
y1crop = 27
xcrop = 1427
otchet_id = "-1001177988357"  # куда отправлять отчет
channel_id = "-1001177988357"  # тестовый канал
handoption = 301  # время общего опциона
cor_time = 0  # корректировка времени по отношению к серверному времени
timeoption = 10
token = '1200302271:AAGwUmVr21OIL13rLv-3M3HX1xub6qoSF4M'
tokenpoll = '1908268664:AAEo_90786_J7RTYjZTRj5IiUFnHzoI4U4Y'  # demopollbot
weekstart = 'https://i.ibb.co/D1N36KK/start.jpg'  # рисунок начала недели
daystart = 'https://i.ibb.co/WDXkXJ6/start.jpg'  # рисунок начала дня
endday = 'https://i.ibb.co/NyGcVDB/finish.jpg'  # рисунок окончания торгов
endweek = 'https://i.ibb.co/WgWSx42/finish.jpg'  # рисунок окончания недели
fanny = [':white_check_mark:']  # эмодзи для ПЛЮС
good = [':beginner:']  # эмодзи для возврат
fuck = [':heavy_minus_sign:']  # эмодзи дня МИНУС
dogon = [':recycling_symbol:']  # эмодзи для догона
screen_url1 = "https://s.tradingview.com/widgetembed/?frameElementId=tradingview_09ab0&symbol=FX%3A"
screen_url2 = "&interval=1&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=%5B%5D&theme=" \
              "Dark&style=1&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=" \
              "%5B%5D&disabled_features=%5B%5D&locale=en&utm_source=binguru.net&utm_medium=widget_new&utm_campaign" \
              "=chart&utm_term=FX%3A"
screen_url3 = "&interval=5&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=%5B%5D&theme=" \
              "Dark&style=1&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=" \
              "%5B%5D&disabled_features=%5B%5D&locale=en&utm_source=binguru.net&utm_medium=widget_new&utm_campaign" \
              "=chart&utm_term=FX%3A"
url_list = [{'name': 'AUD/CAD', 'url': 'https://ru.investing.com/currencies/aud-cad-technical'},
            {'name': 'AUD/JPY', 'url': 'https://ru.investing.com/currencies/aud-jpy-technical'},
            {'name': 'AUD/USD', 'url': 'https://ru.investing.com/currencies/aud-usd-technical'},
            {'name': 'CAD/JPY', 'url': 'https://ru.investing.com/currencies/cad-jpy-technical'},
            {'name': 'CHF/JPY', 'url': 'https://ru.investing.com/currencies/chf-jpy-technical'},
            {'name': 'EUR/CHF', 'url': 'https://ru.investing.com/currencies/eur-chf-technical'},
            {'name': 'CAD/CHF', 'url': 'https://ru.investing.com/currencies/cad-chf-technical'},
            {'name': 'GBP/USD', 'url': 'https://ru.investing.com/currencies/gbp-usd-technical'},
            {'name': 'GBP/CAD', 'url': 'https://ru.investing.com/currencies/gbp-cad-technical'},
            {'name': 'NZD/CAD', 'url': 'https://ru.investing.com/currencies/nzd-cad-technical'},
            {'name': 'EUR/CAD', 'url': 'https://ru.investing.com/currencies/eur-cad-technical'},
            {'name': 'EUR/AUD', 'url': 'https://ru.investing.com/currencies/eur-aud-technical'},
            {'name': 'EUR/NZD', 'url': 'https://ru.investing.com/currencies/eur-nzd-technical'},
            {'name': 'GBP/CHF', 'url': 'https://ru.investing.com/currencies/gbp-chf-technical'},
            {'name': 'EUR/GBP', 'url': 'https://ru.investing.com/currencies/eur-gbp-technical'},
            {'name': 'EUR/JPY', 'url': 'https://ru.investing.com/currencies/eur-jpy-technical'},
            {'name': 'EUR/USD', 'url': 'https://ru.investing.com/currencies/eur-usd-technical'},
            {'name': 'GBP/AUD', 'url': 'https://ru.investing.com/currencies/gbp-aud-technical'},
            {'name': 'GBP/JPY', 'url': 'https://ru.investing.com/currencies/gbp-jpy-technical'},
            {'name': 'NZD/JPY', 'url': 'https://ru.investing.com/currencies/nzd-jpy-technical'},
            {'name': 'NZD/USD', 'url': 'https://ru.investing.com/currencies/nzd-usd-technical'},
            {'name': 'USD/CAD', 'url': 'https://ru.investing.com/currencies/usd-cad-technical'},
            {'name': 'USD/CHF', 'url': 'https://ru.investing.com/currencies/usd-chf-technical'},
            {'name': 'USD/JPY', 'url': 'https://ru.investing.com/currencies/usd-jpy-technical'},
            {'name': 'NZD/CHF', 'url': 'https://ru.investing.com/currencies/nzd-chf-technical'},
            {'name': 'AUD/CHF', 'url': 'https://ru.investing.com/currencies/aud-chf-technical'},
            {'name': 'AUD/NZD', 'url': 'https://ru.investing.com/currencies/aud-nzd-technical'},
            ]  # список валют для торговли
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.138 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9'}
URL = 'https://ru.investing.com/technical/technical-summary'  # адрес для парсинга
s_money = [{'name': 'AUD/CAD', 'em1': ':Australia:', 'em2': ':Canada:', 'plus': 'https://imbt.ga/KbVtD3kF20',
            'minus': 'https://imbt.ga/FXyoNaGOvr', 'buy': 'https://imbt.ga/wVHYjikkr8',
            'sell': 'https://imbt.ga/SsfBnlPWY2', 'dogon': 'https://imbt.ga/0aGwiy5Yjw',
            'vozvrat': 'https://imbt.ga/6XV5jwS6QV', 'bug': 'https://imbt.ga/IbJD1ITS9w', 'korrect': 0.00002,
            'round': 5},
           {'name': 'AUD/JPY', 'em1': ':Australia:', 'em2': ':Japan:', 'plus': 'https://imbt.ga/jDv3tsncyK',
            'minus': 'https://imbt.ga/qcB6R1mlRs', 'buy': 'https://imbt.ga/tCdx3in38t',
            'sell': 'https://imbt.ga/nozY6Ne7pB', 'dogon': 'https://imbt.ga/I9tseWsocY',
            'vozvrat': 'https://imbt.ga/tRPzMRCgOE', 'bug': 'https://imbt.ga/tYQSQOAC3C', 'korrect': 0.002, 'round': 3},
           {'name': 'AUD/USD', 'em1': ':Australia:', 'em2': ':United_States:', 'plus': 'https://imbt.ga/mJdFJs7RtJ',
            'minus': 'https://imbt.ga/Pl9QK5phMv', 'buy': 'https://imbt.ga/30FeKXP7sh',
            'sell': 'https://imbt.ga/Km4hP6e9Wr', 'dogon': 'https://imbt.ga/g0jcL2Y5G0',
            'vozvrat': 'https://imbt.ga/p3DO5m69Rl', 'bug': 'https://imbt.ga/3wMm5t0tdR', 'korrect': 0.00002,
            'round': 5},
           {'name': 'CAD/JPY', 'em1': ':Canada:', 'em2': ':Japan:', 'plus': 'https://imbt.ga/ELZZfAkZiw',
            'minus': 'https://imbt.ga/ISyZsrRmBi', 'buy': 'https://imbt.ga/Ngt2A9q6w6',
            'sell': 'https://imbt.ga/IIIngktusD', 'dogon': 'https://imbt.ga/fAnLHCZxdO',
            'vozvrat': 'https://imbt.ga/Tme3wdb3UC', 'bug': 'https://imbt.ga/olZGuk5EM5', 'korrect': 0.002, 'round': 3},
           {'name': 'CHF/JPY', 'em1': ':Switzerland:', 'em2': ':Japan:', 'plus': 'https://imbt.ga/OcwjReh24b',
            'minus': 'https://imbt.ga/2xaQSAGNeY', 'buy': 'https://imbt.ga/efrp6i983n',
            'sell': 'https://imbt.ga/htl6vJNWFL', 'dogon': 'https://imbt.ga/2CO5s6BIla',
            'vozvrat': 'https://imbt.ga/sRwBbAz78P', 'bug': 'https://imbt.ga/pdiwfQ0PwS', 'korrect': 0.002, 'round': 3},
           {'name': 'EUR/CHF', 'em1': ':European_Union:', 'em2': ':Switzerland:', 'plus': 'https://imbt.ga/lIx2bIhrAk',
            'minus': 'https://imbt.ga/EhvjJydLQW', 'buy': 'https://imbt.ga/2hG2Bc1xbG',
            'sell': 'https://imbt.ga/vKCnuT9fYa', 'dogon': 'https://imbt.ga/Tsq21v6sC8',
            'vozvrat': 'https://imbt.ga/ib0r7JWatt', 'bug': 'https://imbt.ga/FCTUIqExgw', 'korrect': 0.00002,
            'round': 5},
           {'name': 'CAD/CHF', 'em1': ':Canada:', 'em2': ':Switzerland:', 'plus': 'https://imbt.ga/4phSHMUEQ7',
            'minus': 'https://imbt.ga/E3cTX9PKJA', 'buy': 'https://imbt.ga/tWJVdnr8ks',
            'sell': 'https://imbt.ga/102RVtvdAY', 'dogon': 'https://imbt.ga/oq14yVTxkL',
            'vozvrat': 'https://imbt.ga/cMGZ35ZKYb', 'bug': 'https://imbt.ga/jaJFENwcbi', 'korrect': 0.00002,
            'round': 5},
           {'name': 'GBP/USD', 'em1': ':United_Kingdom:', 'em2': ':United_States:',
            'plus': 'https://imbt.ga/PNfNXRYTa5',
            'minus': 'https://imbt.ga/fWBD4MJXrA', 'buy': 'https://imbt.ga/MwW68qw75x',
            'sell': 'https://imbt.ga/npI9sgMK1n', 'dogon': 'https://imbt.ga/8neMhF8vKe',
            'vozvrat': 'https://imbt.ga/DgtgnuhbP5', 'bug': 'https://imbt.ga/T8BsTEqGEO', 'korrect': 0.00002,
            'round': 5},
           {'name': 'GBP/CAD', 'em1': ':United_Kingdom:', 'em2': ':Canada:', 'plus': 'https://imbt.ga/rxtVpPXKm9',
            'minus': 'https://imbt.ga/elwSJLSoR2', 'buy': 'https://imbt.ga/mqmCi6v8la',
            'sell': 'https://imbt.ga/SA00pgSCDx', 'dogon': 'https://imbt.ga/mC5Zv4PoOm',
            'vozvrat': 'https://imbt.ga/g1HOHj7065', 'bug': 'https://imbt.ga/LmCOpI5xUM', 'korrect': 0.00002,
            'round': 5},
           {'name': 'NZD/CAD', 'em1': ':New_Zealand:', 'em2': ':Canada:', 'plus': 'https://imbt.ga/rMEJ2Mq7gu',
            'minus': 'https://imbt.ga/fQY4hG3qPr', 'buy': 'https://imbt.ga/eGlFh4ZoC3',
            'sell': 'https://imbt.ga/4IGaW1VQNN', 'dogon': 'https://imbt.ga/RlZpkhACNM',
            'vozvrat': 'https://imbt.ga/69FwVGs0gV', 'bug': 'https://imbt.ga/RZSahDRb5j', 'korrect': 0.00002,
            'round': 5},
           {'name': 'EUR/CAD', 'em1': ':European_Union:', 'em2': ':Canada:', 'plus': 'https://imbt.ga/91xVqI6RZE',
            'minus': 'https://imbt.ga/jE832r0tqt', 'buy': 'https://imbt.ga/j3laXKggkx',
            'sell': 'https://imbt.ga/83N9DxEhUi', 'dogon': 'https://imbt.ga/ehd0OpmmG0',
            'vozvrat': 'https://imbt.ga/ckjMxaHtmN', 'bug': 'https://imbt.ga/OgHHdWqZva', 'korrect': 0.00002,
            'round': 5},
           {'name': 'EUR/AUD', 'em1': ':European_Union:', 'em2': ':Australia:', 'plus': 'https://imbt.ga/wLoP1NOqVa',
            'minus': 'https://imbt.ga/55evGVgtHy', 'buy': 'https://imbt.ga/EIsmfa3k9R',
            'sell': 'https://imbt.ga/CBywPubdQe', 'dogon': 'https://imbt.ga/A3b0grbOHh',
            'vozvrat': 'https://imbt.ga/woTzrdGR50', 'bug': 'https://imbt.ga/eeArFr4MA5', 'korrect': 0.00002,
            'round': 5},
           {'name': 'EUR/NZD', 'em1': ':European_Union:', 'em2': ':New_Zealand:', 'plus': 'https://imbt.ga/vqjSHRrmox',
            'minus': 'https://imbt.ga/dLdKTgT0hA', 'buy': 'https://imbt.ga/Mu9vzxFK02',
            'sell': 'https://imbt.ga/2EwvOSUFE2', 'dogon': 'https://imbt.ga/yEoZGfXrvf',
            'vozvrat': 'https://imbt.ga/5O08Zs091b', 'bug': 'https://imbt.ga/NtMHufCFdn', 'korrect': 0.00002,
            'round': 5},
           {'name': 'GBP/CHF', 'em1': ':United_Kingdom:', 'em2': ':Switzerland:', 'plus': 'https://imbt.ga/Icz46pCvdw',
            'minus': 'https://imbt.ga/eCkAtOFpIt', 'buy': 'https://imbt.ga/H5t8HZEgPx',
            'sell': 'https://imbt.ga/AmHOBF8v5i', 'dogon': 'https://imbt.ga/j6Wm9GTPT4',
            'vozvrat': 'https://imbt.ga/35DIZP7jG3', 'bug': 'https://imbt.ga/h38fX0yFFk', 'korrect': 0.00002,
            'round': 5},
           {'name': 'EUR/GBP', 'em1': ':European_Union:', 'em2': ':United_Kingdom:',
            'plus': 'https://imbt.ga/2pmGjI7EVT',
            'minus': 'https://imbt.ga/EkNPlOPRpa', 'buy': 'https://imbt.ga/VDfeNiVXia',
            'sell': 'https://imbt.ga/8bhyIbTtpS', 'dogon': 'https://imbt.ga/UrLvy8vjuB',
            'vozvrat': 'https://imbt.ga/PtQixMyigy', 'bug': 'https://imbt.ga/XjqN2va4mW', 'korrect': 0.00002,
            'round': 5},
           {'name': 'EUR/JPY', 'em1': ':European_Union:', 'em2': ':Japan:', 'plus': 'https://imbt.ga/yyIvs6WKON',
            'minus': 'https://imbt.ga/EvKkVpL8gE', 'buy': 'https://imbt.ga/qDmp8ywjVs',
            'sell': 'https://imbt.ga/qM7rZ1XPuN', 'dogon': 'https://imbt.ga/AuCzuYJDRj',
            'vozvrat': 'https://imbt.ga/YKZ0hg4w74', 'bug': 'https://imbt.ga/f3yoIIXBNH', 'korrect': 0.002, 'round': 3},
           {'name': 'EUR/USD', 'em1': ':European_Union:', 'em2': ':United_States:',
            'plus': 'https://imbt.ga/hLzt7JxoG8',
            'minus': 'https://imbt.ga/w18GlCPITl', 'buy': 'https://imbt.ga/Vys7AwZLpo',
            'sell': 'https://imbt.ga/lnKVQciqXv', 'dogon': 'https://imbt.ga/4OSMz7mcM8',
            'vozvrat': 'https://imbt.ga/NaNucxILk8', 'bug': 'https://imbt.ga/DFzbvRWZX3', 'korrect': 0.00002,
            'round': 5},
           {'name': 'GBP/AUD', 'em1': ':United_Kingdom:', 'em2': ':Australia:',
            'plus': 'https://imbt.ga/KWCrbCCnX7',
            'minus': 'https://imbt.ga/Fceu6E87Ki', 'buy': 'https://imbt.ga/28voxGhzfa',
            'sell': 'https://imbt.ga/EP4AoqqXkM', 'dogon': 'https://imbt.ga/8x4YvpG1J2',
            'vozvrat': 'https://imbt.ga/mkYUoPPmUr', 'bug': 'https://imbt.ga/jp95BIF43o', 'korrect': 0.00002,
            'round': 5},
           {'name': 'GBP/JPY', 'em1': ':United_Kingdom:', 'em2': ':Japan:',
            'plus': 'https://imbt.ga/3fWCGaSWaG',
            'minus': 'https://imbt.ga/Q8DvrDtFQv', 'buy': 'https://imbt.ga/Yst1Avy5kI',
            'sell': 'https://imbt.ga/tBKXTydDhf', 'dogon': 'https://imbt.ga/cwlvJRBu4o',
            'vozvrat': 'https://imbt.ga/h89prAp1Xi', 'bug': 'https://imbt.ga/xKjrO9Fite', 'korrect': 0.002, 'round': 3},
           {'name': 'NZD/JPY', 'em1': ':New_Zealand:', 'em2': ':Japan:',
            'plus': 'https://imbt.ga/v5K4OaZ0nU',
            'minus': 'https://imbt.ga/Onlt0IQL0q', 'buy': 'https://imbt.ga/UUgNWzAfpn',
            'sell': 'https://imbt.ga/gub9WTcCvn', 'dogon': 'https://imbt.ga/QngD5673pA',
            'vozvrat': 'https://imbt.ga/78sfzLMIqF', 'bug': 'https://imbt.ga/OHaGII4IMm', 'korrect': 0.002, 'round': 3},
           {'name': 'NZD/USD', 'em1': ':New_Zealand:', 'em2': ':United_States:',
            'plus': 'https://imbt.ga/qi3KchodWn',
            'minus': 'https://imbt.ga/KczHz2i2CF', 'buy': 'https://imbt.ga/cPIOxKMqcw',
            'sell': 'https://imbt.ga/zAM2oGuUO7', 'dogon': 'https://imbt.ga/9lgT9TlUBs',
            'vozvrat': 'https://imbt.ga/yR2BkleFL5', 'bug': 'https://imbt.ga/dO8Bq1TPWi', 'korrect': 0.00002,
            'round': 5},
           {'name': 'USD/CAD', 'em1': ':United_States:', 'em2': ':Canada:',
            'plus': 'https://imbt.ga/f7Qy3y6IWI',
            'minus': 'https://imbt.ga/yHGco73q1p', 'buy': 'https://imbt.ga/viOPCzWc0S',
            'sell': 'https://imbt.ga/4R5FivKDWU', 'dogon': 'https://imbt.ga/fhiZOui83e',
            'vozvrat': 'https://imbt.ga/nUDqg1wM4e', 'bug': 'https://imbt.ga/Gmd5T9YLz8', 'korrect': 0.00002,
            'round': 5},
           {'name': 'USD/CHF', 'em1': ':United_States:', 'em2': ':Switzerland:',
            'plus': 'https://imbt.ga/BnJzyZtlmc',
            'minus': 'https://imbt.ga/eShbU10c1f', 'buy': 'https://imbt.ga/66oHQOG0dm',
            'sell': 'https://imbt.ga/SFFPGUT0Cf', 'dogon': 'https://imbt.ga/mJxMWq0LG9',
            'vozvrat': 'https://imbt.ga/eEP3W07JWH', 'bug': 'https://imbt.ga/GW7Iok8TwK', 'korrect': 0.00002,
            'round': 5},
           {'name': 'USD/JPY', 'em1': ':United_States:', 'em2': ':Japan:',
            'plus': 'https://imbt.ga/xolysh0N13',
            'minus': 'https://imbt.ga/DAntMiSwLR', 'buy': 'https://imbt.ga/Oq1Z2WNBZe',
            'sell': 'https://imbt.ga/ZDdR3R0Kik', 'dogon': 'https://imbt.ga/uIOG3WrQ3V',
            'vozvrat': 'https://imbt.ga/OIkzx14n19', 'bug': 'https://imbt.ga/AuINzWYnIa', 'korrect': 0.002, 'round': 3},
           {'name': 'NZD/CHF', 'em1': ':New_Zealand:', 'em2': ':Switzerland:',
            'plus': 'https://imbt.ga/uKk5WHYmJ7',
            'minus': 'https://imbt.ga/wgFvsnUoWi', 'buy': 'https://imbt.ga/nynN83eJ6r',
            'sell': 'https://imbt.ga/83fgiYN1wW', 'dogon': 'https://imbt.ga/vmhnFM3fRQ',
            'vozvrat': 'https://imbt.ga/N2fXe6neSp', 'bug': 'https://imbt.ga/OYqwK9Kn2B', 'korrect': 0.00002,
            'round': 5},
           {'name': 'AUD/CHF', 'em1': ':Australia:', 'em2': ':Switzerland:',
            'plus': 'https://imbt.ga/b6maEBO6i7',
            'minus': 'https://imbt.ga/jkQcvtwSP5', 'buy': 'https://imbt.ga/B36y1PV1ku',
            'sell': 'https://imbt.ga/mza3wg6tl7', 'dogon': 'https://imbt.ga/wJ9UckfBvE',
            'vozvrat': 'https://imbt.ga/pVS1UWNcIC', 'bug': 'https://imbt.ga/NeyLCwwBcE', 'korrect': 0.00002,
            'round': 5},
           {'name': 'AUD/NZD', 'em1': ':Australia:', 'em2': ':New_Zealand:',
            'plus': 'https://imbt.ga/SmYkBbra7R',
            'minus': 'https://imbt.ga/gc5swFKSGL', 'buy': 'https://imbt.ga/6k6klgs8zu',
            'sell': 'https://imbt.ga/oNnCyNHZmU', 'dogon': 'https://imbt.ga/bkH7SI6qD0',
            'vozvrat': 'https://imbt.ga/JDmEiWQpaV', 'bug': 'https://imbt.ga/IX12nLipWd', 'korrect': 0.00002,
            'round': 5}
           ]  # список валют с набором  эмодзи
t_option = [
    {'time': 185, 'name': '3 минуты'},
    {'time': 245, 'name': '4 минуты'},
    {'time': 305, 'name': '5 минут'},
    {'time': 185, 'name': '3 минуты'}]  # выбор времени сессий
t_dogon = [
    {'time': 125, 'name': '2 минуты', 'intname': 2},
    {'time': 125, 'name': '2 минуты', 'intname': 2},
    {'time': 125, 'name': '2 минуты', 'intname': 2},
    {'time': 125, 'name': '2 минуты', 'intname': 2},
    {'time': 65, 'name': '1 минута', 'intname': 1}]  # выбор времени догона

# s_time = 59400  # время сессии
log_table = {'xl_nomer': ['№ п/п', 0],
             'xl_data': ['Дата', ''],
             'xl_time': ['Время открытия опциона', datetime.datetime],
             'xl_name': ['Валюта', ''],
             'xl_option': ['Опцион', ''],
             't1': ['Время объявления опциона', datetime.datetime],
             'xl_time_option': ['Время опциона, мин', ''],
             'xl_t1t2_delta': ['Время поиска точки входа, с', ''],
             'xl_vh_price': ['Цена входа', 0],
             'xl_plus': ['ПЛЮС', 0],
             'xl_minus': ['МИНУС', 0],
             'xl_vozvrat': ['ВОЗВРАТ', 0],
             'xl_i_price': ['Цена итога', 0],
             'xl_t3t4_delta': ['Время поиска точки входа догона, с', 0],
             'xl_dg1': ['Догон 1 мин.', 0],
             'xl_dg2': ['Догон 2 мин', 0],
             't3': ['Время объявления догона', datetime.datetime],
             't4': ['Время открытия догона', datetime.datetime],
             'xl_vh_price_dogon': ['Цена входа догона', 0],
             'xl_i_price_dogon': ['Цена итога догона', 0],
             'xl_t_bug': ['Текст ошибки', ''],
             'xl_bug': ['Ошибка', 0]}  # словарь для лога
