from utils import clear, wait

class Map:
    def __init__(self):
        self.map = [
                        ['📍', '.', '.', '.', '.', '.', '.', '⛔️', '.', '.', '.', '.', '.', '.'],
                        ['.', '⛔️', '⛔️', '.', '.', '.', '.', '⛔️', '.', '⛔️', '.', '.', '.', '🚪'],
                        ['.', '⛔️', '⛔️', '⛔️', '.', '⛔️', '.', '⛔️', '.', '⛔️', '.', '.', '.', '.'],
                        ['.', '⛔️', '.', '.', '.', '⛔️', '🚪', '⛔️', '.', '.', '⛔️', '.', '.', '.'],
                        ['.', '⛔️', '.', '.', '.', '⛔️', '.', '⛔️', '⛔️', '.', '⛔️', '.', '.', '.'],
                        ['.', '⛔️', '.', '⛔️', '.', '⛔️', '.', '⛔️', '.', '.', '⛔️', '.', '.', '.'],
                        ['.', '⛔️', '.', '⛔️', '.', '⛔️', '⛔️', '⛔️', '.', '.', '⛔️', '.', '.', '.'],
                        ['.', '⛔️', '.', '⛔️', '.', '⛔️', '.', '.', '⛔️', '⛔️', '.', '.', '.', '.'],
                        ['.', '.', '.', '⛔️', '.', '.', '.', '🏁', '.', '.', '.', '.', '.', '.']
                    ]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.starting_char = '📍'
        self.arrival_char = '🏁'
        self.path_char = '🏎'
        self.obstacle_char = '⛔️'
        self.door_char = '🚪'
        self.path = []
        self.waiting_time = 0.01
        self.previous_position = None

    def get_height(self): return self.height

    def get_width(self): return self.width

    def get_starting_point(self):
        for line in range(len(self.map)):
            for column in range(len(self.map[0])):
                if self.map[line][column] == self.starting_char:
                    return (line, column)
        return None

    def get_arrival_point(self):
        for line in range(len(self.map)):
            for column in range(len(self.map[0])):
                if self.map[line][column] == self.arrival_char:
                    return (line, column)
        return None

    def get_map(self): return self.map

    def print_map_(self, map):
        for line in map:
            print(line)
    
    def print_map(self, map):
        for line in map:
            for e in line:
                print(e, end=' ')
            print()

    def get_dummy_path(self):
        return [(0,0), (0,1), (0,2), (0,3), (0,4), (1,4), (2,4)]

    def display_path(self):
        path = self.get_dummy_path()
        map = self.get_map()
        for position in path:
            clear()
            line, column = position
            map[line][column] = self.path_char
            self.print_map(map)
            wait(self.waiting_time)

    def get_path_shortest_path(self):
        return self.get_dummy_path()

    def get_char_at_position(self, line, column):
        return self.map[line][column]

    def get_neighbors(self, line, column):
        neighbors = []
        if line > 0 and not self.is_obstacle(line-1, column): neighbors.append((line-1, column))
        if line < self.height-1 and not self.is_obstacle(line+1, column): neighbors.append((line+1, column))
        if column > 0 and not self.is_obstacle(line, column-1): neighbors.append((line, column-1))
        if column < self.width-1 and not self.is_obstacle(line, column+1): neighbors.append((line, column+1))
        return neighbors

    def get_other_door_position(self, line, column):
        for _line in range(len(self.map)):
            for _column in range(len(self.map[0])):
                if self.map[_line][_column] == self.door_char and (line != _line or _column != column):
                    return (_line, _column)
        return None


    def is_obstacle(self, line, column):
        return self.map[line][column] == self.obstacle_char

    def is_valid(self, line, column):
        return line >= 0 and column >= 0 and line <= self.height-1 and column <= self.width-1

    def is_door(self, line, column):
        return self.map[line][column] == self.door_char

    def mark_at_position_and_display(self, line, column, map):
        if self.previous_position:
            previous_position_line, previous_position_column = self.previous_position 
            if not self.is_door(previous_position_line, previous_position_column):
                self.map[previous_position_line][previous_position_column] = '✨'
        self.previous_position = (line, column)
        if not self.is_door(line, column):
            self.map[line][column] = self.path_char
        wait(1)
        clear()
        self.print_map(map)



