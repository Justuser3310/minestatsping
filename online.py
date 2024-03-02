from mctools import PINGClient
import telebot
from threading import Thread
from time import time, sleep

from db import *

API_TOKEN = read()['token']
bot = telebot.TeleBot(API_TOKEN)

# 764 - 1.20.2
host = 'CoolFunZone.aternos.me'
port = 36413
prot = 764
global c
c = PINGClient(host, port, proto_num = prot)

@bot.message_handler(commands=['online'])
def check_online(message):
	global c

	try:
		stats = c.get_stats()
		ms = c.ping()
	except:
		bot.reply_to(message, "🔴 Сервер оффлайн")
		c.stop()
		c = PINGClient(host, port, proto_num = prot)
		return 0

	maxp = stats['players']['max']
	onp = stats['players']['online']

	try:
		first = True
		for i in stats['players']['sample']:
			if first == True:
				pp = i[0][:i[0].find('[')]
				first = False
			else:
				pp = pp+ ' ; ' +i[0][:i[0].find('[')]
	except:
		pp = ''

	bot.reply_to(message, f"""🟢 Игроки онлайн >> {onp}/{maxp}

{pp}

📡  {round(ms)} ms""")


while True:
	try:
		bot.infinity_polling()
	except KeyboardInterrupt:
		exit()
	except:
		pass


