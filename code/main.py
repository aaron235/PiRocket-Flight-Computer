#!/usr/bin/env python
from time import time
import sensorLoggers
import json
# Configuring our i2c addresses:
ADDRESS_ADS1115 = 0x48
ADDRESS_BMP180 = 0x77

accelData = []
def readData( accel, magnetometer, gyroscope, barometer ):
	outData = dict()
	outData['accelX'] = accel.readX()
	outData['accelY'] = accel.readY()
	outData['accelZ'] = accel.readZ()
	outData['magnetometerX'], outData['magnetometerY'], outData['magnetometerZ'] = magnetometer.read()
	outData['gyroX'] = gyroscope.readX()
	outData['gyroY'] = gyroscope.readY()
	outData['gyroZ'] = gyroscope.readZ()
	#outData['pressure'] = barometer.read()

	return outData


# start er' up
if ( __name__ == "__main__" ):
	accel = sensorLoggers.Accelerometer()
	magnetometer = sensorLoggers.Magnetometer()
	gyroscope = sensorLoggers.Gyroscope()
	barometer = None #sensorLoggers.Barometer()
	while True:
		curTime = int( time() * 1000 )	
		outData = readData( accel, magnetometer, gyroscope, barometer )
		curData = { curTime: outData }
		print( curData )
		with open( 'flight.log', 'a' ) as f:
			f.write( json.dumps( curData ) )

		accelData.append( {
			'accelX': outData['accelX'],
			'accelY': outData['accelY'],
			'accelZ': outData['accelZ']
			} )
