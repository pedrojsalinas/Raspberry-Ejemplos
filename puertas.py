import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def on_pushdown(channel):
    print ("Button Pushed.")

# only add the detection call once!
GPIO.add_event_detect(5, GPIO.RISING, callback=on_pushdown, bouncetime=200)

while(True):
    try:
        # do any other processing, while waiting for the edge detection
        time.sleep(1) # sleep 1 sec
    finally:
        GPIO.cleanup()
