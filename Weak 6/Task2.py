import heapq
import copy
class Node:
    def __init__ (self,value,cost):
        self.value = value
        self.next = None
        self.cost = cost
    def __lt__(self, other):
        # Define the less-than comparison based on the 'value' attribute
        return self.value < other.value


class Graph:
    def __init__(self,numberOfVertices,hueristicList):
        self.vertices = numberOfVertices
        self.hueristics = hueristicList
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
        

        # node = Node(source)
        # node.next = self.graph[destination]
        # self.graph[destination] = node
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
        # second
        # current =  self.graph[d]
        # prev = None
        # while True:
        #     if(current.value == s):
        #         if prev == None:
        #             self.graph[d] = current.next
        #         else:
        #             prev.next = current.next
        #         break
        #     prev = current
        #     current = current.next
        #     if current == None:
        #         break

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
    
    # def is_valid(self,path):
    #     for i in range(len(path)):
    #         if(i < len(path)-1):
    #             if self.are_connected(path[i],path[i+1]) == False :
    #                 return False
    #     return True

def A_star(start,goal,graph):
    priority_queue = []
    path = []
    path.append(start)
    heapq.heappush(priority_queue, (graph.hueristics[start-1]+0, path))
    while priority_queue: 
        priority,currPath = heapq.heappop(priority_queue)
        if(currPath[-1] == goal):
            l = [] 
            for i in range(len(currPath)-1):
                l.append(graph.getStepCost(currPath[i],currPath[i+1]))
            return currPath,sum(l)
        else:
            children = graph.get_connected_nodes(currPath[-1])
            for i in range(len(children)):
                newPath = copy.deepcopy(currPath)
                newPath.append(children[i].value)
                heapq.heappush(priority_queue, (graph.getStepCost(currPath[-1],children[i].value)+graph.hueristics[children[i].value -1]+priority, newPath))







graph = Graph(10,[10,8,6,5,7,5,3,3,1,0])
graph.add_edge(1,2,6)
graph.add_edge(1,3,3)
graph.add_edge(2,4,3)
graph.add_edge(2,5,2)
graph.add_edge(3,6,1)
graph.add_edge(3,7,7)
graph.add_edge(4,5,1)
graph.add_edge(4,8,5)
graph.add_edge(5,8,8)
graph.add_edge(6,9,3)
graph.add_edge(7,9,2)
graph.add_edge(8,9,5)
graph.add_edge(8,10,5)
graph.add_edge(9,10,3)


solution,cost = A_star(1,10,graph)


for i in range (len(solution)):
    print(str(solution[i]) + " -> ",end = "")

print()
print()
print("Total Cost = "+str(cost))