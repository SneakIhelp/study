import telethon
import random
import time

api_id = 6956069
api_hash = 'e846851c160ab65697bb39404f40ae1c'
fraze = ['hi', 'hola', 'привет', 'Ēalā', 'Ola', 'Shlomo', 'Werte', 'Héébee', 'Seavus', 'Вітаю', 'säläm',
         'Здравейте', 'Dobar dan', 'Salud', 'Bonjour', 'Mandi', 'Ahoj', 'ʔédlánet’é']

client = telethon.TelegramClient('session_name', api_id, api_hash)
client.start()

for i in range(1000):
    client.send_message('username', random.choice(fraze))
    # time.sleep(0.3)
