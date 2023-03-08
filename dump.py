#Get home dir
from subprocess import getoutput
global home
home = getoutput("echo $HOME")

#Json
import json
def read():
        global db, home
        with open(f'{home}/db.json', 'r') as openfile:
                db = json.load(openfile)



def dump():
	read()
	tmes = ''
	for i in db:
		ttime = db[i]

		hours = ttime//60//60 ; ttime = ttime - hours*60*60
		minutes = ttime//60 ; ttime = ttime - minutes*60
		seconds = ttime

		tmes = tmes + f'{i[:i.find("[")]} >> {hours}:{minutes}:{seconds}'+'<br>'
	return tmes



#Simple server
import tornado.httpserver, tornado.ioloop, tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(dump())
application = tornado.web.Application([
    (r"/", MainHandler),
])
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start() 

