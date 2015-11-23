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
url = "https://www.followmee.com/api/tracks.aspx?key=fe26a8c25f3235fb56b041665c80f363&username=scottmont&output=json&function=currentforalldevices"
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
	if int(curlocation) > int(locationd):
		oldlocation = curlocation
		move = int(curlocation) - int(locationd)
		curlocation = int(curlocation) - int(move)
		screen.addstr(21, 4, "scott arm from %d to %d\n " % (oldlocation, curlocation))
		screen.addstr(22, 4,  "scott arm %d Microsteps BACKWARD to %d\n"  % (move, curlocation))
		myStepper1.step( int(move), Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
		turnOffMotors()
	elif int(curlocation) < int(locationd):
		oldlocation = curlocation
		move = int(locationd) - int(curlocation)
		curlocation = int(oldlocation) + int(move)
		screen.addstr(21, 4, "scott arm from %s to %s\n" % (oldlocation, curlocation))
		screen.addstr(22, 4, "scott arm %s Microsteps FOREWARD to %s\n"  % (move, curlocation))
          	myStepper1.step( int(move), Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
		turnOffMotors()
	else:
		screen.addstr(15, 4, "scott lat,long %f,%f and stepper %d\n" % (latit,longt,curlocation))
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
        if int(curlocation2) > int(locationd):
                oldlocation = curlocation2
                move = int(curlocation2) - int(locationd)
                curlocation2 = int(curlocation2) - int(move)
		screen.addstr(22, 4, "juliana arm from %d to %d\n " % (oldlocation, curlocation2))
                screen.addstr(23, 4, "juliana arm %d Microsteps BACKWARD to %d\n"  % (move, curlocation2))
                myStepper2.step( int(move), Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        elif int(curlocation2) < int(locationd):
                oldlocation = curlocation2
                move = int(locationd) - int(curlocation2)
                curlocation2 = int(oldlocation) + int(move)
		screen.addstr(22, 4, "juliana arm from %s to %s\n" % (oldlocation, curlocation2))
                screen.addstr(23, 4, "juliana arm %s Microsteps FOREWARD to %s\n"  % (move, curlocation2))
                myStepper2.step( int(move), Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        else:
		screen.addstr(16, 4, "juliana lat,long %f,%f and stepper %d\n" % (jlatit,jlongt,curlocation2))
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
        if int(curlocation3) > int(locationd):
                oldlocation = curlocation3
                move = int(curlocation3) - int(locationd)
                curlocation3 = int(curlocation3) - int(move)
		screen.addstr(24, 4, "maxim arm from %d to %d\n " % (oldlocation, curlocation3))
                screen.addstr(25, 4, "maxim arm %d Microsteps BACKWARD to %s\n"  % (move, curlocation3))
                myStepper2.step( int(move), Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        elif int(curlocation3) < int(locationd):
                oldlocation = curlocation3
                move = int(locationd) - int(curlocation3)
                curlocation3 = int(oldlocation) + int(move)
		screen.addstr(24, 4, "maxim arm from %s to %s\n" % (oldlocation, curlocation3))
                screen.addstr(25, 4, "maxim arm %s Microsteps FOREWARD to %s\n"  % (move, curlocation3))
                myStepper2.step( int(move), Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        else:
		screen.addstr(17, 4, "maxim lat,long %f,%f and stepper %d\n" % (mlatit,mlongt,curlocation3))
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
		screen.addstr(2, 50, "Clock has been started")
		screen.addstr(4, 50, "----------------")
		screen.addstr(8, 50, "----------------")
		screen.addstr(13, 4, "Current Latitute Longitute and stepper location")
		screen.addstr(14, 4, "-----------------------------------------------------")
		screen.addstr(19, 4, "Last moves on the Clock")
                screen.addstr(20, 4, "-----------------------------------------------------")
		# Where is Scott?
		if 43.6358 <= float(latit) <= 43.6378 and -79.4185 >= float(longt) >= -79.4248 :
			newlocation = 100
        		screen.addstr(5, 50, "scott at work\n" )
			motor1thread = threading.Thread(target=motor1)
			motor1thread.start()
		elif 43.6760 <= float(latit) <= 43.6769 and -79.3425 >= float(longt) >= -79.3439 :
			newlocation = 50
        		screen.addstr(5, 50, "scott at home" )
			motor1thread = threading.Thread(target=motor1)
                        motor1thread.start()
		else:
        		screen.addstr(5, 50, "dunno where scott is %f %f" % (latit, longt))
			newlocation = 200
			motor1thread = threading.Thread(target=motor1)
                        motor1thread.start()
		# Where is Juliana?
		if 43.6909 <= float(jlatit) <= 43.6936 and -79.3315 >= float(jlongt) >= -79.3344 :
			newlocation2 = 100
                        screen.addstr(8, 50, "juliana at work" )
                        motor2thread = threading.Thread(target=motor2)
                        motor2thread.start()
		elif 43.6760 <= float(jlatit) <= 43.6769 and -79.3425 >= float(jlongt) >= -79.3439 :
			newlocation2 = 50
                        screen.addstr(6, 50, "juliana at home")
                        motor2thread = threading.Thread(target=motor2)
                        motor2thread.start()
		elif 43.6781 <= float(jlatit) <= 43.6786 and -79.34619 >= float(jlongt) >= -79.34751 :
			newlocation2 = 75 
                        screen.addstr(6, 50, "juliana at daycare") 
                        motor2thread = threading.Thread(target=motor2)
                        motor2thread.start()
		else:
        		screen.addstr(6, 50, "dunno where juliana is  %f %f\n " % (jlatit, jlongt))
			newlocation2 = 200
                        motor1thread = threading.Thread(target=motor2)
                        motor1thread.start()
		# Where is Maxim?
		if 43.6909 <= float(mlatit) <= 43.6936 and -79.3315 >= float(mlongt) >= -79.3344 :
			newlocation3 = 100
                        screen.addstr(7, 50, "maxim at school" )
                        motor3thread = threading.Thread(target=motor3)
                        motor3thread.start()
		elif 43.6760 <= float(mlatit) <= 43.6769 and -79.3425 >= float(mlongt) >= -79.3439 :
			newlocation3 = 50 
                        screen.addstr(7, 50, "maxim at home" )
                        motor3thread = threading.Thread(target=motor3)
                        motor3thread.start()
		else:
			newlocation3 = 200
                        screen.addstr(7, 50, "dunno where maxim is %f %f\n" % (mlatit, mlongt))
                        motor3thread = threading.Thread(target=motor3)
                        motor3thread.start()
		screen.addstr(2, 4, time.strftime("%a, %d %b %Y %H:%M"))
		screen.refresh()
		time.sleep(10)

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input
def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print ""
     if a == 0:
          print "Command executed correctly"
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     print ""
x = 0
fthread = 0
class StopThread(StopIteration):
    pass

threading.SystemExit = SystemExit, StopThread
class finderthread(threading.Thread):
	def _bootstrap(self, stop_thread=False):
          def stop():
            nonlocal stop_thread
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
        exit()

curses.endwin()
