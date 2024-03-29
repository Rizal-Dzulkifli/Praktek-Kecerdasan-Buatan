graph_bfs = {
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

def bfs(visited, graph, start, end):
    queue = []
    path = []

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        path.append(node)

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return path

print("Traversal dari Node A ke Node I menggunakan BFS:")
visited_bfs = set()
print(bfs(visited_bfs, graph_bfs, 'a', 'i'))
