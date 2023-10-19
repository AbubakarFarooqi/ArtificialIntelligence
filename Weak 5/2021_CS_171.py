

# cordinates of " " // space
x = 1
y = 0  

def TransitionModel(state , action):
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
class Node:
    # def TransitionModel(self,state , action):
    #     newState = [[element for element in row] for row in state]
    #     if(action == "left"):
    #         temp =  newState[x][y-1]
    #         newState[x][y-1] = " "
    #         newState[x][y] = temp
    #         y = y-1
    #     elif (action == "right"):
    #         temp =  newState[x][y+1]
    #         newState[x][y+1] = " "
    #         newState[x][y] = temp
    #         y = y+1
    #     elif (action == "up"):
    #         temp =  newState[x-1][y]
    #         newState[x-1][y] = " "
    #         newState[x][y] = temp
    #         x = x-1
    #     elif (action == "down"):
    #         temp =  newState[x+1][y]
    #         newState[x+1][y] = " "
    #         newState[x][y] = temp
    #         x = x+1
    #     return newState
    def __init__(self,parent=None,action = None,h = None):
        if(parent is not None):
            self.State = TransitionModel(parent.State , action)
            self.Action = action
            self.Parent = parent
            self.G = parent.G + 1 # Path Cost
            self.H = h
    

    # def __init__(self,state,h):
    #     self.State = state
    #     self.Action = None
    #     self.Parent = None
    #     self.G = 0
    #     self.H = h
    def createParent(self,state,h):
        self.State = state
        self.Action = None
        self.Parent = None
        self.G = 0
        self.H = h

  
    
    
def GetState(state,action):
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


def GoalTest(node):
        # Check if the dimensions of the two arrays are the same
        if len(node.State) != len(GoalState) or len(node.State[0]) != len(GoalState[0]):
            return False

    # Iterate through the rows and columns
        for i in range(len(node.State)):
            for j in range(len(node.State[0])):
                if node.State[i][j] != GoalState[i][j]:
                    return False  # If any element is different, the arrays are not equal

    # If we reach this point, all elements are the same
        return True
def findH(x1,y1,x2,y2):
    return abs((x1+y1) - (x2+y2))
# def OptimalMove(node):
#         if((y-1) >=0 ):
#             # total_H_value = sum(currentHueristics.values())
#             state = GetState(node.State,"left")
#             element = state[x][y]
#             H_of_element =  findH(x,y,currentHueristicsX[element],currentHueristicsY[element]) 
#             # currentHueristics[element]

#             if((abs(x-y)+ H_of_element) <= H_of_element):
#                 # currentHueristics[element] = abs(H_of_element - (x+y))
#                 currentHueristics[element] = (abs(x-y)+ H_of_element)
#                 return "left"
#         if((y+1) <=2 ):
#             total_H_value = sum(currentHueristics.values())
#             state = GetState(node.State,"right")
#             element = state[x][y]
#             H_of_element = currentHueristics[element]
#             if((abs(x-y)+ H_of_element) <= H_of_element):
#                 currentHueristics[element] = abs(H_of_element + (x+y))
#                 return "right"
#         if((x-1) >=0 ):
#             total_H_value = sum(currentHueristics.values())
#             state = GetState(node.State,"up")
#             element = state[x][y]
#             H_of_element = currentHueristics[element]
#             if((abs(x-y)+ H_of_element) <= H_of_element):
#                 currentHueristics[element] = abs(H_of_element + (x+y))

#                 return "up"
#         if((x+1) <=2 ):
#             total_H_value = sum(currentHueristics.values())
#             state = GetState(node.State,"down")
#             element = state[x][y]
#             H_of_element = currentHueristics[element]
#             if((abs(x-y)+ H_of_element) <= H_of_element):
#                 currentHueristics[element] = abs(H_of_element + (x+y))

#                 return "down"



