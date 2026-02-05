import random

import prompt

from brain_games.cli import welcome_user
from brain_games.common import EvenGame


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    row = 0
    while row < 3:
        riddle = random.randint(0, 100)
        print(f'Question: {riddle}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if riddle % 2 == 0 else 'no' 
        if answer == correct_answer:
            print('Correct!')
            row += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct "
                    f"answer was '{correct_answer}'.")
            row = 0
    print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game = EvenGame(name)
    game.play()


if __name__ == "__main__":
    main()
