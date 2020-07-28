import time
time.sleep(60)
from gardinensteuerung import Gardine
from sunset import SunSet


if SunSet.is_day(time.time()):
    print("auf")
    Gardine.f_auf()
elif not SunSet.is_day(time.time()):
    print("zu")
    Gardine.f_zu()
else:
    print("zu2")
    Gardine.f_zu()
   
