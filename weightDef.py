import networkx as nx
import random
import os
import math

def load_graph(filename):
    G = nx.read_gml(filename, label='id')
    return G

def assign_random_weights_to_networkx(graph, weight_range):
    weights = {}
    for node in graph.nodes():
        weights[node] = random.randint(*weight_range)
    return weights

def assign_degree_based_weights(graph):
    weights = {}
    for node in graph.nodes():
        degree = graph.degree(node)
        weights[node] = math.ceil(degree / 2)
    return weights

def assign_betweenness_based_weights(graph):
    betweenness = nx.betweenness_centrality(graph)
    weights = {node: math.ceil(value * 100) for node, value in betweenness.items()}
    return weights

def save_weights_to_file(weights, filename):
    with open(filename, "w") as f:
        for node_id, weight in weights.items():
            f.write(f"{node_id} {weight}\n")

def main():
    graph_path = input("Inserisci il percorso del file .gml: ")

    G = load_graph(graph_path)

    print("Numero di nodi:", G.number_of_nodes())
    print("Numero di archi:", G.number_of_edges())

    for node in G.nodes():
        print(f"Nodo {node} ha {G.degree(node)} archi")

    method = input("Scegli il metodo per assegnare i pesi ai nodi:\n1. Pesi randomici\n2. Pesi basati sul grado (⌈d(u)/2⌉)\n3. Pesi basati sulla centralità di betweenness\nInserisci 1, 2 o 3: ")

    if method == "1":
        weight_min = int(input("Inserisci il valore minimo del range dei pesi: "))
        weight_max = int(input("Inserisci il valore massimo del range dei pesi: "))
        node_weights = assign_random_weights_to_networkx(G, (weight_min, weight_max))
        file_suffix = "random"
    elif method == "2":
        node_weights = assign_degree_based_weights(G)
        file_suffix = "degree_based"
    elif method == "3":
        node_weights = assign_betweenness_based_weights(G)
        file_suffix = "betweenness_based"
    else:
        print("Metodo non valido. Uscita.")
        return

    print("\nPesi assegnati ai nodi:")
    for node_id, weight in node_weights.items():
        print(f"Nodo {node_id}: Peso {weight}")

    graph_name = os.path.splitext(os.path.basename(graph_path))[0]
    weights_file_name = f"{graph_name}_node_weights_{file_suffix}.txt"

    weights_file_path = os.path.join('risorse', 'weights', weights_file_name)

    os.makedirs(os.path.dirname(weights_file_path), exist_ok=True)

    save_weights_to_file(node_weights, weights_file_path)

    print(f"Pesi salvati in: {weights_file_path}")

if __name__ == "__main__":
    main()
