import random
import copy

class Node:
    State = None
    Parent = None
    Action = None
    Reward = None

    def CreateNode(self, arr, parent, action):
        self.State = arr
        self.Action = action
        self.Parent = parent

    def setReward(self, r):
        self.Reward = r

class Probability:
    def __init__(self, s, s_prime, a):
        self.s = s
        self.a = a
        self.s_prime = s_prime

    def _convert_to_immutable(self, obj):
        if isinstance(obj, list):
            return tuple(self._convert_to_immutable(item) for item in obj)
        return obj

    def __hash__(self):
        return hash((self.s, self._convert_to_immutable(self.s_prime), self.a))

    def __eq__(self, other):
        if isinstance(other, Probability):
            return (self.s, self._convert_to_immutable(self.s_prime), self.a) == \
                   (other.s, self._convert_to_immutable(other.s_prime), other.a)
        return False

class EpisodeInstance:
    def __init__(self, s, a, r, s_prime):
        self.s = s
        self.a = a
        self.r = r
        self.s_prime = s_prime

class TicTacToe:
    @staticmethod
    def IsWin(state, player):
        # Check horizontally
        for i in range(3):
            win = all(state[i][j] == player for j in range(3))
            if win:
                return True

        # Check vertically
        for j in range(3):
            win = all(state[i][j] == player for i in range(3))
            if win:
                return True

        # Check diagonally
        if all(state[i][i] == player for i in range(3)) or all(state[i][2 - i] == player for i in range(3)):
            return True

        return False

    @staticmethod
    def IsBoardComplete(board):
        return all(board[i][j] != 0 for i in range(3) for j in range(3))

    @staticmethod
    def SelectCoordinatesForPlayer(board):
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if board[r][c] == 0:
                return (r, c)
    # @staticmethod
    # def SelectCoordinatesForPlayer(board, epsilon):
    #     if random.uniform(0, 1) < epsilon:
    #         # Explore: Choose a random move
    #         empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    #         return random.choice(empty_cells)
    #     else:
    #         # Exploit: Choose the best move based on Q-values
    #         legal_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    #         return QLearningAgent().get_best_move(tuple(map(tuple, board)), legal_moves)


    @staticmethod
    def are_states_equal(state1, state2):
        return all(state1[i][j] == state2[i][j] for i in range(3) for j in range(3))

    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1

    def display_board(self):
        for row in self.board:
            print(" | ".join(map(str, row)))
            print("-" * 9)

    def make_move(self, move):
        row, col = move
        self.board[row][col] = self.current_player
        self.current_player = 3 - self.current_player

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def is_valid_move(self, move):
        return move in self.available_moves()

    def is_game_over(self):
        return TicTacToe.IsWin(self.board, 1) or TicTacToe.IsWin(self.board, 2) or TicTacToe.IsBoardComplete(self.board)


class QLearningAgent:
    def __init__(self):
        self.Q_values = {}

    def get_q_value(self, state, action):
        return self.Q_values.get((state, action), 0.0)

    def update_q_value(self, state, action, value):
        key = (state, action)
        self.Q_values[key] = self.get_q_value(state, action) + value

    def get_best_move(self, state, legal_moves):
        if not legal_moves:
            return None

        best_move = max(legal_moves, key=lambda move: self.get_q_value(state, move))
        return best_move


def train_q_learning_agent(agent, episodes):
    for episode in episodes:
        for i in range(len(episode) - 1):
            state = tuple(map(tuple, episode[i].s))
            action = episode[i].a
            reward = episode[i].r
            # next_state = tuple(map(tuple, episode[i + 1].s))
            next_state = tuple(map(tuple, episode[i].s_prime))

            best_next_action = agent.get_best_move(next_state, [(i, j) for i in range(3) for j in range(3)])
            if best_next_action is None:
                best_next_q_value = 0.0
            else:
                best_next_q_value = agent.get_q_value(next_state, best_next_action)

            td_error = reward + best_next_q_value - agent.get_q_value(state, action)
            agent.update_q_value(state, action, td_error)


def play_against_agent(agent):
    game = TicTacToe()

    while not game.is_game_over():
        game.display_board()

        if game.current_player == 1:
            # Human's turn
            row, col = map(int, input("Enter your move (row col): ").split())
            move = (row, col)
        else:
            # Agent's turn
            state_key = tuple(map(tuple, game.board))
            legal_moves = game.available_moves()
            move = agent.get_best_move(state_key, legal_moves) or random.choice(legal_moves)

        if game.is_valid_move(move):
            game.make_move(move)
        else:
            print("Invalid move. Try again.")

    game.display_board()
    if TicTacToe.IsWin(game.board, 1):
        print("You win!")
    elif TicTacToe.IsWin(game.board, 2):
        print("Agent wins!")
    else:
        print("It's a draw!")


# Main part of the code

epsilon = 0.1  # Initial value
decay_rate = 0.995

Visited_States = set()
start = [[0 for _ in range(3)] for _ in range(3)]
Episodes = []
currState = copy.deepcopy(start)
newState = copy.deepcopy(start)
Visited_States.add(tuple(map(tuple, currState)))
player = 1
i = 1
Episode = []

while i <= 1000:
    r, c = TicTacToe.SelectCoordinatesForPlayer(currState)
    newState[r][c] = player

    if TicTacToe.IsWin(newState, player):
        if player == 1:
            e = EpisodeInstance(currState, player, -1, newState)
        else:
            e = EpisodeInstance(currState, player, 1, newState)
        Episode.append(e)
        Episodes.append(Episode)
        Visited_States.add(tuple(map(tuple, newState)))
        i += 1
        Episode = []
        currState = copy.deepcopy(start)
        newState = copy.deepcopy(start)
        continue

    if TicTacToe.IsBoardComplete(newState):
        e = EpisodeInstance(currState, player, 0, newState)
        Episode.append(e)
        Episodes.append(Episode)
        Visited_States.add(tuple(map(tuple, newState)))
        i += 1
        Episode = []
        currState = copy.deepcopy(start)
        newState = copy.deepcopy(start)
        continue

    e = EpisodeInstance(currState, player, -0.5, newState)
    Visited_States.add(tuple(map(tuple, newState)))
    currState = copy.deepcopy(newState)
    newState = copy.deepcopy(newState)
    Episode.append(e)
    player = 3 - player
    epsilon *= decay_rate

print("Training the Q-learning agent...")
agent = QLearningAgent()
train_q_learning_agent(agent, Episodes)
print("Training complete.")

print("\nPlaying against the trained agent...")
play_against_agent(agent)
