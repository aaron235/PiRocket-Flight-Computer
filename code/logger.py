import datetime
import csv

import Adafruit_BMP.BMP085 as BMP085
# import Adafruit_ADXL.ADXL377 as ADXL377
# import UltimateGPS


def init():
	global barometer = BMP085.BMP085()
	# global accelerometer = ADXL377.ADXL377()
	global data_writer = csv.writer(open('rocketpi_data.csv', 'w'), delimiter = ',', lineterminator = '\n')


def read():
	data = dict()
	data['Timestamp' = datetime.datetime.now() #fix this - pi0 does not have
	data['Temperature'] = barometer.read_temperature()
	data['Pressure'] = barometer.read_pressure()
	data['Altitude'] = barometer.read_altitude()
	data['Sealevel Pressure'] = barometer.read_sealevel_pressure()
	#add reading from ADXL here
	return data


def save(data):
	row = ''
	for key, value in data:
		row = row + key + ',' + value + ','

	row = row[:-1] #remove last comma from string
	data_writer.writerow(row)

def run():
	while True:
		data = read()
		save(data)

init()
run()
