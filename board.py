import random

from globals import *
from node import *
from player import *


class Board:
    '''
    Contains board-related objects and methods

    DO NOT USE THIS CLASS FOR INTERFACING WITH THE GAME, USE :obj:`Game` METHODS INSTEAD
    '''
    def __init__(self, players=[]):
        '''
        players: a list of player objects, used for speeding up certain calcs
        '''
        self.players = players
        self.init_nodes()
        self.init_tiles()

    def init_nodes(self):
        '''
        populate :attr:`node.neighbours` and :attr:`node.road_connections`
        '''
        self.nodes = [Node() for _ in range(54)] # initially empty nodes, connections are set up in init_nodes
        for i in range(54):
            self.nodes[i].neighbours = [self.nodes[n] for n in NEIGHBOUR_NODES[i]]
            self.nodes[i].road_connections = {p: [] for p in self.players} # initialize empty dict items for speed

    def init_tiles(self):
        '''
        Assign hex tile locations and assign nodes the relevant resource mappings
        '''
        tiles_remaining = RESOURCE_TILES.copy()
        tokens_remaining = NUMBER_TOKENS.copy()
        random.shuffle(tiles_remaining)
        random.shuffle(tokens_remaining)
        for i in range(19):
            current_tile = tiles_remaining.pop()
            if current_tile == 'desert': continue

            current_token = tokens_remaining.pop()
            for node_id in HEX_POINTS[i]:
                current_node = self.nodes[node_id]
                
                if current_token not in current_node.resources:
                    current_node.resources[current_token] = []
                current_node.resources[current_token].append(current_tile)
    
    def place_settlement(self, player:Player, node:Node):
        node.player = player
        node.structure = 1
    
    def place_city(self, player:Player, node:node):
        node.structure = 2

    def place_road(self, player:Player, nodeA:Node, nodeB:Node):
        '''
        Links two nodes together using their :attr:`road_connection` attribute
        '''
        nodeA.road_connections[player].append(nodeB)
        nodeB.road_connections[player].append(nodeA)
    
    def max_road_length(self, node_id:int, player:Player):
        '''
        Wrapper method for :meth:`flood_search`.
        Returns the maximum road length owned by a player

        node_id: the ID of the node to start the search at

        player: the player object being checked
        '''
        res = self.flood_search(self.nodes[node_id], [], 0)

    @staticmethod
    def flood_search(node:Node, visited:list[Node], n:int):
        '''
        Recursively searches along node connections
        '''
        ...

Board()
