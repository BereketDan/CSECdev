from .models import *
import telebot
from datetime import datetime




bot = telebot.TeleBot('6949284535:AAHNR3sl6uJM8MrtDydf6AyiQhecbRQMQyc')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, """Hello 👋 \nWelcome to the CSEC Dev bot. \n CSEC Development Division Official Channel @csec_devs Join \n \n \n \n ⚡️ For feedback click  /feedback """)
    
    



@bot.message_handler(commands=['feedback'])
def handle_feedback(message):
    bot.reply_to(message, """Write Your feedback here ? """ )
    bot.register_next_step_handler(message, handle_feedback_Q)





def handle_feedback_Q(message):
    username_acc = message.from_user.username
    feed_msg =  message.text
    current_date = datetime.now().strftime("%Y-%m-%d")
    return handle_close(message)
    
    


def handle_close(message):
    
  
    bot.reply_to(message, """Thanks for Your Comment """ )





bot.polling()
