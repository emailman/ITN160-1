from itn160 import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

sensor.output('rled', 'on')
sensor.output("buzz", "play")

sleep(3)

sensor.output('rled', 'off')

