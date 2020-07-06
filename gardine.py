import time
time.sleep(60)
from gardineclass import Gardine
from sunset import SunSet

while True:
    if SunSet.is_day(time.time()):
        Gardine.f_auf()
    elif not SunSet.is_day(time.time()):
        Gardine.f_zu()
    else:
        Gardine.f_zu()
    time.sleep(1000)
