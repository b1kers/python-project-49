import random
from abc import ABC, abstractmethod
from math import gcd

import prompt

from .cli import welcome_user


class BaseGame(ABC):
    """
    Abstract base class, there shall be intro in child classes
    """

    def __init__(self):
        self.name = welcome_user()
        self.intro = self.__doc__.strip()

    @abstractmethod
    def get_correct(self, riddle):
        pass

    @abstractmethod
    def get_riddle(self):
        pass

    def play(self):
        print(self.intro)
        row = 0
        while row < 3:
            riddle = self.get_riddle()
            print(f'Question: {riddle}')
            answer = prompt.string('Your answer: ')
            correct_answer = self.get_correct(riddle)
            if answer == correct_answer:
                print('Correct!')
                row += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct "
                        f"answer was '{correct_answer}'.")
                row = 0
        print(f'Congratulations, {self.name}!')


class EvenGame(BaseGame):
    """
    Answer "yes" if the number is even, otherwise answer "no".
    """

    def __init__(self):
        super().__init__()
    
    def get_riddle(self):
        return random.randint(0, 100)
    
    def get_correct(self, riddle):
        return 'yes' if riddle % 2 == 0 else 'no' 
    

class CalcGame(BaseGame):
    """
    What is the result of the expression?
    """

    def __init__(self):
        super().__init__()
    
    def get_riddle(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        op = random.choice(['+', '-', '*'])
        return f'{a} {op} {b}'
    
    def get_correct(self, riddle):
        return str(eval(riddle))
    

class GcdGame(BaseGame):
    """
    Find the greatest common divisor of given numbers.
    """

    def __init__(self):
        super().__init__()
    
    def get_riddle(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        return f'{a} {b}'
    
    def get_correct(self, riddle):
        return str(gcd(*[int(x) for x in riddle.split()]))