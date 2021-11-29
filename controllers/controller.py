from flask import render_template, request
from app import app
import controllers
from models.Game import Game
from models.Player import Player


@app.route("/")
def to_home():
    return render_template("welcome.html")


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
    result = Game.who_wins(new_game)

    if one_choice and two_choice not in ["rock", "paper", "scissors"]:
        return render_template("fail.html")
    elif result == None:
        return render_template("welcome.html")
    else:
        return render_template(
            "index.html", result=result, weapon=one_choice, cpu_move=two_choice
        )


@app.route("/play")
def play():
    return render_template("play.html")


@app.route("/play/result", methods=["POST"])
def play_vs_cpu():
    one_choice = request.form["weapon_one"].lower()
    one_name = request.form["player_name"].lower()
    player_one = Player(one_name, one_choice)
    player_two = Player("Death Bot 3000", Game.cpu_move())
    new_game = Game(player_one, player_two)
    result = Game.who_wins(new_game)
    if result == None:
        return render_template("play.html")
    else:
        return render_template(
            "result.html",
            result=result,
            name=one_name,
            cpu=player_two.name,
            weapon=one_choice,
            cpu_move=player_two.choice,
        )


@app.route("/index")
def random_roll():
    one = Player("You", Game.cpu_move())
    two = Player("They", Game.cpu_move())
    game = Game(one, two)
    return render_template(
        "index.html", result=Game.who_wins(game), weapon=one.choice, cpu_move=two.choice
    )
