from robot import ui, bot, led, const as c
from threading import Thread
import sys


def main():
    print('Starting TA bot')

    # Start the robot
    bot_thread = Thread(target=bot.initialize, name='bot_thread')
    bot_thread.start()

    # Start the LED thread
    led_thread = Thread(target=led.initialize, name='led_thread')
    led_thread.start()

    # Start UI
    ui_thread = Thread(target=ui.initialize, name='ui_thread')
    ui_thread.start()

    # Pause indefinitely until the program is killed
    ui_thread.join()
    c.EXIT = True
    bot_thread.join()

main()