import telethon
from pyowm.owm import OWM
import datetime

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

print(f'В городе {place} температура {t} °C, ощущается как {t1} °C, максимальная тепература {t2} °C, минимальная '
      f'температура {t3} °C, средняя тепература за день {(t3 + t2) / 2} °C')

try:
    monitoring = owm.weather_manager().weather_at_place(place)
    weather = monitoring.weather
    status = weather.detailed_status
    # print(f'It is {status} in {place} now.')
    helpme = 'It is', status, 'in', place, 'now.'
    print(*helpme)
except:
    pass

api_id = 6956069
api_hash = 'e846851c160ab65697bb39404f40ae1c'

client = telethon.TelegramClient('session_name', api_id, api_hash)
client.start()
client.send_message('username', *helpme)
