import json
def read():
        global db
        with open('db.json', 'r') as openfile:
                db = json.load(openfile)

read()

for i in db:
	ttime = db[i]

	hours = ttime//60//60 ; ttime = ttime - hours*60*60
	minutes = ttime//60 ; ttime = ttime - minutes*60
	seconds = ttime

	print(f'{i} >> {hours}:{minutes}:{seconds}')
