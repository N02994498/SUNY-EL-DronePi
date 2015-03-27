class Gps(object):
	"""docstring for Gps"""
	def read(self):
		# temporary mock
		gpsData = {}
		gpsData['latitude'] = '-33/1,66/1,451/100'
		gpsData['longitude'] = '5/1,10/1,15/100'
		gpsData['altitude'] = '71'
		return gpsData
