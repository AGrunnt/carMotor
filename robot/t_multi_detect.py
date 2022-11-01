
from Motor import *
import time


my_Motor = Motor()
max_speed = 4096
start_speed = [0,0,0,0]


def check_speed(key,uniform_speed,current_turn_opt):
	# if a change speed key is click, change speed to that amount

    if key=='7':
        new_speed = max_speed * 0.25
    elif key=='8':
        new_speed = max_speed * 0.50
    elif key=='9':
        new_speed = max_speed * 0.80
    elif key=='0':
        new_speed = max_speed * 1.0
    else:
        new_speed=uniform_speed

    new_speed_list = [int(new_speed) for i in range(4)]


    if key == 'u':
        turn_speed_opt = "fast"
    elif key == 'i':
        turn_speed_opt = "slow"
    elif key == 'o':
        turn_speed_opt = "pin"
    else:
        turn_speed_opt = current_turn_opt

    return new_speed_list, turn_speed_opt


def pin_right(speed_list):
    speed_list[2] = speed_list[2] * 0
    speed_list[3] = speed_list[3] * 0

def pin_left(speed_list):
    speed_list[0] = speed_list[0] * 0
    speed_list[1] = speed_list[1] * 0

def slow_right(speed_list):
    speed_list[2] = speed_list[2] * 0.8
    speed_list[3] = speed_list[3] * 0.8

    return speed_list

def slow_left(speed_list):
    speed_list[0]=speed_list[0] * 0.8
    speed_list[1]=speed_list[1] * 0.8
    return speed_list

def fast_right(speed_list):
    speed_list[2]=speed_list[2] * 0.5
    speed_list[3]=speed_list[3] * 0.5

    return speed_list

def fast_left(speed_list):
    speed_list[0]=speed_list[0] * 0.5
    speed_list[1]=speed_list[1] * 0.5

    return speed_list


def check_turn_speed(key,current_speed,turn_speed_opt):
    if key == "d":
        if turn_speed_opt == "fast":
            return fast_right(current_speed)
        elif turn_speed_opt == "pin":
            return pin_right(current_speed)
        else:
            return slow_right(current_speed)

    if key == "a":
        if turn_speed_opt == "fast":
            return fast_left(current_speed)
        elif turn_speed_opt == "pin":
            return pin_left(current_speed)
        else:
            return slow_left(current_speed)


def forward(uniform_speed):
    return uniform_speed

def backward(uniform_speed):
    new_speed_list = [-speed for speed in uniform_speed]

    return new_speed_list


def turn(key,uniform_speed,turn_speed_opt):
    if key == "d":
        return check_turn_speed(key,uniform_speed,turn_speed_opt)
    if key =="a":
        return check_turn_speed(key,uniform_speed,turn_speed_opt)
    if key == "s":
        return forward(uniform_speed)
    if key == "w":
        return backward(uniform_speed)


def move(speed_list):
    my_Motor.setMotorModel(speed_list[0],speed_list[1],speed_list[2],speed_list[3])




def run():
    import sys
    #import keyboard
    print(sys.argv)
    import time

    current_speed = [0,0,0,0]
    uniform_speed = current_speed
    current_turn_opt = "fast"
    key = ' '
    wheel_speeds=[2000,2000,2000,2000]
    end = time.time()
    start=time.time()

    try:
        while (key != 's' and end-start<10):
            #key=keyboard.read_event().name  #pip install keyboard
            key=input("please")
            uniform_speed,turn_speed_opt = check_speed(key,uniform_speed,current_speed_opt)
            wheel_speeds = turn(key,uniform_speed,turn_speed_opt)
            move(wheel_speeds)
            print("Hit 's' to stop ")
            end=time.time()
            print("time elapsed ",end-start)

    except Exception as a:
        print(a)

    print("should have stopped")
    move([0,0,0,0])

def test():
    print("it worked")


