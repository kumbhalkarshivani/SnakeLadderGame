from snakeLadder.Player import Player
from snakeLadder.SnakeLadderData import SnakeOrLadder
import random


# get number of player form the user
number_of_Players = int(input("Enter number players : "))

# Limiting number of player to 4
if number_of_Players > 4:
    print("Maximum 4 players can play the Game. Starting game with four players")
    number_of_Players = 4

Players = []
won_players = []

# Player object creation
for index in range(1, number_of_Players+1):
    name = input(f"Enter Player{index} Name :: ")
    Players.append(Player(name,0))

# Keepling Rank at 0
rank = 0

# looping through number of player in the Players list till only one plater is left on board
while(len(Players) !=1):
    #iterating player one by one
    for player in Players:
        print(f"{player.name} {random.choice(SnakeOrLadder.text_for_player_turn)}")
        input("Press enter to roll the dice : ")
        # get random value form 1 to 6
        dice_output = player.throws_dice()
        print("Dice output ", dice_output)

        # new position of player after rolling dice
        newPosition = player.player_current_position() + dice_output

        if newPosition == 100:
            # Win condition
            rank += 1
            print(f"Hurreyyyyyyy {player.name} Won The Game with rank {rank} !!!!!!" )
            player.set_rank(rank)
            won_players.append(player)
            removed_Player = Players.pop(Players.index(player))
        elif newPosition > 100:
            # Player is near finish point but getting more number on dice than required
            steps_to_win = 100 - player.player_current_position()
            print(f"{player.name} need {steps_to_win} steps to win but you got {dice_output} on dice")
        else:
            # new position of player if snake bite or got ladder
            newPosition = SnakeOrLadder().is_snake_or_ladder(newPosition)
            player.update_player_position(newPosition)
            print(f"{player.name}'s new position : ", player.player_current_position())
        print("-------------------------------------------------------------")
else:
    for player in won_players:
        print(f"{player.name} WON with rank {player.rank}")
    print(f"{Players[0].name} Better Luck Next Time!!")

