import networkx as nx
import os

def load_graph(filename):
    # Carica il grafo dal file .gml usando networkx con label='id'
    G = nx.read_gml(filename, label='id')
    return G

def load_seed_set(filename):
    seed_set = set()
    with open(filename, 'r') as file:
        for line in file:
            seed_set.add(line.strip())
    return seed_set

def majority_influence_diffusion(graph, initial_states):
    # Copia degli stati iniziali per evitare di modificare l'input originale
    states = initial_states.copy()
    changed = True
    iteration = 0

    while changed:
        changed = False
        new_states = states.copy()

        for node in graph:
            neighbor_states = [states[neighbor] for neighbor in graph.neighbors(node)]
            if neighbor_states:
                majority_state = 1 if neighbor_states.count(1) > neighbor_states.count(0) else 0
                if neighbor_states.count(1) == neighbor_states.count(0):
                    majority_state = states[node]  # Mantenere lo stato corrente in caso di parità

                if new_states[node] != majority_state:
                    new_states[node] = majority_state
                    changed = True

        if changed:
            # Debug: stampa gli stati dei nodi influenzati dopo ogni iterazione
            influenced_nodes = {node for node, state in new_states.items() if state == 1 and states[node] == 0}
            print(f"Iteration {iteration}: {influenced_nodes}")
            iteration += 1
            states = new_states
        else:
            print(f"Iteration {iteration}: No changes")

    return states

def save_expansion_info(expansion, algorithm_name, graph_name):
    # Crea la cartella 'risorse/informazioni' se non esiste
    dir_path = os.path.join('risorse', 'informazioni')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Nome del file
    file_name = f"informazioni_{algorithm_name}_{graph_name}.txt"
    file_path = os.path.join(dir_path, file_name)

    # Salva l'espansione nel file
    with open(file_path, 'w') as file:
        file.write(f"Numero di nodi attivati: {len(expansion)}\n")
        for node in expansion:
            file.write(f"{node}\n")

def main():
    graph_file = input("Inserisci il percorso del file del grafo (.gml): ")
    seed_set_file = input("Inserisci il percorso del file del seed set (.txt): ")

    # Ottieni il nome del file di input per il grafo senza estensione
    graph_name = os.path.splitext(os.path.basename(graph_file))[0]
    # Ottieni il nome del file Python senza estensione
    algorithm_name = os.path.splitext(os.path.basename(__file__))[0]

    G = load_graph(graph_file)
    seed_set = load_seed_set(seed_set_file)

    # Converti tutti i nodi del grafo e del seed set in stringhe
    G = nx.relabel_nodes(G, str)
    seed_set = {str(node) for node in seed_set}

    # Filtra i nodi del seed set che non sono nel grafo
    seed_set = {node for node in seed_set if node in G.nodes()}

    # Imposta lo stato iniziale per ogni nodo (1 per i nodi nel seed set, 0 per gli altri)
    initial_states = {node: 1 if node in seed_set else 0 for node in G.nodes()}

    # Debug: stampa gli stati iniziali dei nodi nel seed set
    initial_seed_set_states = {node: initial_states[node] for node in seed_set}
    print(f"Initial seed set states: {set(initial_seed_set_states.keys())}")

    # Applica l'algoritmo di diffusione dell'influenza
    final_states = majority_influence_diffusion(G, initial_states)

    # Ottieni l'espansione come l'insieme dei nodi influenzati (stato 1)
    expansion = {node for node, state in final_states.items() if state == 1}

    print(f"Numero totale di nodi attivati: {len(expansion)}")

    save_expansion_info(expansion, algorithm_name, graph_name)

if __name__ == "__main__":
    main()
