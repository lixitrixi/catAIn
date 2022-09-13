
class Player:
    def __init__(self):
        self.hand = {
            'brick': 0,
            'grain': 0,
            'lumber': 0,
            'ore': 0,
            'wool': 0
        }
        self.dev_cards = []
        self.vp = 0

    def change_vp(self, p) -> bool:
        self.vp += p
        return self.vp >= 10

class NonePlayer(Player):
    ...
