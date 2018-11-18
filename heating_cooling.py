import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

target_temperature = 60
deadband = 10


while True:
    temperature = int(sensor.input('temperature'))

    if temperature > target_temperature + deadband / 2:
        sensor.output('bled', 'on')
        sensor.output('rled', 'off')
    elif temperature < target_temperature - deadband / 2:
        sensor.output('bled', 'off')
        sensor.output('rled', 'on')
    else:
        sensor.output('bled', 'off')
        sensor.output('rled', 'off')

    sleep(1)
