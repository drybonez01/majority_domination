import networkx as nx
import os


def seedset_alg1(graph_file, cost_file, working_dir):
    def load_graph(filename):
        g = nx.read_gml(filename, label='id')
        return g

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

    def f1(S, V, N):
        result = 0
        for v in V:
            n_v_intersection_s = len(N[v].intersection(S))
            result += min(n_v_intersection_s, len(N[v]) // 2)
        return result

    def cost_seeds_greedy(G, k, c):
        Sp = set()
        Sd = set()
        total_cost = 0

        N = {v: set(G.neighbors(v)) for v in G.nodes}

        while True:
            u = max((v for v in G.nodes if v not in Sd),
                    key=lambda v: (f1(Sd.union({v}), G.nodes, N) - f1(Sd, G.nodes, N)) / c[str(v)])

            node_cost = c[str(u)]

            if total_cost + node_cost > k:
                break

            Sp.add(u)
            Sd.add(u)
            total_cost += node_cost

        return Sp

    def save_seed_set_info(seed_set, graph_name, k):
        file_name = f"seedset_{graph_name}_alg1_budget{k}.txt"
        file_path = os.path.join(working_dir, f"risorse", f"seedset", file_name)

        with open(file_path, 'w') as file:
            for node in seed_set:
                file.write(f"{node}\n")

        return file_path

    k = float(input("\nInserisci il valore di k (budget): "))

    G = load_graph(graph_file)
    c = load_costs(cost_file)

    graph_name = os.path.splitext(os.path.basename(graph_file))[0]

    Sp = cost_seeds_greedy(G, k, c)

    print("Seed set massimale trovato:", Sp)

    return save_seed_set_info(Sp, graph_name, k)
