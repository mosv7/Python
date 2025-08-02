
# class Backend:
#     def __init__(self):
#         self.playerturn = 'X'
    
#     def switch_turn(self):
#         self.playerturn = 'O' if self.playerturn == 'X' else 'X'
    
#     def check_winner(self, board):
#         n = len(board)
#         # Check rows and columns
#         for i in range(n):
#             if all(board[i][j] == self.playerturn for j in range(n)) or all(board[j][i] == self.playerturn for j in range(n)):
#                 print(f'Player {self.playerturn} wins!')
#                 return True
#         # Check diagonals
#         if all(board[i][i] == self.playerturn for i in range(n)) or all(board[i][n - 1 - i] == self.playerturn for i in range(n)):
#             print(f'Player {self.playerturn} wins!')
#             return True
#         # Check for draw
#         if all(board[i][j] != ' ' for i in range(n) for j in range(n)):
#             print("It's a draw!")
#             return True
#         return False

#     def make_move(self, move, board):
#         if board[move[0] - 1][move[1] - 1] == ' ':
#             board[move[0] - 1][move[1] - 1] = self.playerturn



# class Frontend:
#     def __init__(self):
#         self.backend = Backend()
    
#     def draw_board(self, n):
#         self.board = [[' ' for _ in range(n)] for _ in range(n)]
#         for row in self.board:
#             print('|'.join(row))

#     def isvalid_move(self, move, n):
#         return (1 <= move[0] <= n and 1 <= move[1] <= n) and (self.board[move[0] - 1][move[1] - 1] == ' ')

#     def playermove(self, n):
#         playermove = tuple(map(int, input(f'Player {self.backend.playerturn}, make a move: ').split()))
#         while not self.isvalid_move(playermove, n):
#             print("Invalid move. Please try again.")
#             playermove = tuple(map(int, input(f'{self.backend.playerturn}, make a move: ').split()))
#         return playermove

#     def board_size_validation(self):
#         n = int(input("Enter the size of the Tic Tac Toe board (n x n): "))
#         while n < 3:
#             print("Board size must be at least 3. Please try again.")
#             n = int(input("Enter the size of the Tic Tac Toe board (n x n): "))
#         return n

#     def play_game(self):
#         n = self.board_size_validation()
#         self.draw_board(n)
#         while True:
#             move = self.playermove(n)
#             self.backend.make_move(move, self.board)
#             for row in self.board:
#                 print('|'.join(row))
#             if self.backend.check_winner(self.board):
#                 break
#             self.backend.switch_turn()

#     def start_game(self):
#         playagain = 'y'
#         while playagain.lower() == 'y':
#             self.play_game()
#             playagain = input("Do you want to play again? (y/n): ")

# frontend = Frontend()
# frontend.start_game()


# Doctor solution

def find_winner(board):
    n = len(board)

    start_dir = [(r, 0, 0, 1) for r in range(n)]
    start_dir.extend([(0, c, 1, 0) for c in range(n)])
    start_dir.append((0, 0, 1, 1))
    start_dir.append((0, n - 1, 1, -1))

    for r, c, dr, dc in start_dir:
        player = board[r][c]
        if player == ' ':
            continue
        is_win = True
        for s in range(n):
            if board[r][c] != player:
                is_win = False
                break
            r, c = r + dr, c + dc
        if is_win:
            return player
    return None



if __name__ == '__main__':
    n = int(input("Enter the size of the Tic Tac Toe board (n x n): "))
    assert n >= 3, "Board size must be at least 3."
    board = [[' ' for _ in range(n)] for _ in range(n)]
    symbols = 'XO'
    steps, turn = 0, 0

    while True:
        if steps == n * n:
            print("It's a draw!")
            break
        r, c = map(int, input(f"Player {symbols[turn]}, make a move (row col): ").split())
        r, c = r - 1, c - 1
        if not (0 <= r < n and 0 <= c < n) or board[r][c] != ' ':
            print("Invalid move. Try again.")
            continue
        board[r][c] = symbols[turn]
        print('\n'.join(['|'.join(row) for row in board]))

        if (winner := find_winner(board)):
            print(f"Player {winner} wins!")
            break
        turn = 1 - turn
        steps += 1
