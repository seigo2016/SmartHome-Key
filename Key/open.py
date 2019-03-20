import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
flag = True
out1 = 14
GPIO.setup(out1, GPIO.OUT)
servo1 = GPIO.PWM(out1, 50)
servo1.start(0)
def close():
    for i in range(0,50,1):
        servo1.ChangeDutyCycle(7.5-i/10)
        time.sleep(0.01)
    servo1.start(0)
def open():
    for i in range(0,50,1):
        servo1.ChangeDutyCycle(2.5+i/10)
        time.sleep(0.01)
    servo1.start(0)
open()
servo1.stop()
GPIO.cleanup()

