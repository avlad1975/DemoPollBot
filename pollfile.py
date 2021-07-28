import asyncio
import aiogram
import time
import datetime
from aiogram import Dispatcher, types
from constant import tokenpoll, channel_id
from telegram import (
    Bot
)

bot = aiogram.Bot(token=tokenpoll)
bot1 = Bot(tokenpoll)
dp = Dispatcher(bot)
result = [0, 0]  # итоги опроса
timers = 60
questions = ["Вход ВВЕРХ (покупка) 🟢", "Вход ВНИЗ (продажа) 🔴", "Пропускаю вход 🔵"]
loop = asyncio.get_event_loop()


@dp.poll_handler(lambda active_quiz: active_quiz)
async def just_poll_answer(active_quiz: types.Poll):
    """
    Реагирует на закрытие опроса/викторины. Если убрать проверку на poll.is_closed == True,
    то этот хэндлер будет срабатывать при каждом взаимодействии с опросом/викториной, наравне
    с poll_answer_handler
    Чтобы не было путаницы:
    * active_quiz - викторина, в которой кто-то выбрал ответ
    * saved_quiz - викторина, находящаяся в нашем "хранилище" в памяти
    Этот хэндлер частично повторяет тот, что выше, в части, касающейся поиска нужного опроса в нашем "хранилище".
    :param active_quiz: объект Poll
    """
    for i in range(2):  # запись результата опроса
        result[i] = active_quiz.options[i]['voter_count']


async def close_poll():
    dp.stop_polling()
    await dp.wait_closed()


def start(question):
    global result
    result = [0, 0]
    dt = datetime.datetime.now() + datetime.timedelta(seconds=timers)
    msg = bot1.send_poll(chat_id=channel_id,
                         question=question,
                         is_anonymous=True,
                         options=questions,
                         close_date=time.mktime(dt.timetuple()),
                         allows_multiple_answers=False)
    return msg


async def main(quest):
    start(quest)
    try:
        asyncio.get_event_loop().call_later(timers - 2, lambda: asyncio.ensure_future(close_poll()))
        await loop.create_task(dp.start_polling())
        # executor.start_polling(dp, skip_updates=True)
    except Exception as error:
        print('Ошибка цикла - ' + str(error))
    finally:
        print(result)
    return result


def poll(quest):
    loop.run_until_complete(main(quest))
    return result

# if __name__ == "__main__":

# loop.close()
