#!/usr/bin/env python

import sensorLoggers
import json
# Configuring our i2c addresses:
ADDRESS_ADS1115 = 0x48
ADDRESS_BMP180 = 0x77


def readData( accel, magnetometer, gyroscope, barometer, filename ):
	outData = dict()
	outData['accelX'] = accel.readX()
	outData['accelY'] = accel.readY()
	outData['accelZ'] = accel.readZ()
	outData['magnetometerX'], outData['magnetometerY'], outData['magnetometerZ'] = magnetometer.read()
	outData['gyroX'] = gyroscope.readX()
	outData['gyroY'] = gyroscope.readY()
	outData['gyroZ'] = gyroscope.readZ()
	outData['pressure'] = barometer.read()

	return outData




# start er' up
if ( __name__ == "__main__" ):
	accel = sensorLoggers.Accelerometer()
	magnetometer = sensorLoggers.Magnetometer()
	gyroscope = sensorLoggers.Gyroscope()
	barometer = sensorLoggers.Barometer()
	while True:
		outData = readData( accel, magnetometer, gyroscope, barometer )
		print( json.dumps( outData ) )
