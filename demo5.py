import physense_emu
from time import sleep

# create sensor connection
sensor = physense_emu.Sensor()

while True:

    if sensor.input('light') == 'sun':
        # print('day')
        sensor.output('bled', 'off')
        sensor.output('yled', 'on')

    else:
        # print('night')
        sensor.output('bled', 'on')
        sensor.output('yled', 'off')
    sleep(2)
