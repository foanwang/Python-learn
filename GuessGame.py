import random
from abc import ABCMeta, abstractmethod
class GuessGame(metaclass=ABCMeta):
    @abstractmethod
    def message(self, msg):
        pass
    
    @abstractmethod
    def guess(self):
        pass
    
    def go(self):
        self.message(self.welcome)
        number = int(random.random() * 10)
        while True:
            guess = self.guess();
            if guess > number:
                self.message(self.bigger)
            elif guess < number:
                self.message(self.smaller)
            else:
                break
        self.message(self.correct)