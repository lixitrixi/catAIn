class Action:
    def __init__(self, game, do, player):
        '''
        do: Game method
        '''
        self.game = game
        self.do = do
        self.player = player