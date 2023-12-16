import copy
from tabulate import tabulate as tb
# Creating a 6x7 2D array

rows = 6
cols = 7
board = [[0 for _ in range(cols)] for _ in range(rows)]

def LastFreeRow(board,col):
    for i in range(rows-1, -1, -1):
        if(board[i][col] == 0):
            return i
    return -1 # if no free row
        

class ConnectFour:
    def __init__ (self,board):
        self.board =  board
    def succ(self,s,a,p):
        row = LastFreeRow(s,a)
        if(self.IsValidMove(row)):
            succ =copy.deepcopy(s)
            succ[row][a] = p
            return succ
        return None
    def IsValidMove(self,row):
        if(row < 0):
            return False
        return True
    

def is_winner(board, player):
    # Check for horizontal connect four
    for row in board:
        for i in range(4):
            if all(cell == player for cell in row[i:i+4]):
                return True

    # Check for vertical connect four
    for col in range(7):
        for i in range(3):
            if all(board[i + j][col] == player for j in range(4)):
                return True

    # Check for diagonal connect four (up-right direction)
    for i in range(3):
        for j in range(4):
            if all(board[i + k][j + k] == player for k in range(4)):
                return True

    # Check for diagonal connect four (up-left direction)
    for i in range(3):
        for j in range(3, 7):
            if all(board[i + k][j - k] == player for k in range(4)):
                return True

    return False

def is_board_full(board):
    # Check if the board is completely filled
    return all(cell != 0 for row in board for cell in row)


def PossibleMovesOnBoard(board):
    moves = []
    for i in range(cols):
        if(board[0][i] == 0):
            moves.append(i)
    return moves
class ActionUtility:
    def __init__ (self,utility,action):
        self.utility = utility
        self.action = action
# def Minimax(board,player):
#     print("azan")
#     if(is_board_full(board)):
#         return 0
#     if(is_winner(board,player)):
#         if(player == 1):
#             return -1
#         return 1
#     if(player == 2):
#         moves = PossibleMovesOnBoard(board)
#         values = []
#         for i in range(len(moves)):
#             board[LastFreeRow(board,moves[i])][moves[i]] = player
#             player = 3 - player
#             # values.append([Minimax(board,player),moves[i]])
#             values.append(ActionUtility(Minimax(board,player),moves[i]))
#             board[LastFreeRow(board,moves[i])][moves[i]] = 0
        
#         return  max(values, key=lambda x: x.utility)
        
#     if(player == 1):
#         moves = PossibleMovesOnBoard(board)
#         values = []
#         for i in range(len(moves)):
#             board[LastFreeRow(board,moves[i])][moves[i]] = player
#             player = 3 - player
#             # values.append([Minimax(board,player),moves[i]])
#             values.append(ActionUtility(Minimax(board,player),moves[i]))
#             board[LastFreeRow(board,moves[i])][moves[i]] = 0
        
#         return  min(values, key=lambda x: x.utility)


# def Minimax(board, player):
#     print(tb(board, tablefmt="grid"))
#     if is_board_full(board):
#         return ActionUtility(0, None)

#     if is_winner(board, player):
#         if player == 1:
#             return ActionUtility(-1, None)
#         return ActionUtility(1, None)

#     if player == 2:
#         moves = PossibleMovesOnBoard(board)
#         best_move = None
#         max_utility = float('-inf')

#         for i in range(len(moves)):
#             board[LastFreeRow(board, moves[i])][moves[i]] = player
#             player = 3 - player
#             current_utility = Minimax(copy.deepcopy(board), player).utility
#             # board[LastFreeRow(board, moves[i])][moves[i]] = 0

#             if current_utility > max_utility:
#                 max_utility = current_utility
#                 best_move = moves[i]

#         return ActionUtility(max_utility, best_move)

#     if player == 1:
#         moves = PossibleMovesOnBoard(board)
#         best_move = None
#         min_utility = float('inf')

#         for i in range(len(moves)):
#             board[LastFreeRow(board, moves[i])][moves[i]] = player
#             player = 3 - player
#             current_utility = Minimax(copy.deepcopy(board), player).utility
#             # board[LastFreeRow(board, moves[i])][moves[i]] = 0

#             if current_utility < min_utility:
#                 min_utility = current_utility
#                 best_move = moves[i]

#         return ActionUtility(min_utility, best_move)


#alpha beta pruning
        

# def Minimax(board, player, alpha=float('-inf'), beta=float('inf')):
#     print(tb(board, tablefmt="grid"))
#     if is_board_full(board):
#         return ActionUtility(0, None)

#     if is_winner(board, player):
#         if player == 1:
#             return ActionUtility(-1, None)
#         return ActionUtility(1, None)

#     if player == 2:
#         moves = PossibleMovesOnBoard(board)
#         best_move = None
#         max_utility = float('-inf')

