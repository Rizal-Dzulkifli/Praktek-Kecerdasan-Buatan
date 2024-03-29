graph_dfs = {
    'a': ['b', 'c'],
    'b': ['h'],
    'c': ['d', 'e'],
    'd': ['f', 'g'],
    'f': ['h'],
    'g': ['i'],
    'e': ['i'],
    'h': ['i'],
    'i': []
}

def dfs(graph, start, end):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in path:
                if neighbor == end:
                    return path + [neighbor]
                else:
                    stack.append((neighbor, path + [neighbor]))

print("Traversal dari Node A ke Node I menggunakan DFS:")
print(dfs(graph_dfs, 'a', 'i'))


