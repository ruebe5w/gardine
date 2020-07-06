import RPi.GPIO as GPIO
import datetime
import time
import sys


class Gardine:
    morgens = datetime.time(8, 0)
    auf = 2
    zu = 3
    stop = 4

    # print(morgens)
    abends = datetime.time(18, 0)
    # print(abends)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([auf, zu, stop], GPIO.OUT)
    GPIO.output(auf, 1)
    GPIO.output(zu, 1)
    GPIO.output(stop, 0)
    zustand = ""

    def load_zustand(self):
        try:
            with open("zustand.txt", "r") as file:
                Gardine.zustand = file.read()
        except:
            print("Kein Zustand gefunden")
            with open("zustand.txt", "w") as file:
                Gardine.zustand = "offen"

    def __init__(self):
        sys.stdout.write("Hello World!\n")
        print("Hello Gardine!")
        Gardine.load_zustand(self)

    @staticmethod
    def f_auf():
        sys.stdout.write("auf\n")
        GPIO.output(Gardine.auf, 0)
        time.sleep(1)
        GPIO.output(Gardine.auf, 1)
        Gardine.set_zustand("offen")

    @staticmethod
    def f_zu():
        sys.stdout.write("zu\n")
        GPIO.output(Gardine.zu, 0)
        time.sleep(1)
        GPIO.output(Gardine.zu, 1)
        Gardine.set_zustand("zu")

    @staticmethod
    def f_stop():
        GPIO.output(Gardine.stop, 1)
        time.sleep(1)
        GPIO.output(Gardine.stop, 0)

    @staticmethod
    def get_zustand():
        Gardine.load_zustand(Gardine)
        return Gardine.zustand

    @staticmethod
    def set_zustand(zustand):
        with open("zustand.txt", "w") as file:
            file.write(zustand)

    @staticmethod
    def get_abends():
        return Gardine.abends

    @staticmethod
    def get_morgens():
        return Gardine.morgens
