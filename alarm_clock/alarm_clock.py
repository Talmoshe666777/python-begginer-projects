from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  # integer devision, return int
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")  # :02d means return that time with leading zero
    playsound("blues.mp3")


while True:
    minutes = input("Minutes: ")
    seconds = input("Seconds: ")

    if minutes.isdigit():
        minutes = int(minutes)
    else:
        print("Input is not numeric... try again")

    if seconds.isdigit():
        seconds = int(seconds)
    else:
        print("Input is not numeric... try again")

    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)
