from GuessGame import GuessGame
class ConsoleGame(GuessGame):
    def __init__(self):
        self.welcome = "wellcome"
        self.prompt = "input number："
        self.correct = "you get it!!"
        self.bigger = "your number is bigger"
        self.smaller = "your number is smaler"
    
    def message(self, msg):
        print(msg)
    
    def guess(self):
        return int(input(self.prompt))

game = ConsoleGame()
game.go()