from utils import clear, wait

class Node:
    def __init__(self, position):
        self.neighbors = []
        self.position = position

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def get_neighbors(self): return self.neighbors

class Graph:
    def __init__(self):
        self.root = None
        self.seen = {}
        self.step = 0

    def create_graph_from_map(self, map, step):
        self.step = step
        starting_point = map.get_starting_point()
        self.root = Node(starting_point)
        self.addQ(self.root, starting_point, map)
        self.BFS(self.root, map)
        # self.DFS(self.root, map)

    def addQ_(self, node, position, map):
        q = [node]
        seen = {}
        hm_node = {}
        i = 0
        while q:
            node = q.pop(0)
            position = node.position
            line, column = position
            neighbors = map.get_neighbors(line, column)
            for neighbor in neighbors:
                if neighbor not in seen:
                    n = Node(neighbor)
                    node.add_neighbor(n)
                    q.append(n)
                    seen[neighbor] = node

    def addQ(self, node, position, map):
        q = [node]
        seen = {}
        i = 0
        while q:
            node = q.pop(0)
            position = node.position
            line, column = position
            if map.is_door(line, column):
                door_line, door_column = map.get_other_door_position(line, column)
                door_neighbors = map.get_neighbors(door_line, door_column)
                for neighbor in door_neighbors:
                    n = Node(neighbor)
                    node.add_neighbor(n)
                    q.append(n)
                    seen[neighbor] = node
            else:
                neighbors = map.get_neighbors(line, column)
                for neighbor in neighbors:
                    if neighbor not in seen:
                        n = Node(neighbor)
                        node.add_neighbor(n)
                        q.append(n)
                        seen[neighbor] = node




    def add(self, node, position, map):
        self.seen[position] = node
        line, column = position
        neighbors = map.get_neighbors(line, column)
        for neighbor in neighbors:
            n = Node(neighbor)
            node.add_neighbor(n)
            if neighbor not in self.seen:
                self.add(n, neighbor, map)

    def BFS(self, node, map):
        q = [node]
        seen = {}
        arrival_position = map.get_arrival_point()
        start_position = map.get_starting_point()
        while q:
            current_node = q.pop(0)
            neighbors = current_node.get_neighbors()

            # Display progression algorithm
            # map.mark_at_position_and_display(current_node.position[0], current_node.position[1], map.get_map())

            if arrival_position == current_node.position:
                self.construct_path(seen, arrival_position, start_position, map)
                break
            for neighbor in neighbors:
                if neighbor.position not in seen:
                    q.append(neighbor)
                    seen[neighbor.position] = current_node

    def DFS(self, node, map):
        if node:
            map.mark_at_position_and_display(node.position[0], node.position[1], map)
            for neighbor in node.get_neighbors():
                self.DFS(neighbor, map)

    def construct_path(self, seen, arrival_position, start_position, map):

        position = arrival_position
        path = []
        map_layout = map.get_map()
        while position != start_position:
            path.append(position)
            position = seen[position].position
        minimum_step_count = len(path)
        for position in reversed(path):
            map.mark_at_position_and_display(position[0], position[1], map_layout)
            if minimum_step_count == self.step:
                print("YOU WON!")
            else:
                print("YOU LOST")
                print("You did ", self.step - minimum_step_count, " steps more than the minimum")
                print("Here is the shortest path")
