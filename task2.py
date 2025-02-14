import networkx as nx

G = nx.Graph()

G.add_nodes_from(["M Osokorki", "M Levoberezhnaja", "M Demeevskaja", "Pl Darnitskaja", "Bereznyaki", "M Kharkovskaja", "Pr. Grigorenko", "Pl Sevastopolskaja", "Vokzal", "Pl Kontraktovaja", "M Pecherskaja", "Dvorets Ukraina", "M Goloseevskaja", "M Slavutich"])

G.add_edges_from([("M Osokorki", "M Levoberezhnaja"), ("M Osokorki", "M Demeevskaja"), ("M Osokorki", "Pl Sevastopolskaja"), ("M Osokorki", "M Slavutich"), ("M Slavutich", "Pl Sevastopolskaja"), ("M Osokorki", "M Kharkovskaja"), ("M Slavutich", "M Kharkovskaja"), ("M Osokorki", "Pl Darnitskaja"), ("M Osokorki", "Bereznyaki"), ("M Osokorki", "Pr. Grigorenko"), ("M Slavutich", "M Demeevskaja"), ("M Levoberezhnaja", "M Kharkovskaja"), ("M Levoberezhnaja", "Pr. Grigorenko"), ("M Levoberezhnaja", "Bereznyaki"), ("Vokzal", "Pl Sevastopolskaja"), ("Vokzal", "Pl Kontraktovaja"), ("Pl Kontraktovaja", "Pl Darnitskaja"), ("Pl Kontraktovaja", "M Pecherskaja"), ("M Pecherskaja", "Pl Darnitskaja"), ("M Pecherskaja", "Dvorets Ukraina"), ("Dvorets Ukraina", "Pl Sevastopolskaja"), ("M Demeevskaja", "Dvorets Ukraina"), ("M Demeevskaja", "M Goloseevskaja")])

from collections import deque

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:  
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" \n")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited  


def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]  
    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' \n')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  

graph = {
    "M Osokorki": ["M Levoberezhnaja", "M Demeevskaja", "Pl Sevastopolskaja", "M Slavutich", "M Kharkovskaja", "Pl Darnitskaja", "Bereznyaki", "Pr. Grigorenko"],
    "M Slavutich": ["M Osokorki", "Pl Sevastopolskaja", "M Kharkovskaja", "M Demeevskaja"],
    "M Demeevskaja": ["M Osokorki", "M Slavutich", "Dvorets Ukraina", "M Goloseevskaja"],
    "M Kharkovskaja": ["M Osokorki", "M Slavutich", "M Levoberezhnaja"],
    "Pr. Grigorenko": ["M Osokorki", "M Levoberezhnaja"],
    "Bereznyaki": ["M Osokorki", "M Levoberezhnaja"],
    "M Levoberezhnaja": ["M Osokorki", "M Kharkovskaja", "Pr. Grigorenko", "Bereznyaki"],
    "Pl Darnitskaja": ["M Osokorki", "Pl Kontraktovaja", "M Pecherskaja"],
    "M Goloseevskaja": ["M Demeevskaja"],
    "Pl Sevastopolskaja": ["M Osokorki", "M Slavutich", "Vokzal", "Dvorets Ukraina"],
    "Vokzal": ["Pl Sevastopolskaja", "Pl Kontraktovaja"],
    "Pl Kontraktovaja": ["Vokzal", "Pl Darnitskaja", "M Pecherskaja"],
    "M Pecherskaja": ["Pl Kontraktovaja", "Pl Darnitskaja", "Dvorets Ukraina"],
    "Dvorets Ukraina": ["M Pecherskaja", "M Demeevskaja", "Pl Sevastopolskaja"]
}

print("DFS")
dfs_iterative(graph, 'M Osokorki')
print("\nBFS")
bfs_iterative(graph, 'M Osokorki')

