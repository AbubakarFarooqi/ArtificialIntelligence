import random
import copy
# 1 = User
# 2 = Agent
# 0 = Empty Cell


#defining 2D array
rows,cols = (3,3)
arr = [['x' for i in range(cols)] for j in range(rows)]




class Node:
    State = None
    Parent = None
    Action = None
    Reward = None
    def CreateNode(self,arr,parent,action):
        self.State = arr
        self.Action = action
        self.Parent = parent

    def setReward(self,r):
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
        # Recursively convert lists to tuples before hashing
        return hash((self.s, self._convert_to_immutable(self.s_prime), self.a))

    def __eq__(self, other):
        if isinstance(other, Probability):
            # Use _convert_to_immutable(self.s_prime) for comparison as well
            return (self.s, self._convert_to_immutable(self.s_prime), self.a) == \
                   (other.s, self._convert_to_immutable(other.s_prime), other.a)
        return False

class EpisodeInstance:
    def __init__(self,s,a,r,s_prime):
        self.s = s
        self.a = a
        self.r = r
        self.s_prime = s_prime

class TicTacToe:
    @staticmethod
    def IsWin(state,player):
        # this function will check whether a line of 0 or 1 is achied or not
        # check horizontally
        if(player == 1):
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

        # Check the secondary diagonal
            if state[0][2] == 1 and state[1][1] == 1 and state[2][0] == 1:
                return True
        
            return False
        
        if(player == 2):
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

        # Check the secondary diagonal
            if state[0][2] == 2 and state[1][1] == 2 and state[2][0] == 2:
                return True
        
            return False





    # def IsValidSquare:
    #     # this function will check whether the square is empty or not or we are in the Board
    # def DisplayBoard:
    
    # Helper function to check if the board is full
    @staticmethod
    def IsBoardComplete(board):
        return all(board[i][j] != 0 for i in range(3) for j in range(3))

    @staticmethod
    def SelectCoordinatesForPlayer(board):
        while(True):#repeat until a valid cell is found
        #random row number
            r = random.randint(0, 2)
        #random col number
            c = random.randint(0, 2)
            if(board[r][c] == 0):
                return (r,c)
    @staticmethod
    def are_states_equal(state1, state2):
        for i in range(3):
            for j in range(3):
                if state1[i][j] != state2[i][j]:
                    return False
        return True


print("Start")

Visited_States = set()
start = [[0 for i in range(cols)] for j in range(rows)]
Episodes = []
currState =  copy.deepcopy(start)
newState = copy.deepcopy(start)
Visited_States.add(tuple(map(tuple, currState)))
player = 1
i = 1
Episode = []
while (i <= 10):
    r,c = TicTacToe.SelectCoordinatesForPlayer(currState)
    newState[r][c] = player
    if(TicTacToe.IsWin(newState,player)):
        #if player 1 is win then reward is zero as we want agent to win
        if(player == 1):
            e = EpisodeInstance(currState,player,-1,newState)
        else:
            e = EpisodeInstance(currState,player,1,newState)
        Episode.append(e)
        Episodes.append(Episode)
        Visited_States.add(tuple(map(tuple, newState)))
        i = i+1
        Episode = []
        currState =  copy.deepcopy(start)
        newState = copy.deepcopy(start)
        continue
    if(TicTacToe.IsBoardComplete(newState)):
        #it means game is draw
        e = EpisodeInstance(currState,player,0.5,newState)
        Episode.append(e)
        Episodes.append(Episode)
        Visited_States.add(tuple(map(tuple, newState)))
        i = i+1
        Episode = []
        currState =  copy.deepcopy(start)
        newState = copy.deepcopy(start)
        continue
    e = EpisodeInstance(currState,player,0,newState)
    Visited_States.add(tuple(map(tuple, newState)))
    currState = copy.deepcopy(newState)
    newState = copy.deepcopy(newState)
    Episode.append(e)
    player = 3-player

# print("end")
# for episode in Episodes:
#     for instance in episode:
#         # print(instance.s)
#         for row1, row2 in zip(instance.s, instance.s_prime):
#         # Join elements from both boards with a space in between
#             row_str = " | ".join(map(str, row1)) + "    " + " | ".join(map(str, row2))
#             print(row_str)
#             print("-" * 23)
#         print()
#         print()
#         print()
        


#let us count how many times a specific state action pair occurs
NoOfTime_S_A_Occurs = []
states = [list(inner_tuple) for inner_tuple in Visited_States]
# s =  Episodes[77][6].s
i = 1
statesDict = {}
for s in states:
    s_primes = []
    count = 0
    for episode in Episodes:
        for instance in episode:
        # print(instance.s)
            if(TicTacToe.are_states_equal(s,instance.s) and instance.a == 1):
                s_primes.append(instance.s_prime)
                count = count+1
    NoOfTime_S_A_Occurs.append([s,count])
    statesDict[tuple(map(tuple, s))] = s_primes
    print(str(i))
    i = i+1
ProbablityDict = {}
print("This state action pair occurs = " + str(count))
for s,s_primes in statesDict.items():
    for sp in s_primes:
        tpl = tuple(map(tuple, sp))
        count = sum(1 for arr in s_primes if tuple(map(tuple, arr)) == tpl)
        p = Probability(s,sp,2)
        for item in NoOfTime_S_A_Occurs:
            if TicTacToe.are_states_equal( item[0], s) :
                ProbablityDict[p] = count /  item[1]
       
x = 6
        


# start.CreateNode()

    
