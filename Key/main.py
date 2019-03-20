import subprocess
import RPi.GPIO as GPIO
import time
import socket
GPIO.setmode(GPIO.BCM)
flag = True
out3 = 4
out4 = 17
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(out3,GPIO.IN)
def open():
    for i in range(0,50,1):
        servo1.ChangeDutyCycle(7.5-i/10)
        servo2.ChangeDutyCycle(7.5-i/10)
        time.sleep(0.01)
    servo1.start(0)
    servo2.start(0)
def close():
    for i in range(0,50,1):
        servo1.ChangeDutyCycle(2.5+i/10)
        servo2.ChangeDutyCycle(2.5+i/10)
        time.sleep(0.01)
    servo1.start(0)
    servo2.start(0)
try:
    while True:
        if GPIO.input(out3) == GPIO.HIGH and not flag:
            subprocess.call("sudo python3 open.py",shell=True)
            flag = not flag
        elif GPIO.input(out3) == GPIO.HIGH and flag:
            subprocess.call("sudo python3 close.py",shell=True)
            flag = not flag
except KeyboardInterrupt:
    pass

