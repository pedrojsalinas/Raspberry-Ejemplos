import RPi.GPIO as GPIO
import time

ledPin = 18
button = 26

def setup():
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(ledPin, GPIO.LOW) # Set ledPin low to off led

def loop():
        while True:
                GPIO.output(ledPin, not GPIO.input(button))  # led on
                time.sleep(.1)


def destroy():
        GPIO.output(ledPin, GPIO.LOW)     # led off
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()

