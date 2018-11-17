from guizero import *
from PIL import Image

led_widgets = []
light_toggle = False
pb_light = None

# Store the led image files in lists
RED_LED_IMAGES = [Image.open('src/rLedOff.PNG'), Image.open('src/rLedOn.PNG')]
YELLOW_LED_IMAGES = [Image.open('src/yLedOff.PNG'), Image.open('src/yLedOn.PNG')]
GREEN_LED_IMAGES = [Image.open('src/gLedOff.PNG'), Image.open('src/gLedOn.PNG')]
BLUE_LED_IMAGES = [Image.open('src/bLedOff.PNG'), Image.open('src/bLedOn.PNG')]
LIGHT_IMAGES = [Image.open('src/sun.PNG'), Image.open('src/moon.PNG')]


def main():
    global led_widgets, pb_light

    app = App(title='Physical Programming Simulator', bg='tan', height=700, layout='grid')

    Text(app, text=' ' * 8, grid=[0, 0])

    Text(app, text='LEDs', grid=[1, 1, 1, 2])

    Text(app, text='rled', color='red', grid=[1, 3])
    red_led = Picture(app, image=RED_LED_IMAGES[0], grid=[1, 4])

    Text(app, grid=[1, 5])

    Text(app, text='yled', color='yellow', grid=[1, 6])
    yellow_led = Picture(app, image=YELLOW_LED_IMAGES[0], grid=[1, 7])

    Text(app, grid=[1, 8])

    Text(app, text='gled', color='green', grid=[1, 9])
    green_led = Picture(app, image=GREEN_LED_IMAGES[0], grid=[1, 10])

    Text(app, grid=[1, 11])

    Text(app, text='bled', color='blue', grid=[1, 12])
    blue_led = Picture(app, image=BLUE_LED_IMAGES[0], grid=[1, 13])

    # Store the led widgets in a list
    led_widgets = [red_led, yellow_led, green_led, blue_led]

    Text(app, text=' ' * 8, grid=[2, 0])

    Text(app, text='Push', grid=[3, 1])
    Text(app, text='Buttons', grid=[3, 2])

    PushButton(app, text='Button_1', command=lambda: button_click(1), grid=[3, 4])
    PushButton(app, text='Button_2', command=lambda: button_click(2), grid=[3, 7])
    PushButton(app, text='Button_3', command=lambda: button_click(3), grid=[3, 10])
    PushButton(app, text='Button_4', command=lambda: button_click(4), grid=[3, 13])

    Text(app, text=' ' * 8, grid=[4, 0])

    Text(app, text='Light', grid=[5, 1])
    Text(app, text='Sensor', grid=[5, 2])

    pb_light = PushButton(app, image=LIGHT_IMAGES[0], width=180,
                          command=toggle_light, grid=[5, 4])

    Text(app, text=' ' * 8, grid=[6, 0])

    Text(app, text='Temperature', grid=[7, 1])
    Text(app, text='Sensor', grid=[7, 2])

    Slider(app, horizontal=False, start=150, end=-50, align='top',
           width=50, height=200, command=temp_changed, grid=[7, 4, 1, 7])

    # Refresh the display every 500 ms to update the leds
    app.repeat(500, led_update)

    app.display()


def toggle_light():
    global light_toggle
    file = open('src/light.txt', 'w')

    if light_toggle:
        pb_light.image = LIGHT_IMAGES[0]
        file.write('sun')
    else:
        pb_light.image = LIGHT_IMAGES[1]
        file.write('moon')

    file.close()
    light_toggle = not light_toggle


def temp_changed(degc):
    file = open('src/temperature.txt', 'w')
    file.write(degc)
    file.close()


def button_click(btn_num):
    file = open('src/button_status.txt', 'w')
    file.write('Button_' + str(btn_num))
    file.close()


def led_update():
    # Read the required led status from the data file
    file = open('src/led_status.txt', 'r')
    led_status = file.readline().split()
    file.close()

    # Update the leds to the required status
    if int(led_status[0]) == 0:
        led_widgets[0].image = RED_LED_IMAGES[0]
    else:
        led_widgets[0].image = RED_LED_IMAGES[1]

    if int(led_status[1]) == 0:
        led_widgets[1].image = YELLOW_LED_IMAGES[0]
    else:
        led_widgets[1].image = YELLOW_LED_IMAGES[1]

    if int(led_status[2]) == 0:
        led_widgets[2].image = GREEN_LED_IMAGES[0]
    else:
        led_widgets[2].image = GREEN_LED_IMAGES[1]

    if int(led_status[3]) == 0:
        led_widgets[3].image = BLUE_LED_IMAGES[0]
    else:
        led_widgets[3].image = BLUE_LED_IMAGES[1]


main()
