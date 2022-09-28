from board import Board
from errors import *
from node import Node
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
    
    def build_settlement(self, player:Player, node:Node):
        if node.structure: raise BuildException()
        if not node.road_connections[player]: raise BuildException()
        if any(n.structure for n in node.neighbours): raise BuildException()

        player.spend(SETTLEMENT_COST)
        board.place_settlement(player, node)
        player.change_vp(1)
    
    def build_city(self, player:Player, node:Node):
        if node.structure != 1: raise BuildException()
        if node.player != player: raise BuildException()

        player.spend(CITY_COST)
        board.place_city(player, node)
        player.change_vp(1)
