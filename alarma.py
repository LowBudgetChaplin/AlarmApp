from datetime import datetime
import os
from playsound import playsound
import time


# ora_alarma = "12:00 AM"
def validate_time(ora_alarma):
    if int(ora_alarma[:2]) > 12:
        return "Invalid HOUR format! Please try again..."
    elif int(ora_alarma[3:5]) > 59:
        return "Invalid MINUTE format! Please try again..."

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
    # get alarm sound
    alarm_sound = os.path.join(os.getcwd(), "Alarm Clock_alarm.wav")
    return alarm_sound


print(get_current_time())
# print(datetime.now())

# -- main --
try:
    ora_alarma = input("Introduceti ora la care vrei sa te trezesti astfel: HH:MM\n" )
    validate_time(ora_alarma)
except ValueError as e:
    print(f"Invalid time format! Please try again... \n {e}")
else:    
    ora = get_alarm_time(ora_alarma)[0]
    minut = get_alarm_time(ora_alarma)[1]

    while True:
        ora_curenta, minut_curent = get_current_time()
        print(ora_curenta, minut_curent)
        time.sleep(1)
        if ora == ora_curenta and minut == minut_curent:
            print("Wake Up!")
            playsound(alarm_sound_path())
            break