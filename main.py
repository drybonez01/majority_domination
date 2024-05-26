import os
import sys

from methods.weightDef import weightDef
from methods.seedset_alg1 import seedset_alg1
from methods.seedset_alg2 import seedset_alg2
from methods.seedset_alg3 import seedset_alg3
from methods.majority_influence_diffusion import majority_influence_diffusion

if len(sys.argv) > 1:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Per eseguire tutti gli step sequenzialmente:")
        print("\tpython main.py")
        print("\nPer definire i costi della rete:")
        print("\tpython main.py -w (path_to_graph)")
        print("\nPer eseguire rispettivamente il primo, il secondo o il terzo algoritmo per calcolare il seed set:")
        print("\tpython main.py -s1 (path_to_graph) (path_to_weights)")
        print("\tpython main.py -s2 (path_to_graph) (path_to_weights)")
        print("\tpython main.py -s3 (path_to_graph) (path_to_weights)")
        print("\nPer calcolare l'influenza di uno specifico seed set:")
        print("\tpython main.py -m (path_to_graph) (path_to_seedset)")
    elif sys.argv[1] == "-w" or sys.argv[1] == "--weightDef":
        try:
            weightDef(sys.argv[2])
        except:
            print("ERRORE. Percorso errato o inesistente.")
    elif sys.argv[1] == "-s1" or sys.argv[1] == "--seedset_alg1":
        try:
            seedset_alg1(sys.argv[2], sys.argv[3])
        except:
            print("ERRORE. Almeno uno dei percorsi inseriti è errato o inesistente.")
    elif sys.argv[1] == "-s2" or sys.argv[1] == "--seedset_alg2":
        try:
            seedset_alg2(sys.argv[2], sys.argv[3])
        except:
            print("ERRORE. Almeno uno dei percorsi inseriti è errato o inesistente.")
    elif sys.argv[1] == "-s3" or sys.argv[1] == "--seedset_alg3":
        try:
            seedset_alg3(sys.argv[2], sys.argv[3])
        except:
            print("ERRORE. Almeno uno dei percorsi inseriti è errato o inesistente.")
    elif sys.argv[1] == "-m" or sys.argv[1] == "--majority_influence_diffusion":
        try:
            majority_influence_diffusion(sys.argv[2], sys.argv[3])
        except:
            print("ERRORE. Almeno uno dei percorsi inseriti è errato o inesistente.")
    else:
        print("ERRORE. Parametro non valido. Per maggiori informazioni, utilizzare il seguente comando:\n\tpython "
              "main.py -h")

else:
    graph_file_path = input("\nInserisci il percorso del file .gml: ")
    while not os.path.exists(graph_file_path):
        print("ERRORE. Percorso errato o inesistente. Riprovare")
        graph_file_path = input("Inserisci il percorso del file .gml: ")
    weights_file_path = weightDef(graph_file_path)

    seedset_file_path = None
    while True:
        alg = int(input("\nInserire l'algoritmo da utilizzare per la selezione del seed set (1,2,3): "))
        if alg == 1:
            seedset_file_path = seedset_alg1(graph_file_path, weights_file_path)
            break
        elif alg == 2:
            seedset_file_path = seedset_alg2(graph_file_path, weights_file_path)
            break
        elif alg == 3:
            seedset_file_path = seedset_alg3(graph_file_path, weights_file_path)
            break
        else:
            print("Opzione non valida. Riprovare.")

    majority_influence_diffusion(graph_file_path, seedset_file_path)
