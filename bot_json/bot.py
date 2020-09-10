import telebot                          # biblioteca do bot
import json
from urllib.request import urlopen      # acessa urls na internet
from key import API_TOKEN               # token

bot = telebot.TeleBot(API_TOKEN()) # variavel que guarda o token

@bot.message_handler(commands=['cep']) #Comando digitado pelo usuario

def send_cep(message):
    
    # responde o camando cep com uma acao
    msg = bot.reply_to(message, "Digite o CEP:") 
    
    chat_id = message.chat.id # Id do usuario
    
    # armazena a informacao digitada e passa para o proximo passo
    bot.register_next_step_handler(msg, send_cep_step)

def send_cep_step(message):
    
    chat_id = message.chat.id # Id do usuario
    
    mensagem_cep = message.text  # mensagem digitada
    
    url = (f"https://viacep.com.br/ws/{mensagem_cep}/json")
    
    response = urlopen(url) # abrir a url
    
    data = json.loads(response.read()) # carrega o json e ler o arquivo
    
    print(data)
    
    cep = data['cep']
    logradouro = data['logradouro']
    bairro = data['bairro']
    localidade = data['localidade']
    uf = data['uf']
    bot.send_message(chat_id,f"""CEP: {cep}\nLogradouro: {logradouro}
bairro: {bairro} localidade {localidade} uf: {uf}""")
\
bot.polling()
