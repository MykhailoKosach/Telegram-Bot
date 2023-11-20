import telebot
from telebot import types
import variables

bot = variables.bot


# define the menu buttons
aroma = types.KeyboardButton("/aroma")
aroma.text = "Аромабокс"
fav = types.KeyboardButton("/favourite")
fav.text = "Замовити улюблений парфум"
manager = types.KeyboardButton("Зв’язатися з консультантом")
manager.text = "/manager"
test = types.KeyboardButton("Персональний парфум (тест)")
test.text = "/test"

menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menu.add(aroma, fav, manager, test)

unwoman = types.InlineKeyboardButton("Аромабокс “Unisecs” спокусливий ЖІНОЧИЙ")
unman = types.InlineKeyboardButton("Аромабокс “Unisecs” ЧОЛОВІЧИЙ")
aroma1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
aroma1.row(unwoman)
aroma1.row(unman)

testbut = types.InlineKeyboardButton("Пройти тест")
test1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
test1.add(testbut)
 
woman = types.InlineKeyboardButton("Для жінки")
man = types.InlineKeyboardButton("Для чоловіка")
unisecs = types.InlineKeyboardButton("Унісекс")
sex = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sex.row(woman)
sex.row(man)
sex.row(unisecs)

day = types.InlineKeyboardButton("На кожен день")
night = types.InlineKeyboardButton("Вечірні")
type1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
type1.row(day)
type1.row(night)

seksual = types.InlineKeyboardButton("Сексуальний")
soft = types.InlineKeyboardButton("Ніжний")
norm = types.InlineKeyboardButton("Стриманий")
sport = types.InlineKeyboardButton("Спортивний")
haracter = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
haracter.row(seksual)
haracter.row(soft)
haracter.row(norm)
haracter.row(sport)

cytrus = types.InlineKeyboardButton("Цитрусові")
fruit = types.InlineKeyboardButton("Фруктові")
flower = types.InlineKeyboardButton("Квіткові")
water = types.InlineKeyboardButton("Водяні")
leather = types.InlineKeyboardButton("Шкіряні")
wood = types.InlineKeyboardButton("Дереревні")
spice = types.InlineKeyboardButton("Пряні")
gurman = types.InlineKeyboardButton("Гурманські")
aromat = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
aromat.row(cytrus)
aromat.row(fruit)
aromat.row(flower)
aromat.row(water)
aromat.row(leather)
aromat.row(wood)
aromat.row(spice)
aromat.row(gurman)


# define a handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Here's your menu:", reply_markup=menu)


@bot.message_handler(commands=['aroma'])
def aroma(message):
    bot.send_message(message.chat.id, 'Якщо ви вагаєтесь з виборо парфумів - ось рішення!')
    bot.send_message(message.chat.id,
                     'Якісні аромабокси, які перевірені досвідом! Сформований набір з 4 тестерів ароматів по 5 мл, який найбільше отримав  схвалених відгуків від наших клієнтів!')
    bot.send_message(message.chat.id,
                     'Обери “Найпопулярніші аромати 2022” за  відгуками наших клієнтів. Усі аромабокси за ціною 400грн.',
                     reply_markup=aroma1)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Аромабокс “Unisecs” спокусливий ЖІНОЧИЙ":
        bot.send_message(message.chat.id, "Залишіть свій номер телефону, ПІБ, місто на номер поштового відділення")
    elif message.text == "Аромабокс “Unisecs” ЧОЛОВІЧИЙ":
        bot.send_message(message.chat.id, "Залишіть свій номер телефону, ПІБ, місто на номер поштового відділення")
    else:
        bot.send_message(message.chat.id, "Вибачте, я вас не розумію, оберіть аромабокс", reply_markup=aroma1)
    bot.register_next_step_handler(message, contact_info)


def contact_info(message):
    bot.send_message(message.chat.id, "Дякуємо за замовлення! Перед відправленням - ми з тобою зв’яжемося!",
                     reply_markup=menu)


@bot.message_handler(commands=['favourite'])
def favourite(message):
    bot.send_message(message.chat.id, 'Ось перелік частини парфумів, які є у нас в наявності')
    bot.send_message(message.chat.id,
                     'Напишіть нам, який парфум вас зацікавив або напишіть улюблений аромат, а ми підберемо вам аналог')
    bot.register_next_step_handler(message, contact_info2)


