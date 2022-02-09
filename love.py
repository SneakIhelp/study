import time
import asyncio
from turtle import *
from telethon import *

pen = Turtle()
pen.color('red')
bgcolor('black')


def curve(cc, coo):
    for i in range(200):
        pen.right(cc)
        pen.forward(cc)
        


def draw_biggest_heart():
    сс = 1
    coo = 200
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve(сс, coo)
    pen.left(120)
    curve(сс, coo)
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


async def send_message_to_telegram():
    api_id = 6956069
    api_hash = 'e846851c160ab65697bb39404f40ae1c'

    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    await client.send_message("@gorkaork", message="4")



asyncio.run(send_message_to_telegram())
pen.ht()
draw_biggest_heart()
text()
done()