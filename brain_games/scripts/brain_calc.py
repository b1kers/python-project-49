from brain_games.cli import welcome_user
from brain_games.common import CalcGame


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game = CalcGame(name)
    game.play()


if __name__ == "__main__":
    main()
