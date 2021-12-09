import psutil
import subprocess
import setproctitle

setproctitle.setproctitle("G910-CPU-Graph")

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
    return round(percent/100) * 255


while True:
    cpu = psutil.cpu_percent(interval=.1, percpu=True)
    key_string = "\\n"
    for core, percent in enumerate(cpu):
        key_string += F"k {KEYS[core]} {get_color(percent):02x}0000\\n"
    key_string = F"echo -e '{key_string}c'"
    subprocess.call(F"{key_string} | g910-led -pp", shell=True)
