import subprocess
import RPi.GPIO as GPIO
import time
import socket
GPIO.setmode(GPIO.BCM)
flag = True
IN = 10
GPIO.setup(IN,GPIO.IN)
try:
    while True:
        if GPIO.input(IN) == GPIO.HIGH and not flag:
            subprocess.call("sudo python3 open.py",shell=True)
            flag = not flag
        elif GPIO.input(IN) == GPIO.HIGH and flag:
            subprocess.call("sudo python3 close.py",shell=True)
            flag = not flag
except KeyboardInterrupt:
    pass

