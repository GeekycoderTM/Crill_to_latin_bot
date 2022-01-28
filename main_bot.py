# Kirill - lotin bot
# library import qilish
from Crill_to_latin_bot.transliterate import to_cyrillic, to_latin
import telebot

# tokenni kiritib telegrambot bn boglanish
TOKEN = "your taken token from telegram bot father"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# # start, help commandalarga javob beruvchi func
@bot.message_handler(commands=['start'])
def send_welcome(message):
    ans = "Assalomu alaikum Xush kelibsiz! "
    ans += "\n O`zgartirmoqchi bo`lgan Matnni kiriting:"
    ans += "\n Unutmang biz  faqat Lotin va Krill alifbosidan iborat Matnlar bilan ishlay olamiz!!!"
    bot.reply_to(message, ans)

# har qanday habarga javob qaytarish
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
# berilgan matn qaydayligini tekshirib olish sharti
# ans = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)  #first way
    if msg.isascii():    #second way
        ans = to_cyrillic(msg)
    else:
        ans = to_latin(msg)
#berilgan matnni turiga qarab qayta ozgartirib yuborish
    bot.reply_to(message, ans)

bot.polling()
