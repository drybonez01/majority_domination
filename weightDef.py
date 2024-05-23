import snap
import random

# Carica il grafo dal file binario .graph
FIn = snap.TFIn("graph/graph.graph")
snap_graph = snap.TUNGraph.Load(FIn)

# Visualizza alcune informazioni sul grafo
print("Numero di nodi:", snap_graph.GetNodes())
print("Numero di archi:", snap_graph.GetEdges())

# Esempio di alcune operazioni sul grafo
for NI in snap_graph.Nodes():
    print("Nodo %d ha %d archi" % (NI.GetId(), NI.GetDeg()))

# Funzione per assegnare pesi randomici ai nodi
def assign_random_weights_to_snap(snap_graph, weight_range=(1, 10)):
    weights = {}
    for NI in snap_graph.Nodes():
        weights[NI.GetId()] = random.randint(*weight_range)
    return weights

# Assegna pesi randomici ai nodi
node_weights = assign_random_weights_to_snap(snap_graph, weight_range=(1, 10))

# Visualizza i pesi assegnati
print("\nPesi assegnati ai nodi:")
for node_id, weight in node_weights.items():
    print(f"Nodo {node_id}: Peso {weight}")

# Salva il grafo con pesi in un file .graph (opzionale)
# In SNAP, i pesi non vengono memorizzati direttamente, quindi se vuoi salvarli,
# devi gestire manualmente l'associazione nodo-peso in un file separato o come attributo aggiuntivo.
FOut = snap.TFOut("graph/graph_with_weights.graph")
snap_graph.Save(FOut)
FOut.Flush()

# Puoi anche salvare i pesi in un file di testo separato (opzionale)
with open("graph/informazioni/node_weights.txt", "w") as f:
    for node_id, weight in node_weights.items():
        f.write(f"{node_id}: {weight}\n")
