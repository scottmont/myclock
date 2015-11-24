from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import sys
import urllib,json
import time
import atexit
import threading
import curses
from os import system
sys.stdout = open('myclock.log', 'w')
global curlocation,curlocation2,curlocation3
from apikey import *
mh = Adafruit_MotorHAT()

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def calib():
    myStepper1 = mh.getStepper(200, 1)
    myStepper1.setSpeed(1)
    myStepper1.step( 20, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

def motor1():
    while True:
        myStepper1 = mh.getStepper(200, 1) 
        myStepper1.setSpeed(1)                  
        global curlocation
        try:
            curlocation
        except NameError:
            curlocation = 0
        locationd = newlocation
        times = time.strftime('%H:%M:%S')
        if int(curlocation) > int(locationd):
            oldlocation = curlocation
            move = int(curlocation) - int(locationd)
            curlocation = int(curlocation) - int(move)
            screen.addstr(21, 4, "%s : %s arm from %d to %d" % (times, user1, oldlocation, curlocation))
            screen.addstr(22, 4, "%s : %s arm %d Microsteps BACKWARD to %d\n"  % (times, user1, move, curlocation))
            myStepper1.step( int(move), Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
            turnOffMotors()
        elif int(curlocation) < int(locationd):
            oldlocation = curlocation
            move = int(locationd) - int(curlocation)
            curlocation = int(oldlocation) + int(move)
            screen.addstr(21, 4, "%s : %s arm from %s to %s" % (times, user1, oldlocation, curlocation))
            screen.addstr(22, 4, "%s : %s arm %s Microsteps FOREWARD to %s"  % (times, user1, move, curlocation))
            myStepper1.step( int(move), Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
            turnOffMotors()
        else:
            screen.addstr(15, 4, "%s lat,long %f,%f and stepper %d\n" % (user1, latit,longt,curlocation))
        return
def motor2():
    while True:
        myStepper2 = mh.getStepper(200, 2)
        myStepper2.setSpeed(1)
        global curlocation2
        try:
            curlocation2
        except NameError:
            curlocation2 = 0
        locationd = newlocation2
        timej = time.strftime('%H:%M:%S')
        if int(curlocation2) > int(locationd):
                oldlocation = curlocation2
                move = int(curlocation2) - int(locationd)
                curlocation2 = int(curlocation2) - int(move)
                screen.addstr(23, 4, "%s : %s arm from %d to %d\n " % (timej, user2, oldlocation, curlocation2))
                screen.addstr(24, 4, "%s : %s arm %d Microsteps BACKWARD to %d\n"  % (timej, user2, move, curlocation2))
                myStepper2.step( int(move), Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        elif int(curlocation2) < int(locationd):
                oldlocation = curlocation2
                move = int(locationd) - int(curlocation2)
                curlocation2 = int(oldlocation) + int(move)
                screen.addstr(23, 4, "%s : %s arm from %s to %s\n" % (timej, user2, oldlocation, curlocation2))
                screen.addstr(24, 4, "%s : %s arm %s Microsteps FOREWARD to %s\n"  % (timej, user2, move, curlocation2))
                myStepper2.step( int(move), Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        else:
            screen.addstr(16, 4, "%s lat,long %f,%f and stepper %d\n" % (user2,jlatit,jlongt,curlocation2))
        return
def motor3():
    while True:
        myStepper2 = mh.getStepper(200, 2)
        myStepper2.setSpeed(1)
        global curlocation3
        try:
            curlocation3
        except NameError:
                curlocation3 = 0
        locationd = newlocation3
        timem = time.strftime('%H:%M:%S')
        if int(curlocation3) > int(locationd):
                oldlocation = curlocation3
                move = int(curlocation3) - int(locationd)
                curlocation3 = int(curlocation3) - int(move)
                screen.addstr(25, 4, "%s : %s arm from %d to %d\n " % (timem, user3, oldlocation, curlocation3))
                screen.addstr(26, 4, "%s : %s arm %d Microsteps BACKWARD to %s\n"  % (timem, user3, move, curlocation3))
                myStepper2.step( int(move), Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        elif int(curlocation3) < int(locationd):
                oldlocation = curlocation3
                move = int(locationd) - int(curlocation3)
                curlocation3 = int(oldlocation) + int(move)
                screen.addstr(25, 4, "%s : %s arm from %s to %s\n" % (timem, user3, oldlocation, curlocation3))
                screen.addstr(26, 4, "%s : %s arm %s Microsteps FOREWARD to %s\n"  % (timem, user3, move, curlocation3))
                myStepper2.step( int(move), Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        else:
            screen.addstr(17, 4, "%s lat,long %f,%f and stepper %d\n" % (user3,mlatit,mlongt,curlocation3))
            return
def finder():
    while True:
        global latit,longt,jlatit,jlongt,mlongt,mlatit
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        latit = data['Data'][0]['Latitude']
        longt = data['Data'][0]['Longitude']
        jlatit = data['Data'][1]['Latitude']
        jlongt = data['Data'][1]['Longitude']
        mlatit = data['Data'][2]['Latitude']
        mlongt = data['Data'][2]['Longitude']
        global newlocation,newlocation2,newlocation3
        screen.addstr(2, 40, "Clock has been started")
        screen.addstr(4, 40, "----------------")
        screen.addstr(8, 40, "----------------")
        screen.addstr(13, 4, "Current Latitute Longitute and stepper location")
        screen.addstr(14, 4, "-----------------------------------------------------")
        screen.addstr(19, 4, "Last moves on the Clock")
        screen.addstr(20, 4, "-----------------------------------------------------")
        #Where are the Users?
        for i in user1locat:
		if float(i[2]) <= float(latit) <= float(i[3]) and float(i[4]) >= float(longt) >= float(i[5]):
			newlocation = int(i[1])
                	screen.addstr(7, 40, "%s at %s" %(user1, i[0]))
                	motor1thread = threading.Thread(target=motor1)
                	motor1thread.start()
		else:
               		screen.addstr(5, 40, "%s is at an unknown location %f %f\n" % (user1, latit, longt))
              		newlocation = 200
               		motor1thread = threading.Thread(target=motor1)
               		motor1thread.start()
        screen.addstr(2, 4, time.strftime("%a, %d %b %Y %H:%M"))
        screen.refresh()
        time.sleep(10)

x = 0
fthread = 0
class StopThread(StopIteration):
    pass

threading.SystemExit = SystemExit, StopThread
class finderthread(threading.Thread):
    def _bootstrap(self, stop_thread=False):
        def stop():
            stop_thread = True
            self.stop = stop
        def tracer(*_):
            if stop_thread:
                raise StopThread()
            return tracer
        sys.settrace(tracer)
        super()._bootstrap()
while x != ord('4'):
     screen = curses.initscr()

     screen.clear()
     screen.border(0)
     screen.addstr(2, 4, time.strftime("%a, %d %b %Y %H:%M"))
     screen.addstr(4, 4, "1 - Start the Clock")
     screen.addstr(5, 4, "2 - Reload")
     screen.addstr(6, 4, "3 - Update stats")
     screen.addstr(7, 4, "4 - Exit")
     screen.refresh()

     x = screen.getch()

     if x == ord('1'):
            finderthread = threading.Thread(target=finder)
            finderthread.start()
     if x == ord('4'):
        curses.endwin()
        finderthread.stop()
        finderthread.join()
        exit()
curses.endwin()

