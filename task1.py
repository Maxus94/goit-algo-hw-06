import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["M Osokorki", "M Levoberezhnaja", "M Demeevskaja", "Pl Darnitskaja", "Bereznyaki", "M Kharkovskaja", "Pr. Grigorenko", "Pl Sevastopolskaja", "Vokzal", "Pl Kontraktovaja", "M Pecherskaja", "Dvorets Ukraina", "M Goloseevskaja", "M Slavutich"])
G.add_edges_from([("M Osokorki", "M Levoberezhnaja"), ("M Osokorki", "M Demeevskaja"), ("M Osokorki", "Pl Sevastopolskaja"), ("M Osokorki", "M Slavutich"), ("M Slavutich", "Pl Sevastopolskaja"), ("M Osokorki", "M Kharkovskaja"), ("M Slavutich", "M Kharkovskaja"), ("M Osokorki", "Pl Darnitskaja"), ("M Osokorki", "Bereznyaki"), ("M Osokorki", "Pr. Grigorenko"), ("M Slavutich", "M Demeevskaja"), ("M Levoberezhnaja", "M Kharkovskaja"), ("M Levoberezhnaja", "Pr. Grigorenko"), ("M Levoberezhnaja", "Bereznyaki"), ("Vokzal", "Pl Sevastopolskaja"), ("Vokzal", "Pl Kontraktovaja"), ("Pl Kontraktovaja", "Pl Darnitskaja"), ("Pl Kontraktovaja", "M Pecherskaja"), ("M Pecherskaja", "Pl Darnitskaja"), ("M Pecherskaja", "Dvorets Ukraina"), ("Dvorets Ukraina", "Pl Sevastopolskaja"), ("M Demeevskaja", "Dvorets Ukraina"), ("M Demeevskaja", "M Goloseevskaja")])
print("number of nodes ", G.number_of_nodes())
print("number of edges ", G.number_of_edges())

for node in G:
    print("rank of", node, "is", len(G[node]))
pos = nx.random_layout(G)

nx.draw(G, pos, with_labels=True, arrows=True)

plt.show()
