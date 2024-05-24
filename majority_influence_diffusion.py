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

def majority_influence_diffusion(G, seed_set):
    influenced_set = set(seed_set)
    new_influenced_set = set(seed_set)

    iteration = 0
    while True:
        next_influenced_set = set()
        for node in G.nodes():
            if node not in influenced_set:
                neighbors = set(G.neighbors(node))
                influenced_neighbors = neighbors.intersection(influenced_set)
                # Debug: print neighbors and influenced neighbors
                print(f"Node: {node}, Neighbors: {neighbors}, Influenced Neighbors: {influenced_neighbors}")
                if len(influenced_neighbors) > len(neighbors) // 2:
                    next_influenced_set.add(node)

        # Debug: print the new influenced set after each iteration
        print(f"Iteration {iteration}: {next_influenced_set}")
        iteration += 1

        if not next_influenced_set:
            break

        new_influenced_set.update(next_influenced_set)
        influenced_set.update(next_influenced_set)

    return influenced_set

def save_expansion(expansion, algorithm_name, graph_name):
    # Crea la cartella 'risorse' se non esiste
    if not os.path.exists('risorse'):
        os.makedirs('risorse')

    # Nome del file
    file_name = f"expansion_{algorithm_name}_{graph_name}.txt"
    file_path = os.path.join('risorse', file_name)

    # Salva l'espansione nel file
    with open(file_path, 'w') as file:
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

    expansion = majority_influence_diffusion(G, seed_set)

    print(f"Espansione del seed set: {expansion}")

    save_expansion(expansion, algorithm_name, graph_name)

if __name__ == "__main__":
    main()
