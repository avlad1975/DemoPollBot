from datetime import datetime, timedelta
from handtrade import trade_main, start_message, last_message
import time
from constant import cor_time, timeoption,timeoption2

flaghandoption = 0


def bot():
    global flaghandoption
    val_name = 'EUR/RUB'
    cordate = datetime.now() + timedelta(hours=cor_time + 1)
    day = datetime.weekday(cordate)
    if day >= 5:
        return
    day = datetime.weekday(datetime.now())
    if day >= 5:
        return
    while True:
        cordate = datetime.now() + timedelta(hours=cor_time + 1)
        day = datetime.weekday(cordate)
        thour = datetime.now() + timedelta(hours=cor_time)
        hour = thour.hour
        print(str(hour))
        if day >= 5:
            return
        day = datetime.weekday(datetime.now())
        if day >= 5:
            return
        if hour == timeoption or timeoption2:
            if flaghandoption == 0:
                start_message()
                flaghandoption = 1
            volume = trade_main(val_name)
            val_name = volume[1]
            time.sleep(2)
        else:
            if flaghandoption == 1:
                try:
                    last_message()
                except Exception as error:
                    print('Ошибка отправки итогового сообщения - ' + str(error))
            return


if __name__ == '__main__':
    bot()
