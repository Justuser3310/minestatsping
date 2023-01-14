from mctools import PINGClient
ping = PINGClient('play.dmcraft.online')
#stats = ping.get_stats()

#Work with JSON
import json
def read():
	global db
	with open('db.json', 'r') as openfile:
		db = json.load(openfile)
def write():
	global db
	js = json.dumps(db, indent=4)
	with open("db.json", "w") as outfile:
		outfile.write(js)

#My libraries
from time import sleep

#Read
read()

while True:
	sleep(1)

	try:
		stats = ping.get_stats()
		if stats['players']['online'] != 0:
			for i in stats['players']['sample']:
				#Add in db if not in db
				if i[0] not in db:
					db[i[0]] = 1
					write()
				else:
					db[i[0]] = db[i[0]] + 1
					write()

#			print(f'{i[0]}  ++  {db[i[0]]}')
	except:
		print('Maybe server offline')
