import networkx as nx
import os


def majority_influence_diffusion(graph_file, seed_set_file):
    def load_graph(filename):
        G = nx.read_gml(filename, label='id')
        return G

    def load_seed_set(filename):
        seed_set = set()
        with open(filename, 'r') as file:
            for line in file:
                seed_set.add(line.strip())
        return seed_set

    def influence_diffusion(graph, initial_states, seed_set):
        states = initial_states.copy()
        changed = True
        iteration = 0
        total_influenced = 0  # Contatore dei nodi influenzati
        influenced_nodes_set = set()  # Set dei nodi influenzati

        while changed:
            changed = False
            new_states = states.copy()

            for node in graph:
                if node in seed_set or states[node] == 1:
                    continue  # Ignora i nodi già influenzati o appartenenti al seed set

                neighbor_states = [states[neighbor] for neighbor in graph.neighbors(node)]
                if neighbor_states:
                    majority_state = 1 if neighbor_states.count(1) > neighbor_states.count(0) else 0
                    if neighbor_states.count(1) == neighbor_states.count(0):
                        majority_state = states[node]  # Mantenere lo stato corrente in caso di parità

                    if new_states[node] != majority_state:
                        new_states[node] = majority_state
                        changed = True

            if changed:
                influenced_nodes = {node for node, state in new_states.items() if state == 1 and states[node] == 0}
                influenced_nodes_set.update(influenced_nodes)  # Aggiungi i nodi influenzati al set
                total_influenced = len(influenced_nodes_set)  # Aggiorna il contatore
                print(f"Iteration {iteration}: {set(influenced_nodes)}")
                iteration += 1
                states = new_states
            else:
                print(f"Iteration {iteration}: No changes")

        return influenced_nodes_set, total_influenced

    def save_influenced_info(influenced_nodes, algorithm_name, graph_name):
        dir_path = os.path.join('../risorse', 'informazioni')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_name = f"informazioni_{algorithm_name}_{graph_name}.txt"
        file_path = os.path.join(dir_path, file_name)

        with open(file_path, 'w') as file:
            file.write(f"Numero di nodi influenzati: {len(influenced_nodes)}\n")
            for node in influenced_nodes:
                file.write(f"{node}\n")

    '''graph_file = input("Inserisci il percorso del file del grafo (.gml): ")
    seed_set_file = input("Inserisci il percorso del file del seed set (.txt): ")'''

    graph_name = os.path.splitext(os.path.basename(graph_file))[0]
    algorithm_name = os.path.splitext(os.path.basename(__file__))[0]

    G = load_graph(graph_file)
    seed_set = load_seed_set(seed_set_file)

    G = nx.relabel_nodes(G, str)
    seed_set = {str(node) for node in seed_set}
    seed_set = {node for node in seed_set if node in G.nodes()}

    initial_states = {node: 1 if node in seed_set else 0 for node in G.nodes()}
    initial_seed_set_states = {node: initial_states[node] for node in seed_set}
    print(f"\nInitial seed set states: {set(initial_seed_set_states.keys())}")

    influenced_nodes, total_influenced = influence_diffusion(G, initial_states, seed_set)

    print(f"Numero totale di nodi influenzati: {total_influenced}")

    save_influenced_info(influenced_nodes, algorithm_name, graph_name)
