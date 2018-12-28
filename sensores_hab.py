import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
time_stamp = time.time()

sensores = [5,22]
def verificarSensores():
    for i in sensores:
        GPIO.setup(i, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        if(not GPIO.input(i)):
            print("Pin {} ocupado!".format(i))
        else:
            print("Pin {} libre!".format(i))

verificarSensores()

def PIRcallback(channel):
    print ('Sensor detected: ' + PIR.Name + '\nMotion!')
def REEDcallback(channel):
    print ('Sensor detected!')
def VIBRcallback(channel):
    print ('Sensor detected: ' + VIBR.Name + '\nWindow!')

class Sensor:
    def __init__(self, IO, pin, Name, cb_var):
        self.IO = IO
        self.pin = pin
        self.Name = Name
        self.callback_func = cb_var
        if (IO == 'input'):
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        elif (IO == 'output'):
            GPIO.setup(pin, GPIO.OUT)
        else:
            print ('Error: No input/output declared')
        self.addEvent('Up', 500)
    def addEvent(self, UpDown, btime):
        if (UpDown == 'Up'):
            UpDown = GPIO.RISING
        elif (UpDown == 'Down'):
            UpDown = GPIO.FALLING
        GPIO.add_event_detect(self.pin, UpDown, callback=self.cb, bouncetime=btime)
    def getPin(self):
        return self.pin
    def cb(self,channel):
        global time_stamp
        time_now = time.time()
        if (time_now - time_stamp) >= 0.4:
            if(GPIO.input(self.pin)==1):
                print("{} - Hora salida: {}".format(self.Name,time.strftime("%H:%M:%S",time.localtime(time_now))))
            else:
                print("{} - Hora entrada: {}".format(self.Name,time.strftime("%H:%M:%S",time.localtime(time_now))))
            time_stamp = time_now
            self.callback_func(channel)

hab1 = Sensor('input', 5, "hab1", REEDcallback)
hab2 = Sensor('input', 22, "hab2", REEDcallback)

try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    print ("Terminando Programa...")
    time.sleep(1)
finally:
    GPIO.cleanup()
    print ("Cleaned GPIO!")
