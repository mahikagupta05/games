import math
from player import HumanPlayer, ComputerPlayer, AIComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] #[0, 1, 2, 3, 4, 5, 6, 7, 8] except # = ' '
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #[0:3], [3:6], [6:9]
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_w_nums():
        num_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in num_board:
            print('| '+ ' | '.join(row) + ' |')     # 0 | 1 | 2

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def avaliable_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] #returns the indice/num for any ' ' empty spots aka avaliable moves

    def winner(self, square, letter):
        #checking row options
        row_num = square // 3
        row = self.board[row_num*3:(row_num+1)*3]
        #print("row", row)
        if all([s == letter for s in row]):
            return True
        #checking column options
        col_num = square % 3
        column = [self.board[col_num+m*3] for m in range(3)]
        #print("col", column)
        if all([s == letter for s in column]):
            return True
        #checking diagonals
        if square % 2 == 0: #this means it is in a spot where there could be a diagonal (corner or middle)
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #\
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #/
            if all([s == letter for s in diagonal2]):
                return True
        #print("d1", diagonal1)
        #print("d2", diagonal2)
        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_w_nums()
    
    letter = 'O'
    while game.empty_squares(): #while function returns empty spaces
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter
            #swap letters
            letter = 'X' if letter == 'O' else 'O'
    if print_game:
        print("It\'s a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = AIComputerPlayer('O')
    tic = TicTacToe()
    play(tic, x_player, o_player, print_game=True)

        
