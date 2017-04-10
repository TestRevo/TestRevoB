# -*- coding: utf-8 -*-
import telebot
from telebot import types

TOKEN = '345710019:AAGWNUd01WBfGNXnk9lM0yB-sbQTNjaUGCc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)
hide = types.ReplyKeyboardRemove()
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Готов']])
    hello = bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть. Ты готов?(Воспользуйтесь кнопкой внизу экрана)'.format(name=message.text),reply_markup=keyboard)
    bot.register_next_step_handler(hello,name)
def name(message):
    if message.text == 'Готов':
        bot.send_message(message.chat.id,""" 1.	В какой момент необходимо предложить клиенту "Услугу оплаты частями"?(Ответ вводить цифрой, без пробелов. Если ответов несколько, то через запятую и без пробелов, последовательно. Пример: 1,2)
            Ответы:
        1. Когда клиент вошел(-ла) в магазин
	2. Когда клиент выбирает(-ла) товар в торговом зале
	3. Когда клиент стоит в очереди на кассу
	4. После того, как клиент оплатил товар на кассе
	5. Только если клиент сам подойдет и спросит про услугу"""
, parse_mode='Markdown', reply_markup=hide)


@bot.message_handler(content_types=["text"])       
def default_test(message):
    if message.text == '1':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text="Следующий шаг.", callback_data='Следующий шаг.')])
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем", reply_markup=keyboard)
    if message.text == '2':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,3':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2,3':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2,3,4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2,3,4,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard) 
    if message.text == '1,2,3,4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3,4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3,4,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3,4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,4,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
        
@bot.callback_query_handler(func=lambda l: True)
def kek(l):
    if l.message:
        if l.data == "Следующий шаг.":
            bot.edit_message_text(chat_id=l.message.chat.id, message_id=l.message.message_id, text='''2.	Где необходимо предлагать активно услугу "Услугу оплаты частями"?
            Ответы:
        1.	Во входной зоне магазина
	2.	В зале, отделы: игрушки, коляски, одежда 
	3.	В зоне касс
''')
@bot.message_handler(content_types=["text"])       
def kek(m):
    if m.text == '1':
        keyb = types.InlineKeyboardMarkup()
        keyb.add(*[types.InlineKeyboardButton(text="Следующий шаг..", callback_data='Следующий шаг..')])
        bot.send_message(m.chat.id, "Ответ принят! Продолжаем", reply_markup=keyb)
    if message.text == '2':
        keyboard = types.InlineKeyboardMarkup()
        apple = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(apple)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3':
        keyboard = types.InlineKeyboardMarkup()
        apple = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(apple)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2':
        keyboard = types.InlineKeyboardMarkup()
        apple = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(apple)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,3':
        keyboard = types.InlineKeyboardMarkup()
        apple = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(apple)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3':
        keyboard = types.InlineKeyboardMarkup()
        apple = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(apple)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2,3':
        keyboard = types.InlineKeyboardMarkup()
        apple = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(apple)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda i: True)
def inline(i):
    if i.message:
        if i.data == "Следующий шаг.":
            bot.edit_message_text(chat_id=i.message.chat.id, message_id=i.message.message_id, text='''3.	Что необходимо иметь клиенту, чтобы оформить "Услугу оплаты частями"?
            Ответы:
        1. Телефон 
	2. Паспорт 
	3. Ксерокопия паспорта
	4. Справка о доходах 
	5. Водительские права
	6. СНИЛС
''')
    elif i.inline_message_id:
        if i.data == "Следующий шаг..":
            bot.edit_message_text(inline_message_id=i.inline_message_id, text="Бдыщь")
    if message.text == '1':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг...", callback_data='Следующий вопрос1')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '5':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '6':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,3':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,4':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,5':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,6':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,4':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,5':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,6':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,4':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,5':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,6':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4,5':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4,6':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '5,6':
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2,3':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2,3,4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '1,2,3,4,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard) 
    if message.text == '1,2,3,4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3,4':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3,4,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '2,3,4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,4,5':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '3,4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)
    if message.text == '4,5,6':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Следующий шаг", callback_data='Следующий шаг')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Ответ принят! Продолжаем!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda p: True)
def callback(p):
    # Если сообщение из чата с ботом
    if p.message:
        if p.data == "Следующий шаг...":
            bot.edit_message_text(chat_id=p.message.chat.id, message_id=p.message.message_id, text='''1.	Сколько нужно заплатить клиенту сейчас, в качестве обязательного первоначального взноса?
            Ответы:
        1. Нисколько
	2. 20% от цены товара
	3. Любую сумму, но не менее 30% от стоимости
	

''')
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
