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

needsleep = 0
ttime = 0
while True:
	if needsleep == 30:
		needsleep = 0
		sleep(30)
		ttime = 29
	else:
		sleep(1)
		needsleep += 1

	try:
	#if True:
		stats = ping.get_stats()
		if stats['players']['online'] != 0:
			for i in stats['players']['sample']:
				#Add in db if not in db
				if i[0] not in db:
					db[i[0]] = 1 + ttime
					write()
				else:
					db[i[0]] = db[i[0]] + 1 + ttime
					write()
		ttime = 0

	except Exception as e:
		if e == '[Errno 32] Broken pipe':
			sleep(60)
			ttime = 59
			print("CATCHED")
		else:
			print(e)

