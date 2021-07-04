from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pyowm.owm import OWM

owm = OWM('5e53f266fcc1e46be38bb6d8a9a0ab61')
place = 'Moscow'
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature("celsius")
t = temp['temp']
t1 = temp['feels_like']
t2 = temp['temp_max']
t3 = temp['temp_min']
t4 = (t3 + t2) / 2

genius = 'В городе ' + str(place) + ' температура ' + str(round(t)) + ' °C, ощущается как ' + str(round(t1)) + '°C, ' \
         'максимальная тепература ' + str(
    round(t2)) + \
         ' °C, минимальная температура ' + str(round(t3)) + ' °C, средняя тепература за день ' + \
         str(round(t4)) + ' °C '
try:
    monitoring = owm.weather_manager().weather_at_place(place)
    weather = monitoring.weather
    status = weather.detailed_status
    helpme = 'It is ' + str(status) + ' in ' + str(place) + ' now. '
except:
    pass


print("Бот запущен. ")


def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я бот отображающий погоду в Москве \n"
                                                   'Напишите "Покажи погоду", чтобы я отбразил вам погоду в Москве')


def on_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    try:
        if text == "Покажи погоду":
            context.bot.send_message(chat_id=chat.id, text=helpme)
            context.bot.send_message(chat_id=chat.id, text=genius)
        else:
            context.bot.send_message(chat_id=chat.id, text='Что-то пошло не так! \n'
                                                           'Попробуйте написать "Покажи погоду", чтобы я отбразил вам '
                                                           'погоду в Москве')
    except:
        pass


token = "1872137334:AAEcFaJvabvqiKoch_T-0J75WUcgekQ3UMs"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()
