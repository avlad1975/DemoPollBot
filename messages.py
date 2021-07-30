import random
from constant import dogon, fanny, fuck
from emoji import emojize


def first_poll_message(log_data):
    main_str = []
    f_message = '<b>Готовим пару ' + log_data.name + '</b>'
    f_message = f_message + ' ' + emojize(log_data.em1, use_aliases=True) + '<b>/</b>' + emojize(log_data.em2,
                                                                                                 use_aliases=True)
    main_str.append(f_message)
    main_str = '\n'.join(main_str)  # формирование строки вывода 1-го сообщения
    return main_str


def second_poll_message(link):  # второе сообщение в телеграм
    main_str = []
    s_message = '\n<a href="' + link + '">Ссылка на валютную пару </a>📊\n'
    s_message = s_message + '\n<b>Проведите анализ валютной пары, и проголосуйте в опросе ниже 👇</b>'
    main_str.append(s_message)
    main_str = '\n'.join(main_str)  # формирование строки вывода 2-го сообщения
    return main_str


def none_poll_message():  # второе сообщение в телеграм
    main_str = []
    s_message = 'Результаты голосования: <b>5О% продажа 🔴 / 5О% покупка 🟢</b>'
    s_message = s_message + '\n<b>Пропускаем вход в рынок ❗</b>'
    main_str.append(s_message)
    main_str = '\n'.join(main_str)  # формирование строки вывода 2-го сообщения
    return main_str


def third_poll_message(log_data):  # второе сообщение в телеграм
    main_str = []
    s_message = 'Результаты голосования:'
    o_text = ' <b>Вход ВНИЗ (Продажа)</b>'
    o_zy = ":red_circle:"
    if 'ПОКУПАТЬ' in log_data.resume:  # формирование строки вывода для пары Активно покупать
        o_zy = ":green_circle:"
        o_text = ' <b>Вход ВВЕРХ (Покупка)</b>'
    s_message = s_message + '<b>' + o_text + '</b>' + ' ' + emojize(o_zy, use_aliases=True) + '\n'
    s_message = s_message + '\nЦена торгового актива: <b>' + str(log_data.price) + '</b>'
    s_message = s_message + '\nВремя сделки: <b>5 минут </b>🕔'
    main_str.append(s_message)
    main_str = '\n'.join(main_str)  # формирование строки вывода 2-го сообщения
    return main_str


def fourth_poll_message(log_data):  # третье сообщение в телеграм (данные по валютной паре)
    i_text = []
    itog_em = ''
    signal = ''
    if log_data.plus:
        itog_em = random.choice(fanny)
        signal = 'ПЛЮС'
    elif log_data.vozvrat:
        itog_em = random.choice(fanny)
        signal = 'ВОЗВРАТ'
    s_message = 'Валютная пара ' + '<b>' + log_data.name + '</b> '
    s_message = s_message + emojize(log_data.em1, use_aliases=True) + '<b>/</b>'
    s_message = s_message + emojize(log_data.em2, use_aliases=True)
    s_message = s_message + '\nЦена закрытия: <b>' + str(log_data.itg_price) + '</b>'
    s_message = s_message + '\nИтог прогноза: <b>' + signal + '</b>' + ' ' + emojize(itog_em, use_aliases=True)
    i_text.append(s_message)
    return '\n'.join(i_text)


def dogon_poll_message(log_data, link):  # сообщение о догоне в телеграм для голосования
    i_text = []
    s_message = 'Валютная пара ' + '<b>' + log_data.name + '</b> '
    s_message = s_message + ' ' + emojize(log_data.em1, use_aliases=True) + '<b>/</b>'
    s_message = s_message + ' ' + emojize(log_data.em2, use_aliases=True)
    s_message = s_message + '\nЦена закрытия: <b>' + str(log_data.itg_price) + '</b>'
    s_message = s_message + '\nИтог прогноза: <b>МИНУС ❌</b>\n'
    s_message = s_message + '\n<a href="' + link + '">Ссылка на валютную пару </a>📊\n'
    s_message = s_message + '\n<b>Проведите анализ валютной пары, и проголосуйте в опросе ниже 👇</b>'
    i_text.append(s_message)
    return '\n'.join(i_text)


