from telethon import TelegramClient, events, sync
import random

api_id = 6956069
api_hash = 'e846851c160ab65697bb39404f40ae1c'
message_list = ['привет', 'я написал классный код', 'урааааааааааааа', 'урааааааааааааа', 'урааааааааааааа',
                'урааааааааааааа', 'урааааааааааааа']

client = TelegramClient('telegrmsht', api_id, api_hash)
client.start()

print(client.get_me().stringify())
for i in range(1000):
    client.send_message('userhuyser1', random.choice(message_list))
