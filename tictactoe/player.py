import random

class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = int(input(f"{self.letter}\'s turn. Input move (0-8): "))
            try:
                if square not in game.avaliable_moves():
                    raise ValueError
                else:
                    valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return square

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.avaliable_moves())
        return square

