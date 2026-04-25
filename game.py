from dice import roll_dice
from player import add_score

def play_turn(player):
    input(f"\n{player['name']} press Enter to roll dice...")

    value = roll_dice()
    print(f"{player['name']} rolled: {value}")

    add_score(player, value)
    print(f"{player['name']} score: {player['score']}")