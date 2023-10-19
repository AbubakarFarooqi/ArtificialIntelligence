
class Problem:
    def __init__ (self,initialState,goalState):
        self.InitialState = initialState
        self.GoalState = goalState

    def TransitionModel(self,state , action):
        newState = [[element for element in row] for row in state]
        global y
        global x
        if(action == "left"):
            temp =  newState[x][y-1]
            newState[x][y-1] = " "
            newState[x][y] = temp
            y = y-1
        elif (action == "right"):
            temp =  newState[x][y+1]
            newState[x][y+1] = " "
            newState[x][y] = temp
            y = y+1
        elif (action == "up"):
            temp =  newState[x-1][y]
            newState[x-1][y] = " "
            newState[x][y] = temp
            x = x-1
        elif (action == "down"):
            temp =  newState[x+1][y]
            newState[x+1][y] = " "
            newState[x][y] = temp
            x = x+1
        return newState


    def GoalTest(self,node):
        # Check if the dimensions of the two arrays are the same
        if len(node.State) != len(self.GoalState) or len(node.State[0]) != len(GoalState[0]):
            return False

    # Iterate through the rows and columns
        for i in range(len(node.State)):
            for j in range(len(node.State[0])):
                if node.State[i][j] != self.GoalState[i][j]:
                    return False  # If any element is different, the arrays are not equal

    # If we reach this point, all elements are the same
        return True
    def TransitionModel(self,state , action):
        newState = [[element for element in row] for row in state]
        global y
        global x
        if(action == "left"):
            temp =  newState[x][y-1]
            newState[x][y-1] = " "
            newState[x][y] = temp
            y = y-1
        elif (action == "right"):
            temp =  newState[x][y+1]
            newState[x][y+1] = " "
            newState[x][y] = temp
            y = y+1
        elif (action == "up"):
            temp =  newState[x-1][y]
            newState[x-1][y] = " "
            newState[x][y] = temp
            x = x-1
        elif (action == "down"):
            temp =  newState[x+1][y]
            newState[x+1][y] = " "
            newState[x][y] = temp
            x = x+1
        return newState

def returnProblem():
    problem = Problem(InitialState,GoalState)
    return problem
    

class Node:
    
    def __init__(self,parent=None,action=None,h=None):
            if parent is not None:
                self.State = returnProblem().TransitionModel(parent.State , action) # Successor Fucntion
                self.Action = action
                self.Parent = parent
                self.G = parent.G + 1 # Path Cost
    def createParent(self,state,h):
        self.State = state
        self.Action = None
        self.Parent = None
        self.G = 0
        self.H = h
    def InitializeProblem(self,p):
        self.problem = p

class Puzzle:

    def __init__(self,initialState,goalState,problem):
        self.InitialState = initialState
        self.GoalState = goalState
        self.PuzzleProblem = problem


    def CalculateHueristic(self,x1,y1,x2,y2):
        return abs((x1+y1) - (x2+y2))
    

    def GetState(self,state,action):
        newState = [[element for element in row] for row in state]
        if(action == "left"):
            temp =  newState[x][y-1]
            newState[x][y-1] = " "
            newState[x][y] = temp
        elif (action == "right"):
            temp =  newState[x][y+1]
            newState[x][y+1] = " "
            newState[x][y] = temp
        elif (action == "up"):
            temp =  newState[x-1][y]
            newState[x-1][y] = " "
            newState[x][y] = temp
        elif (action == "down"):
            temp =  newState[x+1][y]
            newState[x+1][y] = " "
            newState[x][y] = temp
        return newState

    def OptimalMove(self,node):
        if((y-1) >=0 ):
            # total_H_value = sum(currentHueristics.values())
            state = self.GetState(node.State,"left")
            element = state[x][y]
            H_of_elementOld =  self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],x,y) 
            # currentHueristics[element]

            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y
                
                # currentHueristics[element] = (abs(x-y)+ H_of_element)
                return "left"
        if((y+1) <=2 ):
            # total_H_value = sum(currentHueristics.values())
            state = self.GetState(node.State,"right")
            element = state[x][y]
            H_of_elementOld =  self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],x,y) 

            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y
                return "right"
        if((x-1) >=0 ):
            # total_H_value = sum(currentHueristics.values())
            state = self.GetState(node.State,"up")
            element = state[x][y]
            H_of_elementOld = self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],x,y) 

            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y

                return "up"
        if((x+1) <=2 ):
            # total_H_value = sum(currentHueristics.values())
            state = self.GetState(node.State,"down")
            element = state[x][y]
            H_of_elementOld =  self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  self.CalculateHueristic(goalHueristicsX[element],goalHueristicsY[element],x,y) 
            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y

                return "down"
    
    def SolvePuzzle(self,parentNode):
        if(self.PuzzleProblem.GoalTest(parentNode)):
            return parentNode
            # return Solution(parentNode)
        action = self.OptimalMove(parentNode)
        sum(currentHueristics.values())
        # n = Node(parentNode,action,sum(currentHueristics.values()))
        n = Node(parentNode,action,sum(currentHueristics.values()))
        
        
        for row in n.State:
            for element in row:
                print(element, end=" ")  # Use end=" " to print elements on the same line with a space separator
            print()
        print()
        print("-----------------------------")
        print()
        
        
        
        
        return self.SolvePuzzle(n)


    def PrintSolution(self,Node):
        while Node:
            for row in Node.State:
                for element in row:
                    print(element, end=" ")  # Use end=" " to print elements on the same line with a space separator
                print()
                
            print()
            print("-----------------------------")
            print()
            Node = Node.Parent  # Print a newline after each row





# cordinates of " " // space
x = 1
y = 1  


currentHueristicsX = {
    "1" : 2,
    "2": 0,
    "3": 2,
    "4": 0,
    "5": 1,
    "6": 1,
    "7": 0,
    "8": 2,
}

currentHueristicsY = {
    "1" : 2,
    "2": 1,
    "3": 1,
    "4": 2,
    "5": 0,
    "6": 2,
    "7": 0,
    "8": 0,
}

currentHueristics = {
    "1" : 4,
    "2": 1,
    "3": 2,
    "4": 2,
    "5": 2,
    "6": 3,
    "7": 3,
    "8": 2,
}


goalHueristicsX = {
    "1" : 0,
    "2": 0,
    "3": 1,
    "4": 1,
    "5": 1,
    "6": 2,
    "7": 2,
    "8": 2,
}

goalHueristicsY = {
    "1" : 1,
    "2": 2,
    "3": 0,
    "4": 1,
    "5": 2,
    "6": 0,
    "7": 1,
    "8": 2,
}



InitialState = [[0 for i in range(3)] for j in range(3)]
GoalState = [[0 for i in range(3)] for j in range(3)]

InitialState[0][0] = "7"
InitialState[0][1] = "2"
InitialState[0][2] = "4"
InitialState[1][0] = "5"
InitialState[1][1] = " "
InitialState[1][2] = "6"
InitialState[2][0] = "8"
InitialState[2][1] = "3"
InitialState[2][2] = "1"


GoalState[0][0] = " "
GoalState[0][1] = "1"
GoalState[0][2] = "2"
GoalState[1][0] = "3"
GoalState[1][1] = "4"
GoalState[1][2] = "5"
GoalState[2][0] = "6"
GoalState[2][1] = "7"
GoalState[2][2] = "8"


problem = Problem(InitialState,GoalState)

p = Puzzle(InitialState,GoalState,problem)
n = Node()
n.InitializeProblem(problem)
n.createParent(InitialState,19)
solution = p.SolvePuzzle(n)

p.PrintSolution(solution)
print(solution.G)


