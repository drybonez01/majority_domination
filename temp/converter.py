import networkx as nx
import scipy.io

# Carica la matrice di adiacenza dal file .mtx
matrix = scipy.io.mmread("C:/Users/Josef/Desktop/Uni/RS/Progetto/temp/soc-dolphins.mtx")

# Crea un grafo NetworkX dalla matrice di adiacenza
G = nx.from_scipy_sparse_array(matrix)

# Salva il grafo in formato .gml
nx.write_gml(G, "C:/Users/Josef/Desktop/Uni/RS/Progetto/risorse/graphs/dolphin.gml")

print("Conversione completata! Il file .gml è stato salvato con successo.")
