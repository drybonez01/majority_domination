import snap
import random

# Funzione per caricare il grafo da un file binario .graph
def load_graph(filename):
    FIn = snap.TFIn(filename)
    return snap.TUNGraph.Load(FIn)

# Funzione per assegnare pesi randomici ai nodi
def assign_random_weights_to_snap(snap_graph, weight_range):
    weights = {}
    for NI in snap_graph.Nodes():
        weights[NI.GetId()] = random.randint(*weight_range)
    return weights

# Chiedi all'utente il percorso del file .graph
graph_path = input("Inserisci il percorso del file .graph: ")

# Carica il grafo
snap_graph = load_graph(graph_path)

# Visualizza alcune informazioni sul grafo
print("Numero di nodi:", snap_graph.GetNodes())
print("Numero di archi:", snap_graph.GetEdges())

# Esempio di alcune operazioni sul grafo
for NI in snap_graph.Nodes():
    print("Nodo %d ha %d archi" % (NI.GetId(), NI.GetDeg()))

# Chiedi all'utente il range di valori dei pesi da assegnare
weight_min = int(input("Inserisci il valore minimo del range dei pesi: "))
weight_max = int(input("Inserisci il valore massimo del range dei pesi: "))

# Assegna pesi randomici ai nodi
node_weights = assign_random_weights_to_snap(snap_graph, (weight_min, weight_max))

# Visualizza i pesi assegnati
print("\nPesi assegnati ai nodi:")
for node_id, weight in node_weights.items():
    print(f"Nodo {node_id}: Peso {weight}")

# Salva il grafo con pesi in un file .graph (opzionale)
# In SNAP, i pesi non vengono memorizzati direttamente, quindi se vuoi salvarli,
# devi gestire manualmente l'associazione nodo-peso in un file separato o come attributo aggiuntivo.
# output_graph_path = input("Inserisci il percorso per salvare il file .graph con pesi: ")
# FOut = snap.TFOut(output_graph_path)
# snap_graph.Save(FOut)
# FOut.Flush()

# Salva i pesi in un file di testo separato con il formato corretto
weights_file_path = input("Inserisci il percorso per salvare il file dei pesi (node_weights.txt): ")
with open(weights_file_path, "w") as f:
    for node_id, weight in node_weights.items():
        f.write(f"{node_id} {weight}\n")  # Corretto formato: node_id weight
