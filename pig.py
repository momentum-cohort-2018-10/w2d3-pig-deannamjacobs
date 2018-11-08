import random


class Player:

    def __init__(self, current_score, round_score, total_score, computer_player):
        self.current_score = current_score
        self.total_score = total_score
        self.computer_player = computer_player

    def roll(self):
        self.current_score = random.randint(1, 6)
        self.total_score = self.current_score + self.total_score
        print(roll)

    def add_points(self, points):
        self.score += points


class Game:

    def __init__(self, computer_player, human_player):
        self.computer_player = computer_player
        self.human_player = human_player

    def pick_who_is_first(self):
        return random.choice(self.computer_player, self.human_player)
        # this function randomly chooses who rolls first

    def take_turn(self, player):

        if player == self.computer_player:
            while player.current_score != 1:
             # player.total_score < 21 and player.current_score != 1:
                player.roll()
        elif player == self.human_player:
            choice = input("Would you like to roll?  Please type Y or N.")
            while choice == "Y":
                player.roll()
                if player.current_score == 1:
                    return
                choice = input(
                    "Would you like to roll again?  Pleae type Y or N.")
            return
