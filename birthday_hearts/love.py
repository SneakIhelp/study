import time
from telethon.errors import SessionPasswordNeededError
import math
import asyncio
from turtle import *
from telethon import *

api_id = 6956069
api_hash = 'e846851c160ab65697bb39404f40ae1c'
phone = '89686332011'
username = 'itnorks'

async def send_message_to_telegram():
    async with TelegramClient('birthday_release', api_id, api_hash) as client:
        if not client.is_user_authorized(): 
            client.send_code_request(phone)
            try:
                client.sign_in(phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                client.sign_in(password=input('Password: '))

        await client.start()
        for i in range(100):
            await client.send_message("go_to_the_nafig_pls", message="я тебя очень очень сильно люблю!")


asyncio.run(send_message_to_telegram())

time.sleep(5)

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
    pen.write("Ты зайка!!", font=font)

pen.ht()
draw_sr_heart()
text()
time.sleep(10)
clearscreen()
draw_heart()
done()

