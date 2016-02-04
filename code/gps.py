import serial
import csv

class GPRMC:
    def __init__(self, args):
        self.time = args[1].split('.')[0]
        self.nav = args[2]
        self.lat = args[3]
        self.lat_NS = args[4]
        self.long = args[5]
        self.long_EW = args[6]
        self.speed = args[7]
        self.course = args[8]
        self.date = args[9]
        self.var = args[10]
        self.var_EW = args[11]
        self.checksum = args[12]

s = serial.Serial('COM5', 9600)
w = csv.writer(open('gps_logs.csv', 'w'), delimiter = ',', lineterminator = '\n')

while True:
    line = s.readline()
    args = line.split(',')
    if args[0] == '$GPRMC':
        data = GPRMC(args)
        print 'Time:', data.time, 'Date:',  data.date, 'Status:', data.nav
        print 'Speed:', data.speed, 'Lat:', data.lat, data.lat_NS, 'Long:', data.long, data.long_EW
        print '----------------'
        w.writerow([data.time, data.date, data.lat + data.lat_NS, data.long + data.long_EW])
    
s.close()
    