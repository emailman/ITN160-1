import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

while True:
    if sensor.input("Button_1") == "pressed":
        # sensor.output("buzz", 'play')
        sensor.output('rled', 'on')
        sleep(2)
        sensor.output('rled', 'off')

    elif sensor.input("Button_2") == "pressed":
        # sensor.output("buzz", 'play')
        sensor.output('yled', 'on')
        sleep(2)
        sensor.output('yled', 'off')

    elif sensor.input("Button_3") == "pressed":
        # sensor.output("buzz", 'play')
        sensor.output('gled', 'on')
        sleep(2)
        sensor.output('gled', 'off')

    elif sensor.input("Button_4") == "pressed":
        # sensor.output("buzz", 'play')
        sensor.output('bled', 'on')
        sleep(2)
        sensor.output('bled', 'off')

    sleep(1)
