import physense_emu

from time import sleep

# create sensor connection
sensor = physense_emu.Sensor()


while True:
    temp = sensor.input("temperature")
    print(temp, type(temp))
    sleep(1)
