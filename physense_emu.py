import subprocess


def clear_button():
    # Clear the button status after it's read
    file = open('src/button_status.txt', 'w')
    file.write('None')
    file.close()


class Sensor:

    def __init__(self):
        # Start the simulator
        subprocess.Popen('C:\Program Files (x86)\Python36-32\python.exe physense_emuX.py')

        # Initialize the data files
        file = open('src/led_status.txt', 'w')
        file.write('0 0 0 0')
        file.close()

        file = open('src/button_status.txt', 'w')
        file.write('None')
        file.close()

        file = open('src/temperature.txt', 'w')
        file.write('0')
        file.close()

        file = open('src/light.txt', 'w')
        file.write('sun')
        file.close()

    # Send data to the leds
    @staticmethod
    def output(led, status):

        # Get the current led status
        file = open('src/led_status.txt', 'r')
        led_status = file.readline().split()
        file.close()

        # Change led status as required
        if led == 'rled' and status == 'off':
            led_status[0] = '0'
        elif led == 'rled' and status == 'on':
            led_status[0] = '1'

        if led == 'yled' and status == 'off':
            led_status[1] = '0'
        elif led == 'yled' and status == 'on':
            led_status[1] = '1'

        if led == 'gled' and status == 'off':
            led_status[2] = '0'
        elif led == 'gled' and status == 'on':
            led_status[2] = '1'

        if led == 'bled' and status == 'off':
            led_status[3] = '0'
        elif led == 'bled' and status == 'on':
            led_status[3] = '1'

        # Write the new led status to the data file
        file = open('src/led_status.txt', 'w')
        file.writelines(led_status[0] + ' ' +
                        led_status[1] + ' ' +
                        led_status[2] + ' ' +
                        led_status[3])
        file.close()

    @staticmethod
    def input(phy_obj):

        # Get the name of the most recent button clicked
        file = open('src/button_status.txt', 'r')
        button_status = file.readline()
        file.close()

        # Return the status if a button query
        if phy_obj == button_status:
            clear_button()
            return "pressed"

        elif phy_obj == button_status:
            clear_button()
            return "pressed"

        elif phy_obj == button_status:
            clear_button()
            return "pressed"

        elif phy_obj == button_status:
            clear_button()
            return "pressed"

        # Return the temperature if a temperature query
        elif phy_obj == 'temperature':
            file = open('src/temperature.txt', 'r')
            reading = file.readline()
            file.close()
            return reading

        # Return the light status if a light query
        elif phy_obj == 'light':
            file = open('src/light.txt', 'r')
            reading = file.readline()
            file.close()
            return reading