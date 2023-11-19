# 1 = User
# 2 = Agent
import random
import copy
import numpy as np
import pickle

def is_game_over(board):
    return IsWin(board, 1) or IsWin(board, 2) or IsBoardComplete(board)



def display_board(board):
        for row in board:
            print(" | ".join(map(str, row)))
            print("-" * 9)


def Get_rc_from_move(move):
    r = 0
    c = 0
    if(move==1):
        r = 0
        c = 0 
    if(move==2):
        r = 0
        c = 1 
    if(move==3):
        r = 0
        c = 2 
    if(move==4):
        r = 1
        c = 0 
    if(move==5):
        r = 1
        c = 1 
    if(move==6):
        r = 1
        c = 2 
    if(move==7):
        r = 2
        c = 0 
    if(move==8):
        r = 2
        c = 1 
    if(move==9):
        r = 2
        c = 2
    return (r,c)

def IsValidMove(state,move):

    r,c = Get_rc_from_move(move)
    if(state[r][c] == ' ') :
        return True
    return False
    
def IsBoardComplete(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                return False
    return True


def IsWin(state,player):
        # this function will check whether a line of 0 or 1 is achied or not
        if(player == 1):
        # check horizontally
            for i in range(3):
                win = True
                for j in range(3):
                    if(state[i][j] != 1):
                        win  = False
                if(win):
                    return True
        # check Vertically
            for j in range(3):
                win = True
                for i in range(3):
                    if(state[i][j] != 1):
                        win  = False
                if(win):
                    return True
        # check Diagonally
            if state[0][0] == 1 and state[1][1] == 1 and state[2][2] == 1:
                return True

        # Check the second diagonal
            if state[0][2] == 1 and state[1][1] == 1 and state[2][0] == 1:
                return True
        
            return False
        
        if(player == 2):
            #check horizontally
            for i in range(3):
                win = True
                for j in range(3):
                    if(state[i][j] != 2):
                        win  = False
                if(win):
                    return True
        # check Vertically
            for j in range(3):
                win = True
                for i in range(3):
                    if(state[i][j] != 2):
                        win  = False
                if(win):
                    return True
        # check Diagonally
            if state[0][0] == 2 and state[1][1] ==2  and state[2][2] == 2:
                return True

        # Check the second diagonal
            if state[0][2] == 2 and state[1][1] == 2 and state[2][0] == 2:
                return True
        
            return False



def get_move_from_rc(r,c):
    move = 0
    if(r == 0 and c == 0):
        move=1
    if(r ==0 and c == 1):
        move=2
    if(r ==0 and c ==2 ):
        move=3
    if(r ==1 and c ==0 ):
        move=4
    if(r ==1 and c ==1 ):
        move=5
    if(r ==1 and c ==2 ):
        move=6
    if(r ==2 and c ==0 ):
        move=7
    if(r ==2 and c == 1):
        move=8
    if(r ==2 and c ==2 ):
        move=9
    return move


def choose_optimal_move_for_agent(board):
# Check if a winning move is available for the agent
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 2  # Assume the agent is 2
                if IsWin(board, 2):
                    return row, col
                board[row][col] = ' '  # Undo the move

    # If no winning move, block opponent's winning move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 1  # Assume the opponent is 1
                if IsWin(board, 1):
                    return row, col
                board[row][col] = ' '  # Undo the move
    move = 0
    while True: # repeat until a valid move is found
        move = availableMove[random.randint(0, 8)] # select a random index from available moves
        if(IsValidMove(state,move)):
            break
    return Get_rc_from_move(move)

def choose_optimal_move(board):
    # Check if a winning move is available for the user 
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 1  # Assume the user is 1
                if IsWin(board, 1):
                    return row, col
                board[row][col] = ' '  # Undo the move

    # If no winning move, block opponent's winning move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 2  # Assume the opponent is 2
                if IsWin(board, 2):
                    return row, col
                board[row][col] = ' '  # Undo the move
    move = 0
    while True: # repeat until a valid move is found
        move = availableMove[random.randint(0, 8)] # select a random index from available moves
        if(IsValidMove(state,move)):
            break
    return Get_rc_from_move(move)

rows,cols = (3,3)
arr = [[' ' for i in range(cols)] for j in range(rows)]
availableMove = [1,2,3,4,5,6,7,8,9]
player = 1
states = []
ListOf_SAS_prime_reward= []
ListOf_SA = []


# Load ListOf_SAS_prime_reward from the file
with open('ListOf_SAS_prime_reward.pkl', 'rb') as file:
    ListOf_SAS_prime_reward = pickle.load(file)



for i in range(1000): # no of episodes
    state = copy.deepcopy(arr)
    player = 1
    # print(i)
    while True: # this loop terminates when a episode completes

        if(player == 1): # player is user

            r,c = choose_optimal_move(state)
            state[r][c] = player # creating a state in which user played its turn
            if(IsWin(state,player)):
                lastAdded =  ListOf_SAS_prime_reward[-1]
                lastAdded[3] = -1 # it means agent lose so reward is -1
                lastAdded =  ListOf_SAS_prime_reward[-1]
                break
            if(IsBoardComplete(state)):
                lastAdded =  ListOf_SAS_prime_reward[-1]
                lastAdded[3] = 0.5 # for draw game reward is 0.5
                lastAdded =  ListOf_SAS_prime_reward[-1]
                break
            states.append(state) # pushing the newly created state in the List of all states
            player = 3-player # switching to Agent
            state = copy.deepcopy(state) # updating current state (state) with a deepcopy of state


        else: # if player = 2 i.e agent

            r,c = choose_optimal_move_for_agent(state)
            move = get_move_from_rc(r,c)
            state[r][c] = player # creating a state in which agent played its turn
            isEpisodeComplete = False
            if(IsWin(state,player)):
                ListOf_SAS_prime_reward.append( [states[-1],move,state,1]) # s,a,s',r reward for agent win = 1
                isEpisodeComplete = True
            elif(IsBoardComplete(state) ): # chk if player 2 agent won
                # here states[-1] is thee last eleent i.e our s on which we perform move and get state in which agent played its turn
                ListOf_SAS_prime_reward.append( [states[-1],move,state,0.5]) # draw reward 0.5
                isEpisodeComplete = True
            #  for intermediate state reward is 0.1
            ListOf_SAS_prime_reward.append( [states[-1],move,state,0.1]) # here states[-1] is the last eleent i.e our s on which we perform move and get state in which agent played its turn
            ListOf_SA.append([states[-1],move])  
            player = 3-player # switching to user
            if(isEpisodeComplete):
                break #complete the episode and terminate while loop



# Save ListOf_SAS_prime_reward to a file
with open('ListOf_SAS_prime_reward.pkl', 'wb') as file:
    pickle.dump(ListOf_SAS_prime_reward, file)

# This code creates a dictionary transition_probabilities where
# the keys are tuples (s, a) and the values are dictionaries containing the
# next states s' and their corresponding probabilities. 
# The probabilities are normalized counts of each transition.



# dictionary to store the transition probabilities
transition_probabilities = {}

# Iterate through the list of (s, a, s', r) tuples
for transition in ListOf_SAS_prime_reward:
    s, a, s_prime, _ = transition

    # Convert lists to tuples for hashability
    s_tuple = tuple(map(tuple, s))
    s_prime_tuple = tuple(map(tuple, s_prime))

    # Create a key for the dictionary
    key = (s_tuple, a)

    # If the key is not in the dictionary, add it
    if key not in transition_probabilities:
        transition_probabilities[key] = {}

    # If the next state is not in the sub-dictionary, add it
    if s_prime_tuple not in transition_probabilities[key]:
        transition_probabilities[key][s_prime_tuple] = 0

    # Increment the count for the transition (s, a, s')
    transition_probabilities[key][s_prime_tuple] += 1

# Now, transition_probabilities contains the counts of each transition
# normalizing the counts to get probabilities
for key, value in transition_probabilities.items():
    total_count = sum(value.values())
    probabilities = {s_prime: count / total_count for s_prime, count in value.items()}
    transition_probabilities[key] = probabilities

# Now, transition_probabilities contains the transition probabilities T(s, a, s')


# Convert the ListOf_SAS_prime_reward to a dictionary for easy access
rewards = {(tuple(map(tuple, s)), a): r for s, a, _, r in ListOf_SAS_prime_reward}

# Value iteration function
def value_iteration(transition_probabilities, rewards, gamma=0.9, epsilon=1e-6):
    i = 0
    states = set()
    actions = set()
    for (s, a), s_primes in transition_probabilities.items():
        states.add(s)
        actions.add(a)
        states.update(s_primes.keys())
    V = {s: 0 for s in states}
    optimal_actions = {s: None for s in states}
    while True:
        delta = 0
        for (s, a), s_primes in transition_probabilities.items():
            old_v = V[s]
            q_values = {s_prime: [rewards.get((s, a, s_prime), 0) + gamma * V[s_prime], a] for s_prime in s_primes}
            max_q_pair = max(q_values.items(), key=lambda item: item[1][0])
            V[s] = max_q_pair[1][0]
            optimal_actions[s] = max_q_pair[1][1]
        i+=1
        if i == 1000:
            break
    print()
    print("i is"+" "+str(i))
    return optimal_actions

# Applying value iteration
optimal_actions = value_iteration(transition_probabilities, rewards)



def play_against_agent():
    board = copy.deepcopy(arr)
    player = 1
    while not is_game_over(board):
        display_board(board)
        move = 0
        if player == 1:
            # Human's turn
            move = int( input("Enter your move (1 - 9): "))
        else:
            # Agent's turn
            state_key = tuple(map(tuple, board))
            # move = optimal_actions[state_key]
            default_move = 0
            while True: # repeat until a valid move for agent is found
                default_move = availableMove[random.randint(0, 8)] # select a random index from available moves
                if(IsValidMove(board,default_move)):
                    break
            if state_key in optimal_actions:
                print("this state exist in data")
            move = optimal_actions.get(state_key, default_move)

        if IsValidMove(board,move):
            r,c = Get_rc_from_move(move)
            board[r][c] = player
            player = 3-player
        else:
            print("Invalid move. Try again.")

    display_board(board)
    if IsWin(board, 1):
        print("You win!")
    elif IsWin(board, 2):
        print("Agent wins!")
    else:
        print("It's a draw!")



play_against_agent()
