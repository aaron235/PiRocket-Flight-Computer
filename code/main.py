#!/usr/bin/env python

# Our Adafruit I2C ADC library, for superior 16-bit resolution:
from Adafruit_ADS1x15.Adafruit_ADS1x15 import ADS1x15
# Our library to handle our BMP180 altimeter:
# import Adafruit_BMP.BMP as BMP

# Configuring our i2c addresses:
ADDRESS_ADS1115 = 0x48
ADDRESS_BMP180 = 0x77

# Our calibrated zero values for the accelerometer:
xZero = 1657.8712
yZero = 1660.7111
zZero = 1659.3377
# And, our calibrated scale factors for the accelerometer:
xScale = 7.126831
yScale = 7.286181
zScale = 7.271006
# Number of digits to round to for g-force data:
gForcePrecision = 5


def setup():
	# Create an ADC instance at the preconfigured address using the ADS1115 settting (our ADC)
	global accelADC
	accelADC = ADS1x15( address=ADDRESS_ADS1115, ic=ADS1x15._ADS1x15__IC_ADS11155 )


def main():
	output = open('output.txt', 'ab+')
	while True:
		pickle.dump(mapData(), output)
		


def mapData():
	xAccel = getXAccel()
	yAccel = getYAccel()
	zAccel = getZAccel()
	time = getTime()
	data = dict('xData':(xAccel, time), 'yData':(yAccel, time), 'zData':(zAccel, time))
	return data

def getXAccel():
	xRaw = accelADC.readADCSingleEnded( channel=1, pga=4096, sps=50 )
	xAdj = round( ( ( xRaw - xZero ) / xScale ), gForcePrecision )
	return xAdj


def getYAccel():
	yRaw = accelADC.readADCSingleEnded( channel=2, pga=4096, sps=50 )
	yAdj = round( ( ( yRaw - yZero ) / yScale ), gForcePrecision )
	return yAdj


def getZAccel():
	zRaw = accelADC.readADCSingleEnded( channel=3, pga=4096, sps=50 )
	zAdj = round( ( ( zRaw - zZero ) / zScale ), gForcePrecision )
	return zAdj

# start er' up
if ( __name__ == "__main__" ):
	setup()
	main()
