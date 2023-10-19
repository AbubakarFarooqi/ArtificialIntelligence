from itertools import permutations

import random



class Node:
    def __init__ (self,value,cost):
        self.value = value
        self.next = None
        self.cost = cost
    def __lt__(self, other):
        # Define the less-than comparison based on the 'value' attribute
        return self.value < other.value

class Graph:
    def __init__(self,numberOfVertices):
        self.vertices = numberOfVertices
        self.graph = [None]*self.vertices
    #get Step Cost
    def getStepCost(self,s,d):
        n = self.are_connected(s,d)
        return n.cost
        # return self.graph[vertex].cost
    #Add Edge
    def add_edge(self,source,destination,StepCost):
        node = Node(destination,StepCost)
        node.next = self.graph[source]
        self.graph[source] = node
        

    #Priintf Graph
    def print_graph(self):
        for i in range(self.vertices):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.value), end="")
                temp = temp.next
            print(" \n")
    #Delete edge
    def delete_edge(self,s,d):
        current =  self.graph[s]
        prev = None
        while True:
            if(current.value == d):
                if prev == None:
                    self.graph[s] = current.next
                else:
                    prev.next = current.next
                    del current
                break
            prev = current
            current = current.next
            if current == None:
                break
        
    # get connected node
    def get_connected_nodes(self, node):
        if node < 0 or node >= self.vertices:
            # print("Invalid vertex")
            return None

        # print("Vertex:", node)
        temp = self.graph[node]
        connectedNodes = []
        while temp:
            # print(temp.vertex)
            connectedNodes.append(temp)
            temp = temp.next
        # print("\n")
        return connectedNodes

    def are_connected(self, node1, node2):
        temp = self.graph[node1]
        while temp:
            if(temp.value == node2):
                return temp
            temp=temp.next

        return False
    
    def is_valid(self,path):
        if(has_repeated_letters(path[:4])):
            return False
        if(path[0] != path[len(path)-1]):
            return False
        for i in range(len(path)):
            if(i < len(path)-1):
                if self.are_connected(int( path[i]),int(path[i+1]) ) == False :
                    return False
        return True
    def edgeCost(self,n1,n2):
        temp = self.graph[n1]
        while temp:
            if(temp.value == n2):
                return temp.cost
            temp=temp.next
    def pathCost(self,path):
        cost = 0
        for i in range(len(path)):
            if(i < len(path)-1):
                cost = cost + self.edgeCost(int( path[i]),int(path[i+1]))
        return cost
                # if self.are_connected(int( path[i]),int(path[i+1]) ) == False :
                #     return False



def has_repeated_letters(input_string):
    seen = set()
    for char in input_string:
        if char in seen:
            return True
        seen.add(char)
    return False
from itertools import permutations

def string_permutations(arr , start):
    valid_permutations = []
    first_element = start

    for perm in permutations(arr):
        if perm[0] == first_element:
            valid_permutation = ''.join(perm) + first_element
            valid_permutations.append(valid_permutation)
            # if(graph.is_valid(valid_permutation)):
            #     valid_permutations.append([valid_permutation,graph.pathCost(valid_permutation)])
            # else:
            #     valid_permutations.append([valid_permutation,5000])

    return valid_permutations


def CrossOver(parent1,parent2):
    rnd = random.randint(1, len(parent1)-2)
    offSpring = ""
    for i in range(len(parent1)):
        if i < rnd:
            offSpring = offSpring + parent1[i]
        else:
            offSpring = offSpring + parent2[i]
    return offSpring

def Mutation(offSpring):
    for i in range(10):
        rnd1 = random.randint(1, len(offSpring)-2)
        rnd2 = random.randint(1, len(offSpring)-2)
        offSpring.replace(offSpring[rnd1],offSpring[rnd2])
    return offSpring

    

def TSP_Genetic_Algorithm(graph,population):
    noOfGenerationsWithNoSignificantChanges = 1000
    i = 1
    lower_bound = 0
    upper_bound = len(population)-1
    minimumCost = min(population, key=lambda x: x[1])
    while i <= (noOfGenerationsWithNoSignificantChanges):
        parent1 = population[random.randint(lower_bound, upper_bound)]
        parent2 = population[random.randint(lower_bound, upper_bound)]
        offSpring =  CrossOver(parent1[0],parent2[0])
        offSpring =  Mutation(offSpring)
        if(graph.is_valid(offSpring)):
            cost = graph.pathCost(offSpring)
            population.append([offSpring,cost])
        else:
            population.append([offSpring,10000])
        upper_bound= upper_bound+1
        newMinimumCost = min(population, key=lambda x: x[1])
        if(newMinimumCost >= minimumCost):
            print(i)
            i = i+1
        minimumCost = newMinimumCost
    return sorted(population, key=lambda x: x[1])

def getPopulation(vertices):

    population1 = string_permutations(vertices , '0')
    population2 = string_permutations(vertices , '1')
    population3 = string_permutations(vertices , '2')
    population4 = string_permutations(vertices , '3')
    temp = []
    for i in range(5):
        temp.append(population1[i])
        temp.append(population2[i])
        temp.append(population3[i])
        temp.append(population4[i])
# selected_elements = population1[:5] + population2[:5] + population3[:5] + population4[:5]
    population = []
    for i in range(len(temp)):
        if(graph.is_valid(temp[i])):
            population.append([ temp[i] ,graph.pathCost(temp[i])])
        else:
            population.append([ temp[i] ,10000])
    return population



# graph = Graph(4)
# graph.add_edge(0,1,10)
# graph.add_edge(1,0,10)
# graph.add_edge(2,0,15)
# graph.add_edge(0,2,15)
# graph.add_edge(0,3,20)
# graph.add_edge(3,0,20)
# graph.add_edge(1,2,35)
# graph.add_edge(2,1,35)
# graph.add_edge(3,1,25)
# graph.add_edge(1,3,25)
# graph.add_edge(3,2,30)
# graph.add_edge(2,3,30)

# vertices = ['0','1','2','3']


# print(TSP_Genetic_Algorithm(graph , getPopulation(vertices)))




graph = Graph(6)
graph.add_edge(0,1,45)
graph.add_edge(0,2,92)
graph.add_edge(0,3,40)
graph.add_edge(0,4,71)
graph.add_edge(0,5,67)

graph.add_edge(1,0,45)
graph.add_edge(2,0,92)
graph.add_edge(3,0,40)
graph.add_edge(4,0,71)
graph.add_edge(5,0,67)

graph.add_edge(1,2,50)
graph.add_edge(1,3,20)
graph.add_edge(1,4,42)
graph.add_edge(1,5,54)

graph.add_edge(2,1,50)
graph.add_edge(3,1,20)
graph.add_edge(4,1,42)
graph.add_edge(5,1,54)

graph.add_edge(2,3,54)
graph.add_edge(2,4,36)
graph.add_edge(2,5,58)

graph.add_edge(3,2,54)
graph.add_edge(4,2,36)
graph.add_edge(5,2,58)

graph.add_edge(3,4,32)
graph.add_edge(3,5,36)

graph.add_edge(4,3,32)
graph.add_edge(5,3,36)

graph.add_edge(4,5,22)

graph.add_edge(5,4,22)


vertices = ['0','1','2','3','4','5']


solution =  TSP_Genetic_Algorithm(graph , getPopulation(vertices))[0]

for i in range(len( solution[0])):
    print(solution[0][i]+" -> ",end = "")
print()
print()
print("Optimal Cost = ",solution[1])

