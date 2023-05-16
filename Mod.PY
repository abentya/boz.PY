# boz.PY
import datetime
import winsound

def set_alarm():
    alarm_time = input("Установите время будильника (в формате ЧЧ:ММ): ")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            play_alarm()
            break

def play_alarm():
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)
    print("Проснитесь! Уже время!")

set_alarm()
