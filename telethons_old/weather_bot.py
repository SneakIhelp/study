import telebot
import time
from telebot import apihelper
from telebot import types
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

if __name__ == "__main__":

    while True:
        try:
            print('Bot started')
            config_dict = get_default_config()
            config_dict['language'] = 'ru'

            bot = telebot.TeleBot("1872137334:AAFRvEZS0j7hq-wrFAh9Le8F6-dORggl7xw")


            @bot.message_handler(commands=['start', 'help'])
            def welcome(message):
                chat_id = message.chat.id
                bot.send_message(chat_id, "Привет, я бот, отображающий погоду в любом городе, пожалуйста, напиши свой город",
                                 reply_markup=keyboard())


            @bot.message_handler(func=lambda message: True)
            def gane(message):
                chat_id = message.chat.id
                place = message.text
                owm = OWM('5e53f266fcc1e46be38bb6d8a9a0ab61')
                mgr = owm.weather_manager()
                try:
                    observation = mgr.weather_at_place(place)
                    w = observation.weather
                    temp = w.temperature("celsius")
                    t = round(temp['temp'])
                    t1 = temp['feels_like']
                    t2 = round(temp['temp_max'])
                    t3 = round(temp['temp_min'])
                    t4 = (t3 + t2) / 2

                    genius = f'Сейчас в городе {str(place)} температура {str(t)} °C, ощущается как {str(t1)} °C, ' \
                        f'максимальная температура {str(t2)} °C, минимальная температура {str(t3)} °C, средняя температура ' \
                        f'сегодня {str(t4)} °C '

                    monitoring = owm.weather_manager().weather_at_place(place)
                    weather = monitoring.weather
                    status = weather.detailed_status
                    helpme = f'Сейчас в городе {str(place)} {str(status)}.'

                    bot.send_message(chat_id, helpme)
                    bot.send_message(chat_id, genius)
                except:
                    bot.reply_to(message, "Вы указали неверный город или что-то пошло не так, попробуйте ещё раз!")


            def keyboard():
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                btn0 = types.KeyboardButton('Москва')
                btn1 = types.KeyboardButton('Санкт-Петербург')
                btn2 = types.KeyboardButton('Краснодар')
                btn3 = types.KeyboardButton('Уфа')
                markup.add(btn0, btn1, btn2, btn3)
                return markup


            bot.polling(none_stop=True)

        except Exception as e:
            print(e)
            time.sleep(15)
