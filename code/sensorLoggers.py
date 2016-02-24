import datetime
import csv

import lib.Adafruit_Python_BMP.Adafruit_BMP.BMP085.BMP085 as BMP085
import lib.Adafruit-Raspberry-Pi-Python-Code.Adafruit_ADS1x15.ADS1x15 as ADS1115
import lib.Adafruit-Raspberry-Pi-Python-Code.Adafruit_ADS1x15.ADS1x15 as ADS1115
import lib.Adafruit-Raspberry-Pi-Python-Code.Adafruit_ADS1x15.ADS1x15 as ADS1115

# import Adafruit_ADXL.ADXL377 as ADXL377
# import UltimateGPS


class Barmoeter( object ):
	def __init__( self, mode ):
		self.sensor = BMP085( mode )


class Accelerometer( object ):
	def __init__( self ):
		self.sensor = ADS1115()
		# Our calibrated zero values for the accelerometer:
		self.xZero = 1657.8712
		self.yZero = 1660.7111
		self.zZero = 1659.3377
		# And, our calibrated scale factors for the accelerometer:
		self.xScale = 7.126831
		self.yScale = 7.286181
		self.zScale = 7.271006
		# Number of digits to round to for g-force data:
		self.gForcePrecision = 5

	def readX():
		xRaw = self.sensor.readADCSingleEnded( channel=1, pga=4096, sps=200 )
		xAdj = round( ( ( xRaw - self.xZero ) / self.xScale ), self.gForcePrecision )
		return xAdj

	def readY():
		xRaw = self.sensor.readADCSingleEnded( channel=1, pga=4096, sps=200 )
		xAdj = round( ( ( xRaw - self.xZero ) / self.xScale ), self.gForcePrecision )
		return xAdj

	def readZ():
		xRaw = self.sensor.readADCSingleEnded( channel=1, pga=4096, sps=200 )
		xAdj = round( ( ( xRaw - self.xZero ) / self.xScale ), self.gForcePrecision )
		return xAdj


class Gyroscope( object ):
	def __init__( self ):


class Magnetometer( object ):
	def __init__( self ):


def init():
	global barometer = BMP085.BMP085()
	# global accelerometer = ADXL377.ADXL377()
	global data_writer = csv.writer(open('rocketpi_data.csv', 'w'), delimiter = ',', lineterminator = '\n')


def read():
	data = dict()
	data['Timestamp'] = datetime.datetime.now()  # fix this - pi0 does not have
	data['Temperature'] = barometer.read_temperature()
	data['Pressure'] = barometer.read_pressure()
	data['Altitude'] = barometer.read_altitude()
	data['Sealevel Pressure'] = barometer.read_sealevel_pressure()
	# add reading from ADXL here
	return data


def save(data):
	row = ''
	for key, value in data:
		row = row + key + ',' + value + ','

	row = row[:-1]  # remove last comma from string
	data_writer.writerow(row)


def run():
	while True:
		data = read()
		save(data)

init()
run()
