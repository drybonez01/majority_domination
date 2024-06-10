import networkx as nx
import random
import os
import math


def weightDef(graph_path, working_dir):
    def load_graph(filename):
        graph = nx.read_gml(filename, label='id')
        return graph

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
        weights = {node: max(math.ceil(value * 100), 1) for node, value in betweenness.items()}
        return weights


    def save_weights_to_file(weights, filename):
        with open(filename, "w") as f:
            for node_id, weight in weights.items():
                f.write(f"{node_id} {weight}\n")

    g = load_graph(graph_path)

    print("\nNumero di nodi:", g.number_of_nodes())
    print("Numero di archi:", g.number_of_edges())

    node_weights = None
    file_suffix = None
    while True:
        method = input(
            "\nScegli il metodo per assegnare i pesi ai nodi:\n1. Pesi randomici\n2. Pesi basati sul grado\n3. "
            "Pesi basati sulla centralità di betweenness\nInserisci 1, 2 o 3: ")

        if method == "1":
            weight_min = int(input("\nInserisci il valore minimo del range dei pesi: "))
            weight_max = int(input("Inserisci il valore massimo del range dei pesi: "))
            node_weights = assign_random_weights_to_networkx(g, (weight_min, weight_max))
            file_suffix = "random"
            break
        elif method == "2":
            node_weights = assign_degree_based_weights(g)
            file_suffix = "degree_based"
            break
        elif method == "3":
            node_weights = assign_betweenness_based_weights(g)
            file_suffix = "betweenness_based"
            break
        else:
            print("Metodo non valido. Riprovare.")

    graph_name = os.path.splitext(os.path.basename(graph_path))[0]
    weights_file_name = f"{graph_name}_node_weights_{file_suffix}.txt"
    weights_file_path = os.path.join(working_dir, f"risorse", f"weights", weights_file_name)
    print(weights_file_path)
    os.makedirs(os.path.dirname(weights_file_path), exist_ok=True)
    save_weights_to_file(node_weights, weights_file_path)

    print(f"\nPesi salvati in: {weights_file_path}")
    return weights_file_path
