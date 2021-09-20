import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
import telegram

updater = Updater(token='2042405373:AAGWHU3GKAGZ4O0n7-BGG4SiPBqxowpY1OU', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    keyboard = telegram.KeyboardButton('Categories')
    markup = telegram.ReplyKeyboardMarkup(keyboard=[[keyboard]], one_time_keyboard=False)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Test', reply_markup=markup)


def get_categories(update, context):
    response = requests.get('http://127.0.0.1:8000/api/categories')
    category_list = [f"Products in \"{i['title']}\" category" for i in response.json()]
    for item in response.json():
        markup = telegram.ReplyKeyboardMarkup(keyboard=[category_list], one_time_keyboard=False)
        context.bot.send_message(chat_id=update.effective_chat.id, text=item['title'], reply_markup=markup)


def get_products_by_category(update, context):
    category: str = update.effective_message.text.split('\"')[1]
    response = requests.get(f'http://127.0.0.1:8000/api/products?category={category}')

    for item in response.json():
        message = f"{item['title']}\n{item['description']}\n{item['price']}"
        inline_keyboard = [telegram.InlineKeyboardButton(text='+', callback_data='+'+item['product_uuid']),
                           telegram.InlineKeyboardButton(text='0', callback_data='None'),
                           telegram.InlineKeyboardButton(text='-', callback_data='-'+item['product_uuid'])]
        markup = telegram.InlineKeyboardMarkup([inline_keyboard])
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=markup)


def change_count(update: Update, context: CallbackContext):
    action = update.callback_query.data
    keyboard = update.effective_message.reply_markup['inline_keyboard'][0]
    if '+' in action:
        keyboard[1].text = str(int(keyboard[1].text) + 1)
    else:
        if keyboard[1].text == '0':
            return
        keyboard[1].text = str(int(keyboard[1].text) - 1)

    # TODO add to cart api
    uuid = action[1::]
    markup = telegram.InlineKeyboardMarkup([keyboard])
    context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id, reply_markup=markup)


#handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
captegory_handler = MessageHandler(filters=Filters.regex(r'Categories'), callback=get_categories)
products_handler = MessageHandler(filters=Filters.regex(r'Products in "\w{,30}" category'), callback=get_products_by_category)
add_count_handler = CallbackQueryHandler(pattern=r'\+', callback=change_count)
delete_count_nandler = CallbackQueryHandler(pattern=r"\-", callback=change_count)
dispatcher.add_handler(add_count_handler)
dispatcher.add_handler(delete_count_nandler)
dispatcher.add_handler(captegory_handler)
dispatcher.add_handler(products_handler)

if __name__ == '__main__':
    updater.start_polling()