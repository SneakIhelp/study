import telethon
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import asyncio


config_dict = get_default_config()
config_dict['language'] = 'ru'

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

genius = f'Сейчас в городе {str(place)} температура {str(t)} °C, ощущается как {str(t1)} °C, ' \
         f'максимальная температура {str(t2)} °C, минимальная температура {str(t3)} °C, средняя температура ' \
         f'сегодня {str(t4)} °C '

monitoring = owm.weather_manager().weather_at_place(place)
weather = monitoring.weather
status = weather.detailed_status
helpme = f'Сейчас в городе {str(place)} {str(status)}.'


api_id = 6956069
api_hash = 'e846851c160ab65697bb39404f40ae1c'


async def main():
    async with telethon.TelegramClient('session_name', api_id, api_hash) as client:
        await client.send_message('me', helpme)
        await client.send_message('me', genius)

        await client.run_until_disconnected()


asyncio.run(main())
