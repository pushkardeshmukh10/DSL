from collections import deque  
adj_list = {
    "A": ['B', 'C'],
    "B": ['A', 'D'],
    "C": ['A', 'D'],
    "D": ['B', 'C'],
}

def BFS_list(start, adj_list):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return result 

def menu():
    while True: 
        print("1. BFS Traversal")
        print("2. Exit")
        
        ch = input("Enter choice: ").strip() 
        
        if ch == '1':
            start = input("Enter start node: ").strip()
            if start in adj_list:
                print("BFS:", BFS_list(start, adj_list))
            else:
                print("Node not found. Please enter a valid node.")
        
        elif ch == '2':
            print("Exiting...")  
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Call menu to start program
menu()
