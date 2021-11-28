class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def who_wins(self):
        if self.player_one.choice == self.player_two.choice:
            return None
        elif self.player_one.choice == "rock":
            if self.player_two.choice == "paper":
                return "Paper wraps rock! Player two wins."
            else:
                return "Rock smashes scissors! Player one wins."
        elif self.player_one.choice == "paper":
            if self.player_two.choice == "scissors":
                return "Scissors cut paper! Player two wins."
            else:
                return "Paper wraps rock! Player one wins."
        elif self.player_one.choice == "scissors":
            if self.player_two.choice == "rock":
                return "Rock smash scissors! Player two wins."
            else:
                return "Scissors cut paper! Player one wins."
