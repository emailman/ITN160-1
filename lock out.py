import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

while True:
    # Show green if unlocked, red if locked
    lock_status = sensor.input('light')
    if lock_status == 'on':
        sensor.output('gled', 'on')
        sensor.output('rled', 'off')
    else:
        sensor.output('gled', 'off')
        sensor.output('rled', 'on')

    # Run a cycle only if unlocked
    if sensor.input('Button_4') == 'pressed' and lock_status == 'on':
        for i in range(3):
            sensor.output('bled', 'on')
            sensor.output('buzzer', 'play')
            sleep(1)
            sensor.output('bled', 'off')
            sleep(1)
    else:
        sleep(1)
