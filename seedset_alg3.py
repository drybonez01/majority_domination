import networkx as nx
import os
import random

def load_graph(filename):
    # Carica il grafo dal file .gml usando networkx con label='id'
    G = nx.read_gml(filename, label='id')
    G = nx.relabel_nodes(G, str)  # Rilabel i nodi come stringhe
    return G

def load_costs(filename):
    costs = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2:
                continue  # Ignora le righe non valide
            try:
                node = parts[0]
                cost = float(parts[1])
                costs[node] = cost
            except ValueError as e:
                print(f"Errore nella conversione dei dati: {e}")
                continue
    return costs

def influence_spread(G, S, R):
    """
    Stima la diffusione dell'influenza nel grafo G a partire dal seed set S usando R simulazioni.
    """
    influenced_counts = []
    for _ in range(R):
        new_active = set(S)
        influenced = set(S)
        while new_active:
            next_active = set()
            for node in new_active:
                neighbors = list(G.neighbors(node))
                for neighbor in neighbors:
                    if neighbor not in influenced and random.random() < 0.1:  # Assume a fixed probability of 0.1
                        next_active.add(neighbor)
                        influenced.add(neighbor)
            new_active = next_active
        influenced_counts.append(len(influenced))
    return sum(influenced_counts) / R

def sampling_greedy(G, costs, budget, R):
    S = set()
    total_cost = 0

    while True:
        best_node = None
        best_spread = 0
        for node in G.nodes:
            if node not in S and total_cost + costs[node] <= budget:
                spread = influence_spread(G, S | {node}, R)
                cost_efficiency = spread / costs[node]
                if cost_efficiency > best_spread:
                    best_spread = cost_efficiency
                    best_node = node

        if not best_node:
            break

        S.add(best_node)
        total_cost += costs[best_node]

    return S

def save_seed_set_info(seed_set, graph_name):
    dir_path = os.path.join('risorse', 'seedset')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_name = f"seedset_{graph_name}_alg3.txt"
    file_path = os.path.join(dir_path, file_name)

    with open(file_path, 'w') as file:
        for node in seed_set:
            file.write(f"{node}\n")

def main():
    graph_file = input("Inserisci il percorso del file del grafo (.gml): ")
    cost_file = input("Inserisci il percorso del file dei costi (.txt): ")
    k = float(input("Inserisci il valore di k: "))
    R = int(input("Inserisci il numero di mondi possibili campionati (R): "))

    G = load_graph(graph_file)
    costs = load_costs(cost_file)

    graph_name = os.path.splitext(os.path.basename(graph_file))[0]

    S = sampling_greedy(G, costs, k, R)

    print("Seed set massimale trovato:", S)

    save_seed_set_info(S, graph_name)

if __name__ == "__main__":
    main()
