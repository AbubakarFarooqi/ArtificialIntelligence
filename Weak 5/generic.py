import heapq

class Problem:
    GoalState =None
    InitialState =None
    Actions = None
    @staticmethod
    def TransiotionModel(state,action,x,y):
        newState = [[element for element in row] for row in state]
        (if(action == "left"):
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
            newState[x][y] = temp)
        return newState
    @staticmethod
    def GoalTest(node):
        # Check if the dimensions of the two arrays are the same
        if len(node.State) != len(Problem.GoalState) or len(node.State[0]) != len(Problem.GoalState[0]):
            return False

    # Iterate through the rows and columns
        for i in range(len(node.State)):
            for j in range(len(node.State[0])):
                if node.State[i][j] != Problem.GoalState[i][j]:
                    return False  # If any element is different, the arrays are not equal
         # If we reach this point, all elements are the same
        return True
    

class Node:
    
    def __init__(self,parent=None,action=None,h=None,f = None,state = None, x=0, y=0):
            if parent is not None:
                self.State = state # Successor Fucntion
                self.Action = action
                self.Parent = parent
                self.G = parent.G + 1 # Path Cost
                self.H = h
                self.F = f
                self.X = x
                self.Y = y
    def createParent(self,state,h,f):
        self.State = state
        self.Action = None
        self.Parent = None
        self.G = 0
        self.H = h
        self.F = f
    def InitializeProblem(self,p):
        self.problem = p



class Puzzle:
    x = 0
    y = 0

    def CalculateHueristic(self,x1,y1,x2,y2):
        return abs(x1-x2) + abs(y1-y2)
    
    def isVisited(self,s,visited):
        for matrix in visited:
            if matrix == s:
                return True
        return False
    
    def  F_Score_of(self,node):
        return node.G + node.H
    
    def UpdateXY(self,action,X,Y):
        if(action == "left"):
            self.y = Y-1
            self.x = X
        elif(action == "right"):
            self.y = Y+1
            self.x = X
        elif(action == "down"):
            self.x = X+1
            self.y = Y
        elif(action == "up"):
            self.x = X-1
            self.y = Y
    
    def GetChildNode(self,parentNode,action):
        if(action == "left"):
            if((self.y-1) >=0 ):
                state = Problem.TransiotionModel(parentNode.State,action,self.x,self.y)
                element = state[self.x][self.y]
                H_of_elementOld =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],currentHueristicsX[element],currentHueristicsY[element]) 
                H_of_elementNew =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],self.x,self.y) 
                n = Node(parentNode,action,(sum(currentHueristics.values())) - H_of_elementOld+H_of_elementNew,None,state,self.x,self.y)
                
                n.F = self.F_Score_of(n)
                return n
            else:
                return None
        if(action == "right"):
            if((self.y+1) <=2  ):
                state = Problem.TransiotionModel(parentNode.State,action,self.x,self.y)
                element = state[self.x][self.y]
                H_of_elementOld =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],currentHueristicsX[element],currentHueristicsY[element]) 
                H_of_elementNew =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],self.x,self.y) 
                n = Node(parentNode,action,(sum(currentHueristics.values())) - H_of_elementOld+H_of_elementNew,None,state,self.x,self.y)
                n.F = self.F_Score_of(n)

                return n
            else:
                return None
        if(action == "up"):
            if((self.x-1) >=0  ):
                state = Problem.TransiotionModel(parentNode.State,action,self.x,self.y)
                element = state[self.x][self.y]
                H_of_elementOld =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],currentHueristicsX[element],currentHueristicsY[element]) 
                H_of_elementNew =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],self.x,self.y) 
                n = Node(parentNode,action,(sum(currentHueristics.values())) - H_of_elementOld+H_of_elementNew,None,state,self.x,self.y)

                n.F = self.F_Score_of(n)

                return n
            else:
                return None
        if(action == "down"):
            if((self.x+1) <=2   ):
                state = Problem.TransiotionModel(parentNode.State,action,self.x,self.y)
                element = state[self.x][self.y]
                H_of_elementOld =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],currentHueristicsX[element],currentHueristicsY[element]) 
                H_of_elementNew =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],self.x,self.y) 
                n = Node(parentNode,action,(sum(currentHueristics.values())) - H_of_elementOld+H_of_elementNew,None,state,self.x,self.y)

                n.F = self.F_Score_of(n)

                return n
            else:
                return None

    def IsLowCostStateExistInFrontier(self,childNode,min_priority_queue):
        for i in range(len(min_priority_queue)):
            if(childNode.State == min_priority_queue[i].State):
                if(childNode.F < min_priority_queue[i].F):
                    return i
        return -1

    def SolvePuzzle(self,parentNode):
        visited = []
        
        min_priority_queue = []
        min_priority_queue.append(parentNode)
        while True:
            min_priority_queue =  sorted(min_priority_queue, key=lambda x: x.F)
            node = min_priority_queue.pop(0)
            
            visited.append(node.State)
            if(Problem.GoalTest(node)):
                return node
            element = node.State[self.x][self.y]
            if(element != ' '): # if there is space then do nothing
                H_of_elementNew =  self.CalculateHueristic(GoalStatePostions_X[element],GoalStatePostions_Y[element],node.X,node.Y) 
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = self.x
                currentHueristicsY[element] = self.y
                self.UpdateXY(node.Action,node.X,node.Y)

            for action in Problem.Actions:
                childNode = self.GetChildNode(node,action)
                if childNode is not None:
                    if(self.isVisited(childNode.State,visited) == False):
                        f = int(self.F_Score_of(childNode))
                        index = self.IsLowCostStateExistInFrontier(childNode,min_priority_queue)
                        if(index == -1):
                            min_priority_queue.append(childNode)
                        else:
                            min_priority_queue[index] = childNode
                    




       
    def PrintSolution(self,node):
        i = 1
        while node:
            print(i)
            print("-------")
            for row in node.State:
                for element in row:
                    print(element, end=" ")  # Use end=" " to print elements on the same line with a space separator
                print()
            print()
            print("-----------------------------")
            print()
            node = node.Parent
            i +=1

