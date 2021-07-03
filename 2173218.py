from pyowm import OWM

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
