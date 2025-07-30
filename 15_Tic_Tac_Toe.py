
class Backend:
    def __init__(self):
        self.playerturn = 'X'
    
    def switch_turn(self):
        self.playerturn = 'O' if self.playerturn == 'X' else 'X'
    
    def check_winner(self, board):
        n = len(board)
        # Check rows and columns
        for i in range(n):
            if all(board[i][j] == self.playerturn for j in range(n)) or all(board[j][i] == self.playerturn for j in range(n)):
                print(f'Player {self.playerturn} wins!')
                return True
        # Check diagonals
        if all(board[i][i] == self.playerturn for i in range(n)) or all(board[i][n - 1 - i] == self.playerturn for i in range(n)):
            print(f'Player {self.playerturn} wins!')
            return True
        # Check for draw
        if all(board[i][j] != ' ' for i in range(n) for j in range(n)):
            print("It's a draw!")
            return True
        return False

    def make_move(self, move, board):
        if board[move[0] - 1][move[1] - 1] == ' ':
            board[move[0] - 1][move[1] - 1] = self.playerturn



class Frontend:
    def __init__(self):
        self.backend = Backend()
    
    def draw_board(self, n):
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        for row in self.board:
            print('|'.join(row))

    def isvalid_move(self, move, n):
        return (1 <= move[0] <= n and 1 <= move[1] <= n) and (self.board[move[0] - 1][move[1] - 1] == ' ')

    def playermove(self, n):
        playermove = tuple(map(int, input(f'Player {self.backend.playerturn}, make a move: ').split()))
        while not self.isvalid_move(playermove, n):
            print("Invalid move. Please try again.")
            playermove = tuple(map(int, input(f'{self.backend.playerturn}, make a move: ').split()))
        return playermove

    def board_size_validation(self):
        n = int(input("Enter the size of the Tic Tac Toe board (n x n): "))
        while n < 3:
            print("Board size must be at least 3. Please try again.")
            n = int(input("Enter the size of the Tic Tac Toe board (n x n): "))
        return n

    def play_game(self):
        n = self.board_size_validation()
        self.draw_board(n)
        while True:
            move = self.playermove(n)
            self.backend.make_move(move, self.board)
            for row in self.board:
                print('|'.join(row))
            if self.backend.check_winner(self.board):
                break
            self.backend.switch_turn()

    def start_game(self):
        playagain = 'y'
        while playagain.lower() == 'y':
            self.play_game()
            playagain = input("Do you want to play again? (y/n): ")

frontend = Frontend()
frontend.start_game()
