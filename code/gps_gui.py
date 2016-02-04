import serial
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# TO DO: add error handling 

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
        
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

def data_gen(t=0):
    while True:
        line = s.readline()
        args = line.split(',')
        if args[0] == '$GPRMC':
            data = GPRMC(args)
            print 'Time:', data.time, 'Date:',  data.date, 'Status:', data.nav
            print 'Speed:', data.speed, 'Lat:', data.lat, data.lat_NS, 'Long:', data.long, data.long_EW
            print '----------------'
            # write to csv
            w.writerow([data.time, data.date, data.lat + data.lat_NS, data.long + data.long_EW])  
            t += 1
            yield data.speed, t
    
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
    repeat=False, init_func=init)
    