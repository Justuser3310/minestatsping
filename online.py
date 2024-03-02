from mctools import PINGClient
import telebot

from db import *

API_TOKEN = read()['token']
bot = telebot.TeleBot(API_TOKEN)

ping = PINGClient('CoolFunZone.aternos.me', 36413)

stats = ping.get_stats()
print(stats)

@bot.message_handler(commands=['online'])
def check_online(message):
	try:
		stats = ping.get_stats()
	except:
		bot.reply_to(message, "🔴 Сервер оффлайн")
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

{pp}""")


while True:
	try:
		bot.infinity_polling()
	except KeyboardInterrupt:
		exit()
	except:
		pass


