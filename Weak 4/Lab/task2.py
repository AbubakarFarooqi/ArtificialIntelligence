from collections import deque

def breadth_first_search(graph, start, goal):
    # Initialize a queue for BFS 
    queue = deque()
    visited = set()

    # Add the start node as the initial path
    queue.append([start])

    while queue:
        current_path = queue.popleft()  # Dequeue the current path
        current_node = current_path[-1]  

        if current_node == goal:
            return current_path  

        if current_node not in visited:
            visited.add(current_node)
         
            for neighbor in graph.get(current_node, []):
                new_path = current_path + [neighbor]
                queue.append(new_path)

    return [] 

def depth_first_search(graph, start, goal):
    # Initialize a stack for DFS 
    stack = []
    visited = set()

    # Add the start node as the initial path
    stack.append([start])

    while stack:
        current_path = stack.pop()  
        current_node = current_path[-1]  

        if current_node == goal:
            return current_path  

        if current_node not in visited:
            visited.add(current_node)
            
            for neighbor in graph.get(current_node, []):
                new_path = current_path + [neighbor]
                stack.append(new_path)

    return []  

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

start_node = 'A'
goal_node = 'F'

bfs_result = breadth_first_search(graph, start_node, goal_node)
dfs_result = depth_first_search(graph, start_node, goal_node)

print(bfs_result)
print(dfs_result)