def dogon_poll_sec_message(log_data):  # сообщение о догоне в телеграм (ручной трейдинг)
    dogon_text = []
    dg_message = ''
    if log_data.buy:
        napr = "Вход ВВЕРХ (Покупка) 🟢"
    else:
        napr = "Вход ВНИЗ (Продажа) 🔴"
    if log_data.dgn_price1 > 0:
        dg_message = dg_message + 'Результаты голосования: <b>' + napr + ' </b>\n'
        dg_message = dg_message + '\nЦена торгового актива: <b>' + str(log_data.dgn_price1) + '</b>'
        dg_message = dg_message + '\nВремя перекрытия: <b>3 минуты 🕔</b>'
    dogon_text.append(dg_message)
    return '\n'.join(dogon_text)


def itog_poll_dogon_message(log_data):  # сообщение об итоге догона (входные данные, итоговые данные)
    dgn_res = 0
    itog_text_dogon = []
    if log_data.buy:
        dgn_res = log_data.dgn_itg1 - log_data.dgn_price1
    elif log_data.sell:
        dgn_res = log_data.dgn_price1 - log_data.dgn_itg1
    if dgn_res > 0:
        log_data.plus = True  # Внесение в лог параметра ПЛЮС
    if dgn_res > 0:
        itog_dogon = ' ПЛЮС ✅'
        log_data.plus = True  # Внесение в лог параметра ПЛЮС
    else:
        itog_dogon = "МИНУС ❌"
        log_data.minus = True  # Внесение в лог параметра МИНУС
    dogon_str = 'Валютная пара ' + '<b>' + log_data.name + '</b> ' + ' ' + emojize(
        log_data.em1, use_aliases=True)
    dogon_str = dogon_str + '<b>/</b>' + ' ' + emojize(log_data.em2, use_aliases=True)
    dogon_str = dogon_str + '\nЦена закрытия: <b>' + str(log_data.dgn_itg1) + '</b>'
    dogon_str = dogon_str + '\nИтог прогноза: <b>' + itog_dogon + '</b>'
    # dogon_str = dogon_str + ' ' + emojize(f_emodi, use_aliases=True)
    itog_text_dogon.append(dogon_str)
    return '\n'.join(itog_text_dogon)


def itog_sec_dogon_message(log_data):  # сообщение об итоге догона (входные данные, итоговые данные)
    dgn_res = 0
    itog_text_dogon = []
    if log_data.buy:
        dgn_res = log_data.dgn_itg2 - log_data.dgn_price2
    elif log_data.sell:
        dgn_res = log_data.dgn_price2 - log_data.dgn_itg2
    if dgn_res > 0:
        itog_dogon = 'ПЛЮС'
        log_data.plus = True  # Внесение в лог параметра ПЛЮС
        f_emodi = random.choice(fanny)
    else:
        itog_dogon = "МИНУС"
        log_data.minus = True  # Внесение в лог параметра МИНУС
        f_emodi = random.choice(fuck)
    dogon_str = 'Валютная пара ' + '<b>' + log_data.name + '</b> ' + ' ' + emojize(
        log_data.em1, use_aliases=True)
    dogon_str = dogon_str + '<b>/</b>' + ' ' + emojize(log_data.em2, use_aliases=True)
    dogon_str = dogon_str + '\nЦена закрытия: <b>' + str(log_data.dgn_itg2) + '</b>'
    dogon_str = dogon_str + '\nИтог прогноза: <b>' + itog_dogon + '</b>'
    dogon_str = dogon_str + ' ' + emojize(f_emodi, use_aliases=True)
    itog_text_dogon.append(dogon_str)
    return '\n'.join(itog_text_dogon)


