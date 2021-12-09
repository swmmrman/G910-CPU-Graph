import psutil
import subprocess

BACKGROUND = "562500"
KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', 'q', 'w',
        'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f',
        'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm',
        ',', '.', '/']

subprocess.call(F"g910-led -a {BACKGROUND}")
while True:
    cpu = psutil.cpu_percent(interval=.25, percpu=True)