def OptimalMove(node):
        if((y-1) >=0 ):
            # total_H_value = sum(currentHueristics.values())
            state = GetState(node.State,"left")
            element = state[x][y]
            H_of_elementOld =  findH(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  findH(goalHueristicsX[element],goalHueristicsY[element],x,y) 
            # currentHueristics[element]

            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y
                
                # currentHueristics[element] = (abs(x-y)+ H_of_element)
                return "left"
        if((y+1) <=2 ):
            # total_H_value = sum(currentHueristics.values())
            state = GetState(node.State,"right")
            element = state[x][y]
            H_of_elementOld =  findH(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  findH(goalHueristicsX[element],goalHueristicsY[element],x,y) 

            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y
                return "right"
        if((x-1) >=0 ):
            # total_H_value = sum(currentHueristics.values())
            state = GetState(node.State,"up")
            element = state[x][y]
            H_of_elementOld =  findH(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  findH(goalHueristicsX[element],goalHueristicsY[element],x,y) 

            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y

                return "up"
        if((x+1) <=2 ):
            # total_H_value = sum(currentHueristics.values())
            state = GetState(node.State,"down")
            element = state[x][y]
            H_of_elementOld =  findH(goalHueristicsX[element],goalHueristicsY[element],currentHueristicsX[element],currentHueristicsY[element]) 
            H_of_elementNew =  findH(goalHueristicsX[element],goalHueristicsY[element],x,y) 
            if(H_of_elementNew <= H_of_elementOld):
                currentHueristics[element] = H_of_elementNew
                currentHueristicsX[element] = x
                currentHueristicsY[element] = y

                return "down"

class Puzzle:
   
    # def GetState(self,state,action):
    #     newState = [[element for element in row] for row in state]
    #     if(action == "left"):
    #         temp =  newState[x][y-1]
    #         newState[x][y-1] = " "
    #         newState[x][y] = temp
    #     elif (action == "right"):
    #         temp =  newState[x][y+1]
    #         newState[x][y+1] = " "
    #         newState[x][y] = temp
    #     elif (action == "up"):
    #         temp =  newState[x-1][y]
    #         newState[x-1][y] = " "
    #         newState[x][y] = temp
    #     elif (action == "down"):
    #         temp =  newState[x+1][y]
    #         newState[x+1][y] = " "
    #         newState[x][y] = temp
    #     return newState

    # def OptimalMove(self,node):
    #     if((y-1) >=0 ):
    #         total_H_value = sum(currentHueristics.values())
    #         state = GetState(node.state,"left")
    #         element = state[x][y]
    #         H_of_element = currentHueristics[element]

    #         if(abs(H_of_element - (x+y)) < H_of_element):
    #             currentHueristics[element] = abs(H_of_element - (x+y))
    #             return "left"
    #     if((y+1) <=2 ):
    #         total_H_value = sum(currentHueristics.values())
    #         state = GetState(node.state,"right")
    #         element = state[x][y]
    #         H_of_element = currentHueristics[element]
    #         if(abs(H_of_element - (x+y)) < H_of_element):
    #             currentHueristics[element] = abs(H_of_element - (x+y))
    #             return "right"
    #     if((x-1) >=0 ):
    #         total_H_value = sum(currentHueristics.values())
    #         state = GetState(node.state,"up")
    #         element = state[x][y]
    #         H_of_element = currentHueristics[element]
    #         if(abs(H_of_element - (x+y)) < H_of_element):
    #             currentHueristics[element] = abs(H_of_element - (x+y))
    #             return "up"
    #     if((x+1) <=2 ):
    #         total_H_value = sum(currentHueristics.values())
    #         state = GetState(node.state,"down")
    #         element = state[x][y]
    #         H_of_element = currentHueristics[element]
    #         if(abs(H_of_element - (x+y)) < H_of_element):
    #             currentHueristics[element] = abs(H_of_element - (x+y))
    #             return "down"


        
    # def GoalTest(self,node):
    #     # Check if the dimensions of the two arrays are the same
    #     if len(node.State) != len(GoalState) or len(node.State[0]) != len(GoalState[0]):
    #         return False

    # # Iterate through the rows and columns
    #     for i in range(len(node.State)):
    #         for j in range(len(node.State[0])):
    #             if node.State[i][j] != GoalState[i][j]:
    #                 return False  # If any element is different, the arrays are not equal

    # # If we reach this point, all elements are the same
    #     return True

    

    def __init__(self,initialState,goalState):
        self.InitialState = initialState
        self.GoalState = goalState

    def SolvePuzzle(self,parentNode):
        if(GoalTest(parentNode)):
            for row in parentNode.State:
                for element in row:
                    print(element, end=" ")  # Use end=" " to print elements on the same line with a space separator
                print()  # Print a newline after each row
            return parentNode
            # return Solution(parentNode)
        action = OptimalMove(parentNode)
        sum(currentHueristics.values())
        # n = Node(parentNode,action,sum(currentHueristics.values()))
        n = Node(parentNode,action,sum(currentHueristics.values()))
        
        print()
        self.SolvePuzzle(n)



currentHueristicsX = {
    "1" : 0,
    "2": 0,
    "3": 0,
    "4": 1,
    "5": 2,
    "6": 1,
    "7": 2,
    "8": 2,
}

currentHueristicsY = {
    "1" : 0,
    "2": 1,
    "3": 2,
    "4": 1,
    "5": 1,
    "6": 2,
    "7": 0,
    "8": 2,
}

currentHueristics = {
    "1" : 0,
    "2": 0,
    "3": 0,
    "4": 1,
    "5": 1,
    "6": 0,
    "7": 0,
    "8": 1,
}


goalHueristicsX = {
    "1" : 0,
    "2": 0,
    "3": 0,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 2,
    "8": 2,
}

goalHueristicsY = {
    "1" : 0,
    "2": 1,
    "3": 2,
    "4": 0,
    "5": 1,
    "6": 2,
    "7": 0,
    "8": 1,
}






# cordinates of " " // space
x = 1
y = 0  

InitialState = [[0 for i in range(3)] for j in range(3)]
GoalState = [[0 for i in range(3)] for j in range(3)]

InitialState[0][0] = "1"
InitialState[0][1] = "2"
InitialState[0][2] = "3"
InitialState[1][0] = " "
InitialState[1][1] = "4"
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


p = Puzzle(InitialState,GoalState)
n = Node()
n.createParent(InitialState,3)
p.SolvePuzzle(n)
