import random


print('Hello! What is your mood today? // Happy (H) or Not very good (NG) or I can not say exactly (ICSE)')
answ = input()
if answ == 'H':
    print('Теперь будем на русском :) Ты хочешь сделать что-то полезное? (y or n)')
    utility = input()
    if utility == 'n':
        print('Выбери: раковина, батарея, стул, барная стойка, зарядка')
        ran = input()
        if ran == 'раковина' or 'батарея' or 'стул' or 'барная стойка' or 'зарядка':
            fraze = ['Какой рисунок сделать для предмета "', 'В каком магазине лучше купить товар "']
            print(random.choice(fraze) + ran + '"?')
        else:
            print('Что-то пошло не так')
    elif utility == 'y':
        print('Выбери:')
        polez = input()
        if polez == '':
            fraze = ['']
            print(random.choice(fraze) + polez + '"?')
        else:
            print('Что-то пошло не так')

elif answ == 'NG':
    print('Оу, прости, что на русском! Надеюсь всё наладится. Тогда давай сделаем что-то весёлое!')
    print('Что самое весёлое приходит тебе в голову?')
    smth_happy = input()
    print((smth_happy + " ") * 30)

else:
    print("Что-то пошло не так!")
