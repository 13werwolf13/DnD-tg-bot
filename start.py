import telebot
import randomgenerator
import settings
bones = 4
randomgenerator.getrundomnumber(d = bones)



bot = telebot.TeleBot(settings.token)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Отправь мне /d3 если тебе нужно бросить 4'х гранный куб, /d4 если шести гранный")
    bot.send_message(message.chat.id, "все варианты кубиков: /d3, /d4, /d6, /d8, /d10, /d12, /d20, /d100")
    bot.send_message(message.chat.id, "Удачи в игре")

@bot.message_handler(commands=['d3'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d3)
    bot.send_message(message.chat.id, randomgenerator.num)

@bot.message_handler(commands=['d4'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d4)
    bot.send_message(message.chat.id, randomgenerator.num)

@bot.message_handler(commands=['d6'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d6)
    bot.send_message(message.chat.id, randomgenerator.num)

@bot.message_handler(commands=['d8'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d8)
    bot.send_message(message.chat.id, randomgenerator.num)

@bot.message_handler(commands=['d10'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d10)
    bot.send_message(message.chat.id, randomgenerator.num)

@bot.message_handler(commands=['d12'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d12)
    bot.send_message(message.chat.id, randomgenerator.num)

@bot.message_handler(commands=['d20'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d20)
    bot.send_message(message.chat.id, randomgenerator.num)

@bot.message_handler(commands=['d100'])
def handle_text(message):
    num = randomgenerator.getrundomnumber(d = settings.d100)
    bot.send_message(message.chat.id, randomgenerator.num)

bot.polling(none_stop=True, interval=0)