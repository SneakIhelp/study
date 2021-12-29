import telebot
from datetime import date
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
from telebot import util
import time

while True:
    try:
        print('Bot started')
        bot = telebot.TeleBot("5072410027:AAHoVWbuE0bhAunjTsRmc9E50_qFZl47Ymg")
        # the next condition is to hide the inline keyboards
        if True:
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

            for_ChoosenedSec = InlineKeyboardMarkup(row_width = 1)
            for_ChoosenedSec.add(InlineKeyboardButton("Понедельник", callback_data="FirstDay_Sec"),
                        InlineKeyboardButton("Вторник", callback_data="SecDay_Sec"),
                        InlineKeyboardButton("Среда", callback_data="ThirdDay_Sec"),
                        InlineKeyboardButton("Четверг", callback_data="FourDay_Sec"),
                        InlineKeyboardButton("Пятница", callback_data="FiveDay_Sec"),
                        InlineKeyboardButton("Суббота", callback_data="SixDay_Sec"),
                        InlineKeyboardButton("Воскресенье", callback_data="SevenDay_Sec"),
                        InlineKeyboardButton("Вернуться назад", callback_data="second_group_raspis"))

        def dayOftheWeekFirstgr(n):

            ponedelnikFirstGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\ponedelnikFirst.txt", encoding="utf8").read()
            vtornikFirstGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\vtornikFirst.txt", encoding="utf8").read()
            sredaFirstGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\sredaFirst.txt", encoding="utf8").read()
            chetvFirstGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\chetvFirst.txt", encoding="utf8").read()
            pyatnicaFirstGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\pyatnicaFirst.txt", encoding="utf8").read()
            subbFirstGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\subbotaFirst.txt", encoding="utf8").read()
            voscrFirstGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\voskrFirst.txt", encoding="utf8").read()

            """
            ponedelnikFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\ponedelnikFirst.txt", encoding="utf8").read()
            vtornikFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\vtornikFirst.txt", encoding="utf8").read()
            sredaFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\sredaFirst.txt", encoding="utf8").read()
            chetvFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\chetvFirst.txt", encoding="utf8").read()
            pyatnicaFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\pyatnicaFirst.txt", encoding="utf8").read()
            subbFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\subbotaFirst.txt", encoding="utf8").read()
            voscrFirstGr = open(r"C:\Users\Admin\git\py\study\schoolbot\voskrFirst.txt", encoding="utf8").read()
                                                                                                                                                                """

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
        def dayOftheWeekSecgr(n):
            ponedelnikSecGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\ponedelnikSec.txt", encoding="utf8").read()
            vtornikSecGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\vtornikSec.txt", encoding="utf8").read()
            sredaSecGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\sredaSec.txt", encoding="utf8").read()
            chetvSecGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\chetvSec.txt", encoding="utf8").read()
            pyatnicaSecGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\pyatnicaSec.txt", encoding="utf8").read()
            subbSecGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\subbotaSec.txt", encoding="utf8").read()
            voscrSecGr = open(r"C:\Users\Пользователь\Documents\dev\vscode\git\pystudy\study\schoolbot\voskrSec.txt", encoding="utf8").read()

            """
            ponedelnikSecGr = open(r"C:\Users\Admin\git\py\study\schoolbot\ponedelnikSec.txt", encoding="utf8").read()
            vtornikSecGr = open(r"C:\Users\Admin\git\py\study\schoolbot\vtornikSec.txt", encoding="utf8").read()
            sredaSecGr = open(r"C:\Users\Admin\git\py\study\schoolbot\sredaSec.txt", encoding="utf8").read()
            chetvSecGr = open(r"C:\Users\Admin\git\py\study\schoolbot\chetvSec.txt", encoding="utf8").read()
            pyatnicaSecGr = open(r"C:\Users\Admin\git\py\study\schoolbot\pyatnicaSec.txt", encoding="utf8").read()
            subbSecGr = open(r"C:\Users\Admin\git\py\study\schoolbot\subbotaSec.txt", encoding="utf8").read()
            voscrSecGr = open(r"C:\Users\Admin\git\py\study\schoolbot\voskrSec.txt", encoding="utf8").read()
                                                                                                                        """

            if n == 0:
                return ponedelnikSecGr
            if n == 1:
                return vtornikSecGr
            if n == 2:
                return sredaSecGr
            if n == 3:
                return chetvSecGr
            if n == 4:
                return pyatnicaSecGr
            if n == 5:
                return subbSecGr
            if n == 6:
                return voscrSecGr
        def usable_keyb():
                markup = InlineKeyboardMarkup()
                markup.row_width = 4
                markup.add(InlineKeyboardButton("Физика", callback_data="cb_fiz"),
                           InlineKeyboardButton("Математика", callback_data="cb_matem"),
                           InlineKeyboardButton("Информатика", callback_data="cb_inf"),
                           InlineKeyboardButton("Расписание", callback_data="raspis"))
                return markup


        current_date = date.today()
        denNedSec = dayOftheWeekSecgr(current_date.weekday())
        denNedFirst = dayOftheWeekFirstgr(current_date.weekday())


        @bot.message_handler(commands=['start'])
        def welcome(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, "Привет я помогу тебе с учёбой(нет, ты даун)")
            bot.send_message(chat_id, "Какой предмет тебе нужен, зайка?", reply_markup=usable_keyb())
        
        @bot.message_handler(commands=['help', 'HELP'])
        def help_ms(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, "Привет я помогу тебе с учёбой(нет, ты даун и ваще сам негр чё обзываешься, писать не умеешь)")
            bot.send_message(chat_id, "Какой предмет тебе нужен, зайка?", reply_markup=usable_keyb())

        @bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
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
                elif call.data == "second_group_raspis":
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите какое расписание вы хотите получить:", reply_markup=raspis_secondGroup)
                elif call.data == "first_group_raspis":
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите какое расписание вы хотите получить:", reply_markup=raspis_firstGroup)
                else:
                    if call.data == "today_first":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=denNedFirst, reply_markup=raspis_firstGroup)
                    elif call.data == "tomorrow_first":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(current_date.weekday() + 1), reply_markup=raspis_firstGroup)
                    elif call.data == "choose_ned_first":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите день недели: ", reply_markup=for_ChoosenedFirst)
                    elif call.data == "choose_ned_sec":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите день недели: ", reply_markup=for_ChoosenedSec)
                    elif call.data == "today_sec":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=denNedSec, reply_markup=raspis_secondGroup)
                    elif call.data == "tomorrow_sec":
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(current_date.weekday() + 1), reply_markup=raspis_secondGroup)
                    else:
                        if call.data == "FirstDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(0), reply_markup=raspis_firstGroup)
                        elif call.data == "SecDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(1), reply_markup=raspis_firstGroup)
                        elif call.data == "ThirdDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(2), reply_markup=raspis_firstGroup)
                        elif call.data == "FourDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(3), reply_markup=raspis_firstGroup)
                        elif call.data == "FiveDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(4), reply_markup=raspis_firstGroup)
                        elif call.data == "SixDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(5), reply_markup=raspis_firstGroup)
                        elif call.data == "SevenDay_First":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekFirstgr(6), reply_markup=raspis_firstGroup)
                            
                        elif call.data == "FirstDay_Sec":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(0), reply_markup=raspis_secondGroup)
                        elif call.data == "SecDay_Sec":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(1), reply_markup=raspis_secondGroup)
                        elif call.data == "ThirdDay_Sec":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(2), reply_markup=raspis_secondGroup)
                        elif call.data == "FourDay_Sec":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(3), reply_markup=raspis_secondGroup)
                        elif call.data == "FiveDay_Sec":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(4), reply_markup=raspis_secondGroup)
                        elif call.data == "SixDay_Sec":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(5), reply_markup=raspis_secondGroup)
                        elif call.data == "SevenDay_Sec":
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=dayOftheWeekSecgr(6), reply_markup=raspis_secondGroup)
                    
        @bot.message_handler(func=lambda message: True)
        def mainfunc(message):
            chat_id = message.chat.id   
            mess  = message.text.lower()
            

        bot.polling(none_stop=True)

    except Exception as e:
        print("Error:")
        print(e)
        time.sleep(15)
