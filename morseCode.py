import sys
from time import sleep
import RPi.GPIO as GPIO


LED = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)

def dot():
    GPIO.output(LED, GPIO.HIGH)
    sleep(1)
    GPIO.output(LED, GPIO.LOW)
    sleep(1)

def dash():
    GPIO.output(LED, GPIO.HIGH)
    sleep(3)
    GPIO.output(LED, GPIO.LOW)
    sleep(1)      

def short_space():
    sleep(2)

def long_space():
    sleep(6)
    

def blink(c):
    if c == 'A':
        dot()
        dash()
    if c == 'B':
        dash()
        dot()
        dot()
        dot()
    if c == 'C':
        dash()
        dot()
        dash()
        dot()
    if c == 'D':
        dash()
        dot()
        dot()
    if c == 'E':
        dot()
    if c == 'F':
        dot()
        dot()
        dash()
        dot()
    if c == 'G':
        dash()
        dash()
        dot()
    if c == 'H':
        dot()
        dot()
        dot()
        dot()
    if c == 'I':
        dot()
        dot()
    if c == 'J':
        dot()
        dash()
        dash()
        dash()
    if c == 'K':
        dash()
        dot()
        dash()
    if c == 'L':
        dot()
        dash()
        dot()
        dot()
    if c == 'M':
        dash()
        dash()
    if c == 'N':
        dash()
        dot()
    if c == 'O':
        dash()
        dash()
        dash()
    if c == 'P':
        dot()
        dash()
        dash()
        dot()
    if c == 'Q':
        dash()
        dash()
        dot()
        dash()
    if c == 'R':
        dot()
        dash()
        dot()
    if c == 'S':
        dot()
        dot()
        dot()
    if c == 'U':
        dot()
        dot()
        dash()
    if c == 'V':
        dot()
        dot()
        dot()
        dash()
    if c == 'W':
        dot()
        dash()
        dash()
    if c == 'X':
        dash()
        dot()
        dot()
        dash()
    if c == 'Y':
        dash()
        dot()
        dash()
        dash()
    if c == 'Z':
        dash()
        dash()
        dot()
        dot()
    if c == '1':
        dot()
        dash()
        dash()
        dash()
        dash()
    if c == '2':
        dot()
        dot()
        dash()
        dash()
        dash()
    if c == '3':
        dot()
        dot()
        dot()
        dash()
        dash()
    if c == '4':
        dot()
        dot()
        dot()
        dot()
        dash()
    if c == '5':
        dot()
        dot()
        dot()
        dot()
        dot()
    if c == '6':
        dash()
        dot()
        dot()
        dot()
        dot()
    if c == '7':
        dash()
        dash()
        dot()
        dot()
        dot()
    if c == '8':
        dash()
        dash()
        dash()
        dot()
        dot()
    if c == '9':
        dash()
        dash()
        dash()
        dash()
        dot()
    if c == '0':
        dash()
        dash()
        dash()
        dash()
        dash()
    if c == '?':
        dot()
        dot()
        dash()
        dash()
        dot()
        dot()
    if c == '!':
        dash()
        dot()
        dash()
        dot()
        dash()
        dash()
    if c == '.':
        dot()
        dash()
        dot()
        dash()
        dot()
        dash()
    if c == ',':
        dash()
        dash()
        dot()
        dot()
        dash()
        dash()
    if c == ';':
        dash()
        dot()
        dash()
        dot()
        dash()
        dot()
    if c == ':':
        dash()
        dash()
        dash()
        dot()
        dot()
        dot()
    if c == '+':
        dot()
        dash()
        dot()
        dash()
        dot()
    if c == '-':
        dash()
        dot()
        dot()
        dot()
        dot()
        dash()
    if c == '/':
        dash()
        dot()
        dot()
        dash()
        dot()
    if c == '=':
        dash()
        dot()
        dot()
        dot()
        dash()
        
    else: pass