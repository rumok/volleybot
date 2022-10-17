import telebot;
bot = telebot.TeleBot('5424073084:AAHWGGPpdrvH3gA02GAN-ymIzhqGx2awF5I');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "+":
        bot.send_message(message.from_user.id, "ты записан")
    elif message.text == "-":
        bot.send_message(message.from_user.id, "минус один")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "+ или -")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)