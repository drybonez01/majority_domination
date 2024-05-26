import networkx as nx
import os


def seedset_alg2(graph_file, cost_file):
    def load_graph(filename):
        return nx.read_gml(filename, label='id')

    def load_costs(filename):
        costs = {}
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue
                node, cost = parts
                costs[node] = float(cost)
        return costs

    def wtss_algorithm(G, c, k):
        S = set()
        U = set(G.nodes)
        thresholds = {v: (G.degree(v) + 1) // 2 for v in G.nodes}
        k_v = thresholds.copy()

        total_cost = 0

        while U:
            # Case 1: Find a vertex v in U such that k(v) = 0
            zero_threshold_nodes = {v for v in U if k_v[v] == 0}
            if zero_threshold_nodes:
                v = zero_threshold_nodes.pop()
                U.remove(v)
                for u in G.neighbors(v):
                    k_v[u] = max(0, k_v[u] - 1)
                continue

            # Case 2: Find a vertex v in U such that δ(v) = 0
            zero_degree_nodes = {v for v in U if G.degree(v) == 0}
            if zero_degree_nodes:
                v = zero_degree_nodes.pop()
                S.add(v)
                U.remove(v)
                total_cost += c[str(v)]
                for u in G.neighbors(v):
                    k_v[u] = max(0, k_v[u] - 1)
                continue

            # Case 3: Select the vertex v that maximizes δ(v) / c(v)
            if total_cost >= k:
                break

            u = max(U, key=lambda x: (thresholds[x] / c[str(x)]))
            U.remove(u)
            S.add(u)
            total_cost += c[str(u)]
            for v in G.neighbors(u):
                k_v[v] = max(0, k_v[v] - 1)

        return S

    def save_seed_set(seed_set, graph_name):
        dir_path = '../risorse/seedset'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_name = f"seedset_{graph_name}_alg2.txt"
        file_path = os.path.join(dir_path, file_name)

        with open(file_path, 'w') as file:
            for node in seed_set:
                file.write(f"{node}\n")

        return file_path

    '''graph_file = input("Inserisci il percorso del file del grafo (.gml): ")
    cost_file = input("Inserisci il percorso del file dei costi (.txt): ")'''
    k = float(input("\nInserisci il valore di k (budget): "))

    G = load_graph(graph_file)
    c = load_costs(cost_file)

    S = wtss_algorithm(G, c, k)

    graph_name = os.path.splitext(os.path.basename(graph_file))[0]
    print("Seed set massimale trovato:", S)

    return save_seed_set(S, graph_name)
