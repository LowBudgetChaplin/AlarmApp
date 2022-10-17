from ast import Try
from datetime import datetime
from playsound import playound

try:
    ora_alarma = input("Introduceti ora la care vrei sa te trezesti astfel: "/HH:MM AM/PM:/"" )
except ValueError:
    print("ErROR")


def validate_time(ora_alarma):
    if len(ora_alarma) != 13:
        return "Invalid time format! Please try again..."
    else:
        if int(ora_alarma[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(ora_alarma[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(ora_alarma[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"