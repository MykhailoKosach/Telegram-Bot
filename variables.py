import telebot
from telebot import types


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