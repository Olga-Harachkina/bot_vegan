#import os
import telebot
from telebot import types
import db_coonector
import config

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
sweet_10 = types.InlineKeyboardButton(text='Хэлси шоты', callback_data='healthy shots')
sweet_11 = types.InlineKeyboardButton(text='Горячие напитки☕', callback_data='hot drinks')
markup_inline.add(sweet_1, sweet_2, sweet_3, sweet_4, sweet_5, sweet_6, sweet_7, sweet_8, sweet_9, sweet_10,
                  sweet_11)


db_coonector.create_tables()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,'*Здравствуй,{0}*'.format(message.from_user.first_name), reply_markup=markup,parse_mode='Markdown')
    bot.send_message(message.from_user.id,'*Я-HiJack_CaFe🐾,место о здоровой еде,любви к себе и животным💚\nПожалйста,нажми на одну из кнопок ниже⬇*',parse_mode='Markdown')


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



    elif message.text == 'Меню':
        markmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markmenu.row('НАШИ АКЦИИ','Вернуться в меню')
        markmenu.row('Вернуться в главное меню')
        bot.send_message(message.from_user.id,'*Выберите одну из кнопок меню⬇*',reply_markup=markup_inline,parse_mode='Markdown')
        bot.send_message(message.from_user.id,'*Ещё у нас есть много интерестных предложений для вас⬇*',reply_markup=markmenu,parse_mode='Markdown')

    elif message.text == 'Вернуться в меню':
        markmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markmenu.row('НАШИ АКЦИИ', 'Вернуться в меню')
        glavnoe_menu = types.KeyboardButton('Вернуться в главное меню')
        markmenu.add(glavnoe_menu)
        bot.send_message(message.from_user.id,'*Выберите одну из кнопок меню⬇*',reply_markup=markup_inline,parse_mode='Markdown')

    elif message.text == 'НАШИ АКЦИИ':
        bot.send_message(message.from_user.id,'???????')

    elif message.text == 'Вернуться в главное меню':
        bot.send_message(message.from_user.id,'*Пожалйста,нажми на одну из кнопок ниже⬇*',parse_mode='Markdown',reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    name = message.contact.first_name
    phone = message.contact.phone_number
    print('Received contact: %s, %s ' % (name, phone))
    db_coonector.add_phone(name, phone)



@bot.callback_query_handler(func = lambda call : True)
def pozit(call):
    if call.data == 'row pizza':
       bot.send_photo(caption='*#1\n(основа для пиццы, кешью-майонез, "не мясо", томаты черри, маслины, оливки,руккола, томатный соус)'
                              '\n350г  27р*',parse_mode='Markdown',
                              chat_id=call.from_user.id,
                              photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-11%2014.38.28.HEIC')

       bot.send_photo(caption='*#2\n(основа для пиццы, кешью-майонез,томаты черри, маринованные грибы,тофу, авокадо, маслины, базилик, соус песто)'
                              '\n350г  27р*',parse_mode='Markdown',
                              chat_id= call.from_user.id,
                              photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-11%2014.41.27.HEIC')

    elif call.data == 'hot drinks':
        bot.send_message(call.from_user.id,'*Эспрессо    3р'
                                           '\n\nАмерикано   3р'
                                           '\n\nКапучино    250мл    6p'
                                           '\n\nКапучино    350мл    7p'
                                           '\n\nФлет-уайт    7р'
                                           '\n\nЛатте    7p'
                                           '\n\nКакао    6р'
                                           '\n\nКакао с кэробом    6р'
                                           '\n\nМатча    6р'
                                           '\n\nТравяной чай    3*',parse_mode='Markdown')

    elif call.data == 'freshly squeezed juices':
        bot.send_message(call.from_user.id,'*Апельсин🍊    8р'
                                           '\n\nГрейпфрут    8p'
                                           '\n\nЯблоко🍎    8p'
                                           '\n\nСвёкла-апельсин    8p*',parse_mode='Markdown')
    elif call.data == 'salat':
        bot.send_photo(caption='*Зелёный и полезный'
                                '\n(айсберг, рамен, маринованный тофу, авокадо, огурец, кешью, зелёная горчичная заправка, кукурузные хлебцы)'
                                '\n240г    14p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-11%2016.50.09.HEIC')

        bot.send_photo(caption='*Компромиссо'
                               '\n(aйсберг, руккола, маринованный тофу, авокадо, томаты черри, мисо-майонез, кукурузные хлебцы)'
                               '\n290г    14р*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='')

        bot.send_photo(caption='*Пушка, бомба, ракета'
                                '\n(aйсберг, рамен, "не мясо", томаты Черри,томатный соус, кешью-майонез,кунжут, кукурузные хлебцы)'
                                '\n290г    12р*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='')

    elif call.data == 'spring rolls':
        bot.send_photo(caption='*Чак Нори'
                                '\n(рисовая бумага, тофу, авокадо, огурец, нори, кешью-майонез, кунжут подаются с соевым соусом)'
                                '\n140г    8p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://cloud.mail.ru/public/YVU2/U63bJjHgq/2021-10-11%2016.55.27.HEIC')

        bot.send_photo(caption='*Овощная вечеринка'
                                '\n(рисовая бумага, фунчоза, тофу, авокадо,огурец, красная капуста, морковь, арахис,мята, кунжут подаются с домашним арахисовым соусом)'
                                '\n150г    8p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://cloud.mail.ru/public/YVU2/U63bJjHgq/2021-10-11%2017.08.06.HEIC')


    elif call.data == 'bowls':
        bot.send_photo(caption='*Гречка-боул «Зэ бэст гречка»'
                                '\n(гречка, нори, маринованный тофу, авокадо,оливки, кешью-майонез, кунжут)'
                                '\n330г    12p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-11%2016.36.54.HEIC')

        bot.send_photo(caption='*Лапша-боул «Обещания бывших»'
                               '\n(фунчоза, томаты Черри, морковь,маринованный тофу, авокадо, маринованный вакаме, арахисовый соус, мисо-майонез, кунжут, арахис)'
                               '\n350г    12p*',parse_mode='Markdown',
                               chat_id=call.from_user.id,
                               photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-15%2002.44.16.JPEG')

        bot.send_photo(caption='*Цукини-паста «Зудлс»'
                               '\n(цукини, томаты черри, базилик, кешью,соус песто, кукурузные хлебцы)'
                               '\n290г    13p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-13%2023.21.03.JPEG')

    elif call.data == 'soup':
        bot.send_message(call.from_user.id,'*СУП ДНЯ    7р'
                                           '\nподаётся с кукурузными хлебцами*',parse_mode='Markdown')
    elif call.data == 'sweet':
        bot.send_message(call.from_user.id,'*Торт «Морковныйс черникой и черносливом»    7p'
                                            '\n\nТорт «Морковный с клюквой и курагой»    7p'
                                            '\n\nТорт «Турбо»    7p'
                                            '\n\n«Пряник»    4p'
                                            '\n\n«Печенье»    1.5p'
                                            '\n\n«Халва»    1.5p'
                                            '\n\nХалва шоколадная    1.5p'
                                            '\n\nЭнергобатончик    50г/100г    3/6.5p'
                                            '\n\nПряник🐝    4p'
                                            '\n\nХалва🐝    1.5p'
                                            '\n\nХалва шоколадная🐝    1.5p'
                                            '\n\nЭнергобатончик🐝    50г/100г    3/6.5p*'
                                            '\n\n_🐝-ПРОДУКТ СОДЕРЖИТ МЁД_',parse_mode='Markdown')
    elif call.data == 'smoothies':
        bot.send_photo(caption='*Чоко Бой'
                               '\n(банан, арахисовая паста, какао, зеленая гречка, кэроб,кокосовое или миндальное молоко)'
                               '\n300г   9p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-15%2010.05.24.JPEG')

        bot.send_photo(caption='*Малиновый закат'
                               '\n(малина, черника, банан, зел.гречка, сироп топинамбура, яблоко, кокосовое или миндальное молоко)'
                               '\n300г    9р*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-11%2015.51.36.HEIC')

        bot.send_photo(caption='*Грин дэй'
                                '\n(шпинат, семена льна, банан, яблоко,зелёная гречка, сок лимона, вода)'
                                '\n300г    9р*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-11%2016.03.27.HEIC')

        bot.send_message(call.from_user.id,'*Секси-Рекси'
                                           '\n(банан, клубника,манго, кокосовое и миндальное молоко)'
                                           '\n300г    9p')


    elif call.data == 'smoothies bowls':
        bot.send_photo(caption='*Секси-Рекси'
                                '\n(банан, клубника, манго, кокосовое или миндальное молоко подаётся с гранолой, бананом и кокосовыми чипсами )'
                                '\n420г    12p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='')

        bot.send_photo(caption='*Чоко Бой'
                                '\n(банан, арахисовая паста, какао, зел.гречка кэроб, кокосовое или миндальное молоко подается с гранолой, бананом, кокосовыми чипсами и семенами чиа )'
                                '\n420г    12p*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='')

        bot.send_photo(caption='*Малиновый закат'
                                '\n(малина, черника, банан, яблоко, кокосовое или миндальное молоко, зелёная гречка, сироп топинамбура подаётся с гранолой, яблоком и семенами чиа)'
                                '\n420г    12р*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='')

        bot.send_photo(caption='*Грин дэй'
                                '\n(шпинат, семена льна, банан, яблоко, зелёная гречка, сок лимона, вода подается с гранолой, яблоком и семенами чиа)'
                                '\n420г    12р*',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='')

    elif call.data == 'healthy shots':
        bot.send_photo(caption='\n*«Оранжевый🟠»'
                               '\n(имбирь, мандарин, куркума)'
                               '\n20г    3p'
                               '\n\n«Зелёный🟢»'
                               '\n(сельдерей, яблоко, лайм)'
                               '\n20г    3p'
                               '\n\n«Красный🔴»'
                               '\n(свёкла, грейпфрут, яблоко красное)'
                               '\n20г    3p*'
                               '\n\n_1 ШОТ-3p    2 ШОТА-5.5p    3 ШОТА-8p_',parse_mode='Markdown',
                                chat_id=call.from_user.id,
                                photo='https://thumb.cloud.mail.ru/weblink/thumb/xw1/YVU2/U63bJjHgq/2021-10-11%2017.40.07.HEIC')


bot.polling(none_stop=True,interval=0)

