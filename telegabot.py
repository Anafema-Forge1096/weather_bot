from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('4f47fa8569af6c448a362df40d258982', config_dict)
bot = telebot.TeleBot("5061220227:AAGxFML9Aaq3_bgKw1OMvO38PUlND1v-nxc")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Назовите город, в котором хотите узнать погоду: ')

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    w.detailed_status         # 'clouds'
    w.wind()                  # {'speed': 4.6, 'deg': 330}
    w.humidity                # 87
    w.temperature('celsius') # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w.rain                    # {}
    w.heat_index              # None
    w.clouds                  # 75

    temp = w.temperature('celsius')["temp"]
    temp1=w.temperature('celsius')['feels_like']
    status = w.detailed_status
    wind = w.wind()['speed']
    answer = 'В городе ' + message.text + " сейчас " + str(status)+ '.' + "\n"
    answer += "Температура сейчас в районе " + str(round(temp)) + '°C'+ '.' + "\n"
    answer += 'Ощущается как ' + str(round(temp1)) +  ' °C' + '.' + "\n"
    answer += 'Скорость ветра ' + str(round(wind)) +  ' м/с.' + "\n"
    bot.send_message(message.chat.id, answer)
    
bot.polling(none_stop=True, interval=0)



