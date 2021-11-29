from math import exp
from random import choices
import unittest
import random

from controllers import controller
from models.Player import Player
from models.Game import Game


class TestRPS(unittest.TestCase):
    def setUp(self):
        self.player_one = Player("Ben", "rock")
        self.player_two = Player("Stacy", "paper")
        self.player_three = Player("Doug", "rock")
        self.player_four = Player("Sid", "scissors")

        self.game_one = Game(self.player_one, self.player_two)
        self.game_two = Game(self.player_one, self.player_three)
        self.game_three = Game(self.player_one, self.player_four)

    def test_has_name(self):
        expected = "Ben"
        actual = self.player_one.name
        self.assertEqual(expected, actual)

    def test_has_choice(self):
        expected = "rock"
        actual = self.player_one.choice

        self.assertEqual(expected, actual)

    def test_game_player_choice(self):

        expected = "paper"
        actual = self.game_one.player_two.choice

        self.assertEqual(expected, actual)

    def test_for_none(self):

        expected = None
        actual = Game.who_wins(self.game_two)

        self.assertEqual(expected, actual)

    def test_for_explicit_winner(self):

        expected = 'Paper wraps rock! %s wins.' % self.player_two.name
        actual = Game.who_wins(self.game_one)

        self.assertEqual(expected, actual)

    def test_for_implicit_winner(self):

        expected = 'Rock smashes scissors! %s wins.' % self.player_one.name
        actual = Game.who_wins(self.game_three)

        self.assertEqual(expected, actual)

    def test_for_random_cpu_move(self):
        choices = ["rock", "paper", "scissors"]

        expected = True
        
        actual = Game.cpu_move() in choices
        
        self.assertEqual(expected, actual)

    


# make sure to look at flask testing
