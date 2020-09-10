#!/usr/bin/python3
#-- coding: utf-8 --

from key import API_TOKEN
from telebot import types
import telebot

bot = telebot.TeleBot(API_TOKEN())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = bot.reply_to(message,f"Bem-Vindo {chat_id}")
    bot.send_message(chat_id,"Para ajuda use /ajuda")

@bot.message_handler(commands=['ajuda'])
def send_help(message):
    chat_id = message.chat.id
    msg_help = bot.reply_to(message,"""Opcao: 1 /cadastro
Opcao: 2 /suporte
Opcao: 3 /contato""")
    bot.send_message(chat_id,"Endereco: Rua tau, Numero 9\nBairro: 7, Cidade: F - B")

@bot.message_handler(commands=['cadastro'])
def send_register(message):
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('A', 'B')
        msg_cad = bot.reply_to(message,"Escolha uma: ", reply_markup=markup)

bot.polling()