def bug_message(picture, bot, channel_id):  # сообщение о баге
    i_text = []
    b_message = '<b> Сбой связи с сервером котировок</b>'
    b_message = b_message + '\n<b> Ищу другую пару</b>'
    i_text.append(b_message)
    i_text.append('<a href="' + picture + '">&#8205;</a>')
    bug_text = '\n'.join(i_text)
    bot.send_message(channel_id, bug_text, disable_web_page_preview=False,
                     parse_mode='HTML')  # отправка сообщения о баге
    return


def second_message(log_data):  # второе сообщение в телеграм в испаноязычный канал
    main_str = []
    s_message = ''
    o_text = 'ПРОДАВАТЬ'
    o_picture = '<a href="' + log_data.p_sell + '">&#8205;</a>'
    o_zy = ":red_circle:"
    if 'ПОКУПАТЬ' in log_data.resume:  # формирование строки вывода для пары Активно покупать
        o_zy = ":green_circle:"
        o_picture = '<a href="' + log_data.p_buy + '">&#8205;</a>'
        o_text = 'ПОКУПАТЬ'
    # s_message = s_message + '\n2. Сигнал от робота: <i>( Доступно для партнёров )🚀</i>'
    s_message = s_message + '\nСигнал от робота: <b>' + o_text + '</b>' + emojize(o_zy,
                                                                                  use_aliases=True)
    s_message = s_message + '\nТекущая цена: <b>' + str(log_data.price) + '</b>'

    s_message = s_message + '\nВремя опциона: <b>' + log_data.str_time + '</b>' + emojize(":stopwatch:",
                                                                                          use_aliases=True) + '\n'
    s_message = s_message + '\n<b>Уровни:</b> \n'
    s_message = s_message + 'Локальная область поддержки:  <i><a href="https://t.me/SmokeFXchatbot">' \
                            '( Доступно партнёрам ) </a></i>📉\n'
    s_message = s_message + 'Локальная область сопротивления:  <i><a href="https://t.me/SmokeFXchatbot">' \
                            '( Доступно партнёрам ) </a></i>📈\n'
    s_message = s_message + '\n<b>Точки разворота цены:</b>\n'
    s_message = s_message + 'Котировка разворота #1: <i><a href="https://t.me/SmokeFXchatbot">' \
                            '( Доступно для партнёров ) </a></i>🚫\n'
    s_message = s_message + 'Котировка разворота #2: <i><a href="https://t.me/SmokeFXchatbot">' \
                            '( Доступно для партнёров ) </a></i>🚫\n'
    s_message = s_message + '\nСила направления движения в сторону входа: <i>' \
                            '<a href="https://t.me/SmokeFXchatbot">( Доступно для партнёров ) ❗</a></i>\n'
    s_message = s_message + '\n<i>Резюме: <a href="https://t.me/SmokeFXchatbot">( Доступно для партнёров ) </a></i>🎯'
    main_str.append(s_message)
    main_str.append(o_picture)
    main_str = '\n'.join(main_str)  # формирование строки вывода 2-го сообщения
    return main_str


def third_message(log_data):  # третье сообщение в телеграм в испаноязычный канал(данные по валютной паре)
    i_text = []
    itog_em = ''
    itg_picture = ''
    signal = ''
    if log_data.plus:
        itog_em = random.choice(fanny)
        itg_picture = '<a href="' + log_data.p_plus + '">&#8205;</a>'
        signal = 'ПЛЮС'
    elif log_data.vozvrat:
        itog_em = random.choice(fanny)
        itg_picture = '<a href="' + log_data.p_vozvrat + '">&#8205;</a>'
        signal = 'ВОЗВРАТ'
    if log_data.buy:
        em = ":small_red_triangle:"
    else:
        em = ":small_red_triangle_down:"
    s_message = 'Валютная пара ' + '<b>' + log_data.name + '</b> '
    s_message = s_message + emojize(log_data.em1, use_aliases=True) + '<b>/</b>'
    s_message = s_message + emojize(log_data.em2, use_aliases=True) + emojize(em, use_aliases=True)
    s_message = s_message + '\nЦена закрытия: <b>' + str(log_data.itg_price) + '</b>'
    s_message = s_message + '\nИтог сигнала: <b>' + signal + '</b>' + emojize(itog_em,
                                                                              use_aliases=True)
    i_text.append(s_message)
    i_text.append(itg_picture)
    return '\n'.join(i_text)


