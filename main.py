from Game import Game
from Graph import Graph
from Map import Map

def solver():
    map = Map()
    game = Game(map)
    graph = Graph()
    step = game.start()
    graph.create_graph_from_map(map, step)

if __name__ == '__main__':
    solver()
