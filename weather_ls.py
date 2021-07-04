import telethon
from pyowm.owm import OWM
import asyncio

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
t4 = (t3 + t2) / 2

genius = 'В городе ' + str(place) + ' температура ' + str(round(t)) + ' °C, ощущается как ' + str(round(t1)) + '°C, ' \
         'максимальная тепература ' + str(
    round(t2)) + \
         ' °C, минимальная температура ' + str(round(t3)) + ' °C, средняя тепература за день ' + \
         str(round(t4)) + ' °C '
try:
    monitoring = owm.weather_manager().weather_at_place(place)
    weather = monitoring.weather
    status = weather.detailed_status
    helpme = 'It is ' + str(status) + ' in ' + str(place) + ' now. '
except:
    pass

api_id = 6956069
api_hash = 'e846851c160ab65697bb39404f40ae1c'


async def main():
    async with telethon.TelegramClient('session_name', api_id, api_hash) as client:
        await client.send_message('me', helpme)
        await client.send_message('me', genius)

        await client.run_until_disconnected()


asyncio.run(main())
