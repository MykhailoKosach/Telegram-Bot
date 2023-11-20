import telebot
from telebot import types
import variables
import key

bot = key.bot
var = variables

aroma = types.KeyboardButton("/aroma")
aroma.text = "Аромабокс"
fav = types.KeyboardButton("/favourite")
fav.text = "Замовити улюблений парфум"
manager = types.KeyboardButton("Зв’язатися з консультантом")
manager.text = "/manager"
test = types.KeyboardButton("Персональний парфум (тест)")
test.text = "/test"


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Here's your menu:", reply_markup=variables.menu)

@bot.message_handler(commands=['aroma'])
def aroma(message):
    bot.send_message(message.chat.id, 'Якщо ви вагаєтесь з виборо парфумів - ось рішення!')
    bot.send_message(message.chat.id,
                     'Якісні аромабокси, які перевірені досвідом! Сформований набір з 4 тестерів ароматів по 5 мл, який найбільше отримав  схвалених відгуків від наших клієнтів!')
    bot.send_message(message.chat.id,
                     'Обери “Найпопулярніші аромати 2022” за  відгуками наших клієнтів. Усі аромабокси за ціною 400грн.',
                     reply_markup=var.aroma1)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Аромабокс “Unisecs” спокусливий ЖІНОЧИЙ":
        bot.send_message(message.chat.id, "Залишіть свій номер телефону, ПІБ, місто на номер поштового відділення")
    elif message.text == "Аромабокс “Unisecs” ЧОЛОВІЧИЙ":
        bot.send_message(message.chat.id, "Залишіть свій номер телефону, ПІБ, місто на номер поштового відділення")
    else:
        bot.send_message(message.chat.id, "Вибачте, я вас не розумію, оберіть аромабокс", reply_markup=var.aroma1)
        bot.register_next_step_handler(message, contact_info)

def contact_info(message):
    bot.send_message(message.chat.id, "Дякуємо за замовлення! Перед відправленням - ми з тобою зв’яжемося!",
                     reply_markup=var.menu)