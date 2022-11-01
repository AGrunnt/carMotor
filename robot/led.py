from robot.directions import LEDs
from robot import const as c
from robot.library.Led import *


def initialize():
    global led

    print('Initializing LED...')

    try:
        led = Led()
    except:
        print('Failed to start LEDs')

    listener()


def listener():
    try:
        while not c.EXIT:
            if c.LED == LEDs.DESIGN_1:
                run_design_1()
            elif c.LED == LEDs.DESIGN_2:
                run_design_2()
            elif c.LED == LEDs.DESIGN_3:
                run_design_3()
            elif c.LED == LEDs.DESIGN_4:
                run_design_4()
            elif c.LED == LEDs.DESIGN_5:
                run_design_5()
            else:
                disable_leds()

        disable_leds()
    except:
        pass


def disable_leds():
    led.colorWipe(led.strip, Color(0,0,0))


def run_design_1():
    led.ledIndex(0x01,255,0,0)      #Red
    led.ledIndex(0x02,255,125,0)    #orange
    led.ledIndex(0x04,255,255,0)    #yellow
    led.ledIndex(0x08,0,255,0)      #green
    led.ledIndex(0x10,0,255,255)    #cyan-blue
    led.ledIndex(0x20,0,0,255)      #blue
    led.ledIndex(0x40,128,0,128)    #purple
    led.ledIndex(0x80,255,255,255)  #white


def run_design_2():
    # Red on all LEDs
    led.ledIndex(0x01,255,0,0)
    led.ledIndex(0x02,255,0,0)
    led.ledIndex(0x04,255,0,0)
    led.ledIndex(0x08,255,0,0)
    led.ledIndex(0x10,255,0,0)
    led.ledIndex(0x20,255,0,0)
    led.ledIndex(0x40,255,0,0)
    led.ledIndex(0x80,255,0,0)


def run_design_3():
    # Green on all LEDs
    led.ledIndex(0x01,0,225,0)
    led.ledIndex(0x02,0,225,0)
    led.ledIndex(0x04,0,225,0)
    led.ledIndex(0x08,0,225,0)
    led.ledIndex(0x10,0,225,0)
    led.ledIndex(0x20,0,225,0)
    led.ledIndex(0x40,0,225,0)
    led.ledIndex(0x80,0,225,0)


def run_design_4():
    # Blue on all LEDs
    led.ledIndex(0x01,0,0,225)
    led.ledIndex(0x02,0,0,225)
    led.ledIndex(0x04,0,0,225)
    led.ledIndex(0x08,0,0,225)
    led.ledIndex(0x10,0,0,225)
    led.ledIndex(0x20,0,0,225)
    led.ledIndex(0x40,0,0,225)
    led.ledIndex(0x80,0,0,225)


def run_design_5():
    # White on all LEDs
    led.ledIndex(0x01,225,225,225)
    led.ledIndex(0x02,225,225,225)
    led.ledIndex(0x04,225,225,225)
    led.ledIndex(0x08,225,225,225)
    led.ledIndex(0x10,225,225,225)
    led.ledIndex(0x20,225,225,225)
    led.ledIndex(0x40,225,225,225)
    led.ledIndex(0x80,225,225,225)
