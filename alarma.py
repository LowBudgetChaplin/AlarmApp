from datetime import datetime
import os, sys
from playsound import playsound
import time


# ora_alarma = "12:00 AM" 
# 24 hour format
def validate_time(ora_alarma):
    if int(ora_alarma[:2]) > 23:
        print ("Invalid HOUR format! Please try again...")
        return True
    elif int(ora_alarma[3:5]) > 59:
        print ("Invalid MINUTE format! Please try again...")
        return True
    else: return False

def get_alarm_time(ora_alarma):
    ora = ora_alarma[:2]
    minut = ora_alarma[3:5]
    return ora, minut

def get_current_time():
    # get current time
    now = datetime.now()
    ora = now.strftime("%H") 
    minut = now.strftime("%M")
    return ora, minut

def alarm_sound_path():
    # get alarm sound path
    alarm_sound = os.path.join(os.getcwd(), "Alarm_Clock.wav")
    return alarm_sound


print(get_current_time())
# print(datetime.now())

# -- main --
try:
    ora_alarma = input("Introduceti ora la care vrei sa te trezesti astfel: HH:MM\n" )
    while validate_time(ora_alarma):
        ora_alarma = input("Introduceti ora la care vrei sa te trezesti astfel: HH:MM\n" )
              
except ValueError as e:
    print(f"Invalid time format! Please try again... \n {e}")
    
else:
    # get ora and minut from given alarm time input    
    ora = get_alarm_time(ora_alarma)[0]
    minut = get_alarm_time(ora_alarma)[1]

    while True:
        ora_curenta, minut_curent = get_current_time()
        # to see the current time, uncomment
        #print(ora_curenta, minut_curent) 
        time.sleep(1)
        if ora == ora_curenta and minut == minut_curent:
            print("Wake Up!")
            playsound(alarm_sound_path())
            break