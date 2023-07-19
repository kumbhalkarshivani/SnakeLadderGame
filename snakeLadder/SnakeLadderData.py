import random


class SnakeOrLadder:
    snakePositions = {
        17:7,
        54:34,
        62:19,
        64:60,
        87:36,
        93:73,
        95:75,
        98:79
    }
    LadderPostions = {
        1:38,
        4:14,
        9:31,
        21:42,
        28:84,
        51:67,
        72:91,
        80:99
    }
    text_for_player_turn = [
            "Its your turn. Hit enter to roll the dice.",
            "Are you prepared?",
            "Lets Go.",
            "Please move along.",
            "You are doing great.",
            "Ready to be a champion."
    ]

    #function for printing the text for snake bite
    text_for_snake_bite = [
            "boom!",
            "bang!",
            "snake bite",
            "oops!",
            "dang",
            "oh shit",
            "alas!"
    ]

    #function for printing the text for ladder jump
    text_for_ladder_jump = [
            "yipee!",
            "wahoo!",
            "hurrah!",
            "oh my Goodness...",
            "you are on fire",
            "you are a champion",
            "you are going to win this"
    ]
    def is_snake_or_ladder(self, new_position):
        if new_position in self.snakePositions.keys():
            print(f"{random.choice(self.text_for_snake_bite)} snake bite at {new_position} position")
            return self.snakePositions[new_position]
        elif new_position in self.LadderPostions.keys():
            print(f"{random.choice(self.text_for_ladder_jump)} got ladder at {new_position} position")
            return self.LadderPostions[new_position]
        else:
            return new_position