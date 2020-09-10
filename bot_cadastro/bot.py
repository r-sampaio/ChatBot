#!/usr/bin/python3
#-- coding: utf-8 --

from key import API_TOKEN #Importa o Tokem
from telebot import types #Chama a funcao types dentro da telebot
import telebot #Biblioteca do bot

bot = telebot.TeleBot(API_TOKEN()) #Ler o token e salva na variavel bot

@bot.message_handler(commands=['start']) #Comando digitado pelo usuario
def send_welcome(message):
    chat_id = message.chat.id #pega o ID do usuario
    msg = bot.reply_to(message,f"Bem-Vindo {chat_id}") #resposta
    bot.send_message(chat_id,"Para ajuda use /ajuda")

@bot.message_handler(commands=['ajuda']) #Comando digitado pelo usuario
def send_help(message):
    chat_id = message.chat.id
    msg_help = bot.reply_to(message,"""Opcao: 1 /cadastro
Opcao: 2 /suporte
Opcao: 3 /contato""") #resposta
    bot.send_message(chat_id,"Endereco: Rua tau, Numero 9\nBairro: 7, Cidade: F - B")
    #envia uma mensagem

@bot.message_handler(commands=['cadastro']) #Comando digitado pelo usuario
def send_register(message):
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        #o usuario apenas pode escolher uma  das opcoes
        markup.add('A', 'B')
        msg_cad = bot.reply_to(message,"Escolha uma: ", reply_markup=markup)

bot.polling() #fica ouvindo, esperando que o usuario digite algo
