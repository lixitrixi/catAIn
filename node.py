from player import *

class Node:
    def __init__(self):
        self.player = NonePlayer()
        self.structure = 0
        self.neighbours = []
        self.resources = dict()
        self.road_connections = dict()

    def allot(self, num:int) -> None:
        '''
        Allot the owner of a node the resources for a given dice roll
        times the structure level (0-2) of the node

        num: the dice roll
        '''
        for r in self.resources[num]:
            # gain 0 if empty, 1 if settlement, 2 if city
            self.player.hand[r] += self.structure
