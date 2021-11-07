
@bot.message_handler(commands=['start'])
def start(message):
    rmk = types.ReplyKeyboardMarkup()
    rmk.add(types.ReplyKeyboardMarkup('Меню'), types.ReplyKeyboardMarkup('Контактная информация'),types.ReplyKeyboardMarkup('О нашем заведении'))

    msg = bot.send_message(message.chat.id,'Здравствуйте,я-VEGAN BOT,нажмите на одну из кнопок', reply_markup= rmk)
    bot.register_next_step_handler(msg, user_answer)

#def user_answer(message):
#    if message.text == 'Меню':
#        msg1 = bot.send_message(message.chat.id, 'Выберите одну из позиций')
#        bot.register_next_step_handler(msg1)

bot.polling(interval=0,none_stop=True)

bot.send_message(call.from_user.id,
                 '*#1\n(основа для пиццы, кешью-майонез, "не мясо", томаты черри, маслины, оливки,руккола, томатный соус)'
                 '\n350г  27р'
                 '\n\n#2\n(основа для пиццы, кешью-майонез,томаты черри, маринованные грибы,тофу, авокадо, маслины, базилик, соус песто)'
                 '\n350г  27р*', parse_mode='Markdown')

elif message.text == 'О нашем кафе🐈':
bot.send_message(message.from_user.id,
                 '*Hi!👋\nЭто страница твой путеводитель по здоровой свежей веганской еде без сахара,глютена и жареного🌱*',
                 parse_mode='Markdown')
directory = 'C:\\Users\\olgor\\Desktop\\photo\\информация о нас'
all_files_in_directory = os.listdir(directory)
print(all_files_in_directory)
for file in all_files_in_directory:
    img = open(directory + '/' + file, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    caption = 'внутри и снаружи'
    bot.send_photo(message.from_user.id, img, caption)
    img.close()
markup_inline = types.InlineKeyboardMarkup()
sweet_1 = types.InlineKeyboardButton(text='Raw пицца', callback_data='row pizza')
sweet_2 = types.InlineKeyboardButton(text='Салаты', callback_data='salat')
sweet_3 = types.InlineKeyboardButton(text='Спринг-роллы', callback_data='spring rolls')
sweet_4 = types.InlineKeyboardButton(text='Боулы', callback_data='bowls')
sweet_5 = types.InlineKeyboardButton(text='Супы', callback_data='soup')
sweet_6 = types.InlineKeyboardButton(text='Сладкое', callback_data='sweet')
sweet_7 = types.InlineKeyboardButton(text='Смузи', callback_data='smoothies')
sweet_8 = types.InlineKeyboardButton(text='Смузи боулы', callback_data='smoothies bowls')
sweet_9 = types.InlineKeyboardButton(text='Свежевыжатые соки', callback_data='freshly squeezed juices')
sweet_10 = types.InlineKeyboardButton(text='Хэлси шоты', callback_data='healthy shots')
sweet_11 = types.InlineKeyboardButton(text='Горячие напитки', callback_data='hot drinks')
markup_inline.add(sweet_1, sweet_2, sweet_3, sweet_4, sweet_5, sweet_6, sweet_7, sweet_8, sweet_9,sweet_10,sweet_11)

