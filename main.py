#!/usr/bin/python3
import psutil
import subprocess
import setproctitle
import signal
import os

setproctitle.setproctitle("G910-CPU-Graph")


def stop(signal, frame):
    print("\rGood Bye")
    global RUNNING
    RUNNING = False


signal.signal(signal.SIGABRT, stop)
signal.signal(signal.SIGTERM, stop)
signal.signal(signal.SIGHUP, stop)
signal.signal(signal.SIGINT, stop)

RUNNING = True
BACKGROUND = "562500"
START_COLOR = "210000"
KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'num0', 'num1', 'num2',
        'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9']


subprocess.call(F"g910-led -a {BACKGROUND}", shell=True)
cpu_count = psutil.cpu_count()
init_string = "\\n"
for core in range(0, cpu_count):
    init_string += F"k {KEYS[core]} {START_COLOR}\\n"
init_string = F"echo -e '{init_string}c'"

ret = subprocess.call(F"{init_string} | g910-led -pp", shell=True)  # ", shell=True)


def get_color(percent):
    frac = percent / 100
    return F"{round(frac * 255):02x}{(110 - round(frac * 110)):02x}00"


cpu_sensor = ""
sensors = os.listdir('/sys/class/thermal/')
for sensor in sensors:
    line = open(F'/sys/class/thermal/{sensor}/type').readline()
    if line.strip() == "x86_pkg_temp":
        cpu_sensor = F'/sys/class/thermal/{sensor}/temp'
while RUNNING:
    cpu = psutil.cpu_percent(interval=0.05, percpu=True)
    temp = int(open(cpu_sensor).readline())/1000
    key_string = "\\n"
    for core, percent in enumerate(cpu):
        key_string += F"k {KEYS[core]} {get_color(percent)}\\n"
    key_string += F"g logo {get_color(temp)}\\n"
    key_string = F"echo -e '{key_string}c'"
    subprocess.call(F"{key_string} | g910-led -pp", shell=True)
else:
    subprocess.call(F"g910-led -a {BACKGROUND}", shell=True)
