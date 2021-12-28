import telebot
from datetime import date
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
from telebot import util
import time

while True:
    try:
        print('Bot started')

        def dayOftheWeek(n):
            ponedelnikFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\ponedelnikFirst.txt", encoding="utf8").read()
            vtornikFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\vtornikFirst.txt", encoding="utf8").read()
            sredaFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\sredaFirst.txt", encoding="utf8").read()
            chetvFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\chetvFirst.txt", encoding="utf8").read()
            pyatnicaFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\pyatnicaFirst.txt", encoding="utf8").read()
            subbFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\subbotaFirst.txt", encoding="utf8").read()
            voscrFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\voskrFirst.txt", encoding="utf8").read()

            if n == 0:
                return ponedelnikFirstGr
            if n == 1:
                return vtornikFirstGr
            if n == 2:
                return sredaFirstGr
            if n == 3:
                return chetvFirstGr
            if n == 4:
                return pyatnicaFirstGr
            if n == 5:
                return subbFirstGr
            if n == 6:
                return voscrFirstGr


        current_date = date.today()
        denNed = dayOftheWeek(current_date.weekday())

        

        def keyboard():
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn0 = types.KeyboardButton('Да')
            btn1 = types.KeyboardButton('Нет')
            markup.add(btn0, btn1)
            return markup
        
        def usable_keyb():
                markup = InlineKeyboardMarkup()
                markup.row_width = 4
                markup.add(InlineKeyboardButton("Физика", callback_data="cb_fiz"),
                           InlineKeyboardButton("Математика", callback_data="cb_matem"),
                           InlineKeyboardButton("Информатика", callback_data="cb_inf"),
                           InlineKeyboardButton("Расписание", callback_data="raspis"))
                return markup
        
        
        choose_fiz = InlineKeyboardMarkup(row_width = 2)
        choose_fiz.add(InlineKeyboardButton("Ссылка на файл по физике", url="https://docs.google.com/document/d/1cffoD8vB6r8kj6EOPzNLT6cLAoIC5ZRH/edit?rtpof=true"),
                    InlineKeyboardButton("Темы", callback_data="tems_fiz"),
                    InlineKeyboardButton("Вернуться назад", callback_data="backuptoChoose"))

        choose_inf = InlineKeyboardMarkup(row_width = 2)
        choose_inf.add(InlineKeyboardButton("Ссылка на файл по информатике", url="https://docs.google.com/document/d/1DltZQKCpGnKrdafVkb56YSBJNkB1E86H/edit"),
                    InlineKeyboardButton("Темы", callback_data="tems_inf"),
                    InlineKeyboardButton("Вернуться назад", callback_data="backuptoChoose"))

        choose_mat = InlineKeyboardMarkup(row_width = 2)
        choose_mat.add(InlineKeyboardButton("Билеты по математике первое полугодие", url="https://docs.google.com/document/d/1dd0CWRmZjNurdPl-jypfI378EDEPViWPM3y3Fq8pR1o/edit"),
                    InlineKeyboardButton("Темы", callback_data="tems_mat"),
                    InlineKeyboardButton("Вернуться назад", callback_data="backuptoChoose"))

        choose_raspis_group = InlineKeyboardMarkup(row_width=2)
        choose_raspis_group.add(InlineKeyboardButton("1 подгруппа", callback_data="first_group_raspis"), 
                                InlineKeyboardButton("2 подгруппа", callback_data="second_group_raspis"),
                                InlineKeyboardButton("Вернуться назад", callback_data="backuptoChoose"))

        bot = telebot.TeleBot("5072410027:AAHoVWbuE0bhAunjTsRmc9E50_qFZl47Ymg")

        @bot.message_handler(commands=['start'])
        def welcome(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, "куку")
            bot.send_message(chat_id, "Ты хуесос?", reply_markup=keyboard())
        
        @bot.message_handler(commands=['help'])
        def help_ms(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, "сам ты негр")
            bot.send_message(chat_id, "Ты хуесос?", reply_markup=keyboard())

        @bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            forbetasitfiz = InlineKeyboardMarkup(row_width = 1)
            forbetasitfiz.add(InlineKeyboardButton("Вернуться назад", callback_data="cb_fiz"))

            forbetasitmatem = InlineKeyboardMarkup(row_width = 1)
            forbetasitmatem.add(InlineKeyboardButton("Вернуться назад", callback_data="cb_matem"))
            
            forbetasitinf = InlineKeyboardMarkup(row_width = 1)
            forbetasitinf.add(InlineKeyboardButton("Вернуться назад", callback_data="cb_inf"))

            raspis_firstGroup  = InlineKeyboardMarkup(row_width = 4)
            raspis_firstGroup.add(InlineKeyboardButton("Сегодня", callback_data="today_first"),
                                  InlineKeyboardButton("Завтра", callback_data="tomorrow_first"),
                                  InlineKeyboardButton("Произвольный день недели", callback_data="choose_ned_first"),
                                  InlineKeyboardButton("Неделя", callback_data="week_first"),
                                  InlineKeyboardButton("Вернуться назад", callback_data="raspis"))

            raspis_secondGroup  = InlineKeyboardMarkup(row_width = 4)
            raspis_secondGroup.add(InlineKeyboardButton("Сегодня", callback_data="today_sec"),
                                  InlineKeyboardButton("Завтра", callback_data="tomorrow_sec"),
                                  InlineKeyboardButton("Произвольный день недели", callback_data="choose_ned_sec"),
                                  InlineKeyboardButton("Неделя", callback_data="week_sec"),
                                  InlineKeyboardButton("Вернуться назад", callback_data="raspis"))
            
            for_ChoosenedFirst = InlineKeyboardMarkup(row_width = 1)
            for_ChoosenedFirst.add(InlineKeyboardButton("Понедельник", callback_data="FirstDay_First"),
                                   InlineKeyboardButton("Вторник", callback_data="SecDay_First"),
                                   InlineKeyboardButton("Среда", callback_data="ThirdDay_First"),
                                   InlineKeyboardButton("Четверг", callback_data="FourDay_First"),
                                   InlineKeyboardButton("Пятница", callback_data="FiveDay_First"),
                                   InlineKeyboardButton("Суббота", callback_data="SixDay_First"),
                                   InlineKeyboardButton("Воскресенье", callback_data="SevenDay_First"),
                                   InlineKeyboardButton("Вернуться назад", callback_data="first_group_raspis"))

            if call.data == "cb_fiz":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Всё что известно по физике:", reply_markup=choose_fiz)
            elif call.data == "cb_matem":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Всё что известно по математике:", reply_markup=choose_mat)
            elif call.data == "cb_inf":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Всё что известно по информатике:", reply_markup=choose_inf)
            elif call.data == "tems_fiz":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="[beta]", reply_markup=forbetasitfiz)
            elif call.data == "tems_inf":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="[beta]", reply_markup=forbetasitinf)
            elif call.data == "tems_mat":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="[beta]", reply_markup=forbetasitmatem)
            elif call.data == "backuptoChoose":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какой предмет тебе нужен, зайка?", reply_markup=usable_keyb())
            else:
                if call.data == "raspis":
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери подгруппу:", reply_markup=choose_raspis_group)
                elif call.data == "first_group_raspis":
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите какое расписание вы хотите получить:", reply_markup=raspis_firstGroup)
                elif call.data == "second_group_raspis":
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите какое расписание вы хотите получить:", reply_markup=raspis_secondGroup)
                else:
                    if call.data == "today_first":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=denNed, reply_markup=raspis_firstGroup)
                    elif call.data == "tomorrow_first":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(current_date.weekday() + 1), reply_markup=raspis_firstGroup)
                    elif call.data == "choose_ned_first":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите день недели: ", reply_markup=for_ChoosenedFirst)
                    else:
                        if call.data == "FirstDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(0), reply_markup=raspis_firstGroup)
                        elif call.data == "SecDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(1), reply_markup=raspis_firstGroup)
                        elif call.data == "ThirdDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(2), reply_markup=raspis_firstGroup)
                        elif call.data == "FourDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(3), reply_markup=raspis_firstGroup)
                        elif call.data == "FiveDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(4), reply_markup=raspis_firstGroup)
                        elif call.data == "SixDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(5), reply_markup=raspis_firstGroup)
                        elif call.data == "SevenDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeek(6), reply_markup=raspis_firstGroup)
                

        @bot.message_handler(func=lambda message: True)
        def mainfunc(message):
            chat_id = message.chat.id   
            if message.text.lower() == "да":
                bot.send_message(chat_id, "Какой предмет тебе нужен, зайка?", reply_markup=usable_keyb())

            else:
                bot.send_message(chat_id, "ну и пошёл нахуй(")

        bot.polling(none_stop=True)

    except Exception as e:
        print("Error:")
        print(e)
        time.sleep(15)
