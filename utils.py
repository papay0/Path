import sys
import tty
import termios
import os
import time

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get_input(position, map):
    inkey = _Getch()
    line, column = position
    while 1:
        while 1:
            k = inkey()
            if k != '': break
        if k == '\x1b[A' and map.is_valid(line-1, column) and not map.is_obstacle(line-1, column):
            if map.is_door(line - 1, column):
                return map.get_other_door_position(line-1, column)
            return (line - 1, column)
        elif k == '\x1b[B' and map.is_valid(line+1, column) and not map.is_obstacle(line+1, column):
            if map.is_door(line + 1, column):
                return map.get_other_door_position(line+1, column)
            return (line + 1, column)
        elif k == '\x1b[C' and map.is_valid(line, column+1) and not map.is_obstacle(line, column+1):
            if map.is_door(line, column+1):
                return map.get_other_door_position(line, column+1)
            return (line, column + 1)
        elif k == '\x1b[D' and map.is_valid(line, column-1) and not map.is_obstacle(line, column-1) :
            if map.is_door(line, column-1):
                return map.get_other_door_position(line, column-1)
            return (line, column - 1)
        elif k == '\x1b[A' or k == '\x1b[B' or k == '\x1b[C' or k == '\x1b[D':
            return "same"
        else:
            return None

def clear():
    os.system('clear')
def wait(t):
    time.sleep(0.5)
