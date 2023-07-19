from snakeLadder.Dice import Dice

class Player:
    def __init__(self, name, position):
        self.name = name
        self.rank = 0
        self.position = position

    def player_current_position(self):
        return self.position

    def throws_dice(self):
        return Dice.throw_a_dice()

    def update_player_position(self,newPosition):
        self.position = newPosition

    def get_rank(self):
        return self.rank

    def set_rank(self, r):
        self.rank = r
