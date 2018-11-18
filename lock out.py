import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

while True:
    lock_status = sensor.input('light')
    if lock_status == 'on':
        sensor.output('gled', 'on')
        sensor.output('rled', 'off')
    else:
        sensor.output('gled', 'off')
        sensor.output('rled', 'on')

    if sensor.input('Button_4') == 'pressed' and lock_status == 'on':
        for i in range(5):
            sensor.output('bled', 'on')
            sleep(1)
            sensor.output('bled', 'off')
            sleep(1)
    else:
        sleep(1)
