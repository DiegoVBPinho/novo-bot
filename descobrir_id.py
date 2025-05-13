import telebot

bot = telebot.TeleBot('7438251863:AAH9KEeqTTLMhaP_7XhDLAXs61SBwCXXaog')

@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    bot.reply_to(msg, 'Bot ativo! ✅')
    print(f'[INFO] Seu chat ID é: {msg.chat.id}')

bot.infinity_polling()
