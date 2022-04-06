import time
import math
import asyncio
from turtle import *
from telethon import *

pen = Turtle()
pen.speed(200)
pen.color('red')
bgcolor('black')


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def draw_sr_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()


def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * \
        math.cos(2 * t) - 2 * \
        math.cos(3 * t) - \
        math.cos(4 * t)

def draw_heart():
    t = Turtle()
    t.speed(5000)
    colormode(255)
    Screen().bgcolor(0, 0, 0)
    for i in range(510):
        t.goto((xt(i) * 20, yt(i) * 20))
        t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
        t.goto(0, 0)
    
    update()
    mainloop()


font = ("Monteserrat", 16, "bold")


def text():
    pen.up()
    pen.setpos(-52, 90)
    pen.down()
    pen.color('black')
    pen.write("Ты котик!!", font=font)


async def send_message_to_telegram():
    api_id = 6956069
    api_hash = 'e846851c160ab65697bb39404f40ae1c'

    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    for i in range(200):
        await client.send_message("me", message="я тебя очень очень сильно люблю!")



pen.ht()
draw_sr_heart()
text()
time.sleep(10)
clearscreen()
draw_heart()
done()

asyncio.run(send_message_to_telegram())