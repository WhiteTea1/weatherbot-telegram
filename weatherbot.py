import telebot
import requests
import json

token = '6230500274:AAEwvnh0WPFkjUbOp0K2iW5DiFyiKfQND9w'
API = '737fe8338bf6bd1683549fb04d9311c9'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот который поможет узнать тебе температуру на улицах твоего либо любого другого города на нашей планете. Просто отправь мне название города.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text
    req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(req.text)
    bot.reply_to(message, f'Сейчас на улицах города {city} - {data["main"]["temp"]}' + "°" + " По цельсию")

bot.polling(none_stop=True)