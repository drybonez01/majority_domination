import snap
import random
import networkx as nx
import matplotlib.pyplot as plt

# Funzione per convertire un grafo SNAP in un grafo NetworkX
def snap_to_nx(snap_graph):
    nx_graph = nx.Graph()
    for NI in snap_graph.Nodes():
        nx_graph.add_node(NI.GetId())
    for EI in snap_graph.Edges():
        nx_graph.add_edge(EI.GetSrcNId(), EI.GetDstNId())
    return nx_graph

# Funzione per assegnare pesi randomici ai nodi
def assign_random_weights_to_snap(snap_graph, weight_range=(1, 10)):
    weights = {}
    for NI in snap_graph.Nodes():
        weights[NI.GetId()] = random.randint(*weight_range)
    return weights

# Carica il grafo da un file binario
FIn = snap.TFIn("graph/graph.graph")
snap_graph = snap.TUNGraph.Load(FIn)

# Assegna pesi randomici ai nodi
node_weights = assign_random_weights_to_snap(snap_graph, weight_range=(1, 10))

# Converte il grafo SNAP in un grafo NetworkX
nx_graph = snap_to_nx(snap_graph)

# Aggiungi i pesi come attributi ai nodi nel grafo NetworkX
nx.set_node_attributes(nx_graph, node_weights, 'weight')

# Visualizza il grafo con pesi
pos = nx.spring_layout(nx_graph)  # layout del grafo
plt.figure(figsize=(12, 8))  # dimensioni della figura

# Disegna i nodi con i pesi come etichette
node_labels = {node: f"{node}\n({data['weight']})" for node, data in nx_graph.nodes(data=True)}
nx.draw(nx_graph, pos, with_labels=True, labels=node_labels, node_size=500, node_color="skyblue", font_size=10, font_color="black", edge_color="gray")

plt.title("Visualizzazione del Grafo con Pesi Randomici")
plt.show()
