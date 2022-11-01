from robot import const as c
from robot import key_handler
from robot import ui_config as uic

import curses
from curses import wrapper

from pynput import keyboard

import time, sys

# Curses stuff: https://docs.python.org/3/howto/curses.html

WIN = None

"""
Initialize the UI in the terminal using curses. This should be run in its own thread.
"""
def initialize():
    print('Initializing UI')
    wrapper(_run_ui)


def setup_window(win):
    # Initialize window
    set_colors()

    # Print the program title
    print_centered(win, 1, uic.WINDOW_TITLE, curses.A_REVERSE | curses.A_BOLD)
    print_centered(win, 2, '-' * 30)

    # Determine the x position of the four fields
    row_1_len = (
        uic.DIRECTION_FIELD_MAX_LEN + uic.INFO_FIELD_SPACING + uic.GEAR_FIELD_MAX_LEN
    )
    row_2_len = (
        uic.TURN_SPEED_FIELD_MAX_LEN + uic.INFO_FIELD_SPACING + uic.DRIFT_FIELD_MAX_LEN
    )

    uic.direction_field_x = int((curses.COLS - 1 - row_1_len) / 2)
    uic.gear_field_x = (
        uic.direction_field_x + uic.DIRECTION_FIELD_MAX_LEN + uic.INFO_FIELD_SPACING
    )

    uic.turn_speed_field_x = int((curses.COLS - 1 - row_2_len) / 2)
    uic.drift_field_x = (
        uic.turn_speed_field_x + uic.TURN_SPEED_FIELD_MAX_LEN + uic.INFO_FIELD_SPACING
    )

    # Print the labels for the fields
    print_field(win, 4, uic.direction_field_x, 'Direction: ')
    print_field(win, 4, uic.gear_field_x, 'Gear: ')
    print_field(win, 6, uic.turn_speed_field_x, 'Turn_Speed: ')
    print_field(win, 6, uic.drift_field_x, 'Drift: ')

    # Update the x positions, moving them over to account for the labels
    uic.direction_field_x = uic.direction_field_x + 11
    uic.gear_field_x = uic.gear_field_x + 6
    uic.turn_speed_field_x = uic.turn_speed_field_x + 12
    uic.drift_field_x = uic.drift_field_x + 7

    # Determine the column positions for the key list
    col_1_x = int(
        (curses.COLS - 1 - (uic.KEY_COL_COUNT - 1) * (uic.KEY_COL_SPACING + 1)) / 2
    )
    uic.key_col_xs = [
        col_1_x + (uic.KEY_COL_SPACING + 1) * i for i in range(uic.KEY_COL_COUNT)
    ]

    # Print the main four fields
    update_fields(win)

    print_centered(win, 8, '-' * 30)

    # Print the key list
    update_key_display(win)

    draw_border(win)
    win.refresh()


def _run_ui(stdscr):
    try:
        win = curses.newwin(curses.LINES - 1, curses.COLS - 1, 0, 0)
        setup_window(win)

        #update_key_display(win)

        while True:
            with keyboard.Events() as events:
                for event in events:
                    process_event(event, win)

    except KeyboardInterrupt:
        pass


def process_event(event, win):
    key = event.key

    # If the user pressed escape, exit the program
    if isinstance(key, keyboard.Key):
        if key == keyboard.Key.esc:
            sys.exit()
        return

    # If the user didn't press an alphanumeric key, ignore the event
    if not isinstance(key, keyboard.KeyCode):
        return

    # Pass the key and press state to the key_handler. If it returns True (indicating
    # that something changed), update the key display.
    if key_handler.process_keys(key.char, isinstance(event, keyboard.Events.Press)):
        update_key_display(win)
        update_fields(win)
        win.refresh()


"""
Update the list of keys being tracked. Print them brighter if they're currently
pressed down.
"""
def update_key_display(win):
    y = 10
    col_num = 0

    for k in c.KEYS:
        win.addstr(
            y,
            uic.key_col_xs[col_num],
            k,
            (curses.A_BOLD | curses.color_pair(3)) if c.KEYS[k] else curses.color_pair(2)
        )

        col_num = col_num + 1
        if col_num == len(uic.key_col_xs):
            col_num = 0
            y = y + 1

    #t = time.localtime(time.time())
    #win.addstr(len(c.KEYS) + 8, 0, f'Current Time: {t.tm_hour}:{t.tm_min}:{t.tm_sec}')


"""
Set the color pairs used later when printing text. This is called once when the window
is first initialized.
"""
def set_colors() -> None:
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)


"""
Print the border around the given window. This is called once when the window is first
initialized.
"""
def draw_border(win) -> None:
    win.addstr(0, 0, '+' + '-' * (curses.COLS - 3) + '+')
    win.addstr(curses.LINES - 3, 0, '+' + '-' * (curses.COLS - 3) + '+')
    for i in range(1, curses.LINES - 3):
        win.addstr(i, 0, '|')
        win.addstr(i, curses.COLS - 2, '|')


"""
Update the four main fields.
"""
def update_fields(win) -> None:
    # Print the name of the current enum value for each field. Pad with spaces
    # to reach the length of the longest enum name from that class.
    print_field(win, 4, uic.direction_field_x, f'{c.DIRECTION.name:<14}')
    print_field(win, 4, uic.gear_field_x, f'{c.GEAR.name:<12}')
    print_field(win, 6, uic.turn_speed_field_x, f'{c.TURN_SPEED.name:<9}')
    print_field(win, 6, uic.drift_field_x, f'{c.DRIFT.name:<14}')


"""
Print one of the four user-adjustable fields (direction, gear, turn_speed, and drift).

This is basically just calling win.addstr() with some specific attributes.
"""
def print_field(win, y: int, x: int, text: str) -> None:
    win.addstr(y, x, text, curses.A_BOLD | curses.color_pair(1))


"""
Print some text centered on the given line (y pos).
"""
def print_centered(win, y: int, text: str, args = 0) -> None:
    win.addstr(y, int((curses.COLS - len(text)) / 2), text, args)