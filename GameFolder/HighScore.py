def load_high_score():
    try:
        with open("saved_score/highscore.txt", "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0
def save_high_score(score):
    with open("saved_score/highscore.txt", "w") as file:
        file.write(str(score))