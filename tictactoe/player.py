import random
import math

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

class AIComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.avaliable_moves()) == 9:
            square = random.choice(game.avaliable_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif state.num_empty_squares() == 0:
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for move in state.avaliable_moves():
            state.make_move(move, player)
            sim_score = self.minimax(state, other_player)
            #undo move
            state.board[move] = ' '
            state.current_winner = None
            sim_score['position'] = move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
        