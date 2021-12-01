import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button = types.KeyboardButton('Тест по ВВАБИМ')
	markup.add(button)

	bot.send_message(message.chat.id, 'Привет, {0.first_name}! Приготовься пройти тест по лучшей диспиплине на нашей кафедре.'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private' and message.text == 'Тест по ВВАБИМ':
	    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	    prepod1 = types.KeyboardButton('Елена Вайц')
	    prepod2 = types.KeyboardButton('Варвара Александровна')
	    prepod3 = types.KeyboardButton('Вероника Михайловна')
	    markup.add(prepod1, prepod2, prepod3)
	    bot.send_message(message.chat.id, 'Давай начнем с простого, как зовут преподавателя по ВВАБИМ?'.format(message.from_user), reply_markup=markup)
	elif message.text == 'Елена Вайц' or message.text == 'Варвара Александровна':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.chat.id, 'Попробуй ещё раз, а вообще стыдно не знать!'.format(message.from_user), reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Вероника Михайловна':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		prepod1 = types.KeyboardButton('Вопрос №1')
		markup.add(prepod1)
		bot.send_message(message.chat.id, 'Молодец, верно!'.format(message.from_user), reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Вопрос №1':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('Делаем, как в методичке с турбиной')
		var2 = types.KeyboardButton('Берем свои данные')
		markup.add(var1, var2)
		bot.send_message(message.chat.id,'Какие данные берем для 1-ой лабы?'.format(message.from_user),reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Делаем, как в методичке с турбиной':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.chat.id, 'А если подумать?'.format(message.from_user),reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Берем свои данные':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('Вопрос №2')
		markup.add(var1)
		bot.send_message(message.chat.id, 'А в тебе есть потенциал!'.format(message.from_user),reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Вопрос №2':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		prepod1 = types.KeyboardButton('1')
		prepod2 = types.KeyboardButton('2')
		prepod3 = types.KeyboardButton('3')
		markup.add(prepod1, prepod2, prepod3)
		img = open('foto/foto1.jpg', 'rb')
		bot.send_photo(message.chat.id, img)
		bot.send_message(message.chat.id,'Что означает зеленая точка на фото? \n1: Точка остановки обучения \n2: Точка окончания работы \n3: Точка переобучения'.format(message.from_user),reply_markup=markup)
	elif message.chat.type == 'private' and message.text == '1':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		prepod1 = types.KeyboardButton('Вопрос №3')
		markup.add(prepod1)
		bot.send_message(message.chat.id, 'Неплохо, идем дальше.'.format(message.from_user), reply_markup=markup)
	elif message.text == '2' or message.text == '3':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.chat.id, 'Методичку читал вообще?! Пробуй еще раз.'.format(message.from_user), reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Вопрос №3':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('10')
		var2 = types.KeyboardButton('100')
		var3 = types.KeyboardButton('50')
		markup.add(var1, var2,var3)
		bot.send_message(message.chat.id, 'Сколько раз мы обучаем каждый символ для распознавания номеро машин?'.format(message.from_user),reply_markup=markup)
	elif message.text == '10' or message.text == '50':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.chat.id, 'Вообще можно в папку зайти и не гадать на кофейной гуще. Ладно, давай помогу:'.format(message.from_user), reply_markup=markup)
		img = open('foto/foto2.png', 'rb')
		bot.send_photo(message.chat.id, img)
	elif message.text == '100':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('Вопрос №4')
		markup.add(var1)
		bot.send_message(message.chat.id, 'Ну ведь можешь же, когда хочешь...'.format(message.from_user), reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Вопрос №4':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('а)')
		var2 = types.KeyboardButton('б)')
		var3 = types.KeyboardButton('в)')
		markup.add(var1, var2, var3)
		bot.send_message(message.chat.id, 'Чем 4-ая лаба принципиально отличается от предыдущих? \nа): Данные берутся с другого сайта \nб): Нейронную сеть обучаем сами \nв): Используется более сложная нейронная сеть'.format(message.from_user),reply_markup=markup)
	elif message.text == 'а)' or message.text == 'в)':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.chat.id,'А ты думал легко будет? Думай.'.format(message.from_user), reply_markup=markup)
	elif message.text == 'б)':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('Вопрос №5')
		markup.add(var1)
		bot.send_message(message.chat.id, 'Отлично, у тебя есть все шансы закрыть зачет досрочно!'.format(message.from_user),reply_markup=markup)
	elif message.chat.type == 'private' and message.text == 'Вопрос №5':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('а')
		var2 = types.KeyboardButton('б')
		markup.add(var1, var2)
		bot.send_message(message.chat.id,'Что позволяет делать метод k-средних? \nа: Позволяет визуализировать классы \nб: Позволяет характеризовать кластеры по значениям их центров'.format(message.from_user),reply_markup=markup)
	elif message.text == 'а':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		bot.send_message(message.chat.id, 'Несовсем'.format(message.from_user),reply_markup=markup)
	elif message.text == 'б':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		var1 = types.KeyboardButton('Победа')
		markup.add(var1)
		bot.send_message(message.chat.id,'Поздравляю, можешь смело идти сдавать ВВАБИМ, да пребудет с тобой шоколадка для Вероники Михайловны!'.format(message.from_user),reply_markup=markup)
	else:
		bot.send_message(message.chat.id, 'У меня лапки,мяу)')

bot.polling(none_stop=True)