# currentHueristicsX = {
#     "1" : 2,
#     "2": 0,
#     "3": 2,
#     "4": 0,
#     "5": 1,
#     "6": 1,
#     "7": 0,
#     "8": 2,
# }

# currentHueristicsY = {
#     "1" : 2,
#     "2": 1,
#     "3": 1,
#     "4": 2,
#     "5": 0,
#     "6": 2,
#     "7": 0,
#     "8": 0,
# }

# currentHueristics = {
#     "1" : 3,
#     "2": 1,
#     "3": 2,
#     "4": 2,
#     "5": 2,
#     "6": 3,
#     "7": 3,
#     "8": 2,
# }


# GoalStatePostions_X = {
#     "1" : 0,
#     "2": 0,
#     "3": 1,
#     "4": 1,
#     "5": 1,
#     "6": 2,
#     "7": 2,
#     "8": 2,
# }

# GoalStatePostions_Y = {
#     "1" : 1,
#     "2": 2,
#     "3": 0,
#     "4": 1,
#     "5": 2,
#     "6": 0,
#     "7": 1,
#     "8": 2,
# }




currentHueristicsX = {
    "1" : 1,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 2,
    "6": 1,
    "7": 2,
    "8": 2,
}

currentHueristicsY = {
    "1" : 0,
    "2": 0,
    "3": 2,
    "4": 1,
    "5": 1,
    "6": 2,
    "7": 0,
    "8": 2,
}

currentHueristics = {
    "1" : 1,
    "2": 1,
    "3": 0,
    "4": 2,
    "5": 1,
    "6": 0,
    "7": 0,
    "8": 1,
}


