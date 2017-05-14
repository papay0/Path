from utils import clear, wait

class Map:
    def __init__(self):
        self.map = [
                        ['S', 'U', '-', '-', '-', '-', '-', '-', 'U', '-', '-', '-', '-', '-'],
                        ['-', 'U', '-', '-', '-', '-', '-', '-', 'U', '-', '-', '-', '-', '-'],
                        ['-', 'U', '-', '-', '-', 'U', '-', 'U', '-', '-', '-', '-', '-', '-'],
                        ['-', 'U', '-', '-', '-', 'U', '-', 'U', '-', '-', '-', '-', '-', '-'],
                        ['-', 'U', '-', '-', 'U', 'U', '-', 'U', 'U', '-', '-', '-', '-', '-'],
                        ['A', 'U', '-', 'U', 'U', '-', '-', 'U', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', 'U', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', 'U', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', 'U', '-', '-', '-', '-', '-', '-', '-', '-']
                    ]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.starting_char = 'S'
        self.arrival_char = 'A'
        self.path_char = 'X'
        self.obstacle_char = 'U'
        self.path = []
        self.waiting_time = 0.01

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

    def print_map(self, map):
        for line in map:
            print(line)

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

    def is_obstacle(self, line, column):
        return self.map[line][column] == self.obstacle_char

    def is_valid(self, line, column):
        return line >= 0 and column >= 0 and line <= self.height-1 and column <= self.width-1

    def mark_at_position_and_display(self, line, column, map):
        self.map[line][column] = self.path_char
        self.print_map(map)
        wait(1)
        clear()