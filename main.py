
import telebot
from telebot import types

TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

# Comando de start e boas-vindas
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    suporte_button = types.InlineKeyboardButton(text='💬 Suporte no WhatsApp', url='https://wa.me/5547992666718')
    instagram_button = types.InlineKeyboardButton(text='📷 Instagram', url='https://instagram.com/allisontraderfx')
    markup.add(suporte_button, instagram_button)

    with open('logo.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption='🚀 Bem-vindo ao canal oficial da King's Trading!\n\nFique atento às nossas atualizações e oportunidades exclusivas!',
                       reply_markup=markup)

# Iniciar o bot
print('Bot está rodando...')
bot.polling()
