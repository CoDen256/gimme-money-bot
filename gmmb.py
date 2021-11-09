import telebot

bot = telebot.TeleBot("2106720826:AAET8-1Lgo8Ou_Iq7E8DvqWb-Azz3QgDnhs", threaded=False)
bot.send_message(283382228, "Starting GMMB")


@bot.message_handler(commands=['start', 'help'])
def start(message):
    try:
        bot.send_message(
            message.chat.id,
            text="Hello, I need your money",
            parse_mode='markdown'
        )

    except Exception as e:
        bot.send_message(message.chat.id, e)
        log(str(e))



""" DEBUG """
def log(text):
    bot.send_message(283382228, text=f"{text}")


bot.polling()