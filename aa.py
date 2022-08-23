import telebot

bot = telebot.TeleBot("5569517557:AAHEPxk21TdyycOmAFA0jy7UWLhdMq_Q5GQ")

@bot.message_handler(commands=['start'])
def abc(m):
    nm = m.from_user.first_name
    bot.send_message(m.chat.id,"Oye "+nm+" Okajer bot e aisen ken?")
    print(nm+" called /start")

bot.polling()
