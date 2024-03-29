from collections import defaultdict

class Graph_DFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dfs_util(self, current, visited, end):
        print(current, end=" ")
        if current == end:
            return True

        for neighbor, _ in self.graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                if self.dfs_util(neighbor, visited, end):
                    return True
        return False

    def dfs(self, start, end):
        visited = set()
        visited.add(start)
        self.dfs_util(start, visited, end)

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

    g = Graph_DFS()
    for node, neighbors in graf.items():
        for neighbor, weight in neighbors:
            g.add_edge(node, neighbor, weight)

    print("\nDFS Traversal (0 ke 7):")
    g.dfs('0', '7')
