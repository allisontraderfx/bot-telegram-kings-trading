
import telebot

TOKEN = '7615498121:AAE5oRU_ILio7I5GDbRx-u5WqEBNmu1-Fmk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Seja bem-vindo ao nosso canal oficial!\nAqui você vai receber atualizações e tutoriais do nosso robô!")

bot.polling()
