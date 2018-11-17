import physense_emu
from time import sleep

# create sensor connection
sensor = physense_emu.Sensor()


while True:
    sleep(1)
    if sensor.input('Button_1'):
        print('clicked')
        sensor.output('gled', 'on')
        sleep(5)
        sensor.output('gled', 'off')
