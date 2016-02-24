#!/usr/bin/env python

# Our Adafruit I2C ADC library, for superior 16-bit resolution:
from Adafruit_ADS1x15.Adafruit_ADS1x15 import ADS1x15
# Our library to handle our BMP180 altimeter:
# import Adafruit_BMP.BMP as BMP
import sensorLoggers

# Configuring our i2c addresses:
ADDRESS_ADS1115 = 0x48
ADDRESS_BMP180 = 0x77


def main():
	while True:
		


# start er' up
if ( __name__ == "__main__" ):
	accel = sensorLoggers.Accelerometer()
	main()
