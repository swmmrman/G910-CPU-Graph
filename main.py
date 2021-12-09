import psutil
import subprocess

BACKGROUND = "562500"
START_COLOR = "210000"
KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', 'q', 'w',
        'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f',
        'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm',
        ',', '.', '/']

subprocess.call(F"g910-led -a {BACKGROUND}", shell=True)
cpu_count = psutil.cpu_count()
init_string = "\\n"
for core in range(0, cpu_count):
    init_string += F"k {KEYS[core]} {START_COLOR}\\n"
init_string = F"echo -e '{init_string}c'"

ret = subprocess.call(F"{init_string} | g910-led -pp", shell=True)  # ", shell=True)

while True:
    cpu = psutil.cpu_percent(interval=.25, percpu=True)
