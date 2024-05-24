import snap
import networkx as nx

# Funzione per convertire un grafo NetworkX in un grafo SNAP
def nx_to_snap(nx_graph):
    snap_graph = snap.TUNGraph.New()
    for node in nx_graph.nodes():
        snap_graph.AddNode(node)
    for edge in nx_graph.edges():
        snap_graph.AddEdge(edge[0], edge[1])
    return snap_graph

# Carica il grafo da un file GML utilizzando NetworkX
nx_graph = nx.read_gml("risorse/as-22july06.gml", label=None)

# Converti il grafo NetworkX in un grafo SNAP
snap_graph = nx_to_snap(nx_graph)

# Visualizza alcune informazioni sul grafo SNAP
print("Numero di nodi:", snap_graph.GetNodes())
print("Numero di archi:", snap_graph.GetEdges())

# Esempio di alcune operazioni sul grafo SNAP
for NI in snap_graph.Nodes():
    print("Nodo %d ha %d archi" % (NI.GetId(), NI.GetDeg()))

# Salvare il grafo in un file binario
FOut = snap.TFOut("internet.graph")
snap_graph.Save(FOut)
FOut.Flush()

# Caricare il grafo dal file binario
FIn = snap.TFIn("internet.graph")
graph_loaded = snap.TUNGraph.Load(FIn)
