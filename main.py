import os
import sys

from methods.weightDef import weightDef
from methods.seedset_alg1 import seedset_alg1

'''while True:
    print("")
    print("1 - Definisci i pesi")
    print("0 - Termina")
    n = int(input("Seleziona un'operazione da eseguire: "))

    if n == 1:
        weightDef()
    elif n == 0:
        print("Arrivederci.")
        break
    else:
        print("Operazione non valida. Riprovare.")'''

if len(sys.argv) > 1:
    if sys.argv[1] == "-w" or sys.argv[1] == "--weightDef":
        try:
            weightDef(sys.argv[2])
        except:
            print("ERRORE. Percorso errato o inesistente.")
    elif sys.argv[1] == "-s1" or sys.argv[1] == "--seedset_alg1":
        try:
            seedset_alg1(sys.argv[2], sys.argv[3])
        except:
            print("ERRORE. Almeno uno dei percorsi inseriti è errato o inesistente.")
else:
    graph_path = input("\nInserisci il percorso del file .gml: ")
    while not os.path.exists(graph_path):
        print("ERRORE. Percorso errato o inesistente. Riprovare")
        graph_path = input("Inserisci il percorso del file .gml: ")
    weights_file_path = weightDef(graph_path)

    seedset_file_path = None
    while True:
        alg = int(input("\nInserire l'algoritmo da utilizzare per la selezione del seed set (1,2,3): "))
        if alg == 1:
            seedset_file_path = seedset_alg1(graph_path, weights_file_path)
            break
        else:
            print("Opzione non valida. Riprovare.")
