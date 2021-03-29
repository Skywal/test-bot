import telebot
import datetime
import time

bot = telebot.TeleBot("1405639485:AAH1sgnJS5DbLgl3aXjbZbDzGfXjD8w6rI8")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Hello ")

@bot.message_handler(content_types=['text'])
def conversation(message): 
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)