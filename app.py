import telebot
import time

TOKEN = "8418479418:AAEi-QfPRs8Hew9wX1fqEMOGJIqGcr4wo8c:

bot = telebot.TeleBot(TOKEN)

def get_answer(text):
    return f"سمعتك: {text} - بداية وعي الإنسان"

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    reply = get_answer(message.text)
    bot.reply_to(message, reply)

# هادي هي اللي كتمنع البوت يطيح
while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"طاح، كنعاود: {e}")
        time.sleep(5)
