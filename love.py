import time
from turtle import *
import telethon

pen = Turtle()
pen.color('red')
bgcolor('black')


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()


font = ("Monteserrat", 16, "bold")


def text():
    pen.up()
    pen.setpos(-72, 90)
    pen.down()
    pen.color('black')
    pen.write("Я люблю тебя!", font=font)
    pen.up()
    pen.setpos(-63, 70)
    pen.down()
    time.sleep(1)
    pen.write("И хочу спать", font=font)


def send_message_to_telegram():
    api_id = 6956069
    api_hash = 'e846851c160ab65697bb39404f40ae1c'

    client = telethon.TelegramClient('session_name', api_id, api_hash)
    client.start()

    


pen.ht()
draw_heart()
text()
send_message_to_telegram()
done()
