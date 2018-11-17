import physense_emu
from time import sleep

toggle = True


def blink():
    global toggle
    toggle = not toggle
    if toggle:
        sensor.output(colorLED1, "on")
    else:
        sensor.output(colorLED1, "off")


# create sensor connection
sensor = physense_emu.Sensor()

colorLED1 = "rled"
colorLED2 = "yled"
colorLED3 = "gled"
colorLED4 = "bled"

while True:
    try:
        sleep(1)
        sensor.output(colorLED1, "on")
        sleep(1)
        sensor.output(colorLED1, "off")

    except KeyboardInterrupt:
        sensor.output(colorLED1, "off")
        print('bye')
        break
