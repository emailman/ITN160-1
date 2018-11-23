import physense_emu
from time import sleep

sensor = physense_emu.Sensor()

while True:
    if sensor.input("Button_1") == "pressed":
        sensor.output('rled', 'on')
        sensor.output("buzz", 'play')
        sleep(2)
        sensor.output('rled', 'off')

    elif sensor.input("Button_2") == "pressed":
        sensor.output('yled', 'on')
        sensor.output('buzz', 'play')
        sleep(2)
        sensor.output('yled', 'off')

    elif sensor.input("Button_3") == "pressed":
        sensor.output('gled', 'on')
        sensor.output('buzz', 'play')
        sleep(2)
        sensor.output('gled', 'off')

    elif sensor.input("Button_4") == "pressed":
        sensor.output('bled', 'on')
        sensor.output('buzz', 'play')
        sleep(2)
        sensor.output('bled', 'off')

    sleep(1)
