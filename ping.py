from mctools import PINGClient
ping = PINGClient('135.181.170.94',25630)
#stats = ping.get_stats()

#Get home dir
from subprocess import getoutput
global home
home = getoutput("echo $HOME")

#Work with JSON
import json
def read():
	global db, home
	with open(f'{home}/db.json', 'r') as openfile:
		db = json.load(openfile)
def write():
	global db
	js = json.dumps(db, indent=4)
	with open(f'{home}/db.json', 'w') as outfile:
		outfile.write(js)

#My libraries
from time import sleep

#Read
read()

ttime = 0
while True:
	sleep(1)

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
		ping = PINGClient('135.181.170.94',25630)
		print(e)

