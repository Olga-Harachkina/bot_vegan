import telebot
from telebot import types
import db_coonector
import config_reader

bot = telebot.TeleBot('1885102912:AAGGNu8pzR78HFRDl53gn0K8XmOaUDm_RPE')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('Меню','О нашем кафе🐈')
button_phone = types.KeyboardButton('Оставить номер телефона📲', request_contact=True)
information = types.KeyboardButton('Контактная информация')
markup.add(button_phone,information)
markup_url = types.InlineKeyboardMarkup()
url = types.InlineKeyboardButton(text='instagram', url='https://instagram.com/hijack.by?utm_medium=copy_link')
markup_url.add(url)


markup_inline = types.InlineKeyboardMarkup()
sweet_1 = types.InlineKeyboardButton(text='Raw пицца🍕', callback_data='row pizza')
sweet_2 = types.InlineKeyboardButton(text='Салаты🥗', callback_data='salat')
sweet_3 = types.InlineKeyboardButton(text='Спринг-роллы🥢', callback_data='spring rolls')
sweet_4 = types.InlineKeyboardButton(text='Боулы🍜', callback_data='bowls')
sweet_5 = types.InlineKeyboardButton(text='Супы🥘', callback_data='soup')
sweet_6 = types.InlineKeyboardButton(text='Сладкое🍰', callback_data='sweet')
sweet_7 = types.InlineKeyboardButton(text='Смузи', callback_data='smoothies')
sweet_8 = types.InlineKeyboardButton(text='Смузи боулы', callback_data='smoothies bowls')
sweet_9 = types.InlineKeyboardButton(text='Свежевыжатые соки', callback_data='freshly squeezed juices')
sweet_10 = types.InlineKeyboardButton(text='Хэлси шоты💪', callback_data='healthy shots')
sweet_11 = types.InlineKeyboardButton(text='Горячие напитки☕', callback_data='hot drinks')
markup_inline.add(sweet_1, sweet_2, sweet_3, sweet_4, sweet_5, sweet_6, sweet_7, sweet_8, sweet_9, sweet_10,
                  sweet_11)

static_content = config_reader.read_json()

db_coonector.create_tables_new()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,'*Здравствуй,{0}👋 \nЯ-HiJack_CaFe🐾,место о здоровой еде,любви к себе и животным💚\nПожалйста,нажми на одну из кнопок ниже⬇*'.format(message.from_user.first_name), reply_markup=markup,parse_mode='Markdown')
    bot.send_message(message.from_user.id,'_Оставьте свой номер,чтобы одним из первых узнать о наших новых акция и предложениях📲_',parse_mode='Markdown')

