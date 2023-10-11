import telebot
import wikipedia

wikipedia.set_lang("ru")

TOKEN = "6484610577:AAEhD5BvdUVUO75pp8Jfz9hN3-nmCTaDkd8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте, я текстовый бот")

@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, "Бро! У меня эта функция не прописана! Сорян! :)")

@bot.message_handler(func=lambda message: True)
def talk(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Здравствуйте, как у Вас дела?")
    elif message.text == "Хорошо":
        bot.send_message(message.chat.id, "Отлично! Рад за Вас!")
    else:
        low_r = message.text
        low_r = low_r.replace(" ", "_")
        try:
            page = wikipedia.page(low_r)
            bot.send_message(message.chat.id, page.summary)
        except wikipedia.exceptions.PageError:
            bot.send_message(message.chat.id, "Статья не найдена")

bot.polling(none_stop=True)
