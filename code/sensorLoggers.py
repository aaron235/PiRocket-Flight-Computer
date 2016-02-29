import csv

from lib.Adafruit_Python_BMP.Adafruit_BMP.BMP085 import BMP085 as BMP085
from lib.Adafruit_Raspberry_Pi_Python_Code.Adafruit_ADS1x15.Adafruit_ADS1x15 import ADS1x15 as ADS1115
from lib.hmc5883l.hmc5883l import hmc5883l as HMC5883L
from lib.Gyro_L3GD20_Python.L3GD20 import L3GD20 as L3GD20

# L3GD20 is dependent on the following 3rd-party libraries (not included on github):
# numpy, smbus

# import Adafruit_ADXL.ADXL377 as ADXL377
# import UltimateGPS

# TO DO: finish read() of missing components

class Barometer( object ):
	def __init__( self, mode ):
		self.sensor = BMP085( mode )

	def read( self ):
		baroData = dict()
		baroData['Temperature'] = self.sensor.read_temperature()
		baroData['Pressure'] = self.sensor.read_pressure()
		baroData['Altitude'] = self.sensor.read_altitude()
		baroData['Sealevel Pressure'] = self.sensor.read_sealevel_pressure()
		return baroData

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

	def readX( self ):
		xRaw = self.sensor.readADCSingleEnded( channel=1, pga=4096, sps=200 )
		xAdj = round( ( ( xRaw - self.xZero ) / self.xScale ), self.gForcePrecision )
		return xAdj

	def readY( self ):
		xRaw = self.sensor.readADCSingleEnded( channel=1, pga=4096, sps=200 )
		xAdj = round( ( ( xRaw - self.xZero ) / self.xScale ), self.gForcePrecision )
		return xAdj

	def readZ( self ):
		xRaw = self.sensor.readADCSingleEnded( channel=1, pga=2048, sps=200 )
		xAdj = round( ( ( xRaw - self.xZero ) / self.xScale ), self.gForcePrecision )
		return xAdj

	def read( self ):
		accelData = dict()
		accelData['X Accel'] = readX()
		accelData['Y Accel'] = readY()
		accelData['Z Accel'] = readZ()
		return accelData

class Gyroscope( object ):
	def __init__( self ):
		self.sensor = L3GD20(busId=1, slaveAddr=0x6b, ifLog=False, ifWriteBlock=False)
		self.sensor.Set_PowerMode('Normal')
		self.sensor.Set_FullScale_Value('2000dps')
		self.sensor.Set_AxisX_Enabled(True)
		self.sensor.Set_AxisY_Enabled(True)
		self.sensor.Set_AxisZ_Enabled(True)
		self.sensor.Init()
		self.sensor.Calibrate()

	def readX( self ):
		return self.sensor.Get_CalOutX_Value()

	def readY( self ):
		return self.sensor.Get_CalOutY_Value()

	def readZ( self ):
		self.sensor.Get_CalOutZ_Value()


class Magnetometer( object ):
	def __init__( self ):
		self.sensor = HMC5883L()

	def read( self ):
		return self.sensor.axes()

