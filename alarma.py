from datetime import datetime
# from playsound import playound

try:
    ora_alarma = input("Introduceti ora la care vrei sa te trezesti astfel: HH:MM AM//PM:" )
except ValueError as e:
    print(f"Invalid time format! Please try again... \n {e}")

# ora_alarma = "12:00 AM"
def validate_time(ora_alarma):
    if int(ora_alarma[:2]) > 12:
        return "Invalid HOUR format! Please try again..."
    elif int(ora_alarma[3:5]) > 59:
        return "Invalid MINUTE format! Please try again..."

