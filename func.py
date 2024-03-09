from db import *
import json
import os

def stat_exist(date):
	if not os.path.exists(f'data/{date}.json'):
		db = {}
		js = json.dumps(db, indent=2)
		with open(f'data/{date}.json', "w") as outfile:
			outfile.write(js)

		# Заполняем БД, если она пустая
		# Пинг
		# "ping": {"time": ["14:30:36", "14:30:41"], "ms": [42, 39]}
		db["ping"] = {"time": [], "ms": []}
		# Онлайн
		# "online": {"time": ["14:30:36", "14:30:41"], "count": [1, 0]}
		db["online"] = {"time": [], "count":[]}

		write(db, f'data/{date}.json')