def contact_info2(message):
    bot.send_message(message.chat.id, "Дякуємо за Ваш запит! Наш менеджер зв'яжеться з Вами, для уточнення деталей",
                     reply_markup=menu)


@bot.message_handler(commands=['manager'])
def manager(message):
    bot.send_message(message.chat.id,
                     'Доброго дня! Напишіть повідомлення нашому консультанту і він одразу з вами зв’яжиться, коли буде онлайн')
    bot.register_next_step_handler(message, contact_info3)


def contact_info3(message):
    send_contact = types.KeyboardButton("Залишити", request_contact=True)
    cancel = types.KeyboardButton("Ні, дякую")
    contact_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_btn.add(send_contact, cancel)
    bot.send_message(message.chat.id,
                     "Залиште, будь ласка, Ваш номер телефону, аби менеджер міг безперешкодно з Вами зв'язатися😉",
                     reply_markup=contact_btn)
    bot.register_next_step_handler(message, thanks)


def thanks(message):
    bot.send_message(message.chat.id, 'Дякуюємо за Ваше звернення', reply_markup=menu)


@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id,
                     "Наші парфумерні консультанти  зможуть підібрати парфум, який найкраще підійде саме вам за аналізом тесту.",
                     reply_markup=test1)
    bot.register_next_step_handler(message, test_exe1)


def test_exe1(message):
    if message.text == "Пройти тест":
        bot.send_message(message.chat.id, "Для кого?", reply_markup=sex)
    else:
        bot.send_message(message.chat.id, "Вибачте, я вас не розумію, оберіть аромабокс", reply_markup=test1)
    bot.register_next_step_handler(message, test_exe2)


def test_exe2(message):
    messageresponse = "Який тип парфумів?"
    if message.text == woman or message.text == man or message.text == unisecs:
        bot.send_message(message.chat.id, messageresponse, reply_markup=type1)
    else:
        bot.send_message(message.chat.id, "Вибачте, я вас не розумію, оберіть аромабокс", reply_markup=sex)
    bot.register_next_step_handler(message, test_exe3)

def test_exe3(message):
    if message.text == "На кожен день":
        bot.send_message(message.chat.id, "Характер парфумів?", reply_markup=haracter)
    elif message.text == "Вечірні":
        bot.send_message(message.chat.id, "Характер парфумів?", reply_markup=haracter)
    else:
        bot.send_message(message.chat.id, "Вибачте, я вас не розумію, оберіть аромабокс", reply_markup=type1)
    bot.register_next_step_handler(message, test_exe4)


def test_exe4(message):
    messageresponse = "Парфуми з яким ароматом Вас цікавлять?"
    if message.text == seksual or message.text == soft or message.text == norm or message.text == sport:
        bot.send_message(message.chat.id, messageresponse , reply_markup=aromat)
    else:
        bot.send_message(message.chat.id, "Вибачте, я вас не розумію, оберіть аромабокс", reply_markup=haracter)
    bot.register_next_step_handler(message, test_exe5)


def test_exe5(message):
    messageresponse = "Чудово! Результат вашого тесту проаналізують наші консультанти і зроблять найкращий підбір для Вас."
    if message.text == cytrus or  message.text == fruit or message.text == flower or message.text == water or message.text == leather or message.text == wood or message.text == spice or message.text == gurman:
        bot.send_message(message.chat.id, messageresponse)
    else:
        bot.send_message(message.chat.id, "Вибачте, я вас не розумію, оберіть аромабокс", reply_markup=aromat)
    bot.register_next_step_handler(message, contact_info4)

def contact_info4(message):
    send_contact = types.KeyboardButton("Залишити", request_contact=True)
    cancel = types.KeyboardButton("Ні, дякую")
    contact_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_btn.add(send_contact, cancel)
    bot.send_message(message.chat.id, "Залиште, будь ласка, Ваш номер телефону, аби менеджер міг безперешкодно з Вами зв'язатися😉", reply_markup=contact_btn)
    bot.register_next_step_handler(message, end)


def end(message):
    bot.send_message(message.chat.id, 'Дякуюємо за Ваше звернення', reply_markup=menu)
    start


bot.polling(none_stop=True)
