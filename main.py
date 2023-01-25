import random
import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup as b

API_KEY = '5712049694:AAFxxGC9nvwry0Ov4mGWjfIsb3ZDoLQ5uZU'
bot = telebot.TeleBot(API_KEY)
test_current = []


def parser(pages, url):
    global test_current
    if pages is not None and url is not None:
        random_page = random.randint(1, pages)
        url_new = (url + str(random_page))
        print(random_page)
        r = requests.get(url_new)  # код страницы
        soup = b(r.text, 'html.parser')
        # --- Вопросы ---
        tests = soup.find_all('div', class_='text-justify')
        random_int = random.randint(1, len(tests) - 1)
        test1 = tests[random_int].text
        # Номер вопроса
        numbers_of_questions = soup.find_all('div', class_='text-left font-bold')
        numbers_of_questions_clear = [c.text for c in numbers_of_questions]
        number_of_question = numbers_of_questions_clear[random_int]
        # --- Ответы ---
        question_blocks = soup.find_all('div', class_='bg-white mt-1 p-1 md:mt-5 md:p-5')
        question = question_blocks[random_int]
        answer_sections = question.find_all('div', class_='flex-grow')
        answer_sections_clear = [c.text for c in answer_sections]
        test_current = [number_of_question, test1, answer_sections_clear[0], answer_sections_clear[1], answer_sections_clear[2], answer_sections_clear[3], answer_sections_clear[4]]


KROK_current = 0
year_current = ''
program_current = ''
url_current = ''
pages_current = ''
TEST = []
test = parser(1,
              'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/165-normalna-fiziologiya-baza-testiv-2014-roku/base?page=')
