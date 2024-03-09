from mctools import PINGClient
from time import sleep, time

from datetime import datetime
now = datetime.now

host = 'CoolFunZone.aternos.me'
port = 36413
# 764 - 1.20.2
prot = 764
global c
c = PINGClient(host, port, proto_num = prot)

from db import *
from func import *

date = now().strftime("%Y-%m-%d")
# Проверяем существует ли
stat_exist(date)
db = read(f'data/{date}.json')

# КАК ЧАСТО ОБНОВЛЯЕМ (секунды)
update = 60

while True:
	try:
		raw = c.get_stats()
		ms = round( c.ping() ) # Пинг
	except:
		c.stop()
		c = PINGClient(host, port, proto_num = prot)
		continue

	if "sample" in raw["players"]:
		# Список игроков
		players_raw = raw["players"]["sample"]
		# Оставляем только ники (без айди)
		players = []
		for i in players_raw:
			players.append(i[0][:i[0].find('[')])
		# Онлайн
		online = raw["players"]["online"]
	else:
		players = []
		online = 0

	# Фикс атерноса
	max = raw["players"]["max"]
	if max == 0:
		ms = 0

	# Открываем БД.
	# Дата
	date = now().strftime("%Y-%m-%d")
	# Проверяем существует ли
	stat_exist(date)
	db = read(f'data/{date}.json')

	# Заполняем БД
	# Пинг
	db["ping"]["time"].append( now().strftime('%H:%M') )
	db["ping"]["ms"].append( ms )
	# Онлайн
	db["online"]["time"].append( now().strftime('%H:%M') )
	db["online"]["count"].append( online )


	# Топ игроков по времени и последнее время захода
	stat = read('data/stat.json')
	# Перебираем игроков
	for i in players:
		# Если игрок уже в базе
		if i in stat["players"]["time"]:
			stat["players"]["time"][i] += update
		else:
			stat["players"]["time"][i] = update
		# Время захода
		stat["players"]["last"][i] = time()


	# Записываем изменения
	write(db, f'data/{date}.json')

	write(stat, 'data/stat.json')

	# Задержка
	sleep(update)
