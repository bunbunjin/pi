from bottle import route, run, template, request
import RPi.GPIO as GPIO
from time import sleep
from voice import voice
import random
from datetime import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
sound = ['voice1.mp3', 'voice2.mp3', 'voice3.mp3']
itterassyai = ['voice4.mp3', 'voice5.mp3']
morning = ['voice9.mp3', 'voice10.mp3', 'voice11.mp3', 'voice12.mp3']


class Okaeri:

    def __init__(self, random):
        self.random = random

    def ran(self):
        choice = random.choice(sound)
        voice(choice)
        sleep(10.0)


class Itterassyai:

    def __init__(self, random):
        self.random = random

    def ran(self):
        choice = random.choice(itterassyai)
        voice(choice)
        sleep(5.0)


class Alram:

    def __init__(self, random):
        self.random = random

    def ran(self):
        choice = random.choice(morning)
        voice(choice)
        sleep(3.5)


class Input_text:

    def __init__(self, input_text):
        self.input_text = input_text

    def go(self):
        request.forms.input_text
        print()


def pi():
    while True:
        time_zone = datetime.now()
        str_date = str(time_zone)
        hour = str_date[8:-13]
        now = str_date[11:-10]
        try:
            if GPIO.input(25) == GPIO.HIGH:
                input_text = request.forms.input_text
                while GPIO.input(25) == GPIO.HIGH:

                    if input_text == now:
                        alram = Alram(morning)
                        alram.ran()
                        time_zone = datetime.now()
                        str_date = str(time_zone)
                        now = str_date[11:-10]

                input_text = ''

            else:

                if hour == '07':
                    oha = Itterassyai(random)
                    oha.ran()

                else:
                    ran_cho = Okaeri(random)
                    ran_cho.ran()

        except KeyboardInterrupt:
            pass


pi()
GPIO.cleanup()
