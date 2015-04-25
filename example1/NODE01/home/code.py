#!/usr/bin/env python

# ----- BEGIN INITIALIZATION -----
import os
from serial import Serial

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SERIAL_PATH = os.path.join(BASE_DIR, 'dev', 'ttyS0')
ROOT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))

serial = Serial(SERIAL_PATH, 38400)

import sys
sys.path.insert(1, os.path.join(ROOT_DIR, 'copernicus-api'))

from copernicus import Copernicus
api = Copernicus(serial)
# ----- END INITIALIZATION -----

from time import sleep
from threading import Thread

def rotate_servo(pos):
    api.command('servo', pos / 2)

def switch_led1(state):
    api.command('led', state)

def switch_led2(state):
    if state == True:
        api.command('rgb', 'yellow')
    else:
        api.command('rgb', 'green')

def _delayed_motion():
    sleep(3)
    api.command('rgb', 'off')

def motion(state):
    if state == True:
        api.command('rgb', 'blue')
        Thread(target=_delayed_motion).start()

api.command('subscribe', 'knob', 'button1', 'button2', 'motion')
api.set_handler('knob', rotate_servo)
api.set_handler('button1', switch_led1)
api.set_handler('button2', switch_led2)
api.set_handler('motion', motion)

while True:
    api.listen()
