import RPi.GPIO as GPIO
from time import sleep
from pi_voice import voice
import random
from datetime import date, time, datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
sound = ['voice1.mp3', 'voice2.mp3', 'voice3.mp3']
itterassyai = ['voice4.mp3', 'voice5.mp3']

date = datetime.now()
str_date = str(date)
hour = str_date[8:-13]

class Okaeri:
    def __init__(self, random):
        self.random = random
    def ran(self):
        choice = random.choice(sound)
        voice(choice)
        sleep(5.0)

class Itterassyai:
    def __init__(self, random):
        self.random = random
    def ran(self):
        choice = random.choice(itterassyai)
        voice(choice)
        sleep(5.0)

while True:
    try: 
        if GPIO.input(24) == GPIO.HIGH:
            pass
        else:
            if hour == '06' or '07':
                oha = Itterassyai(random)
                oha.ran()
            else:
                ran_cho = Okaeri(random)
                ran_cho.ran()
    except KeyboardInterrupt:
        pass

GPIO.cleanup()
