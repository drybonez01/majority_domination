import networkx as nx
import os
import random


def seedset_alg3(graph_file, cost_file, working_dir):
    def load_graph(filename):
        G = nx.read_gml(filename, label='id')
        G = nx.relabel_nodes(G, str)
        return G

    def load_costs(filename):
        costs = {}
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue
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
                        if neighbor not in influenced and random.random() < 0.1:
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

    def save_seed_set_info(seed_set, graph_name, k):
        file_name = f"seedset_{graph_name}_alg3_budget{k}.txt"
        file_path = os.path.join(working_dir, f"risorse", f"seedset", file_name)

        with open(file_path, 'w') as file:
            for node in seed_set:
                file.write(f"{node}\n")

        return file_path

    k = float(input("\nInserisci il valore di k (budget): "))
    R = int(input("Inserisci il numero di mondi possibili campionati (R): "))

    G = load_graph(graph_file)
    costs = load_costs(cost_file)

    graph_name = os.path.splitext(os.path.basename(graph_file))[0]

    S = sampling_greedy(G, costs, k, R)

    print("Seed set massimale trovato:", S)

    return save_seed_set_info(S, graph_name, k)
