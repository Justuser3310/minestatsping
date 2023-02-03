from mctools import PINGClient
ping = PINGClient('135.181.170.94', 25630)

import telebot
API_TOKEN = '6142777478:AAHTyrHPhr8j0jWoSEIyPvpvmozVp6axLKE'
bot = telebot.TeleBot(API_TOKEN)


stats = ping.get_stats()
print(stats)

@bot.message_handler(commands=['online'])
def send_welcome(message):
	stats = ping.get_stats()
	
	maxp = stats['players']['max']
	onp= stats['players']['online']
	
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



bot.infinity_polling()
