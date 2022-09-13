from platform import node
from globals import *
from node import *
import random

class Board:
    nodes = []
    def create_nodes(self):
        for i in range(1, 55):
            self.nodes.append(Node())

    def populate_neighbours(self):
        for i in range(1,55):
            self.nodes[i-1].neighbours = NEIGHBOUR_TABLE[i]

    def place_tiles(self):
        tiles_remaining = RESOURCE_TILES.copy()
        tokens_remaining = NUMBER_TOKENS.copy()
        random.shuffle(tiles_remaining)
        random.shuffle(tokens_remaining)
        for i in range(1,20):
            current_tile = tiles_remaining.pop()
            current_token = tokens_remaining.pop()
            for node_ref in HEX_TILES[i]:
                
                if current_token not in self.nodes[node_ref-1].resources:
                    self.nodes[node_ref-1].resources[current_token] = [current_tile]
                else:
                    self.nodes[node_ref-1].resources[current_token].append(current_tile) 

    def __init__(self):
        self.create_nodes()
        self.populate_neighbours()
        self.place_tiles()

Board()