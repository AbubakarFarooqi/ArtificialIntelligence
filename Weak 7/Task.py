from itertools import permutations




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
        for i in range(len(path)-1):
            if(i < len(path)-1):
                cost = cost + self.edgeCost(int( path[i]),int(path[i+1]))
                return cost
                # if self.are_connected(int( path[i]),int(path[i+1]) ) == False :
                #     return False




from itertools import permutations

def string_permutations(arr , start):
    valid_permutations = []
    first_element = start

    for perm in permutations(arr):
        if perm[0] == first_element:
            valid_permutation = ''.join(perm) + first_element
            # valid_permutations.append(valid_permutation)
            if(graph.is_valid(valid_permutation)):
                valid_permutations.append([valid_permutation,graph.pathCost(valid_permutation)])
            else:
                valid_permutations.append([valid_permutation,5000])

    return valid_permutations


graph = Graph(4)
graph.add_edge(0,1,4)
graph.add_edge(1,0,4)
graph.add_edge(1,2,2)
graph.add_edge(2,1,2)
graph.add_edge(2,0,6)
graph.add_edge(0,2,6)
graph.add_edge(0,3,7)
graph.add_edge(3,0,7)
graph.add_edge(3,1,8)
graph.add_edge(1,3,8)

vertices = ['0','1','2','3']

population = string_permutations(vertices , '0')
for permutation in population:
        print(permutation)



# for i in range(1000):
#     CrossOver()
#     Mutation()
