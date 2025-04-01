graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs_stack(graph,start_node):
  stack=[start_node]
  visited=set()
  while stack:
    current_node=stack.pop()
    if current_node not in visited:
      print(current_node,end=' ')
      visited.add(current_node)
      for neighbor in reversed(graph[current_node]):
        if neighbor not in visited:
          stack.append(neighbor)
print("DFs traversal order (using stack):")
dfs_stack(graph,'A')


   
