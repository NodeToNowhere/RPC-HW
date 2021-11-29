import random


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def who_wins(self):
        if self.player_one.choice == self.player_two.choice:
            return "It's a draw."
        elif self.player_one.choice == "rock" and self.player_two.choice == "paper":
            return "Paper wraps rock! %s wins." % self.player_two.name

        elif self.player_one.choice == "rock" and self.player_two.choice == "scissors":
            return "Rock smashes scissors! %s wins." % self.player_one.name

        elif self.player_one.choice == "paper" and self.player_two.choice == "rock":
            return "Paper wraps rock! %s wins." % self.player_one.name

        elif self.player_one.choice == "paper" and self.player_two.choice == "scissors":
            return "Scissors cut paper! %s wins" % self.player_two.name

        elif self.player_one.choice == "scissors" and self.player_two.choice == "rock":
            return "Rock smashes scissors. %s wins" % self.player_two.name

        elif self.player_one.choice == "scissors" and self.player_two.choice == "paper":
            return "Scissors cut paper! %s wins." % self.player_one.name

    def cpu_move():
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