def dogon_message(
        log_data):  # сообщение о догоне в испаноязычный канал (данные по валютной паре, время догона,цена входа)
    itog_picture = '<a href="' + log_data.p_dgn + '">&#8205;</a>'
    dogon_text = []
    dg_message = ''
    if log_data.buy:
        em = ":small_red_triangle:"
    else:
        em = ":small_red_triangle_down:"
    if log_data.dgn_price == 0:
        dg_message = '<b>Перекрытие — анализирую точку входа 🎯\n</b>'
        # dg_message = dg_message + '<b>Анализирую точку входа.\n</b>'
        # dg_message = dg_message + 'Валютная пара ' + '<b>' + log_data.name + '</b> '
        # dg_message = dg_message + emojize(log_data.em1, use_aliases=True) + '<b>/</b>'
        # dg_message = dg_message + emojize(log_data.em2, use_aliases=True) + emojize(em, use_aliases=True)
    if log_data.dgn_price > 0:
        dg_message = dg_message + '\nИтог сигнала: <b>ПЕРЕКРЫТИЕ </b>' + emojize(random.choice(dogon), use_aliases=True)
        dg_message = dg_message + '\nЦена входа: <b>' + str(log_data.dgn_price) + '</b>'
        dg_message = dg_message + '\nВремя перекрытия: <b>' + log_data.str_dgn_time + '</b>'
    dogon_text.append(dg_message)
    if log_data.dgn_price > 0:
        dogon_text.append(itog_picture)
    return '\n'.join(dogon_text)


def itog_dogon_message(
        log_data):  # сообщение об итоге догона для испаноязычного канала(входные данные, итоговые данные)
    dgn_res = 0
    itog_text_dogon = []
    if log_data.buy:
        dgn_res = log_data.dgn_itg - log_data.dgn_price
    elif log_data.sell:
        dgn_res = log_data.dgn_price - log_data.dgn_itg
    if dgn_res > 0:
        itog_dogon = 'ПЛЮС'
        log_data.plus = True  # Внесение в лог параметра ПЛЮС
        f_emodi = random.choice(fanny)
        res_dogon = '<a href="' + log_data.p_plus + '">&#8205;</a>'
    else:
        itog_dogon = "Первое перекрытие МИНУС"
        log_data.minus = True  # Внесение в лог параметра МИНУС
        f_emodi = random.choice(fuck)
        res_dogon = '<a href="' + log_data.p_minus + '">&#8205;</a>'
    dogon_str = 'Валютная пара ' + '<b>' + log_data.name + '</b> ' + emojize(
        log_data.em1, use_aliases=True)
    dogon_str = dogon_str + '<b>/</b>' + emojize(log_data.em2, use_aliases=True)
    dogon_str = dogon_str + '\nЦена закрытия: <b>' + str(log_data.dgn_itg) + '</b>'
    dogon_str = dogon_str + '\nИтог сигнала: <b>' + itog_dogon + '</b>'
    dogon_str = dogon_str + emojize(f_emodi, use_aliases=True)
    itog_text_dogon.append(dogon_str)
    itog_text_dogon.append(res_dogon)
    return '\n'.join(itog_text_dogon)


def first_message(log_data):  # Первое сообщение для испанского канала
    f_message = '<b>Валютная пара ' + log_data.name + '</b>'
    f_message = f_message + emojize(log_data.em1, use_aliases=True) + '<b>/</b>' + emojize(log_data.em2,
                                                                                           use_aliases=True)
    return f_message
