import random
from abc import ABC, abstractmethod

import prompt


class BaseGame(ABC):

    def __init__(self, name, intro):
        self.name = name
        self.intro = intro

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

    def __init__(self, name, intro='Answer "yes" if the number is even, otherwise answer "no".'):
        super().__init__(name, intro)
    
    def get_riddle(self):
        return random.randint(0, 100)
    
    def get_correct(self, riddle):
        return 'yes' if riddle % 2 == 0 else 'no' 
    

class CalcGame(BaseGame):

    def __init__(self, name, intro='What is the result of the expression?'):
        super().__init__(name, intro)
    
    def get_riddle(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        op = random.choice(['+', '-', '*'])
        return f'{a} {op} {b}'
    
    def get_correct(self, riddle):
        return str(eval(riddle))