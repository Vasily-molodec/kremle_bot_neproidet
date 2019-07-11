import telebot
import time
from telebot import types


bot = telebot.TeleBot('759513597:AAEaq63U1g8oL1spLgN-OiEhAWfp7Hfk3Mw')
firstnum = 0
secondnum = 0
point = ''


def Plus (x, y):
    print (x + y)
def Multiply (x, y):
    print (x * y)
def Divide (x, y):
    print (x / y)
def minus (x, y):
    print (x - y)
def square (x):
    y = x * x
    print (y)

@bot.message_handler(content_types = ['text'])
def start(message):
    if (message.text == '/start'):
        bot.send_message(message.from_user.id, "Добро пожаловать, напиши пожалуйса первое число")
        bot.send_sticker(message.from_user.id, "CAADAgADHQEAAk6bZAJ6H3tM82FMtgI")
        bot.register_next_step_handler(message, get_firstnum)

    elif(message.text == 'Привет'):
        bot.send_message(message.from_user.id,  "Напиши /help")
    elif(message.text == "/help"):
        bot.send_message(message.from_user.id, "У меня, есть функции калькулятора, напиши /start")


    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")

def get_firstnum (message):
    global firstnum
    try:
        firstnum = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, "Ты ввел неверное число, попробуй еще раз")
        bot.register_next_step_handler(message, get_firstnum)
        time.sleep(10)
    mark1 = types.ReplyKeyboardMarkup(one_time_keyboard = True, row_width=2)
    plus_button = types.KeyboardButton(text = '+')
    minus_button = types.KeyboardButton(text = '-')
    multiply_button = types.KeyboardButton(text = '×')
    division_button = types.KeyboardButton(text = '÷')
    mark1.add(plus_button, minus_button, multiply_button, division_button)
    bot.send_message(message.from_user.id, "Здорово, теперь введите знак", reply_markup= mark1)


    bot.register_next_step_handler(message, get_point)


def get_point (message):
    global point
    point = message.text
    bot.send_message(message.from_user.id, "Хорошая работа, теперь введи вторую цифру")
    bot.register_next_step_handler(message, get_secondnum)


def get_secondnum (message):
    global secondnum
    global result
    try:
        secondnum = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, "Ты ввел неверное число, попробуй еще раз, написав /start")
        bot.register_next_step_handler(message, get_secondnum)
        time.sleep(10)

    if point == '÷':
        try:
            result = firstnum / secondnum
        except Exception:
            bot.send_message(message.from_user.id, "НА НОЛЬ ДЕЛИТЬ НИЛЬЗЯ!!!!")
            bot.send_sticker(message.from_user.id,"CAADAgADVQEAAs3ASBjsN6GRMJd02AI")
    elif (point == "+"):
        result = secondnum + firstnum
    elif (point == "-"):
        result = firstnum - secondnum
    elif (point == "×"):
        result = secondnum * firstnum
    else:
        bot.send_message(message.from_user.id, "Неверный формат для знака, просьба начать заново. Напишите /start")
    final_result = "Первое число: " + str(firstnum) + "\nВторое число: " + str(secondnum) + "\nЗнак: " + point + "\nРезультат: " + str(result)
    bot.send_message(message.from_user.id, final_result)
    mark = types.InlineKeyboardMarkup()
    button_site = types.InlineKeyboardButton(text = 'Таблица Умножения',  url = 'https://ru.wikipedia.org/wiki/Таблица_умножения')
    mark.add(button_site)
    button_site2 = types.InlineKeyboardButton(text = 'Сайт для рещения ЕГЭ', url = 'https://ege.sdamgia.ru')
    mark.add(button_site2)
    button_site3 = types.InlineKeyboardButton(text = 'Наш Инстаграм', url = 'https://www.instagram.com/mr_bot_dvadvavosem/?hl=ru')
    mark.add(button_site3)
    bot.send_message(message.from_user.id, "Получай полезные ресурсы по учебе", reply_markup = mark)
    time.sleep(4)
    bot.send_message(message.from_user.id, "Я тебя по ip вычислил")
    bot.send_sticker(message.from_user.id,"CAADAgADeQEAAs3ASBjwjZqBnpJdPAI")
    time.sleep(3)
    bot.send_message(message.from_user.id, "шутка)")
    bot.send_sticker(message.from_user.id,"CAADAgADnwEAAs3ASBghVd0_ekaiTAI")
    time.sleep(2)
    bot.send_message(message.from_user.id, "Всегда рад помочь, лишь напишите /start")


bot.polling (none_stop = True, interval = 0)
