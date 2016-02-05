import math
import serial
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GPRMC:
    def __init__(self, args):
        self.time = args[1][:2] + ':' + args[1][2:4] + ':' + args[1][4:6]
        self.date = args[9][:2] + '/' + args[1][2:4] + '/' + args[1][4:6]
        self.nav = args[2]
        
        if self.nav == 'A': 
            self.lat = float(args[3][:2]) + float(args[3][2:])
            self.lat_NS = args[4]
            self.long = float(args[5][:3]) + float(args[5][3:])
            self.long_EW = args[6]
            self.speed = float(args[7]) 
            self.course = float(args[8])            
            self.var = args[10] # Not available with Adafruit Ultimate GPS)
            self.var_EW = args[11] # Not available with Adafruit Ultimate GPS)
        else:
            self.lat = ''
            self.lat_NS = ''
            self.long = ''
            self.long_EW = ''
            self.speed = '' 
            self.course = ''            
            self.var = ''
            self.var_EW = ''
            
        self.checksum = args[12]

s = serial.Serial('COM3', 9600)
w = csv.writer(open('gps_logs.csv', 'w'), delimiter = ',', lineterminator = '\n')        
        
def init():
    ax.set_ylim(0, 10)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

def data_gen(t = 0):
    while True:
        line = s.readline()
        args = line.split(',')
        if args[0] == '$GPRMC':
            data = GPRMC(args)
            print line
            print 'Time:', data.time, 'Date:',  data.date, 'Status:', data.nav
            print 'Speed:', data.speed, 'Lat:', data.lat, data.lat_NS, 'Long:', data.long, data.long_EW
            print 'Course:', data.course
            print '----------------'
            
            # write to csv
            w.writerow([data.time, data.date, data.lat, data.lat_NS, data.long, data.long_EW])  
            t += 1
            yield t, data.speed
    
fig, ax = plt.subplots()
line, = ax.plot([], [], lw = 2)
ax.grid()
xdata, ydata = [], []

def run(data):
    # update the data
    t, speed = data
    xdata.append(t)
    ydata.append(speed)
    xmin, xmax = ax.get_xlim()
    speed_min, speed_max = ax.get_ylim()
    
    if t >= xmax:
        ax.set_xlim(xmin, xmax + 10)
        ax.figure.canvas.draw()
    if speed > speed_max:
        ax.set_ylim(speed_min, speed)
        ax.figure.canvas.draw()
        
    line.set_data(xdata, ydata)

    return line,


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
    repeat=False, init_func=init)

plt.title('Speed vs Time')
plt.xlabel('Time [Seconds]')
plt.ylabel('Speed [Knots]')    
fig.canvas.set_window_title('RocketPi') 
plt.show()
    