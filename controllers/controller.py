from flask import render_template, request
from app import app
from models.Game import Game
from models.Player import Player

winner = ""


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/<weapon_one>/<weapon_two>")
def pass_choices(weapon_one, weapon_two):
    one_choice = weapon_one.lower()
    two_choice = weapon_two.lower()
    player_one = Player("Player One", one_choice)
    player_two = Player("Player Two", two_choice)
    new_game = Game(player_one, player_two)
    winner = Game.who_wins(new_game)

    if one_choice and two_choice not in ["rock", "paper", "scissors"]:
        return render_template("welcome.html")
    elif winner == None:
        return render_template("welcome.html")
    else:
        return render_template("winner.html", result=winner)
