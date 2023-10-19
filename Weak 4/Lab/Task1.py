class Graph:
    def __init__(self,numberOfVertices):
        self.vertices = numberOfVertices
        self.graph = [None]*self.vertices
    #Add Edge
    def add_edge(self,source,destination):
        node = Node(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = Node(source)
        node.next = self.graph[destination]
        self.graph[destination] = node
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
        current =  self.graph[d]
        prev = None
        while True:
            if(current.value == s):
                if prev == None:
                    self.graph[d] = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next
            if current == None:
                break

    # get connected node
    def get_connected_nodes(self, node):
        if node < 0 or node >= self.V:
            print("Invalid vertex")
            return

        print("Vertex:", node)
        temp = self.graph[node]
        while temp:
            print(temp.vertex)
            temp = temp.next
        print("\n")

    def are_connected(self, node1, node2):
        temp = self.graph[node1]
        while temp:
            if(temp.vertex == node2):
                return True
            temp=temp.next

        return False
    
    def is_valid(self,path):
        for i in range(len(path)):
            if(i < len(path)-1):
                if self.are_connected(path[i],path[i+1]) == False :
                    return False

        return True
        


    

class Node:
    def __init__ (self,value):
        self.value = value
        self.next = None




graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)







graph.print_graph()
graph.delete_edge(0,3)
graph.print_graph()



