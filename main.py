from player import create_player
from game import play_turn

def start_game():
    print("🎲 Welcome to Roll a Dice Game 🎲")

    name1 = input("Enter Player 1 name: ")
    name2 = input("Enter Player 2 name: ")

    p1 = create_player(name1)
    p2 = create_player(name2)

    rounds = int(input("Enter number of rounds: "))

    for i in range(rounds):
        print(f"\n===== Round {i+1} =====")
        play_turn(p1)
        play_turn(p2)

    print("\n🏁 FINAL RESULT 🏁")
    print(f"{p1['name']} : {p1['score']}")
    print(f"{p2['name']} : {p2['score']}")

    if p1["score"] > p2["score"]:
        print(f"🏆 Winner: {p1['name']}")
    elif p2["score"] > p1["score"]:
        print(f"🏆 Winner: {p2['name']}")
    else:
        print("🤝 It's a Tie!")

start_game()