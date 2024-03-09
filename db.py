import os
import json

if not os.path.exists('config.json'):
	db = {}
	js = json.dumps(db, indent=2)
	with open("config.json", "w") as outfile:
		outfile.write(js)
	print('Created new config.json')
	exit()


def read(file = 'config.json'):
	if not os.path.exists(file):
		with open(file, "w") as f:
			f.write("{}")
		f.close()

	with open(file, "r", encoding="utf-8") as openfile:
		db = json.load(openfile)
	return db

def write(db, file = 'config.json'):
	js = json.dumps(db, indent=2, ensure_ascii=False)
	with open(file, "w", encoding="utf-8") as outfile:
		outfile.write(js)
