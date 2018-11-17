import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

while True:
    if sensor.input('light') == 'sun':
        sensor.output('yled', 'on')
        sensor.output('bled', 'off')
    else:
        sensor.output('yled', 'off')
        sensor.output('bled', 'on')

    sleep(1)
