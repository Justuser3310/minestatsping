from dash import Dash, html, dcc, Input, Output, callback
import plotly.graph_objs as go

from time import strftime, localtime

from db import *

from func import stat_exist
from datetime import datetime
now = datetime.now

app = Dash(__name__)

app.layout = html.Div([

	html.Div([
		dcc.Dropdown(["Сервер", "Игроки"], "Сервер", id = "select", clearable=False, searchable=False, style = {"flex": 70}),
		dcc.Dropdown(id = "date", clearable=True, searchable=False, style = {"flex": 30}, placeholder="Дата"),
	], style = {"display": "flex", "flexDirection": "row"}),

	html.Div([], id = "out")

])


def server(date = None):
	if not date:
		date = now().strftime("%Y-%m-%d")
	stat_exist(date)
	db = read(f'data/{date}.json')

	# Настройка для графика без рамок
	layout = go.Layout( margin=go.layout.Margin(l=0, r=0, b=0, t=0,), height = 300 )

	ping = db["ping"]
	ping_fig = go.Figure(data=[go.Scatter(x = ping["time"], y = ping["ms"] )], layout = layout )
	#ping_fig.update_xaxes(visible=False)
	ping_fig.update_traces(hoverinfo='y')
	#ping_fig.update_layout(yaxis=dict(dtick=1))

	online = db["online"]
	online_fig = go.Figure(data=[go.Scatter(x = online["time"], y = online["count"] )], layout = layout)
	#online_fig.update_xaxes(visible=False)
	online_fig.update_traces(hoverinfo='y')
	online_fig.update_layout(yaxis=dict(dtick=1))

	gr_conf = {"displayModeBar": False, "showAxisDragHandles": False, "showAxisRangeEntryBoxes": False, "fillFrame": False}
	return html.Div([
		html.H2("Пинг"),
		dcc.Graph(
				id = 'ping',
				figure = ping_fig,
				config = gr_conf
  ),
		html.H2("Онлайн"),
		dcc.Graph(
				id = 'online',
				figure = online_fig,
				config = gr_conf
		)
	])


def players():
	db = read('data/stat.json')

	layout = go.Layout( margin=go.layout.Margin(l=0, r=0, b=0, t=0,), height = 300 )

	time = db["players"]["time"]
	# Конвертируем в вид ["hythe", "freedom"] и [1764, 6532]
	time_nick = list(time.keys())
	time_time = list(time.values())
	# Сортируем по времени (3, 2, 1)
	sorted = False
	while not sorted:
		sorted = True
		for i in range(len(time_time) - 1):
			# Если [5, 7] => [7, 5]
			if time_time[i + 1] > time_time[i]:
				sorted = False
				# Меняем местами
				time_time[i], time_time[i + 1] = time_time[i + 1], time_time[i]
				time_nick[i], time_nick[i + 1] = time_nick[i + 1], time_nick[i]

	# Конвертируем 12960 => 3:36
	conv_time = []
	for i in range(len(time_time)):
		seconds = time_time[i]
		hours = seconds // 3600
		minutes = (seconds-hours*3600) // 60

		conv_time.append(f"Время: {hours} час. {minutes} мин.")

	time_fig = go.Figure(data=[go.Bar(x = time_nick, y = time_time, hovertemplate=conv_time, name="",
																		text=conv_time, textposition='inside', insidetextfont=dict(size=16, color='white')
																		)], layout = layout )
	time_fig.update_yaxes(visible=False)
	#time_fig.update_xaxes(visible=False)
	time_fig.update_xaxes({"tickfont": {"size": 18} })
	time_fig.update_traces(hoverinfo='y')

	last = db["players"]["last"]
	# Конвертируем в вид ["hythe"] и [1434657.567523]
	last_nick = list(last.keys())
	last_time = list(last.values())
	# Сортируем по времени (3, 2, 1)
	# Сортируем по времени
	sorted = False
	while not sorted:
		sorted = True
		for i in range(len(last_time) - 1):
			# Если [5, 7] => [7, 5]
			if float(last_time[i + 1]) > float(last_time[i]):
				sorted = False
				# Меняем местами
				last_time[i], last_time[i + 1] = last_time[i + 1], last_time[i]
				last_nick[i], last_nick[i + 1] = last_nick[i + 1], last_nick[i]

	# Конвертируем 1709475944.625857 => '2012-09-13 02:22:50'
	for i in range(len(last_time)):
		last_time[i] = strftime('%Y-%m-%d %H:%M:%S', localtime( float(last_time[i]) ))

	last_fig = go.Figure(data= [go.Table(header={"values": ["Игрок","Время захода"], "font": {"size": 18}, "height": 40},
																							cells={"values": [last_nick, last_time], "font_size": 18, "height": 30},
																							) ], layout = layout )

	gr_conf = {"displayModeBar": False, "showAxisDragHandles": False, "showAxisRangeEntryBoxes": False, "fillFrame": False}
	return html.Div([
		html.H2("Топ по времени"),
		dcc.Graph(
				id = 'ping',
				figure = time_fig,
				config = gr_conf
		),
		html.H2("Последний заход"),
		dcc.Graph(
			id = 'ping',
			figure = last_fig,
			config = gr_conf
		)
	])



def av_stats():
	raw = sorted( next(os.walk('data/'), (None, None, []))[2] )
	# Убираем .json
	dates = []
	for i in raw:
		if i != "stat.json":
			dates.append(i[:i.find(".json")])

	return dates

@callback(
	Output('out', 'children'),
	Output('date', 'options'),
	Input('date', 'value'),
	Input('select', 'value'),
)
def main(date, select):
	if select == "Сервер":
		return server(date), av_stats()
	elif select == "Игроки":
		return players(), av_stats()

while True:
	try:
		app.run(debug=False)
	except KeyboardInterrupt:
		exit()
	except:
		pass
