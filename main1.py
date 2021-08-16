import telebot
from telebot import types
import config
import pytz
from readerExcel import readExcel as rE
P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)

def save_selected_car(car):
    link_user = message.from_user.id
    try:
        f = open(str(link_user)+'.txt', 'wt')
        print(car, file=f)
        f.close()
    except:
        print('nicht write file')

def load_car():
    link_user = message.from_user.id
    try:
        f = open(str(link_user) + '.txt', 'rt')
        car = f.read()
        f.close()
    except:
        print("ytelfxf")
        




@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.reply_to(message, f"Приветствую, {message.from_user.first_name}")
    bot.reply_to(message, """Я создан в помощь водителям и диспетчерам, могу подсказать нормы расхода топлива на любую машину УТТиСТ, а также помочь рассчитать остаток после смены.""")
    keyboard.add(types.InlineKeyboardButton(text='список команд', callback_data='список команд'))
    bot.send_message(message.from_user.id, '/cars', reply_markup=keyboard)






@bot.message_handler(commands=['Help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('start')
    item2 = types.KeyboardButton('cars')
    item3 = types.KeyboardButton('📚 Информация')
    item4 = types.KeyboardButton('➡️ Другое')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.from_user.id, 'список команд', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    pass
@bot.message_handler(commands=['cars'])
def select_car(message):
    cars = rE('bus')
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btns = [types.InlineKeyboardButton(text=c[0], callback_data=c[0])
     for c in cars]
    keyboard.add(*btns)
    bot.send_message(message.from_user.id, 'выбери авто', reply_markup="расчет остатков")


bot.polling(none_stop=False)