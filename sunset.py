# Bitte vorher installieren:
# $ pip install requests

import re
import requests
import time
from datetime import datetime


class SunSet:
    @staticmethod
    def get_api():
        print()
    @staticmethod
    def get_sunrise():
        regex = r"\"sunrise\":(\d+),"

        answer = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?id=6557397&APPID=d3bb270e740c32655f9f0441805047f5')
        test_str = answer.text

        matches = re.search(regex, test_str)

        return int(matches.groups(0)[0])

    @staticmethod
    def get_sunset():
        regex = r"\"sunset\":(\d+)}"

        answer = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?id=6557397&APPID=d3bb270e740c32655f9f0441805047f5')
        input_str = answer.text

        matches = re.search(regex, input_str)

        return int(matches.groups(0)[0])

    @staticmethod
    def is_day(time):
        bol=False
        if SunSet.get_sunrise() > time:
            bol= False
        if SunSet.get_sunrise() <= time < SunSet.get_sunset():
            bol= True
        if time < datetime.fromtimestamp(time).replace(hour=7, minute=0).timestamp():
            bol= False
        if time > datetime.fromtimestamp(time).replace(hour=21,minute=0).timestamp():
            bol= False
        else:
            bol=False
        return bol
