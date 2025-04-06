import telebot
import os
from flask import Flask, request

API_TOKEN = '7615498121:AAE5oRU_ILio7I5GDbRx-u5WqEBNmu1-Fmk'
WEBHOOK_URL = 'https://bot-telegram-kings-trading-1.onrender.com/'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Mensagem de boas-vindas
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('📲 Suporte', '📸 Instagram')
    bot.send_message(message.chat.id, "Bem-vindo ao Bot Kings Trading! Escolha uma opção abaixo:", reply_markup=markup)

# Respostas para os botões
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == '📲 Suporte':
        bot.reply_to(message, "Entre em contato com o nosso suporte: https://t.me/seusuporte")
    elif message.text == '📸 Instagram':
        bot.reply_to(message, "Siga nosso Instagram: https://instagram.com/seuinstagram")
    else:
        bot.reply_to(message, "Opção não reconhecida. Por favor, escolha uma opção abaixo.")

# Webhook
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
