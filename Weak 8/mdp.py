import numpy as np


#defining 2D array
rows,cols = (4,4)
arr = [[0 for i in range(cols)] for j in range(rows)]
# initializaing array
arr[0][0] = 'A'
arr[0][1] = 'F'
arr[0][2] = 'F'
arr[0][3] = 'F'
arr[1][0] = 'F'
arr[1][1] = 'H'
arr[1][2] = 'F'
arr[1][3] = 'H'
arr[1][0] = 'F'
arr[2][1] = 'F'
arr[2][2] = 'F'
arr[2][3] = 'H'
arr[2][0] = 'F'
arr[3][0] = 'H'
arr[3][1] = 'F'
arr[3][2] = 'F'
arr[3][3] = 'G'

#Hole Cordinated
hx1 = 1
hx2 = 1
hx3 = 2
hx4 = 3

hy1 = 1
hy2 = 3
hy3 = 3
hy4 = 0
# agent coordinates
agentX = 0
agentY = 0
# goal coordinates
goalX = 3
goalY = 3







actions = ['left','right','up','down']



class Cell:
    def __init__(self,reward,action):
        self.reward = reward
        self.action = action


def isValidAction(action,X,Y):
    if(action == "left"):
        if((Y-1) >= 0):
            return True
    elif (action == "right"):
        if((Y+1) <= 3):
            return True
    elif (action == "up"):
        if((X-1) >= 0):
            return True    
    elif (action == "down"):
        if((X+1) <= 3):
            return True
    return False   


def summation(V,action,j,k):
    sum = 0
    p = 0.8
    oneMinusP = (1-p)/3
    df = 0.51 #discount factor gamma
    reward = -0.01
    if(action == "left"):
        
        sum = sum + p*(reward + df*V[j][k-1].reward)

        if(isValidAction("right",j,k)):

            sum = sum + oneMinusP*(reward + df*V[j][k+1].reward)
        else: # if not valid move then ending up in same state
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)


        if(isValidAction("up",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j-1][k].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)


        if(isValidAction("down",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j+1][k].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)


    elif (action == "right"):
        sum = sum + p*(reward + df*V[j][k+1].reward)

        if(isValidAction("left",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j][k-1].reward)
        else: # if not valid move then ending up in same state
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)

        if(isValidAction("up",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j-1][k].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)


        if(isValidAction("down",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j+1][k].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)

    elif (action == "up"):

        sum = sum + p*(reward + df*V[j-1][k].reward)

        if(isValidAction("left",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j][k-1].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)
        if(isValidAction("right",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j][k+1].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)
        if(isValidAction("down",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j+1][k].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)
    elif (action == "down"):
        sum = sum + p*(reward + df*V[j+1][k].reward)

        if(isValidAction("left",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j][k-1].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)
        if(isValidAction("right",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j][k+1].reward)
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)
        if(isValidAction("up",j,k)):
            sum = sum + oneMinusP*(reward + df*V[j-1][k].reward)  
        else:
            sum = sum + oneMinusP*(reward + df*V[j][k].reward)
    return sum



def value_Iteration():
    rows,cols = (4,4)
    V_opt = [[Cell(0,None) for i in range(cols)] for j in range(rows)]
    V_opt[3][3] = Cell(1,None)
    V_opt[hx1][hy1] = Cell(-1,None)
    V_opt[hx2][hy2] = Cell(-1,None)
    V_opt[hx3][hy3] = Cell(-1,None)
    V_opt[hx4][hy4] = Cell(-1,None)
    for i in range(1,1000):
        V = [[Cell(0,None) for i in range(cols)] for j in range(rows)]
        for j in range (rows):
            for k in range(cols):
                bellmanSums = []
                for a in actions:
                    if(j == 0 and k == 1):
                        xyz = 1
                    sum = 0
                    if(j == goalX and k == goalY):
                        bellmanSums.append(["Win",1])
                    elif ((j == hx1 and k == hy1) or (j == hx2 and k == hy2) or (j == hx3 and k == hy3) or (j == hx4 and k == hy4)):
                        bellmanSums.append(["Lose",-1])
                    elif (isValidAction(a,j,k)):
                        sum = summation(V_opt,a,j,k)
                        bellmanSums.append([a,sum])
                        # sum = sum + 0.1*(-0.1 + V_opt[j][k].reward)
                        # sum = sum + 0.3*(-0.1 + V_opt[j][k].reward)
                        # sum = sum + 0.3*(-0.1 + V_opt[j][k].reward)
                        # sum = sum + 0.3*(-0.1 + V_opt[j][k].reward)
                max = sorted(bellmanSums, key=lambda x: x[1], reverse=True) #max element
                # max = sorted(bellmanSums, key=lambda x: x[1]) #max element
                V[j][k] = Cell(max[0][1],max[0][0])
        V_opt = V
        # flag = True
        # for i in range(4):
        #     for j in range(4):
        #         if((abs(V_opt[i][j].reward - V[i][j].reward) < 0.01)):
        #             flag = False
        # if(flag):
        #     break


        # for i in range(4):
        #     for j in range(4):
        #         print(f'{V_opt[i][j].action:8}', end="")
        #     print()
        # print()
        # print()








    for i in range(4):
        for j in range(4):
            print(f'{V_opt[i][j].action:8}', end="")
        print()
    print()
    print()

    # for i in range(4):
    #     for j in range(4):
    #         print(str(V_opt[i][j].reward) + " " , end="")
    #     print()

value_Iteration()
print("This is the optimal Policy!")






























































