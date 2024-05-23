import networkx as nx
import matplotlib.pyplot as plt

# Carica il grafo da un file GML utilizzando NetworkX
nx_graph = nx.read_gml("risorse/karate.gml", label=None)

# Visualizza il grafo
pos = nx.spring_layout(nx_graph)  # layout del grafo
plt.figure(figsize=(24, 16))  # dimensioni della figura
nx.draw(nx_graph, pos, with_labels=True, node_size=34, node_color="skyblue", font_size=10, font_color="black", edge_color="gray")
plt.title("Visualizzazione del Grafo Karate Club")
plt.show()
