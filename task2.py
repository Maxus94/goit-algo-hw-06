import networkx as nx

G = nx.Graph()

# Додавання ребер
G.add_nodes_from(["M Osokorki", "M Levoberezhnaja", "M Demeevskaja", "Pl Darnitskaja", "Bereznyaki", "M Kharkovskaja", "Pr. Grigorenko", "Pl Sevastopolskaja", "Vokzal", "Pl Kontraktovaja", "M Pecherskaja", "Dvorets Ukraina", "M Goloseevskaja", "M Slavutich"])

G.add_edges_from([("M Osokorki", "M Levoberezhnaja"), ("M Osokorki", "M Demeevskaja"), ("M Osokorki", "Pl Sevastopolskaja"), ("M Osokorki", "M Slavutich"), ("M Slavutich", "Pl Sevastopolskaja"), ("M Osokorki", "M Kharkovskaja"), ("M Slavutich", "M Kharkovskaja"), ("M Osokorki", "Pl Darnitskaja"), ("M Osokorki", "Bereznyaki"), ("M Osokorki", "Pr. Grigorenko"), ("M Slavutich", "M Demeevskaja"), ("M Levoberezhnaja", "M Kharkovskaja"), ("M Levoberezhnaja", "Pr. Grigorenko"), ("M Levoberezhnaja", "Bereznyaki"), ("Vokzal", "Pl Sevastopolskaja"), ("Vokzal", "Pl Kontraktovaja"), ("Pl Kontraktovaja", "Pl Darnitskaja"), ("Pl Kontraktovaja", "M Pecherskaja"), ("M Pecherskaja", "Pl Darnitskaja"), ("M Pecherskaja", "Dvorets Ukraina"), ("Dvorets Ukraina", "Pl Sevastopolskaja"), ("M Demeevskaja", "Dvorets Ukraina"), ("M Demeevskaja", "M Goloseevskaja")])

from collections import deque

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" \n")
            
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  


def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' \n')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))  

# Представлення графа за допомогою списку суміжності
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
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

# Виклик функції DFS
print("DFS")
dfs_iterative(graph, 'M Osokorki')
print("\nBFS")
bfs_iterative(graph, 'M Osokorki')

