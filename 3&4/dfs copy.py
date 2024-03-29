from collections import defaultdict

class Graf:
    def __init__(self):
        self.graf = defaultdict(list)

    def tambah_sisi(self, u, v, bobot):
        self.graf[u].append((v, bobot))
        self.graf[v].append((u, bobot))

    def dfs(self, awal, tujuan):
        tumpukan = [(awal, [awal], 0)] 
        while tumpukan:
            (node, path, total_bobot) = tumpukan.pop()
            if node == tujuan:
                return path, total_bobot
            for node_tetangga, bobot_sisi in self.graf[node]:
                if node_tetangga not in path:
                    tumpukan.append((node_tetangga, path + [node_tetangga], total_bobot + bobot_sisi))

graf = {
    '1': [('2', 1), ('3', 2)],
    '2': [('5', 12), ('4', 6)],
    '3': [('4', 3), ('6', 4)],
    '4': [('5', 4), ('7', 15), ('8', 7), ('6', 3)],
    '5': [('7', 7)],
    '6': [('8', 7), ('9', 15)],
    '7': [('9', 3)],
    '8': [('9', 10)],
    '9': []
}

g = Graf()

for node, sisi in graf.items():
    for sisi_tujuan, bobot in sisi:
        g.tambah_sisi(node, sisi_tujuan, bobot)

node_awal = '1'  # Rumah
node_tujuan = '9'   # Kantor
path_dfs, bobot_dfs = g.dfs(node_awal, node_tujuan)

# Cetak jalur DFS dan total bobot
print("\nJalur DFS dari Rumah ke Kantor:", path_dfs)
print("Total Bobot Jalur DFS:", bobot_dfs)
