#-- coding: utf-8 --

from key import API_TOKEN
import telebot


bot = telebot.TeleBot(API_TOKEN())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(message,"Bem-Vindo")

bot.polling()
