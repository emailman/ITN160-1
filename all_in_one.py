import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

while True:

    sensor.output('rled', 'on')
    sleep(1)
    sensor.output('rled', 'off')

    sensor.output('yled', 'on')
    sleep(1)
    sensor.output('yled', 'off')

    sensor.output('gled', 'on')
    sleep(1)
    sensor.output('gled', 'off')

    sensor.output('bled', 'on')
    sleep(1)
    sensor.output('bled', 'off')
