from collections import defaultdict, deque

class Graph_BFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def bfs(self, start, end):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            if current == end:
                break

            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

if __name__ == "__main__":
    graf = {
        '0': [('3', 8), ('4', 4)],
        '3': [('7', 9), ('1', 6)],
        '1': [('0', 2), ('6', 11)],
        '7': [('5', 3)],
        '5': [('7', 2), ('6', 0)],
        '6': [('4', 0), ('2', 4)],
        '4': [('6', 5)],
        '2': [('5', 0), ('6', 1)],
        '9': []
    }

    g = Graph_BFS()
    for node, neighbors in graf.items():
        for neighbor, weight in neighbors:
            g.add_edge(node, neighbor, weight)

    print("BFS Traversal (0 ke 7):")
    g.bfs('0', '7')