GoalStatePostions_X = {
    "1" : 0,
    "2": 0,
    "3": 0,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 2,
    "8": 2,
}

GoalStatePostions_Y = {
    "1" : 0,
    "2": 1,
    "3": 2,
    "4": 0,
    "5": 1,
    "6": 2,
    "7": 0,
    "8": 1,
}







# currentHueristicsX = {
#     "1" : 1,
#     "2": 0,
#     "3": 2,
#     "4": 2,
#     "5": 1,
#     "6": 1,
#     "7": 0,
#     "8": 2,
# }

# currentHueristicsY = {
#     "1" : 1,
#     "2": 1,
#     "3": 0,
#     "4": 1,
#     "5": 0,
#     "6": 2,
#     "7": 0,
#     "8": 2,
# }

# currentHueristics = {
#     "1": 2,
#     "2": 0,
#     "3": 4,
#     "4": 2,
#     "5": 1,
#     "6": 0,
#     "7": 2,
#     "8": 1,
# }


# GoalStatePostions_X = {
#     "1" : 0,
#     "2": 0,
#     "3": 0,
#     "4": 1,
#     "5": 1,
#     "6": 1,
#     "7": 2,
#     "8": 2,
# }

# GoalStatePostions_Y = {
#     "1" : 0,
#     "2": 1,
#     "3": 2,
#     "4": 0,
#     "5": 1,
#     "6": 2,
#     "7": 0,
#     "8": 1,
# }







InitialState = [[0 for i in range(3)] for j in range(3)]
GoalState = [[0 for i in range(3)] for j in range(3)]

# InitialState[0][0] = "7"
# InitialState[0][1] = "2"
# InitialState[0][2] = "4"
# InitialState[1][0] = "5"
# InitialState[1][1] = " "
# InitialState[1][2] = "6"
# InitialState[2][0] = "8"
# InitialState[2][1] = "3"
# InitialState[2][2] = "1"


# GoalState[0][0] = " "
# GoalState[0][1] = "1"
# GoalState[0][2] = "2"
# GoalState[1][0] = "3"
# GoalState[1][1] = "4"
# GoalState[1][2] = "5"
# GoalState[2][0] = "6"
# GoalState[2][1] = "7"
# GoalState[2][2] = "8"


InitialState[0][0] = "2"
InitialState[0][1] = "4"
InitialState[0][2] = "3"
InitialState[1][0] = "1"
InitialState[1][1] = " "
InitialState[1][2] = "6"
InitialState[2][0] = "7"
InitialState[2][1] = "5"
InitialState[2][2] = "8"


GoalState[0][0] = "1"
GoalState[0][1] = "2"
GoalState[0][2] = "3"
GoalState[1][0] = "4"
GoalState[1][1] = "5"
GoalState[1][2] = "6"
GoalState[2][0] = "7"
GoalState[2][1] = "8"
GoalState[2][2] = " "



# InitialState[0][0] = "7"
# InitialState[0][1] = "2"
# InitialState[0][2] = " "
# InitialState[1][0] = "5"
# InitialState[1][1] = "1"
# InitialState[1][2] = "6"
# InitialState[2][0] = "3"
# InitialState[2][1] = "4"
# InitialState[2][2] = "8"


# GoalState[0][0] = "1"
# GoalState[0][1] = "2"
# GoalState[0][2] = "3"
# GoalState[1][0] = "4"
# GoalState[1][1] = "5"
# GoalState[1][2] = "6"
# GoalState[2][0] = "7"
# GoalState[2][1] = "8"
# GoalState[2][2] = " "







Problem.InitialState = InitialState
Problem.GoalState = GoalState
Problem.Actions = ["left","right","up","down"]

parentNode = Node()
parentNode.createParent(InitialState,6,6)
parentNode.X = 1
parentNode.Y = 1

p = Puzzle()
p.x = 1
p.y = 1
solution = p.SolvePuzzle(parentNode)
p.PrintSolution(solution)
