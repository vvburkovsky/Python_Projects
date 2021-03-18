import telebot
import weather_current as wc
import weather_3_days as wc3
from subprocess import call

API_TOKEN = '123456789'
bot = telebot.TeleBot(API_TOKEN)
admin_user_id = 123 or 456

@bot.message_handler(commands=['start'])
def start(message):
  check_id = message.from_user.id
  if check_id == admin_user_id:
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row ('Погода')
    keyboard.row ('Роутер')
    bot.send_message(message.chat.id, text = 'Что надо:', reply_markup = keyboard)
  if check_id != admin_user_id:
    bot.send_message(message.chat.id, text = 'Уходи')


#Получить USER ID 
@bot.message_handler(commands=['id'])
def send_start(message):
	to_check_id = message.from_user.id
	bot.reply_to(message, to_check_id)

@bot.message_handler(content_types = ['text'])
def main (message):

#Возврат в основное меню
    back = telebot.types.ReplyKeyboardMarkup()
    back.row ('Погода')
    back.row ('Роутер')

#Подменю погода
    menu1 = telebot.types.ReplyKeyboardMarkup()
    menu1.row ('Погода сейчас')
    menu1.row ('Погода на 3 дня')
    menu1.row ('Назад')

#Подменю Роутер
    menu2 = telebot.types.ReplyKeyboardMarkup()
    menu2.row ('вкл WIFI')
    menu2.row ('выкл WIFI')
#    menu2.row ('статус WIFI')
    menu2.row ('Назад')
    
    if message.text == 'Роутер':
      bot.send_message(message.chat.id, text = 'Что надо:', reply_markup = menu2)

    if message.text == 'Погода':
      bot.send_message(message.chat.id, text ='На когда надо', reply_markup = menu1)

    if message.text == 'Погода сейчас':
      bot.send_message(message.chat.id, '\n'.join(wc.weather_one_day()))
    
    if message.text == 'Погода на 3 дня':
      bot.send_message(message.chat.id, wc3.weather_3_days())

    if message.text == 'Назад':
      bot.send_message(message.chat.id, text ='Что надо', reply_markup = back)
    
    if message.text == 'вкл WIFI':
      call(["/bin/sh /usr/bin/Telegram_bot/on_wifi.sh"], shell=True)
      bot.send_message(message.chat.id, text ='WIFI включен!')


    if message.text == 'выкл WIFI':
      call(["/bin/sh /usr/bin/Telegram_bot/off_wifi.sh"], shell=True)
      bot.send_message(message.chat.id, text ='WIFI выключен!')

#    if message.text == 'статус WIFI': #не работает
#      bot.send_message(message.chat.id, '\n'.join(wc.current))


bot.polling()