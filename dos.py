#ONLY FOR HOME USING!!!
#NO PROXY
#NO NULLPING

from mctools import PINGClient
#ping = PINGClient('play.dmcraft.online')
ping = PINGClient('127.0.0.1')

#My libraries
from time import sleep



needsleep = 0
while True:
    sleep(0.001)
    ping.get_stats()
    #print('Ping')
