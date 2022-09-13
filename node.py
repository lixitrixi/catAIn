from player import *

class Node:
    def __init__():
        self.player = NonePlayer()
        self.structure = 0
        self.neighbours = set()
        self.resources = dict()

    def allot(self, num):
        '''
        Allot the owner of a node the resources for a given dice roll
        multiplied by the structure level (0-2) of the node

        num: the dice roll
        '''
        for r in self.resources[num]:
            self.player.hand[r] += self.structure
