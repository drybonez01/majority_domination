import snap
import random


# Funzione per caricare il grafo da un file binario .graph
def load_graph(filename):
    FIn = snap.TFIn(filename)
    return snap.TUNGraph.Load(FIn)


# Funzione per caricare i pesi dei nodi da un file separato
def load_node_weights(filename):
    weights = {}
    with open(filename, 'r') as file:
        for line in file:
            node_id, weight = line.strip().split()
            weights[int(node_id)] = int(weight)
    return weights


# Funzione per calcolare il grado del nodo
def node_degree(graph):
    d = {}
    for NI in graph.Nodes():
        d[NI.GetId()] = NI.GetDeg()
    return d


# Funzione WTSS combinata con vincoli di peso
def wtss_algorithm_with_budget(graph, c, budget):
    S = set()
    U = set([NI.GetId() for NI in graph.Nodes()])
    delta = node_degree(graph)

    total_cost = 0

    while U and total_cost <= budget:
        if any(delta[v] == 0 for v in U):
            for v in U:
                if delta[v] == 0:
                    break
            for u in graph.GetNI(v).GetOutEdges():
                if u in U:
                    delta[u] = max(0, delta[u] - 1)
        else:
            v = max(U, key=lambda u: c[u] / (delta[u] * (delta[u] + 1)))
            if total_cost + c[v] <= budget:
                S.add(v)
                total_cost += c[v]
                for u in graph.GetNI(v).GetOutEdges():
                    if u in U:
                        delta[u] -= 1

        U.remove(v)

    return S


# Funzione per il modello di attivazione con majority
def majority_activation_model(graph, seed_set):
    activated_nodes = set(seed_set)
    newly_activated = set(seed_set)

    iteration = 0
    while newly_activated:
        iteration += 1
        current_activated = set()
        print(f"\nIterazione {iteration}:")
        for NI in graph.Nodes():
            node_id = NI.GetId()
            if node_id not in activated_nodes:
                neighbors = [u for u in NI.GetOutEdges() if u in activated_nodes]
                print(f"Nodo {node_id} ha {len(neighbors)} vicini attivi (grado totale: {NI.GetDeg()})")
                if len(neighbors) > NI.GetDeg() / 2:
                    current_activated.add(node_id)

        newly_activated = current_activated - activated_nodes
        if newly_activated:
            print(f"Nodi attivati in questa iterazione: {newly_activated}")

        activated_nodes.update(newly_activated)

    return activated_nodes


# Carica il grafo
graph_path = input("Inserisci il percorso del file .graph: ")
snap_graph = load_graph(graph_path)

# Carica i pesi dei nodi da un file separato
weights_file_path = input("Inserisci il percorso del file dei pesi (node_weights.txt): ")
node_weights = load_node_weights(weights_file_path)

# Ottieni il budget dall'utente
budget = int(input("Inserisci il budget (soglia) per i nodi: "))

# Applica l'algoritmo WTSS con vincoli di peso
optimal_seed_set = wtss_algorithm_with_budget(snap_graph, node_weights, budget)

# Visualizza il seed set ottimale
print("\nSeed set ottimale:", optimal_seed_set)
print("Somma dei pesi nel seed set:", sum(node_weights[v] for v in optimal_seed_set))
print("Numero di nodi nel seed set:", len(optimal_seed_set))

# Esegui il processo di attivazione usando il modello majority
activated_nodes = majority_activation_model(snap_graph, optimal_seed_set)

# Visualizza l'insieme dei nodi attivati
print("\nInsieme dei nodi attivati Inf[S]:", activated_nodes)
print("Numero di nodi attivati:", len(activated_nodes))

# Stampa dei dettagli per il debug
for node in activated_nodes:
    print(f"Nodo attivato: {node}")