button1_ = '📝 Обрати КРОК'
button2_ = '❔ Рандомне тестування'
button3_ = '❔ Рандомні тести з відповідями'
button4_ = '💳 На каву'
button5_ = 'Вчити тести'
button6_ = 'Пройти тестування'
button7_ = '🚪 Головне меню'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(button1_)
    item4 = types.KeyboardButton(button4_)
    markup.add(item1, item4)
    bot.send_message(message.chat.id, 'Розроблено: @pozeetron. Джерело інформації: тестування.укр')
    bot.send_message(message.chat.id,
                     'Вітаю, {0.first_name}! Цей бот створений для крок-тестування.\nОберіть, будь-ласка, спосіб тестування.'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def number(message):
    if message.chat.type == 'private':
        global url_current
        global pages_current
        global KROK_current
        global program_current
        global year_current
        global test
        global test_current
        if message.text == 'Повернутись' or message.text == button7_:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton(button1_)
            item4 = types.KeyboardButton(button4_)
            markup.add(item1, item4)
            bot.send_message(message.chat.id, 'Розроблено: @pozeetron. Джерело інформації: тестування.укр')
            bot.send_message(message.chat.id,
                             'Вітаю, {0.first_name}! Цей бот створений для крок-тестування.\nОберіть, будь-ласка, спосіб тестування.'.format(
                                 message.from_user), reply_markup=markup)
        if message.text == '💳 На каву':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Повернутись')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Монобанк: 4441114451716482\nПриватбанк: 4149439020752592',
                             reply_markup=markup)
        if message.text == button1_:  # Обрати крок
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('КРОК 1')
            item2 = types.KeyboardButton('КРОК 2')
            item3 = types.KeyboardButton('КРОК 3')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Оберіть КРОК', reply_markup=markup)
        if message.text == 'КРОК 1':
            KROK_current = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('2014')
            item2 = types.KeyboardButton('2013')
            item3 = types.KeyboardButton('2012')
            item4 = types.KeyboardButton('2011')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Оберіть рік', reply_markup=markup)
        if message.text == 'КРОК 2':
            KROK_current = 2
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('2005-2018')
            item2 = types.KeyboardButton('2014')
            item3 = types.KeyboardButton('2012')
            item4 = types.KeyboardButton('2011')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Оберіть рік', reply_markup=markup)
        if message.text == 'КРОК 3':
            KROK_current = 3
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('2009-2015')
            item2 = types.KeyboardButton('2014')
            item3 = types.KeyboardButton('2013')
            item4 = types.KeyboardButton('2012')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Оберіть рік', reply_markup=markup)
        if message.text == '2014':
            if KROK_current == 1:
                year_current = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Фармакологія')
                item2 = types.KeyboardButton('Патологічна фізіологія')
                item3 = types.KeyboardButton('Патологічна анатомія')
                item4 = types.KeyboardButton('Нормальна фізіологія')
                item5 = types.KeyboardButton('Нормальна анатомія')
                item6 = types.KeyboardButton('Мікробіологія')
                item7 = types.KeyboardButton('Гістологія')
                item8 = types.KeyboardButton('Біохімія')
                item9 = types.KeyboardButton('Біологія')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
            if KROK_current == 2:
                year_current = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Хірургічний профіль Доповнення')
                item2 = types.KeyboardButton('Хірургічний профіль')
                item3 = types.KeyboardButton('Терапевтичний профіль Доповнення')
                item4 = types.KeyboardButton('Терапевтичний профіль')
                item5 = types.KeyboardButton('Педіатричний профіль Доповнення')
                item6 = types.KeyboardButton('Педіатричний профіль')
                item7 = types.KeyboardButton('Гігієна, ООЗ Доповнення')
                item8 = types.KeyboardButton('Гігієна, ООЗ')
                item9 = types.KeyboardButton('Акушерство і гінекологія Доповнення')
                item10 = types.KeyboardButton('Акушерство і гінекологія')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
            if KROK_current == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Хірургічний профіль - осінь')
                item2 = types.KeyboardButton('Хірургічний профіль - весна')
                item3 = types.KeyboardButton('Терапевтичний профіль - осінь')
                item4 = types.KeyboardButton('Терапевтичний профіль - весна')
                item5 = types.KeyboardButton('Педіатричний профіль - осінь')
                item6 = types.KeyboardButton('Педіатричний профіль - весна')
                item7 = types.KeyboardButton('Акушерство та гінекологія - осінь')
                item8 = types.KeyboardButton('Акушерство та гінекологія - весна')
                item9 = types.KeyboardButton('Інфекційний профіль - осінь')
                item10 = types.KeyboardButton('Інфекційний профіль - весна')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
        if message.text == '2013':
            if KROK_current == 1:
                year_current = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Фармакологія')
                item2 = types.KeyboardButton('Патологічна фізіологія')
                item3 = types.KeyboardButton('Патологічна анатомія')
                item4 = types.KeyboardButton('Нормальна фізіологія')
                item5 = types.KeyboardButton('Нормальна анатомія')
                item6 = types.KeyboardButton('Мікробіологія')
                item7 = types.KeyboardButton('Гістологія')
                item8 = types.KeyboardButton('Біохімія')
                item9 = types.KeyboardButton('Біологія')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
            if KROK_current == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Хірургічний профіль')
                item2 = types.KeyboardButton('Терапевтичний профіль')
                item3 = types.KeyboardButton('Педіатричний профіль')
                item4 = types.KeyboardButton('Акушерство та гінекологія')
                item5 = types.KeyboardButton('Інфекційний профіль')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
        if message.text == '2012':
            if KROK_current == 1:
                year_current = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Фармакологія')
                item2 = types.KeyboardButton('Патологічна фізіологія')
                item3 = types.KeyboardButton('Патологічна анатомія')
                item4 = types.KeyboardButton('Нормальна фізіологія')
                item5 = types.KeyboardButton('Нормальна анатомія')
                item6 = types.KeyboardButton('Мікробіологія')
                item7 = types.KeyboardButton('Гістологія')
                item8 = types.KeyboardButton('Біохімія')
                item9 = types.KeyboardButton('Біологія')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
            if KROK_current == 2:
                year_current = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Хірургічний профіль')
                item2 = types.KeyboardButton('Терапевтичний профіль')
                item3 = types.KeyboardButton('Педіатричний профіль')
                item4 = types.KeyboardButton('Гігієна та ООЗ')
                item5 = types.KeyboardButton('Акушерство та гінекологія')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
            if KROK_current == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Хірургічний профіль')
                item2 = types.KeyboardButton('Терапевтичний профіль')
                item3 = types.KeyboardButton('Педіатричний профіль')
                item4 = types.KeyboardButton('Акушерство та гінекологія')
                item5 = types.KeyboardButton('Інфекційний профіль')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
        if message.text == '2011':
            if KROK_current == 1:
                year_current = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Фармакологія')
                item2 = types.KeyboardButton('Патологічна фізіологія')
                item3 = types.KeyboardButton('Патологічна анатомія')
                item4 = types.KeyboardButton('Нормальна фізіологія')
                item5 = types.KeyboardButton('Нормальна анатомія')
                item6 = types.KeyboardButton('Мікробіологія')
                item7 = types.KeyboardButton('Гістологія')
                item8 = types.KeyboardButton('Біохімія')
                item9 = types.KeyboardButton('Біологія')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
            if KROK_current == 2:
                year_current = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Хірургічний профіль')
                item2 = types.KeyboardButton('Терапевтичний профіль')
                item3 = types.KeyboardButton('Педіатричний профіль')
                item4 = types.KeyboardButton('Гігієна, ООЗ')
                item5 = types.KeyboardButton('Акушерство та гінекологія')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Оберіть профіль', reply_markup=markup)
        if message.text == '2005-2018' or message.text == '2009-2015' or message.text == 'Фармакологія' or message.text == 'Патологічна фізіологія' or message.text == 'Патологічна анатомія' or message.text == 'Нормальна фізіологія' or message.text == 'Нормальна анатомія' or message.text == 'Мікробіологія' or message.text == 'Гістологія' or message.text == 'Біохімія' or message.text == 'Біологія' or message.text == 'Хірургічний профіль Доповнення' or message.text == 'Хірургічний профіль' or message.text == 'Терапевтичний профіль Доповнення' or message.text == 'Терапевтичний профіль' or message.text == 'Педіатричний профіль Доповнення' or message.text == 'Педіатричний профіль' or message.text == 'Гігієна, ООЗ Доповнення' or message.text == 'Гігієна, ООЗ' or message.text == 'Акушерство і гінекологія Доповнення' or message.text == 'Акушерство і гінекологія' or message.text == 'Гігієна та ООЗ' or message.text == 'Хірургічний профіль - осінь' or message.text == 'Хірургічний профіль - весна' or message.text == 'Терапевтичний профіль - осінь' or message.text == 'Терапевтичний профіль - весна' or message.text == 'Педіатричний профіль - осінь' or message.text == 'Педіатричний профіль - весна' or message.text == 'Акушерство та гінекологія - осінь' or message.text == 'Акушерство та гінекологія - весна' or message.text == 'Інфекційний профіль - осінь' or message.text == 'Акушерство та гінекологія - весна' or message.text == 'Інфекційний профіль - осінь' or message.text == 'Інфекційний профіль - весна':
            program_current = message.text
            if KROK_current == 1:
                if year_current == '2014':
                    if program_current == 'Фармакологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/163-farmakologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/166-patologicna-fiziologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/167-patologicna-anatomiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/165-normalna-fiziologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/164-normalna-anatomiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/162-mikrobiologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(2,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/161-gistologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/160-bioximiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/159-biologiya-baza-testiv-2014-roku/base?page=')
                if year_current == '2013':
                    if program_current == 'Фармакологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/172-farmakologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/169-patologicna-fiziologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/168-patologicna-anatomiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/170-normalna-fiziologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/171-normalna-anatomiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/175-mikrobiologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(2,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/174-gistologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/173-bioximiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/85-biologiya-baza-testiv-2013-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Фармакологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/158-farmakologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/157-patologicna-fiziologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/156-patologicna-anatomiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/155-normalna-fiziologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/154-normalna-anatomiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/153-mikrobiologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/152-gistologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/151-bioximiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/150-biologiya-baza-testiv-2012-roku/base?page=')
                if year_current == '2011':
                    if program_current == 'Фармакологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/149-farmakologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/148-patologicna-fiziologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/147-patologicna-anatomiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/146-normalna-fiziologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/145-normalna-anatomiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/144-mikrobiologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/143-gistologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/142-bioximiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/141-biologiya-baza-testiv-2011-roku/base?page=')
            if KROK_current == 2:
                if year_current == '2005-2018':
                    parser(49,
                           'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/809-bukleti-2005-2018-bez-povtoren-zapitan-baza-testiv/base?page=')
                if year_current == '2014':
                    if program_current == 'Хірургічний профіль Доповнення':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/329-xirurgicnii-profil-dopovnennya-baza-testiv-2014-ro/base?page=')
                    if program_current == 'Хірургічний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/328-xirurgicnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль Доповнення':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/330-terapevticnii-profil-dopovnennya-baza-testiv-2014-/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/327-terapevticnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/331-pediatricnii-profil-dopovnennya-baza-testiv-2014-r/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/326-pediatricnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/332-gigijena-ooz-dopovnennya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/325-gigijena-ooz-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Акушерство і гінекологія Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/333-akuserstvo-i-ginekologiya-dopovnennya-baza-testiv-/base?page=')
                    if program_current == 'Акушерство і гінекологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/324-akuserstvo-i-ginekologiya-baza-testiv-2014-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Хірургічний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/323-xirurgicnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(13,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/322-terapevticnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/321-pediatricnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Гігієна та ООЗ':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/320-gigijena-ta-ooz-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/319-akuserstvo-ta-ginekologiya-baza-testiv-2012-roku/base?page=')
                if year_current == '2011':
                    if program_current == 'Хірургічний профіль':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/318-xirurgicnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/317-terapevticnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/316-pediatricnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/315-gigijena-ooz-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/314-akuserstvo-ta-ginekologiya-baza-testiv-2011-roku/base?page=')
            if KROK_current == 3:
                if year_current == '2009-2015':
                    parser(40,
                           'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/645-bukleti-vesna-osin-2009-2015-bez-povtorennya-zapit/base?page=')
                if year_current == '2014':
                    if program_current == 'Хірургічний профіль - осінь':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/411-xirurgicnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Хірургічний профіль - весна':
                        parser(11,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/650-xirurgicnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль - осінь':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/412-terapevticnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль - весна':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/649-terapevticnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль - осінь':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/413-pediatricnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль - весна':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/648-pediatricnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія - осінь':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/415-akuserstvo-ta-ginekologiya-osin-baza-testiv-2014-r/base?page=')
                    if program_current == 'Акушерство та гінекологія - весна':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/646-akuserstvo-ta-ginekologiya-vesna-baza-testiv-2014-/base?page=')
                    if program_current == 'Інфекційний профіль - осінь':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/414-infekciinii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Інфекційний профіль - весна':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/647-infekciinii-profil-vesna-baza-testiv-2014-roku/base?page=')
                if year_current == '2013':
                    if program_current == 'Хірургічний профіль':
                        parser(10,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/410-xirurgicnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(17,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/405-terapevticnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/404-pediatricnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/398-akuserstvo-ta-ginekologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Інфекційний профіль':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/399-infekciinii-profil-baza-testiv-2013-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Хірургічний профіль':
                        parser(10,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/409-xirurgicnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/406-terapevticnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/403-pediatricnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/397-akuserstvo-ta-ginekologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Інфекційний профіль':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/400-infekciinii-profil-baza-testiv-2012-roku/base?page=')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            answ1 = types.KeyboardButton(test_current[2].replace('\n', ''))
            answ2 = types.KeyboardButton(test_current[3].replace('\n', ''))
            answ3 = types.KeyboardButton(test_current[4].replace('\n', ''))
            answ4 = types.KeyboardButton(test_current[5].replace('\n', ''))
            answ5 = types.KeyboardButton(test_current[6].replace('\n', ''))
            item6 = types.KeyboardButton(button7_)
            random_arr = [answ1, answ2, answ3, answ4, answ5]
            random.shuffle(random_arr)
            for c in random_arr:
                markup.add(c)
            markup.add(item6)
            bot.send_message(message.chat.id, 'Тест ' + str(test_current[0]) + '\n' + test_current[1], reply_markup=markup)
        if message.text in test_current[2]:
            bot.send_message(message.chat.id, '✅ Правильно!')
            if KROK_current == 1:
                if year_current == '2014':
                    if program_current == 'Фармакологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/163-farmakologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/166-patologicna-fiziologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/167-patologicna-anatomiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/165-normalna-fiziologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/164-normalna-anatomiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/162-mikrobiologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(2,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/161-gistologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/160-bioximiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/159-biologiya-baza-testiv-2014-roku/base?page=')
                if year_current == '2013':
                    if program_current == 'Фармакологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/172-farmakologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/169-patologicna-fiziologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/168-patologicna-anatomiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/170-normalna-fiziologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/171-normalna-anatomiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/175-mikrobiologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(2,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/174-gistologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/173-bioximiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/85-biologiya-baza-testiv-2013-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Фармакологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/158-farmakologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/157-patologicna-fiziologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/156-patologicna-anatomiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/155-normalna-fiziologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/154-normalna-anatomiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/153-mikrobiologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/152-gistologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/151-bioximiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/150-biologiya-baza-testiv-2012-roku/base?page=')
                if year_current == '2011':
                    if program_current == 'Фармакологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/149-farmakologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/148-patologicna-fiziologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/147-patologicna-anatomiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/146-normalna-fiziologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/145-normalna-anatomiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/144-mikrobiologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/143-gistologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/142-bioximiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/141-biologiya-baza-testiv-2011-roku/base?page=')
            if KROK_current == 2:
                if year_current == '2005-2018':
                    parser(49,
                           'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/809-bukleti-2005-2018-bez-povtoren-zapitan-baza-testiv/base?page=')
                if year_current == '2014':
                    if program_current == 'Хірургічний профіль Доповнення':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/329-xirurgicnii-profil-dopovnennya-baza-testiv-2014-ro/base?page=')
                    if program_current == 'Хірургічний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/328-xirurgicnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль Доповнення':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/330-terapevticnii-profil-dopovnennya-baza-testiv-2014-/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/327-terapevticnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/331-pediatricnii-profil-dopovnennya-baza-testiv-2014-r/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/326-pediatricnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/332-gigijena-ooz-dopovnennya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/325-gigijena-ooz-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Акушерство і гінекологія Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/333-akuserstvo-i-ginekologiya-dopovnennya-baza-testiv-/base?page=')
                    if program_current == 'Акушерство і гінекологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/324-akuserstvo-i-ginekologiya-baza-testiv-2014-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Хірургічний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/323-xirurgicnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(13,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/322-terapevticnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/321-pediatricnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Гігієна та ООЗ':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/320-gigijena-ta-ooz-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/319-akuserstvo-ta-ginekologiya-baza-testiv-2012-roku/base?page=')
                if year_current == '2011':
                    if program_current == 'Хірургічний профіль':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/318-xirurgicnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/317-terapevticnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/316-pediatricnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/315-gigijena-ooz-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/314-akuserstvo-ta-ginekologiya-baza-testiv-2011-roku/base?page=')
            if KROK_current == 3:
                if year_current == '2009-2015':
                    parser(40,
                           'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/645-bukleti-vesna-osin-2009-2015-bez-povtorennya-zapit/base?page=')
                if year_current == '2014':
                    if program_current == 'Хірургічний профіль - осінь':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/411-xirurgicnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Хірургічний профіль - весна':
                        parser(11,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/650-xirurgicnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль - осінь':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/412-terapevticnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль - весна':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/649-terapevticnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль - осінь':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/413-pediatricnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль - весна':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/648-pediatricnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія - осінь':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/415-akuserstvo-ta-ginekologiya-osin-baza-testiv-2014-r/base?page=')
                    if program_current == 'Акушерство та гінекологія - весна':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/646-akuserstvo-ta-ginekologiya-vesna-baza-testiv-2014-/base?page=')
                    if program_current == 'Інфекційний профіль - осінь':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/414-infekciinii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Інфекційний профіль - весна':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/647-infekciinii-profil-vesna-baza-testiv-2014-roku/base?page=')
                if year_current == '2013':
                    if program_current == 'Хірургічний профіль':
                        parser(10,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/410-xirurgicnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(17,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/405-terapevticnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/404-pediatricnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/398-akuserstvo-ta-ginekologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Інфекційний профіль':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/399-infekciinii-profil-baza-testiv-2013-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Хірургічний профіль':
                        parser(10,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/409-xirurgicnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/406-terapevticnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/403-pediatricnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/397-akuserstvo-ta-ginekologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Інфекційний профіль':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/400-infekciinii-profil-baza-testiv-2012-roku/base?page=')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            answ1 = types.KeyboardButton(test_current[2].replace('\n', ''))
            answ2 = types.KeyboardButton(test_current[3].replace('\n', ''))
            answ3 = types.KeyboardButton(test_current[4].replace('\n', ''))
            answ4 = types.KeyboardButton(test_current[5].replace('\n', ''))
            answ5 = types.KeyboardButton(test_current[6].replace('\n', ''))
            item6 = types.KeyboardButton(button7_)
            random_arr = [answ1, answ2, answ3, answ4, answ5]
            random.shuffle(random_arr)
            for c in random_arr:
                markup.add(c)
            markup.add(item6)
            bot.send_message(message.chat.id, 'Тест ' + str(test_current[0]) + '\n' + test_current[1],
                             reply_markup=markup)
        if message.text in test_current[3] or message.text in test_current[4] or message.text in test_current[
            5] or message.text in test_current[6]:
            bot.send_message(message.chat.id, '❌ Неправильно!')
            bot.send_message(message.chat.id, 'Правильна відповідь: ' + test_current[2])
            if KROK_current == 1:
                if year_current == '2014':
                    if program_current == 'Фармакологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/163-farmakologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/166-patologicna-fiziologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/167-patologicna-anatomiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/165-normalna-fiziologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/164-normalna-anatomiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/162-mikrobiologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(2,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/161-gistologiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/160-bioximiya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/159-biologiya-baza-testiv-2014-roku/base?page=')
                if year_current == '2013':
                    if program_current == 'Фармакологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/172-farmakologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/169-patologicna-fiziologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/168-patologicna-anatomiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/170-normalna-fiziologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/171-normalna-anatomiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/175-mikrobiologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(2,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/174-gistologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/173-bioximiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/85-biologiya-baza-testiv-2013-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Фармакологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/158-farmakologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/157-patologicna-fiziologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/156-patologicna-anatomiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/155-normalna-fiziologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/154-normalna-anatomiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/153-mikrobiologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/152-gistologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/151-bioximiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/150-biologiya-baza-testiv-2012-roku/base?page=')
                if year_current == '2011':
                    if program_current == 'Фармакологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/149-farmakologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Патологічна фізіологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/148-patologicna-fiziologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Патологічна анатомія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/147-patologicna-anatomiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Нормальна фізіологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/146-normalna-fiziologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Нормальна анатомія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/145-normalna-anatomiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Мікробіологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/144-mikrobiologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Гістологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/143-gistologiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Біохімія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/142-bioximiya-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Біологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/141-biologiya-baza-testiv-2011-roku/base?page=')
            if KROK_current == 2:
                if year_current == '2005-2018':
                    parser(49,
                           'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/809-bukleti-2005-2018-bez-povtoren-zapitan-baza-testiv/base?page=')
                if year_current == '2014':
                    if program_current == 'Хірургічний профіль Доповнення':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/329-xirurgicnii-profil-dopovnennya-baza-testiv-2014-ro/base?page=')
                    if program_current == 'Хірургічний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/328-xirurgicnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль Доповнення':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/330-terapevticnii-profil-dopovnennya-baza-testiv-2014-/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/327-terapevticnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/331-pediatricnii-profil-dopovnennya-baza-testiv-2014-r/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/326-pediatricnii-profil-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/332-gigijena-ooz-dopovnennya-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/325-gigijena-ooz-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Акушерство і гінекологія Доповнення':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/333-akuserstvo-i-ginekologiya-dopovnennya-baza-testiv-/base?page=')
                    if program_current == 'Акушерство і гінекологія':
                        parser(5,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/324-akuserstvo-i-ginekologiya-baza-testiv-2014-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Хірургічний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/323-xirurgicnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(13,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/322-terapevticnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/321-pediatricnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Гігієна та ООЗ':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/320-gigijena-ta-ooz-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/319-akuserstvo-ta-ginekologiya-baza-testiv-2012-roku/base?page=')
                if year_current == '2011':
                    if program_current == 'Хірургічний профіль':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/318-xirurgicnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/317-terapevticnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/316-pediatricnii-profil-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Гігієна, ООЗ':
                        parser(6,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/315-gigijena-ooz-baza-testiv-2011-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(7,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/314-akuserstvo-ta-ginekologiya-baza-testiv-2011-roku/base?page=')
            if KROK_current == 3:
                if year_current == '2009-2015':
                    parser(40,
                           'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/645-bukleti-vesna-osin-2009-2015-bez-povtorennya-zapit/base?page=')
                if year_current == '2014':
                    if program_current == 'Хірургічний профіль - осінь':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/411-xirurgicnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Хірургічний профіль - весна':
                        parser(11,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/650-xirurgicnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль - осінь':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/412-terapevticnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Терапевтичний профіль - весна':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/649-terapevticnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль - осінь':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/413-pediatricnii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Педіатричний профіль - весна':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/648-pediatricnii-profil-vesna-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія - осінь':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/415-akuserstvo-ta-ginekologiya-osin-baza-testiv-2014-r/base?page=')
                    if program_current == 'Акушерство та гінекологія - весна':
                        parser(4,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/646-akuserstvo-ta-ginekologiya-vesna-baza-testiv-2014-/base?page=')
                    if program_current == 'Інфекційний профіль - осінь':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/414-infekciinii-profil-osin-baza-testiv-2014-roku/base?page=')
                    if program_current == 'Інфекційний профіль - весна':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/647-infekciinii-profil-vesna-baza-testiv-2014-roku/base?page=')
                if year_current == '2013':
                    if program_current == 'Хірургічний профіль':
                        parser(10,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/410-xirurgicnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(17,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/405-terapevticnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/404-pediatricnii-profil-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/398-akuserstvo-ta-ginekologiya-baza-testiv-2013-roku/base?page=')
                    if program_current == 'Інфекційний профіль':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/399-infekciinii-profil-baza-testiv-2013-roku/base?page=')
                if year_current == '2012':
                    if program_current == 'Хірургічний профіль':
                        parser(10,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/409-xirurgicnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Терапевтичний профіль':
                        parser(16,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/406-terapevticnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Педіатричний профіль':
                        parser(9,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/403-pediatricnii-profil-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Акушерство та гінекологія':
                        parser(8,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/397-akuserstvo-ta-ginekologiya-baza-testiv-2012-roku/base?page=')
                    if program_current == 'Інфекційний профіль':
                        parser(3,
                               'https://xn--80adi8aaufcj8j.xn--j1amh/testing/collection/400-infekciinii-profil-baza-testiv-2012-roku/base?page=')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            answ1 = types.KeyboardButton(test_current[2].replace('\n', ''))
            answ2 = types.KeyboardButton(test_current[3].replace('\n', ''))
            answ3 = types.KeyboardButton(test_current[4].replace('\n', ''))
            answ4 = types.KeyboardButton(test_current[5].replace('\n', ''))
            answ5 = types.KeyboardButton(test_current[6].replace('\n', ''))
            item6 = types.KeyboardButton(button7_)
            random_arr = [answ1, answ2, answ3, answ4, answ5]
            random.shuffle(random_arr)
            for c in random_arr:
                markup.add(c)
            markup.add(item6)
            bot.send_message(message.chat.id, 'Тест ' + str(test_current[0]) + '\n' + test_current[1],
                             reply_markup=markup)
        print(test)


bot.polling(none_stop=True)
