import os
from gps import *
from time import *
import time
import threading

gpsd = None

os.system('clear')

class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd
		gpsd = gps(mode=WATCH_ENABLE)
		self.current_value = None
		self.running = True
	
	def run(self):
		global gpsd
		while gpsp.running:
			gpsd.next()
	def read(self):
                gpsData = {}
                gpsData['latitude'] = gpsd.fix.latitude
                gpsData['longitude'] = gpsd.fix.longitude
                gpsData['altitude'] = gpsd.fix.altitude
                return gpsData


#			time.sleep(2)

	except (KeyboardInterrupt, SystemExit):
		print "\nKilling Thread..."
		gpsp.running = False
		gpsp.join()
		print "Do. \nExiting."