#/contacts-узнать номера телефонов в базе
@bot.message_handler(commands=['contacts'])
def start(message):
    nums = db_coonector.all_numbers()
    bot.send_message(message.from_user.id, str(nums), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer_user(message):
    if message.text == 'Контактная информация':
        bot.send_chat_action(message.from_user.id,'find_location')
        bot.send_location(message.from_user.id,53.90520881610152, 27.54810644007897)
        bot.send_message(message.from_user.id,'*Адрес:г.Минск,ул.Раковская 20'
                                              '\n\nРежим работы: Понедельника-воскресенье c 12-22'
                                              '\n\nТелефон:+375291427888'
                                              '\n\nНаш Instagram:*',
                         reply_markup=markup_url,parse_mode='Markdown')


    elif message.text == 'О нашем кафе🐈':
        bot.send_photo(caption='',
                       chat_id=message.from_user.id,
                       photo='https://cloud.mail.ru/public/GdVn/5QjEq3awP')
        bot.send_photo(caption='*Hi!👋\nЭто страница твой путеводитель по здоровой свежей веганской еде без сахара,глютена и жареного🌱*',parse_mode='Markdown',
                       chat_id=message.from_user.id,
                       photo='https://cloud.mail.ru/public/fbPU/GjuagHDDK')

    elif message.text == 'Оставить номер телефона📲':
        bot.send_message(message.from_user.id,'Оставьте свой номер,чтобы одним из первых узнать о наших новых акция и предложениях📲',reply_markup=markup)


    elif message.text == 'Меню':
        markmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markmenu.row('НАШИ АКЦИИ🔥','Вернуться в меню')
        markmenu.row('Вернуться в главное меню')
        bot.send_message(message.from_user.id,'*Выберите одну из кнопок меню⬇*',reply_markup=markup_inline,parse_mode='Markdown')
        bot.send_message(message.from_user.id,'*Ещё у нас есть много интерестных предложений для вас⬇*',reply_markup=markmenu,parse_mode='Markdown')

    elif message.text == 'Вернуться в меню':
        markmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markmenu.row('НАШИ АКЦИИ🔥', 'Вернуться в меню')
        glavnoe_menu = types.KeyboardButton('Вернуться в главное меню')
        markmenu.add(glavnoe_menu)
        bot.send_message(message.from_user.id,'*Выберите одну из кнопок меню⬇*',reply_markup=markup_inline,parse_mode='Markdown')

    elif message.text == 'НАШИ АКЦИИ🔥':
        for k, v in static_content['АКЦИИ'].items():
            bot.send_photo(caption= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=message.from_user.id, photo=v['Фото'])

    elif message.text == 'Вернуться в главное меню':
        bot.send_message(message.from_user.id,'*Пожалйста,нажми на одну из кнопок ниже⬇*',parse_mode='Markdown',reply_markup=markup)

#выводит данные в терминале
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    name = message.contact.first_name
    phone = message.contact.phone_number
    print('Received contact: %s, %s ' % (name, phone))
    db_coonector.add_phone(name, phone)



@bot.callback_query_handler(func = lambda call : True)
def pozit(call):
    if call.data == 'row pizza':
        for k, v in static_content['RAW ПИЦЦА'].items():
            bot.send_photo(caption= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id, photo=v['Фото'])

    elif call.data == 'hot drinks':
        for k, v in static_content['ГОРЯЧИЕ НАПИТКИ'].items():
            bot.send_message(text= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id)

    elif call.data == 'freshly squeezed juices':
        for k, v in static_content['СВЕЖЕВЫЖАТЫЕ'].items():
            bot.send_message(text= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id)

    elif call.data == 'salat':
        for k, v in static_content['САЛАТЫ'].items():
            bot.send_photo(caption= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id, photo=v['Фото'])

    elif call.data == 'spring rolls':
        for k, v in static_content['СПРИНГ-РОЛЛЫ'].items():
            bot.send_photo(caption= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id, photo=v['Фото'])

    elif call.data == 'bowls':
        for k, v in static_content['БОУЛЫ'].items():
            bot.send_photo(caption="*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown',chat_id=call.from_user.id, photo=v['Фото'])

    elif call.data == 'soup':
        for k, v in static_content['СУПЫ'].items():
            bot.send_photo(caption="*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown',chat_id=call.from_user.id, photo=v['Фото'])

    elif call.data == 'sweet':
        for k, v in static_content['СЛАДКОЕ'].items():
            bot.send_photo(caption="*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown',chat_id=call.from_user.id, photo=v['Фото'])
        bot.send_message(call.from_user.id,'_🐝-ПРОДУКТ СОДЕРЖИТ МЁД_',parse_mode='Markdown')

    elif call.data == 'smoothies':
        for k, v in static_content['СМУЗИ'].items():
            bot.send_photo(caption= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id, photo=v['Фото'])

    elif call.data == 'smoothies bowls':
        for k, v in static_content['СМУЗИ-БОУЛ'].items():
            bot.send_photo(caption= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id, photo=v['Фото'])

    elif call.data == 'healthy shots':
        for k, v in static_content['ШОТЫ'].items():
            bot.send_photo(caption= "*" + k + "\n" + v['Описание'] + "*", parse_mode='Markdown', chat_id=call.from_user.id, photo=v['Фото'])
        bot.send_message(call.from_user.id,'_1 ШОТ-3p    2 ШОТА-5.5p    3 ШОТА-8p_',parse_mode='Markdown')

bot.polling(none_stop=True,interval=0)

