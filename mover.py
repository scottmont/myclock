from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import urllib,json
import time
import atexit
url = "https://www.followmee.com/api/tracks.aspx?key=fe26a8c25f3235fb56b041665c80f363&username=scottmont&output=json&function=currentforalldevices"
mh = Adafruit_MotorHAT()
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

print('The Clock')

myStepper = mh.getStepper(200, 1)       # 200 steps/rev, motor port #1
myStepper.setSpeed(1)                  # 30 RPM


def calib():
        myStepper.step( 250, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
def park():
        myStepper.step( 75, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
        myStepper.step( 75, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

def main():
    while True:
        myStepper.setSpeed(1)
        try:
                curlocation
        except NameError:
        	curlocation = raw_input('Where are you?') 
	locationd = raw_input('Where to?')
        if int(curlocation) > int(locationd):
                oldlocation = curlocation
                move = int(curlocation) - int(locationd)
                curlocation = int(curlocation) - int(move)
                print ( 'moving from', oldlocation, 'to location ', curlocation )
                print ( move, ' Microsteps BACKWARD to ' , curlocation )
                myStepper.step( int(move), Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        elif int(curlocation) < int(locationd):
                oldlocation = curlocation
                move = int(locationd) - int(curlocation)
                curlocation = int(oldlocation) + int(move)
                print ( 'moving from', oldlocation, 'to location ', curlocation )
                print ( move, ' Microsteps FORWARD to ' , curlocation )
                myStepper.step( int(move), Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                turnOffMotors()
        else:
                print ' You are already here '
main()
