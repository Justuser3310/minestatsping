#ONLY FOR HOME USING!!!
#NO PROXY
#NO NULLPING

from mctools import PINGClient

#My libraries
from time import sleep
import threading

def main():
	ping = PINGClient('127.0.0.1', 25577)
	while True:
		sleep(0.00001)
		ping.ping()

for i in range(10000):
	th = threading.Thread(target=main)
	th.start()
