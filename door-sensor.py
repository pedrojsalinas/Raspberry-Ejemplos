import RPi.GPIO as GPIO
import time

ledPinRed = 18
ledPinGreen = 12
DOOR_SENSOR_PIN = 5

# Initially we don't know if the door sensor is open or closed...
isOpen = None
oldIsOpen = None

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ledPinRed, GPIO.OUT)
        GPIO.setup(ledPinGreen, GPIO.OUT)
        GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.output(ledPinRed, GPIO.LOW)
        GPIO.output(ledPinGreen, GPIO.LOW)

def loop():
        while True:
            isOpen = GPIO.input(DOOR_SENSOR_PIN)

            if (isOpen and (isOpen != None)):
                print("Space is unoccupied!")
                GPIO.output(ledPinRed, False)
                GPIO.output(ledPinGreen, True)
            elif (isOpen != None):
                print("Space is occupied!")
                GPIO.output(ledPinRed, True)
                GPIO.output(ledPinGreen, False)


            time.sleep(0.1)

def destroy():
        GPIO.output(ledPinRed, GPIO.LOW)     # led off
        GPIO.output(ledPinGreen, GPIO.LOW)     # led off
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()

