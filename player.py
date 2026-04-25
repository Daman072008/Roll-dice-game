def create_player(name):
    return {
        "name": name,
        "score": 0
    }

def add_score(player, value):
    player["score"] += value