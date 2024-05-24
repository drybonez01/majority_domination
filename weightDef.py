import networkx as nx
import random
import os

# Funzione per caricare il grafo da un file .gml
def load_graph(filename):
    G = nx.read_gml(filename, label='id')
    return G

# Funzione per assegnare pesi randomici ai nodi
def assign_random_weights_to_networkx(graph, weight_range):
    weights = {}
    for node in graph.nodes():
        weights[node] = random.randint(*weight_range)
    return weights

def save_weights_to_file(weights, filename):
    with open(filename, "w") as f:
        for node_id, weight in weights.items():
            f.write(f"{node_id} {weight}\n")

def main():
    # Chiedi all'utente il percorso del file .gml
    graph_path = input("Inserisci il percorso del file .gml: ")

    # Carica il grafo
    G = load_graph(graph_path)

    # Visualizza alcune informazioni sul grafo
    print("Numero di nodi:", G.number_of_nodes())
    print("Numero di archi:", G.number_of_edges())

    # Esempio di alcune operazioni sul grafo
    for node in G.nodes():
        print(f"Nodo {node} ha {G.degree(node)} archi")

    # Chiedi all'utente il range di valori dei pesi da assegnare
    weight_min = int(input("Inserisci il valore minimo del range dei pesi: "))
    weight_max = int(input("Inserisci il valore massimo del range dei pesi: "))

    # Assegna pesi randomici ai nodi
    node_weights = assign_random_weights_to_networkx(G, (weight_min, weight_max))

    # Visualizza i pesi assegnati
    print("\nPesi assegnati ai nodi:")
    for node_id, weight in node_weights.items():
        print(f"Nodo {node_id}: Peso {weight}")

    # Salva i pesi in un file di testo separato
    weights_file_path = input("Inserisci il percorso per salvare il file dei pesi (node_weights.txt): ")
    save_weights_to_file(node_weights, weights_file_path)

if __name__ == "__main__":
    main()
