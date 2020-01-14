import config
import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('1030497018:AAF8bccwaWuXOzdoYq87RWE_ylMdCqQ03xE')

regions = ['Andijon','Namangan','Fargona']

@bot.message_handler(commands=["start"])
def start_bot(message):
	print(message.entities)
	markup = create_menu(regions, back=False)
	sms = bot.send_message(message.chat.id, 'Hududni tanlang', reply_markup=markup)
	bot.register_next_step_handler(sms, result)

@bot.message_handler(content_types=["text"])
def result(message):
	city = message.text
	append = 'd13b4c810c63472366e44e1555093111'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+append
	
	data = requests.get(url.format(city)).json()
	
	Obxavo = None
	print(data['weather'][0]['main'])
	if data['weather'][0]['main'] == 'Rain':
		Obxavo = "Yo'mg'ir"
	elif data['weather'][0]['main'] == 'Mist':
		Obxavo = "Tuman"	
	elif data['weather'][0]['main'] == 'Clouds':
		Obxavo = 'Bulut'
	elif data['weather'][0]['main'] == 'Snow':
		Obxavo = 'Qor'		
	results = "Xarorat {0} gradus \n Shamol tezligi {1} kms \n Ob-xavo {2}li".format(data['main']['temp'],data['wind']['speed'],Obxavo)
  bot.send_message(message.chat.id, results)

bot.polling(none_stop=True, interval=0)		

