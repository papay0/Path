from utils import get_input
from utils import clear
from copy import deepcopy

class Game:
    def __init__(self, map):
        self.map = map
        self.start_position = map.get_starting_point()
        self.arrival_position = map.get_arrival_point()
        self.map_layout = deepcopy(map.get_map())

    def main_loop_game(self):
        position = self.start_position
        step = 0
        previous_position = None
        while position != self.arrival_position:
            self.map.print_map(self.map_layout)
            print("Next move? (Use arrow key to play, something else to quit)")
            print("Current step count: ", step)
            position_tmp = get_input(position, self.map)
            if not position_tmp:
                print("BYE BYE!")
                exit(-1)
            elif position_tmp == "same":
                pass
                clear()
            else:
                if previous_position:
                    previous_position_line, previous_position_column = previous_position
                    self.map_layout[previous_position_line][previous_position_column] = '✨'
                position = position_tmp
                line, column = position
                self.map_layout[line][column] = '🚗'
                previous_position = position
                clear()
                step += 1
        return step


    def start(self):
        self.init()
        return self.main_loop_game()


    def init(self):
        print("Welcome to my find shortest path")
        print("Push a key to start")
        input()
        clear()






