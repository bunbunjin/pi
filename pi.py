from bottle import route, run, template, request
import RPi.GPIO as GPIO
from time import sleep
from pi_voice import voice
import random
from datetime import date, time, datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
sound = ['voice1.mp3', 'voice2.mp3', 'voice3.mp3']
itterassyai = ['voice4.mp3', 'voice5.mp3']
morning = 'goodmorning.mp3'

time_zone = datetime.now()
str_date = str(time_zone)
hour = str_date[8:-13]
minute = str_date[14:-10]
now = str_date[10:-11]


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


@route('/pi')
def pi():
    text = '起動中'
    while True:
        try:
            if GPIO.input(25) == GPIO.HIGH:
                pass
            else:
                if hour == '07':
                    oha = Itterassyai(random)
                    oha.ran()
                else:
                    ran_cho = Okaeri(random)
                    ran_cho.ran()
        except KeyboardInterrupt:
            pass
        return template('pi', text=text)


@route('/pi/alram')
def alram():
    return template('alram', text='')


@route('/pi/alram', method='POST')
def do_alram():
    input_text = request.forms.input_text
    in_text = Input_text(input_text)
    input_text = in_text
    print(input_text)
    if now == input_text:
        while GPIO.input(25) == GPIO.HIGH:
            Alram(random).ran()

    return template('alram', text=input_text)


run(host='localhost', port=8080, debug=True)

GPIO.cleanup()
