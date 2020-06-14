import psutil
import os
import time
import sys

sys.setrecursionlimit(10**6)
# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


def check_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if (battery.percent <= 80 and plugged==False):
        notify(title = 'Charge',
            subtitle = percent+"%",
            message  = 'Please, charge your battery!')
    print percent
    time.sleep(450)
    check_battery()

if __name__ == '__main__':
    check_battery()

