import random
from abc import ABC, abstractmethod
from math import gcd, sqrt

import prompt

from .cli import welcome_user


def is_prime(n):
    """
    Checks if an integer 'n' is a prime number.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
            
    return True


class BaseGame(ABC):
    """
    Abstract base class, there shall be intro in child classes
    """

    def __init__(self):
        self.name = welcome_user()
        self.intro = self.__doc__.strip()
        self.correct = None

    def get_correct(self, riddle):
        return self.correct

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
        riddle = random.randint(0, 100)
        self.correct = 'yes' if riddle % 2 == 0 else 'no'
        return riddle


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
        riddle = f'{a} {op} {b}'
        self.correct = str(eval(riddle))
        return riddle
    

class GcdGame(BaseGame):
    """
    Find the greatest common divisor of given numbers.
    """

    def __init__(self):
        super().__init__()
    
    def get_riddle(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        self.correct = f'{gcd(a, b)}'
        return f'{a} {b}'
    
    def get_correct(self, riddle):
        return self.correct
    

class ProgGame(BaseGame):
    """
    What number is missing in the progression?
    """

    def __init__(self):
        super().__init__()
    
    def get_riddle(self):
        start = random.randint(0, 20)
        step = random.randint(1, 10)
        prog_list = list()
        length = random.randint(5, 10)
        missing_idx = random.choice(range(length))
        for index in range(length):
            current = start + index * step
            if index == missing_idx:
                self.correct = str(current)
                prog_list.append('..')
            else:
                prog_list.append(current)
        return ' '.join(str(x) for x in prog_list)


class PrimeGame(BaseGame):
    """
    Answer "yes" if given number is prime. Otherwise answer "no".
    """

    def __init__(self):
        super().__init__()

    def get_riddle(self):
        number = random.randint(0, 100)
        self.correct = 'yes' if is_prime(number) else 'no'
        return f'{number}'
