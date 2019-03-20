import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
flag = True
out1 = 14
out2 = 15
out3 = 4
out4 = 17
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(out3,GPIO.IN)
servo1 = GPIO.PWM(out1, 50)
servo2 = GPIO.PWM(out2, 50)
servo1.start(0)
servo2.start(0)
def close():
    for i in range(0,50,1):
        servo1.ChangeDutyCycle(7.5-i/10)
        servo2.ChangeDutyCycle(7.5-i/10)
        time.sleep(0.01)
    servo1.start(0)
    servo2.start(0)
def open():
    for i in range(0,50,1):
        servo1.ChangeDutyCycle(2.5+i/10)
        servo2.ChangeDutyCycle(2.5+i/10)
        time.sleep(0.01)
    servo1.start(0)
    servo2.start(0)
close()
servo1.stop()
servo2.stop()
GPIO.cleanup()