#         for i in range(len(moves)):
#             board[LastFreeRow(board, moves[i])][moves[i]] = player
#             player = 3 - player
#             current_utility = Minimax(copy.deepcopy(board), player, alpha, beta).utility
#             # board[LastFreeRow(board, moves[i])][moves[i]] = 0

#             if current_utility > max_utility:
#                 max_utility = current_utility
#                 best_move = moves[i]

#             alpha = max(alpha, max_utility)
#             if beta <= alpha:
#                 break

#         return ActionUtility(max_utility, best_move)

#     if player == 1:
#         moves = PossibleMovesOnBoard(board)
#         best_move = None
#         min_utility = float('inf')

#         for i in range(len(moves)):
#             board[LastFreeRow(board, moves[i])][moves[i]] = player
#             player = 3 - player
#             current_utility = Minimax(copy.deepcopy(board), player, alpha, beta).utility
#             # board[LastFreeRow(board, moves[i])][moves[i]] = 0

#             if current_utility < min_utility:
#                 min_utility = current_utility
#                 best_move = moves[i]

#             beta = min(beta, min_utility)
#             if beta <= alpha:
#                 break

#         return ActionUtility(min_utility, best_move)






#expected utility
def calculate_expected_utility(board, player):
    if is_winner(board, player):
        if(player == 2):
            return 1.0  # Player has already won
        else:
            return -1.0
    if(is_board_full(board)):
        return 0

    # if is_winner(board, 3 - player):
    #     return -1.0  # Opponent has already won

    # Evaluate potential winning combinations for the current player and the opponent
    player_wins = count_potential_wins(board, player)
    opponent_wins = count_potential_wins(board, 3 - player)

    # Assuming a simple heuristic with different weights for player and opponent wins
    if(player == 1):
        player_weight = -50
        opponent_weight = 1
    else:
        player_weight = 1
        opponent_weight = -50
    expected_utility = player_weight * player_wins + opponent_weight * opponent_wins

    return expected_utility

#CHAT GPT CODE
def count_potential_wins(board, player):
    win_count = 0

    # Check horizontally
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            window = board[row][col:col+4]
            if window.count(player) == 3 and window.count(0) == 1:
                win_count += 1

    # Check vertically
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            window = [board[row+i][col] for i in range(4)]
            if window.count(player) == 3 and window.count(0) == 1:
                win_count += 1

    # Check diagonally (from bottom-left to top-right)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            window = [board[row-i][col+i] for i in range(4)]
            if window.count(player) == 3 and window.count(0) == 1:
                win_count += 1

    # Check diagonally (from top-left to bottom-right)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            window = [board[row+i][col+i] for i in range(4)]
            if window.count(player) == 3 and window.count(0) == 1:
                win_count += 1

    return win_count

def Minimax(board, player, depth, alpha=float('-inf'), beta=float('inf')):
    print(str(depth))
    if depth == 0 or is_board_full(board) or is_winner(board, player):
        return ActionUtility(calculate_expected_utility(board, player), None)
    if player == 2:  # Maximizing player
        moves = PossibleMovesOnBoard(board)
        best_move = None
        max_utility = float('-inf')
        for i in range(len(moves)):
            lfr =LastFreeRow(board, moves[i])
            board[lfr][moves[i]] = player
            current_utility = Minimax(copy.deepcopy(board), 3-player, depth - 1, alpha, beta).utility
            board[lfr][moves[i]] = 0
            if current_utility > max_utility:
                max_utility = current_utility
                best_move = moves[i]
            alpha = max(alpha, max_utility)
            if beta <= alpha:
                break
        player = 3 - player
        return ActionUtility(max_utility, best_move)
    if player == 1:  # Minimizing player
        moves = PossibleMovesOnBoard(board)
        best_move = None
        min_utility = float('inf')
        for i in range(len(moves)):
            lfr =LastFreeRow(board, moves[i])
            board[lfr][moves[i]] = player
            current_utility = Minimax(copy.deepcopy(board), 3-player, depth - 1, alpha, beta).utility
            board[lfr][moves[i]] = 0
            if current_utility < min_utility:
                min_utility = current_utility
                best_move = moves[i]
            beta = min(beta, min_utility)
            if beta <= alpha:
                break
        player = 3 - player
        return ActionUtility(min_utility, best_move)


game = ConnectFour(board)
player = 1
print(tb(game.board, tablefmt="grid"))

while(True):
    print("--------------------------------------------------------------------------------")
    if(player == 1):
        move = int(input("Enter your move (column number): "))
        sPrime = game.succ(game.board,move,player)
        if(sPrime != None):
            game.board = sPrime
    else:
        actionUtility = Minimax(copy.deepcopy(game.board),player,3)
        sPrime = game.succ(game.board,actionUtility.action,player)
        game.board = sPrime
    print(tb(game.board, tablefmt="grid"))
    if(is_winner(game.board,player)):
        print(str(player) +" is winner")
        break
    if(is_board_full(game.board)):
        print("Game Draw!")
        break
    player = 3 - player


        
        